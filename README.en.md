# Bank reconciliation: statement × spreadsheet × chat receipts

🇧🇷 [Português](README.md)

> Portfolio project. Code adapted from a real automation in production; **all data, names, IDs and amounts are fictitious**.

## Problem
Payments were agreed and proven in WhatsApp chats but recorded in a separate spreadsheet. Checking that every receipt had an entry (and vice versa) was manual.

## Solution
- Reads the WhatsApp chat export and extracts messages with receipts (date, description).
- Reads the expense spreadsheet (CSV).
- Matches by date and description similarity and lists: reconciled items, receipts without an entry and entries without a receipt.

## Result
Automated cross-check between entries and receipts, producing a pending-items report for the monthly closing.

## Stack
Python, Google Sheets (CSV), AI (development support)

## How to run
`python conciliar.py demo/conversa_demo.txt demo/planilha_demo.csv`

## Author
Hadassa Lopes — [LinkedIn](https://www.linkedin.com/in/kesia-hadassa-vieira)
