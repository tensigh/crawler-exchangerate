# -*- coding: utf-8 -*-
# This gets the daily JPY -> USD rate from x-rates.com
# Designed to put into a crontab and run daily
import scrapy
from exchangerate.items import ExchangerateItem

class ExchangeRateSpider(scrapy.Spider):
    name = 'ratecrawl'
    allowed_domains = ['www.x-rates.com']
    start_urls = ['http://www.x-rates.com/table/?from=JPY&amount=1',]
    custom_settings = {
	'FEED_EXPORT_FIELDS': ["date", "base", "todaysrate"],
	}

    def parse(self, response):
        newrate = ExchangerateItem()
        newrate['date'] = response.css('span.ratesTimestamp::text').extract_first()
        newrate['base'] = response.css('th.rtHeader.rtHeaderValues ::text').extract_first()
        newrate['todaysrate'] = response.css('td.rtRates ::text').extract()[1]
        yield newrate