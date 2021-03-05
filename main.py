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

lastDayVaccinationData = [x for x in json_vaccine if x['VaccinationStatus'] == 'InProgress'][-1]
lastDayCompletedVaccinationData = [x for x in json_vaccine if x['VaccinationStatus'] == 'Completed'][-1]

completedVaccinationPercentage = lastDayCompletedVaccinationData["PopulationCoverage"]
partialVaccinationPercentage = round(lastDayVaccinationData["PopulationCoverage"] - lastDayCompletedVaccinationData["PopulationCoverage"], 3)

print("Completed vaccination percentage: " + str(completedVaccinationPercentage) + "\n")
print("Partial vaccination percentage: " + str(partialVaccinationPercentage) + "\n")
