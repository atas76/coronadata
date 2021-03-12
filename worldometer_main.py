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


def get_daily_cases_ratio(country):
    return country.get_daily_cases_ratio()


def print_array(sorted_array):
    for entry in sorted_array:
        print(entry)


def display_sorted(sorted_countries):
    cases_ordinal = 1
    for sortedCountry in sorted_countries:
        print(str(cases_ordinal) + ": " + sortedCountry.to_str())
        cases_ordinal = cases_ordinal + 1


with open('worldometer.jl') as f:
    country_data = json.load(f)

countries = []
for country_entry in country_data:
    countries.append(Country(country_entry["country"], country_entry["daily cases"], country_entry["daily deaths"], country_entry["population"]))

sortedByPopulation = sorted(countries, key=get_population, reverse=True)
sortedByCases = sorted(countries, key=get_cases, reverse=True)
sortedByDeaths = sorted(countries, key=get_deaths, reverse=True)
sortedByCasesRatio = sorted(countries, key=get_daily_cases_ratio, reverse=True)

# display_sorted(sortedByCases)
# display_sorted(sortedByDeaths)
# display_sorted(sortedByPopulation)

display_sorted(sortedByCasesRatio)
