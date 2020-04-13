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
        for ora in self.oracles:
            res += str(ora)
        res += "&"
        res += str(self.candidates)
        res += "&"
        res += str(self.newinfections)
        return res

    def __str__(self):
        return self.name

    def run(self):
        while True:
            new_oracle = self.oracles.pop()
            definively_negative_population = new_oracle.calculate(self.candidates)
            downloaded_bits_per_individual = new_oracle.individual_download_size
            self.leastfpp = new_oracle.fpp
            self.logger.log(str(self), definively_negative_population, downloaded_bits_per_individual)
            if self.leastfpp < fpp_threshold:
                break


class Datastructure:
    def calculate(self, candidates):
        pass
    def __str__(self):
        pass


class RawList(Datastructure):
    def __init__(self, fpp):
        self.fpp = fpp
        self.individual_download_size = 1000000

    def __str__(self):
        return "list" + str(self.fpp)

    def calculate(self, candidates):
        return candidates


def main():
    logger = CSVLogger()
    scenario = Scenario(population=80000000, newinfections=60000, oracles=[RawList(0)], logger=logger)
    scenario.run()
    logger.print()


main()
