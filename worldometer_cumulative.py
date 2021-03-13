from os import walk
from re import search

_, _, filenames = next(walk('./reports'))

casesFiles = filter(lambda filename: search('daily_cases_all', filename), filenames)
deathsFiles = filter(lambda filename: search('daily_deaths_all', filename), filenames)
testsFiles = filter(lambda filename: search('tests', filename), filenames)
