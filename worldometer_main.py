import json
import country
from datetime import date, timedelta


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


def get_daily_deaths_ratio(country):
    return country.get_daily_deaths_ratio()


def get_positive_tests_perc(country):
    return country.get_positive_tests_perc()


def print_array(sorted_array):
    for entry in sorted_array:
        print(entry)


def display_sorted(sorted_countries):
    cases_ordinal = 1
    for sortedCountry in sorted_countries:
        print(str(cases_ordinal) + ": " + sortedCountry.to_str())
        cases_ordinal = cases_ordinal + 1


def create_csv(sorted_countries):
    cases_ordinal = 1
    csv = "Ordinal Position, Country, New Cases, New Deaths, New Cases Ratio, New Deaths Ratio, Positive Tests Percentage, Population\n"
    for sortedCountry in sorted_countries:
        csv += str(cases_ordinal) + ", " + sortedCountry.to_csv() + "\n"
        cases_ordinal = cases_ordinal + 1
    return csv


def write_sorted(sorted_countries, label, current_date):
    filename = 'report_' + label + "_" + current_date + ".csv"
    with open('./reports/' + filename, 'w+') as f:
        f.write(create_csv(sorted_countries))
    f.close()


def get_tests(country_name, test_data):
    try:
        current_tests = next(country_tests for country_tests in test_data if country_tests["country"] == country_name)["tests"]
        return int(current_tests.replace(",", ""))
    except (AttributeError, StopIteration):
        return 0


today = date.today() - timedelta(1)
previousday = today - timedelta(1)

CURRENT_DATE = today.strftime("%Y%m%d")[2:]
PREVIOUS_DATE = previousday.strftime("%Y%m%d")[2:]

with open('worldometer_' + CURRENT_DATE + '.jl') as f:
    country_data = json.load(f)

with open('worldometer_tests_' + CURRENT_DATE + '.jl') as f:
    current_test_data = json.load(f)

with open('worldometer_tests_' + PREVIOUS_DATE + '.jl') as f:
    previous_test_data = json.load(f)

POPULATION_THRESHOLD = 1000000
REFERENCE_COUNTRY = 'Andorra'
DEATH_TOLL_THRESHOLD = int(next(c for c in country_data if c["country"] == REFERENCE_COUNTRY)["deaths"])

countries = []
biggerCountries = []
deathTollCountries = []
for country_entry in country_data:
    countryName = country_entry["country"]
    dailyTests = get_tests(countryName, current_test_data) - get_tests(countryName, previous_test_data)
    currentCountry = Country(country_entry["country"], country_entry["daily cases"], country_entry["deaths"], country_entry["daily deaths"], country_entry["population"], dailyTests)
    countries.append(currentCountry)
    if currentCountry.population is not None and currentCountry.population != " ":
        if int(currentCountry.population.replace(",", "")) > POPULATION_THRESHOLD:
            biggerCountries.append(currentCountry)
    if currentCountry.deaths is not None and currentCountry.deaths != " ":
        if int(currentCountry.deaths.replace(",", "")) >= DEATH_TOLL_THRESHOLD:
            deathTollCountries.append(currentCountry)

# sortedByPopulation = sorted(countries, key=get_population, reverse=True)
# sortedByCases = sorted(countries, key=get_cases, reverse=True)
# sortedByDeaths = sorted(countries, key=get_deaths, reverse=True)

sortedByCasesRatio = sorted(biggerCountries, key=get_daily_cases_ratio, reverse=True)
sortedByDeathsRatio = sorted(deathTollCountries, key=get_daily_deaths_ratio, reverse=True)

sortedByCasesRatioAllCountries = sorted(countries, key=get_daily_cases_ratio, reverse=True)
sortedByDeathsRatioAllCountries = sorted(countries, key=get_daily_deaths_ratio, reverse=True)
sortedByPositiveTests = sorted(countries, key=get_positive_tests_perc, reverse=True)

# display_sorted(sortedByCases)
# display_sorted(sortedByDeaths)
# display_sorted(sortedByPopulation)

# display_sorted(sortedByCasesRatio)

# display_sorted(sortedByDeathsRatio)

write_sorted(sortedByCasesRatio, 'daily_cases', CURRENT_DATE)
write_sorted(sortedByDeathsRatio, 'daily_deaths', CURRENT_DATE)

write_sorted(sortedByCasesRatioAllCountries, 'daily_cases_all_countries', CURRENT_DATE)
write_sorted(sortedByDeathsRatioAllCountries, 'daily_deaths_all_countries', CURRENT_DATE)

write_sorted(sortedByPositiveTests, 'positive_tests', CURRENT_DATE)
