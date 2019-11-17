from Transaction import Transaction
import re
import sys

class Parser():
    FILE_HEADER = "Date, From_IBAN, To_IBAN, From, To, Details, Terminal, Credit, Debit, Balance"
    def __init__(self, filenames = [], ibans = []):
        self.filenames = filenames
        self.transactions = []
        self.ibans = ibans
        self.f_iac = open("inter_account_trades.csv", 'w+')
        self.f_iac.write(Parser.FILE_HEADER + "\n")
        self.f_agg = open("aggregated.csv", 'w+')
        self.f_agg.write(Parser.FILE_HEADER + "\n")

    def dump_transactions(self):
        for transaction in self.transactions:
            h = hash(transaction)
            print("{}, {}".format(h, transaction))

    def parse(self):
        for f in self.filenames:
            self.parse_file(f)

    def parse_file(self, fname=""):
        if not fname:
            print("Empty filename!")
            return
        print("Parsing file: {}".format(fname))

        f = open(fname)
        fout = open(fname.replace(".csv", "_parsed.csv"), "w+")
        lines = f.readlines()
        saved_line = ""
        for l in lines:
            match = re.search("^[0-9+]", l)
            if match:
                if saved_line:
                    tr = Transaction(text=saved_line)
                    self.transactions.append(tr)
                    fout.write(str(tr) + "\n")
                    if tr.to_iban in self.ibans or\
                        tr.from_iban in self.ibans:
                        self.f_iac.write(str(tr) + "\n")
                    else:
                        self.f_agg.write(str(tr) + "\n")
                clean_line = ""
                ok_to_stripp = 0
                for c in l.strip():
                    oc = c
                    if c == "\"":
                        ok_to_stripp += 1
                        continue
                    if ok_to_stripp % 2 == 1:
                        if c == ".":
                            continue
                        if c == ",":
                            oc = "."
                    clean_line += oc
                saved_line = clean_line.replace(",,,", ",*,*,")
            elif l.startswith(",,,"):
                saved_line += l.strip()
            else:
                continue
        f.close()
        fout.close()

    def __del__(self):
        self.f_agg.close()
        self.f_iac.close()