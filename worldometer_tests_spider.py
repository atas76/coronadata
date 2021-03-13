import scrapy


class WorldometerSpider(scrapy.Spider):
    name = 'worldometer'
    start_urls = [
        'https://www.worldometers.info/coronavirus/',
    ]

    def parse(self, response):
        for row in response.xpath('//*[@id="main_table_countries_yesterday"]//tbody/tr'):
            yield {
                'country': row.xpath('td[2]//text()').extract_first(),
                'tests': row.xpath('td[13]//text()').extract_first()
            }
