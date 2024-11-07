import data
from build_data import get_data
#part 1
def population_total(values:list[data.CountyDemographics])->int:
    total_population = 0
    for value in values:
        total_population = total_population + value.population['2014 Population']
    return total_population
#part2

#part3

#part4

#part5
