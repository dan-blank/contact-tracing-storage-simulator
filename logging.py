class CSVLogger:
    def __init__(self):
        self.tbl = {}

    def log(self, key, neg, indsize):
        value = str(neg) + " " + str(6 * indsize) + " "
        if key in self.tbl:
            self.tbl[key] = self.tbl[key] + value
        else:
            self.tbl[key] = value

    def print(self):
        for key, val in self.tbl.items():
            print(key + " | " + val)

