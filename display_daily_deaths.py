import os
from datetime import date, timedelta

today = date.today() - timedelta(1)
current_date = today.strftime("%Y%m%d")[2:]

os.system("csvtotable ./reports/report_" + "daily_deaths_" + current_date + ".csv --serve -c DailyDeaths")
