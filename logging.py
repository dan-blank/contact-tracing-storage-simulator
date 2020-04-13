# https://stackoverflow.com/a/1094933
def sizeof_fmt(num, suffix='B'):
    for unit in ['', 'K', 'M', 'G']:
        if abs(num) < 1024.0:
            return "%3.1f%s%s" % (num, unit, suffix)
        num /= 1024.0
    return "%.1f%s%s" % (num, 'Yi', suffix)


class CSVLogger:
    def __init__(self):
        self.tbl = {}

    def log(self, key, neg, indsize):
        value = str(neg) + " " + str(sizeof_fmt((4 * 24 * 5 * indsize) / 8)) + " "
        if key in self.tbl:
            self.tbl[key] = self.tbl[key] + value
        else:
            self.tbl[key] = value

    def print(self):
        for key, val in self.tbl.items():
            print(key + " | " + val)
