import scrapy


class EastmoneyGubaSpider(scrapy.Spider):
    name = 'eastmoney_guba'
    allowed_domains = ['gubaf10.eastmoney.com']
    start_urls = ['http://gubaf10.eastmoney.com/']

    def parse(self, response):
        pass
