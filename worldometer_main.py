import json
import country

Country = country.Country


def get_cases(country):
    try:
        return int(country.daily_cases.replace(',', ''))
    except (ValueError, AttributeError):
        return 0


def get_deaths(country):
    try:
        return int(country.daily_deaths.replace(',', ''))
    except (ValueError, AttributeError):
        return 0


def get_population(country):
    try:
        return int(country.population.replace(',', ''))
    except (ValueError, AttributeError):
        return 0


def print_array(sorted_array):
    for entry in sorted_array:
        print(entry)

with open('worldometer.jl') as f:
    country_data = json.load(f)

countries = []
for country_entry in country_data:
    countries.append(Country(country_entry["country"], country_entry["daily cases"], country_entry["daily deaths"], country_entry["population"]))

sortedByPopulation = sorted(countries, key=get_population, reverse=True)
sortedByCases = sorted(countries, key=get_cases, reverse=True)
sortedByDeaths = sorted(countries, key=get_deaths, reverse=True)

casesOrdinal = 1

# for country in sortedByDeaths:
#    print(str(casesOrdinal) + ", " + country.name + ", " + str(country.daily_deaths))
#    casesOrdinal = casesOrdinal + 1

for country in sortedByCases:
    print(str(casesOrdinal) + ", " + country.name + ", " + str(country.daily_cases))
    casesOrdinal = casesOrdinal + 1

# for country in sortedByPopulation:
#    print(str(casesOrdinal) + ", " + country.name + ", " + country.population)
#    casesOrdinal = casesOrdinal + 1

