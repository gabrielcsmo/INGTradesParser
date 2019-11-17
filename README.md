# INGTradeParser
Starting from RAW csv with transactions exported by ING, generates a parsed csv that can be easily used for statistics.


Usage:
  python3 main.py input.json


Input JSON format descriptions:

input_files: al list of all csv files you want to parse

ibans: your personal IBAN - used to generate interaccount transaction list

