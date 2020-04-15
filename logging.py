# This formatting function is from https://stackoverflow.com/a/1094933
def sizeof_fmt(num, suffix='B'):
    for unit in ['', 'K', 'M', 'G']:
        if abs(num) < 1024.0:
            return "%3.1f%s%s" % (num, unit, suffix)
        num /= 1024.0
    return "%.1f%s%s" % (num, 'Yi', suffix)


class Defaultlogger:
    def __init__(self):
        self.logging_table = {}

    def log(self, filter_name, individuals_with_negative_checks, filter_size_in_bits):
        value = str(individuals_with_negative_checks) + " " + str(
            sizeof_fmt(4 * 24 * 5 * (filter_size_in_bits / 8))) + " "
        if filter_name in self.logging_table:
            self.logging_table[filter_name] = self.logging_table[filter_name] + value
        else:
            self.logging_table[filter_name] = value

    def print(self):
        for key, val in self.logging_table.items():
            print(key + " | " + val)
