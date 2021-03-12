class Country:
    def __init__(self, name, daily_cases, daily_deaths, population):
        self.name = name
        self.daily_cases = daily_cases
        self.daily_deaths = daily_deaths
        self.population = population

    def get_daily_cases_ratio(self):
        try:
            return int(self.daily_cases[1:].replace(",", "")) / int(self.population.replace(",", "")) * 1000000
        except TypeError:
            return 0

    def to_str(self):
        return self.name + ", daily cases: " + str(self.daily_cases) + ", daily deaths: " + str(self.daily_deaths) + ", population: " + str(self.population) + ", daily cases ratio: " + str(self.get_daily_cases_ratio())
