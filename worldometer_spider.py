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
                'daily cases': row.xpath('td[4]//text()').extract_first(),
                'daily deaths': row.xpath('td[6]//text()').extract_first(),
                'population': row.xpath('td[15]//text()').extract_first()
            }