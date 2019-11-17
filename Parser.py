from Transaction import Transaction
import re

class Parser():
    def __init__(self, filenames = []):
        self.filenames = filenames
        self.transactions = []

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
        lines = f.readlines()
        saved_line = ""
        for l in lines:
            match = re.search("^[0-9+]", l)
            if match:
                if saved_line:
                    self.transactions.append(Transaction(text=saved_line))
                saved_line = l.strip().replace(",,,", ";*;*;")
            elif l.startswith(",,,"):
                saved_line += l.strip().replace(",",";")
            else:
                continue
        f.close()