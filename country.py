class Country:
    def __init__(self, name, daily_cases, deaths, daily_deaths, population):
        self.name = name
        self.daily_cases = daily_cases
        self.deaths = deaths
        self.daily_deaths = daily_deaths
        self.population = population

    def get_daily_cases_ratio(self):
        try:
            return int(self.daily_cases[1:].replace(",", "")) / int(self.population.replace(",", "")) * 1000000
        except TypeError:
            return 0

    def get_daily_deaths_ratio(self):
        try:
            return int(self.daily_deaths[1:].replace(",", "")) / int(self.population.replace(",", "")) * 1000000
        except TypeError:
            return 0

    def to_str(self):
        return self.name + ", daily cases: " + str(self.daily_cases) + ", daily deaths: " + str(self.daily_deaths) + ", population: " + str(self.population) + ", daily cases ratio: " + str(self.get_daily_cases_ratio()) + ", daily deaths ratio: " + str(self.get_daily_deaths_ratio())

    def to_csv(self):
        return self.name + ", daily cases: " + str(self.daily_cases).replace(",", "") + ", daily deaths: " + str(
            self.daily_deaths).replace(",", "") + ", population: " + str(self.population).replace(",", "_") + ", daily cases ratio: " + str(
            self.get_daily_cases_ratio()).replace(",", "") + ", daily deaths ratio: " + str(self.get_daily_deaths_ratio()).replace(",", "")
