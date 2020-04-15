from constants import population, logger, fpp_threshold

class Scenario:
    def __init__(self, oracles):
        self.oracles = oracles
        # The amount of individuals that do not have a negative test yet.
        self.candidates = population
        # The highest amount of uncertainty that can be found in the population.
        # Example: An least_fpp_across_population of 0.01 means
        #   1) There is at least one individual that had a positive check that is false positive with likelihood of 1%.
        #   2) All other individuals with a positive check have an even or lower likelihood of being false positive.
        self.highest_fpp_in_population = 100
        self.name = self.generate_name()

    def generate_name(self):
        name = str(self.oracles[0])
        for oracle in self.oracles[1:]:
            name += "#" + str(oracle)
        return name

    def __str__(self):
        return self.name

    def run(self):
        while True:
            # Get next oracle. It will be bigger in size and have a lower rate of false positives.
            next_oracle = self.oracles.pop()
            # Some individuals will get a negative check by using the oracle. Remember the number of remaining canditates.
            definitely_negative_population = next_oracle.calculate(self.candidates)
            self.candidates -= definitely_negative_population
            # The remaining candidates got a positive check. Remember how high the fpp is for there positive checks.
            self.highest_fpp_in_population = next_oracle.fpp
            # Log the results.
            logger.log(str(self), definitely_negative_population, next_oracle.size)
            # Stop querying for the next oracle when everyone in the population is confident enough in their result.
            if self.highest_fpp_in_population <= fpp_threshold:
                break