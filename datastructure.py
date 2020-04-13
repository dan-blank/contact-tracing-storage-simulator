import math

percentage_of_actually_infected_candidates = 60594 / 80000000


class Datastructure:
    def __init__(self, fpp, infectedentries):
        self.fpp = fpp
        self.totalcandidates = infectedentries

    def calculate(self, candidates):
        actually_infected = percentage_of_actually_infected_candidates * candidates
        falsely_identified = candidates * self.fpp
        return candidates - actually_infected - falsely_identified

    def __str__(self):
        pass


class BloomFilter(Datastructure):
    def __init__(self, fpp, infectedentries):
        Datastructure.__init__(self, fpp, infectedentries)
        bit_per_entry = 1.44 * math.log(1 / fpp, 2)
        self.individual_download_size = bit_per_entry * infectedentries

    def __str__(self):
        return "bf" + str(self.fpp)


class CuckooFilter(Datastructure):
    def __init__(self, fpp, infectedentries):
        Datastructure.__init__(self, fpp, infectedentries)
        bit_per_entry = (math.log(1 / fpp, 2) + 2) / 0.955
        self.individual_download_size = bit_per_entry * infectedentries

    def __str__(self):
        return "cf" + str(self.fpp)
