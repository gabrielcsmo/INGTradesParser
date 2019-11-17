class Transaction():
    def __init__(self, text="", from_iban = "*", to_iban = "*", details = "*", credit = 0.0,
                 debit = 0.0, balance = 0.0, to = "*", benef = "*", date="01.01.2000"):
        if not text:
            self.from_iban = from_iban
            self.to_iban = to_iban
            self.date = date
            self.details = details
            self.credit = credit
            self.debit = debit
            self.balance = balance
            self.to = to
            self.benef = benef
        else:
            self.raw = text
            self.parse_line()

    def parse_line(self):
        entries = self.raw.split(";")
        non_empty_entry = [e for e in entries if e.strip()]
        print(non_empty_entry)

    def __str__(self):
        ret_str = "{}, {}, {}, {}, {}, {}, {}, {}, {}".format(
            self.date, self.from_iban, self.to_iban, self.benef, self.details,
            self.to, self.benef, self.credit, self.debit, self.balance)

