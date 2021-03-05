import numpy as np
import requests

API_ENDPOINT = "https://opendata.digilugu.ee/opendata_covid19_test_county_all.json"
VACCINE_ENDPOINT = "https://opendata.digilugu.ee/opendata_covid19_vaccination_total.json"
CURRENT_DATE = "2021-03-04"

def get_json_data(url) -> any:
    # Open data endpoint
    r = requests.get(url=url)
    return r.json()


# json_data = get_json_data(API_ENDPOINT)
json_vaccine = get_json_data(VACCINE_ENDPOINT)

# res = filter(lambda rec: rec["County"] == "Harju maakond" and rec["StatisticsDate"] == CURRENT_DATE and rec["ResultValue"] == "P", json_data)
# print(list(res)[0])

lastDayVaccinationData = [x for x in json_vaccine if x['VaccinationStatus'] == 'InProgress'][-1]
lastDayCompletedVaccinationData = [x for x in json_vaccine if x['VaccinationStatus'] == 'Completed'][-1]

completedVaccinationPercentage = lastDayCompletedVaccinationData["PopulationCoverage"]
partialVaccinationPercentage = round(lastDayVaccinationData["PopulationCoverage"] - lastDayCompletedVaccinationData["PopulationCoverage"], 3)

# estoniaTotalCases = np.sum([res["StatisticsDate"] == CURRENT_DATE for res in json_data])
# estoniaPositiveCases = np.sum([res["ResultValue"] == "P" and res["StatisticsDate"] == CURRENT_DATE for res in json_data])
# estoniaPositiveRate = round(estoniaPositiveCases / estoniaTotalCases * 100, 2)

# harjuResults = np.sum([res["County"] == "Harju maakond" and res["StatisticsDate"] == CURRENT_DATE for res in json_data])
#harjuPositiveCases = np.sum([res["ResultValue"] == "P" and res["County"] == "Harju maakond" and res["StatisticsDate"] == CURRENT_DATE for res in json_data])
# harjuPositiveRate = round(harjuPositiveCases / harjuTotalCases * 100, 2)

# print("Positive tests percentage in Harju county at " + CURRENT_DATE + ": " + str(harjuPositiveRate) + "\n")
# print("Positive tests percentage in Estonia at " + CURRENT_DATE + ": " + str(estoniaPositiveRate) + "\n")

print("Completed vaccination percentage: " + str(completedVaccinationPercentage) + "\n")
print("Partial vaccination percentage: " + str(partialVaccinationPercentage) + "\n")
