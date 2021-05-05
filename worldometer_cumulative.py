from os import walk
from re import search


def get_dates(files, prefix):
    data_dates = []
    for data_file in files:
        data_dates.append(data_file[prefix:-4])
    return data_dates


def is_leap_year(year): return int(year) % 4 == 0


def check_previous_to(previous_value, next_value):

    previous_year_value = previous_value[0:2]
    next_year_value = next_value[0:2]

    previous_month_value = previous_value[2:4]
    next_month_value = next_value[2:4]

    previous_day_value = previous_value[4:]
    next_day_value = next_value[4:]

    month_days = {
        1: 31,
        2: 29 if is_leap_year(previous_year_value) else 28,
        3: 31,
        4: 30,
        5: 31,
        6: 30,
        7: 31,
        8: 31,
        9: 30,
        10: 31,
        11: 30,
        12: 31
    }

    if previous_year_value == next_year_value:
        if previous_month_value == next_month_value:
            previous_day_value = int(previous_day_value)
            next_day_value = int(next_day_value)
            return next_day_value == previous_day_value + 1
        else:
            return int(previous_day_value) == month_days[int(previous_month_value)] and int(next_day_value) == 1
    else:
        return int(previous_month_value) == 11 and int(previous_day_value) == 31 and next_month_value == 1 and next_day_value == 1


def check_sorted_and_consecutive(date_values):
    for index, value in enumerate(date_values):
        if index < len(date_values) - 1:
            if not check_previous_to(value, date_values[index + 1]):
                print("Failed at: " + value)
                return False
    return True


def check_and_report_data_completeness(data_dates, data_description):
    is_data_complete = check_sorted_and_consecutive(data_dates[-14:])
    print(data_description + " data complete: " + "yes" if is_data_complete else "no")


_, _, filenames = next(walk('./reports'))

casesFiles = filter(lambda filename: search('daily_cases_all', filename), filenames)
deathsFiles = filter(lambda filename: search('daily_deaths_all', filename), filenames)
testsFiles = filter(lambda filename: search('tests', filename), filenames)

casesPrefix = len("report_daily_cases_all_countries_")
deathsPrefix = len("report_daily_deaths_all_countries_")
testsPrefix = len("report_positive_tests_")

casesDates = get_dates(casesFiles, casesPrefix)
# for casesDate in casesDates:
#    print(casesDate)

deathsDates = get_dates(deathsFiles, deathsPrefix)
# for deathsDate in deathsDates:
#    print(deathsDate)

testsDates = get_dates(testsFiles, testsPrefix)
# for testsDate in testsDates[-14:]:
#    print(testsDate)

check_and_report_data_completeness(casesDates, "Cases")
check_and_report_data_completeness(deathsDates, "Deaths")
check_and_report_data_completeness(testsDates, "Tests")
