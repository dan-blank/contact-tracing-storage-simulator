from datastructure import RawList, BloomFilter
from logging import CSVLogger

fpp_threshold = 0.001


class Scenario:
    def __init__(self, population, newinfections, oracles, logger):
        self.candidates = population  # Initially, every individual is a potentially infected person
        self.newinfections = newinfections
        self.oracles = oracles
        self.logger = logger
        self.leastfpp = 100
        self.name = self.generate_name()

    def generate_name(self):
        res = ""
        res += str(self.oracles[0])
        for ora in self.oracles[1:]:
            res += "#" + str(ora)
        res += "*"
        res += str(self.candidates)
        res += "*"
        res += str(self.newinfections)
        return res

    def __str__(self):
        return self.name

    def run(self):
        while True:
            new_oracle = self.oracles.pop()
            knowing_population = new_oracle.calculate(self.candidates)
            self.candidates -= knowing_population
            downloaded_bits_per_individual = new_oracle.individual_download_size
            self.leastfpp = new_oracle.fpp
            self.logger.log(str(self), knowing_population, downloaded_bits_per_individual)
            if self.leastfpp <= fpp_threshold:
                break


def main():
    logger = CSVLogger()
    Scenario(population=80000000, newinfections=40000, oracles=[RawList(0, 40000)], logger=logger).run()
    Scenario(population=80000000, newinfections=40000, oracles=[BloomFilter(0.000001, 40000)], logger=logger).run()
    Scenario(population=80000000, newinfections=40000, oracles=[RawList(0, 40000), BloomFilter(0.01, 40000)], logger=logger).run()
    Scenario(population=80000000, newinfections=40000, oracles=[BloomFilter(0.00000000001, 40000), BloomFilter(0.002, 40000), BloomFilter(0.01, 40000)], logger=logger).run()
    logger.print()


main()
