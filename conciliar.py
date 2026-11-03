"""Concilia comprovantes citados num chat exportado com lançamentos de uma planilha CSV."""
import csv, re, sys, unicodedata
from datetime import datetime
from difflib import SequenceMatcher

def norm(s):
    s = unicodedata.normalize("NFD", s.lower())
    return re.sub(r"[^a-z0-9 ]", "", "".join(c for c in s if unicodedata.category(c) != "Mn")).strip()

def ler_chat(path):
    itens, data = [], None
    for linha in open(path, encoding="utf-8"):
        m = re.match(r"^(\d{2}/\d{2}/\d{4}) \d{2}:\d{2} - [^:]+: (.+)$", linha.strip())
        if m:
            data, msg = datetime.strptime(m[1], "%d/%m/%Y").date(), m[2]
            if not msg.startswith("<"):
                itens.append({"data": data, "descricao": msg})
    return itens

def ler_planilha(path):
    return [{"data": datetime.strptime(r["data"], "%Y-%m-%d").date(), "descricao": r["descricao"], "valor": r["valor"]}
            for r in csv.DictReader(open(path, encoding="utf-8"))]

def conciliar(chat, planilha, limiar=0.55):
    livres, ok, sem_lanc = list(planilha), [], []
    for c in chat:
        cands = [(1.0 if (norm(p["descricao"]) in norm(c["descricao"]) or norm(c["descricao"]) in norm(p["descricao"])) else SequenceMatcher(None, norm(c["descricao"]), norm(p["descricao"])).ratio(), p) for p in livres if p["data"] == c["data"]]
        cands.sort(key=lambda x: -x[0])
        if cands and cands[0][0] >= limiar:
            ok.append((c, cands[0][1])); livres.remove(cands[0][1])
        else:
            sem_lanc.append(c)
    return ok, sem_lanc, livres

if __name__ == "__main__":
    ok, sem_lanc, sem_comp = conciliar(ler_chat(sys.argv[1]), ler_planilha(sys.argv[2]))
    print(f"Conciliados: {len(ok)}")
    print("Comprovante sem lançamento:", *[f"  {c['data']} {c['descricao']}" for c in sem_lanc], sep="\n")
    print("Lançamento sem comprovante:", *[f"  {p['data']} {p['descricao']} {p['valor']}" for p in sem_comp], sep="\n")
