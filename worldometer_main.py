import json


def get_cases(country):
    try:
        return int(country["daily cases"].replace(',', ''))
    except (ValueError, AttributeError):
        return 0


def get_deaths(country):
    try:
        return int(country["daily deaths"].replace(',', ''))
    except (ValueError, AttributeError):
        return 0


def get_population(country):
    try:
        return int(country["population"].replace(',', ''))
    except (ValueError, AttributeError):
        return 0


def print_array(sorted_array):
    for entry in sorted_array:
        print(entry)


with open('worldometer.jl') as f:
    country_data = json.load(f)

sortedByPopulation = sorted(country_data, key=get_population, reverse=True)
sortedByCases = sorted(country_data, key=get_cases, reverse=True)
sortedByDeaths = sorted(country_data, key=get_deaths, reverse=True)

# print_array(sortedByPopulation)
print_array(sortedByCases)
# print_array(sortedByDeaths)
