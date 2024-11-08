from functools import total_ordering

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
def population_by_education(counties:list[data.CountyDemographics], degree:str) -> float:
    result = 0
    for county in counties:
        if degree in county.education:
            result =result + county.education[degree]
    return round(result,3)
def population_by_ethnicity(counties:list[data.CountyDemographics], race:str) -> float:
    result = 0
    for county in counties:
        if race in county.ethnicities:
            result =result + county.ethnicities[race]
    return result
def population_below_poverty_level(population:list[data.CountyDemographics]) -> float:
    result = 0
    for counties in range(len(population)):
        result = result + population[counties].income['Persons Below Poverty Level']
    return round(result)
#part4
def percent_by_education(counties:list[data.CountyDemographics],degree: str) -> float:
    result = population_by_education(counties,degree)
    print(population_total(counties))
    print(result)
    return round((result/population_total(counties)*100),3)
def percent_by_ethnicity(counties:list[data.CountyDemographics], race:str) -> float:
    result = population_by_ethnicity(counties,race)
    return round((result / population_total(counties) * 100), 3)
def percent_below_poverty_level(counties:list[data.CountyDemographics]) -> float:
    result = population_below_poverty_level(counties)
    return round((result / population_total(counties) * 100), 3)

#part5
