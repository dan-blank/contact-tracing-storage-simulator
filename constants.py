from logging import Defaultlogger

# At what false positive rate do we take a positive check for granted?
fpp_threshold = 0.00000000026700
# How many individuals are in our population?
population = 80000000
# How many people get diagnosed as infected (and therefor upload their entries) each day?
new_infections_per_day = 40000
# How likely is it that any given individual of the population is infected with the coronavirus?
percentage_of_actually_infected_candidates = 60594 / 80000000
# A logger for the results
logger = Defaultlogger()
