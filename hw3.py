import data
import hw3_tests
from build_data import get_data
#part 1
def population_total(values:list[data.CountyDemographics])->int:
    total_population = 0
    for counties in range(len(values)):
        total_population = total_population + values[counties].population['2014 Population']
    return total_population
#part2
def filter_by_state(counties:list[data.CountyDemographics], state:str) -> list[data.CountyDemographics]:
    state_demographics = []
    for county in counties:
        if state in county.state:
            state_demographics.append(county)
    return state_demographics

#part3
def population_by_education(counties:list[CountyDemographics], degree:str) -> float:
    result = 0
    for county in counties:
        if


#part4

#part5
