# Conciliação bancária: extrato × planilha × comprovantes de chat

> Projeto de portfólio. Código adaptado de uma automação real em produção; **todos os dados, nomes, IDs e valores são fictícios**.

## Problema
Pagamentos eram combinados e comprovados em conversas de WhatsApp, mas lançados em uma planilha separada. Conferir se todo comprovante tinha lançamento (e vice-versa) era manual.

## Solução
- Lê a exportação de conversa do WhatsApp e extrai mensagens com comprovantes (data, descrição).
- Lê a planilha de despesas (CSV).
- Casa por data e similaridade de descrição e lista: conciliados, comprovantes sem lançamento e lançamentos sem comprovante.

## Resultado
Conferência entre lançamentos e comprovantes automatizada, gerando relatório de pendências para o fechamento mensal.

## Stack
Python, Google Sheets (CSV), IA (apoio no desenvolvimento)

## Como rodar
`python conciliar.py demo/conversa_demo.txt demo/planilha_demo.csv`

## Autora
Hadassa Lopes — [LinkedIn](https://www.linkedin.com/in/kesia-hadassa-vieira)
