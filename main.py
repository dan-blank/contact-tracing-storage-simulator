from constants import fpp_threshold, logger
from datastructures import CuckooFilter
from scenario import Scenario

def main():
    Scenario(oracles=[CuckooFilter(fpp_threshold)]).run()
    Scenario(oracles=[CuckooFilter(fpp_threshold), CuckooFilter(0.00002)]).run()
    Scenario(oracles=[CuckooFilter(fpp_threshold), CuckooFilter(0.000001), CuckooFilter(0.00001)]).run()
    logger.print()

main()
