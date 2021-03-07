import requests

API_ENDPOINT = "https://opendata.digilugu.ee/opendata_covid19_test_county_all.json"
VACCINE_ENDPOINT = "https://opendata.digilugu.ee/opendata_covid19_vaccination_total.json"
HOSPITAL_ENDPOINT = "https://opendata.digilugu.ee/opendata_covid19_hospitalization_timeline.json"
CURRENT_DATE = "2021-03-04"


def get_json_data(url) -> any:
    # Open data endpoint
    r = requests.get(url=url)
    return r.json()


def diff(current, previous, feature) -> any:
    numdiff = int(current[feature]) - int(previous[feature])
    return "+" + str(numdiff) if numdiff > 0 else str(numdiff)


# json_data = get_json_data(API_ENDPOINT)
json_vaccine = get_json_data(VACCINE_ENDPOINT)
json_hospital = get_json_data(HOSPITAL_ENDPOINT)

lastDayVaccinationData = [x for x in json_vaccine if x['VaccinationStatus'] == 'InProgress'][-1]
lastDayCompletedVaccinationData = [x for x in json_vaccine if x['VaccinationStatus'] == 'Completed'][-1]

previousDayVaccinationData = [x for x in json_vaccine if x['VaccinationStatus'] == 'InProgress'][-2]
previousDayCompletedVaccinationData = [x for x in json_vaccine if x['VaccinationStatus'] == 'Completed'][-2]

completedVaccinationPercentage = lastDayCompletedVaccinationData["PopulationCoverage"]
previousDayCompletedVaccinationPercentage = previousDayCompletedVaccinationData["PopulationCoverage"]
partialVaccinationPercentage = round(lastDayVaccinationData["PopulationCoverage"] - lastDayCompletedVaccinationData["PopulationCoverage"], 3)
previousDayPartialVaccinationPercentage = round(previousDayVaccinationData["PopulationCoverage"] - previousDayCompletedVaccinationData["PopulationCoverage"], 3)

currentDayHospital = json_hospital[-1]
previousDayHospital = json_hospital[-2]

print("\n")

print("Completed vaccination percentage: " + str(completedVaccinationPercentage) + " (" + str(previousDayCompletedVaccinationPercentage) + ")")
print("Partial vaccination percentage: " + str(partialVaccinationPercentage) + " (" + str(previousDayPartialVaccinationPercentage) + ")" + "\n")

diffVentilation = diff(currentDayHospital, previousDayHospital, "IsOnVentilation")
diffIntensiveCare = diff(currentDayHospital, previousDayHospital, "IsInIntensive")
diffNewCases = diff(currentDayHospital, previousDayHospital, "NewCases")

print("On ventilation: " + str(currentDayHospital["IsOnVentilation"]))
print("Difference: " + diffVentilation + "\n")

print("In intensive care: " + str(currentDayHospital["IsInIntensive"]))
print("Difference: " + diffIntensiveCare + "\n")

print("New cases: " + str(currentDayHospital["NewCases"]))
print("Difference: " + diffNewCases + "\n")
