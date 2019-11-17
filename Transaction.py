class Transaction():
    DATE_IDX = 0
    NAME_IDX = 3
    DEBIT_IDX = 4
    CREDIT_IDX = 6
    BALANCE_IDX = 7

    TO_PREFIX = "Beneficiar: "
    TOIBAN_PREFIX = "In contul: "
    DETAILS_PREFIX = "Detalii: "
    FROMIBAN_PREFIX = "Din contul: "
    TERMINAL_PREFIX = "Terminal: "
    FROM_PREFIX = "Ordonator: "

    def __init__(self, text = "", from_iban = "*", to_iban = "*", details = "*", credit = 0.0,
                 debit = 0.0, balance = 0.0, to_ = "*", from_ = "*", date = "01.01.2000",
                 name = "", terminal = ""):
        if not text:
            self.from_iban = from_iban
            self.to_iban = to_iban
            self.date = date
            self.details = details
            self.credit = credit
            self.debit = debit
            self.balance = balance
            self.to_ = to_
            self.from_ = from_
            self.name = name
            self.terminal = terminal
        else:
            self.raw = text
            self.from_iban = ""
            self.to_iban = ""
            self.date = ""
            self.details = ""
            self.credit = 0.0
            self.debit = 0.0
            self.balance = 0.0
            self.to_ = ""
            self.from_ = ""
            self.name = ""
            self.terminal = ""
            self.parse_line()

    def parse_line(self):
        entries = self.raw.split(",")
        """non empty entries"""
        es = [e for e in entries if e.strip()]
        self.date = es[Transaction.DATE_IDX]
        self.name = es[Transaction.NAME_IDX]
        debit = es[Transaction.DEBIT_IDX]
        if debit == "*":
            self.debit = 0.0
        else:
            self.debit = float(debit)
        credit = es[Transaction.CREDIT_IDX]
        if credit == "*":
            self.credit = 0.0
        else:
            self.credit = float(credit)
        self.balance = float(es[Transaction.BALANCE_IDX])
        for entry in es[Transaction.BALANCE_IDX + 1:]:
            if entry.startswith(Transaction.TO_PREFIX):
                self.to_ = entry.strip().replace(Transaction.TO_PREFIX, "")
            elif entry.startswith(Transaction.FROM_PREFIX):
                self.from_ = entry.strip().replace(Transaction.FROM_PREFIX, "")
            elif entry.startswith(Transaction.TOIBAN_PREFIX):
                self.to_iban = entry.strip().replace(Transaction.TOIBAN_PREFIX, "")
            elif entry.startswith(Transaction.FROMIBAN_PREFIX):
                self.from_iban = entry.strip().replace(Transaction.FROMIBAN_PREFIX, "")
            elif entry.startswith(Transaction.DETAILS_PREFIX):
                self.details_iban = entry.strip().replace(Transaction.DETAILS_PREFIX, "")
            elif entry.startswith(Transaction.TERMINAL_PREFIX):
                self.terminal = entry.strip().replace(Transaction.TERMINAL_PREFIX, "")
            else:
                continue

    def __str__(self):
        ret_str = "{}, {}, {}, {}, {}, {}, {}, {}, {}, {}".format(
            self.date, self.from_iban, self.to_iban, self.from_, self.to_,
            self.details, self.terminal, self.credit, self.debit, self.balance)
        return ret_str

