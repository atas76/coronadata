import numpy as np
import requests

API_ENDPOINT = "https://opendata.digilugu.ee/opendata_covid19_test_results.json"
CURRENT_DATE = "2021-02-09"

def get_json_data(url) -> any:
    # Open data endpoint
    r = requests.get(url=url)
    return r.json()


json_data = get_json_data(API_ENDPOINT)

estoniaTotalCases = np.sum([res["StatisticsDate"] == CURRENT_DATE for res in json_data])
estoniaPositiveCases = np.sum([res["ResultValue"] == "P" and res["StatisticsDate"] == CURRENT_DATE for res in json_data])
estoniaPositiveRate = round(estoniaPositiveCases / estoniaTotalCases * 100, 2)

harjuTotalCases = np.sum([res["County"] == "Harju maakond" and res["StatisticsDate"] == CURRENT_DATE for res in json_data])
harjuPositiveCases = np.sum([res["ResultValue"] == "P" and res["County"] == "Harju maakond" and res["StatisticsDate"] == CURRENT_DATE for res in json_data])
harjuPositiveRate = round(harjuPositiveCases / harjuTotalCases * 100, 2)

print("Positive tests percentage in Harju county at " + CURRENT_DATE + ": " + str(harjuPositiveRate) + "\n")
print("Positive tests percentage in Estonia at " + CURRENT_DATE + ": " + str(estoniaPositiveRate) + "\n")
