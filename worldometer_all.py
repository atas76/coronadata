import os

os.system("scrapy runspider worldometer_spider.py -o worldometer_raw.jl")
os.system("scrapy runspider worldometer_tests_spider.py -o worldometer_tests_raw.jl")
os.system("python3 cleanup.py")
os.system("python3 worldometer_main.py")
