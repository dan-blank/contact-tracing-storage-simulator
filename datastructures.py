import math

from constants import percentage_of_actually_infected_candidates, new_infections_per_day

class Datastructure:
    def __init__(self, fpp):
        self.fpp = fpp

    def calculate(self, candidates):
        actually_infected = percentage_of_actually_infected_candidates * candidates
        chance_for_false_positive = 1.0 - ((1.0 - self.fpp)) ** (14 * 24 * 4 * 4)
        falsely_identified = candidates * chance_for_false_positive
        return candidates - min(candidates, actually_infected + falsely_identified)

    def __str__(self):
        pass

class BloomFilter(Datastructure):
    def __init__(self, fpp):
        Datastructure.__init__(self, fpp)
        bit_per_entry = 1.44 * math.log(1 / fpp, 2)
        self.size = bit_per_entry * new_infections_per_day

    def __str__(self):
        return "bf" + str(self.fpp)

class CuckooFilter(Datastructure):
    def __init__(self, fpp):
        Datastructure.__init__(self, fpp)
        bit_per_entry = (math.log(1 / fpp, 2) + 2) / 0.955
        self.size = bit_per_entry * new_infections_per_day

    def __str__(self):
        return "cf" + str(self.fpp)
