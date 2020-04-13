class Datastructure:
    def __init__(self, fpp):
        self.fpp = fpp
    def calculate(self, candidates):
        uncertain_candidates = candidates * self.fpp
        return candidates - uncertain_candidates
    def __str__(self):
        pass


class RawList(Datastructure):
    def __init__(self, fpp):
        Datastructure.__init__(self, fpp)
        self.individual_download_size = 1000000
    def __str__(self):
        return "list" + str(self.fpp)


class BloomFilter(Datastructure):
    def __init__(self, fpp):
        Datastructure.__init__(self, fpp)
        self.individual_download_size = 50000
    def __str__(self):
        return "bf" + str(self.fpp)