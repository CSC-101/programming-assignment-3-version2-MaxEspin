import array

from data import CountyDemographics

#part1
def population_total(county_list: list[CountyDemographics]) -> int:
    p = 0
    for county in county_list:
        p += county.population.get('2014 Population')
    return p
#part2
def filter_by_state( c: list[CountyDemographics], s: str) -> list[CountyDemographics]:
    l = []
    for county in c:
        if county.state == s:
            l.append(county)

    return l
#3
def population_by_education(e: list[CountyDemographics], f: str) -> float:
    s = 0

    for county in e:
        if f not in county.education:
            continue
        s += (county.education.get(f)/100*county.population.get('2014 Population'))

    return s

def population_by_ethnicity(e: list[CountyDemographics], f: str) -> float:
    s = 0

    for county in e:
        if f not in county.ethnicities:
            continue
        s += county.ethnicities.get(f)/100*county.population.get('2014 Population')
    return s

def population_below_poverty_level(e: list[CountyDemographics], f: str) -> float:
    s = 0

    for county in e:
        if f not in county.income:
            continue
        s += county.income.get(f)/100*county.population.get('2014 Population')
    return s
#part4
def percent_by_education(l:list[CountyDemographics], s: str) -> float:
    total = population_total(l)
    sub_total = population_by_education(l,s)

    return sub_total/total*100

def percent_by_ethnicity(l:list[CountyDemographics], s: str) -> float:
    total = population_total(l)
    sub_total = population_by_ethnicity(l,s)
    return sub_total/total*100

def percent_below_poverty_level(l:list[CountyDemographics], s: str) -> float:
    total = population_total(l)
    sub_total = population_below_poverty_level(l,s)
    return sub_total/total*100
#part5
def education_greater_than(c:list[CountyDemographics], s:str, f: float) -> list[CountyDemographics]:
    l = []
    for county in c:
        if s in county.education:
            if percent_by_education(c, s) >= f:
                l.append(county)
    return l

def education_less_than(c:list[CountyDemographics], s:str, f: float) -> list[CountyDemographics]:
    l = []
    for county in c:
        if s in county.education:
            if percent_by_education(c, s) <= f:
                l.append(county)
    return l


def ethnicity_greater_than(c: list[CountyDemographics], s: str, f: float) -> list[CountyDemographics]:
    l = []
    for county in c:
        if s in county.ethnicities:
            if percent_by_ethnicity(c, s) >= f:
                l.append(county)
    return l


def ethnicity_less_than(c: list[CountyDemographics], s: str, f: float) -> list[CountyDemographics]:
    l = []
    for county in c:
        if s in county.ethnicities:
            if percent_by_ethnicity(c, s) <= f:
                l.append(county)
    return l


def below_poverty_level_greater_than(c: list[CountyDemographics], s: str, f: float) -> list[CountyDemographics]:
    l = []
    for county in c:
        if s in county.income:
            if percent_below_poverty_level(c, s) >= f:
                l.append(county)
    return l


def below_poverty_level_less_than(c: list[CountyDemographics], s: str, f: float) -> list[CountyDemographics]:
    l = []
    for county in c:
        if s in county.income:
            if percent_below_poverty_level(c, s) <= f:
                l.append(county)
    return l











