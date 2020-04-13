import math


class Datastructure:
    def __init__(self, fpp, infectedentries):
        self.fpp = fpp
        self.totalcandidates = infectedentries
    def calculate(self, candidates):
        uncertain_candidates = candidates * self.fpp
        return candidates - uncertain_candidates
    def __str__(self):
        pass


class RawList(Datastructure):
    def __init__(self, fpp, infectedentries):
        Datastructure.__init__(self, fpp, infectedentries)
        self.individual_download_size = 32 * infectedentries
    def __str__(self):
        return "list" + str(self.fpp)


class BloomFilter(Datastructure):
    def __init__(self, fpp, infectedentries):
        Datastructure.__init__(self, fpp, infectedentries)
        bit_per_entry = 1.44 * math.log(1 / fpp, 2)
        self.individual_download_size = bit_per_entry * infectedentries
    def __str__(self):
        return "bf" + str(self.fpp)