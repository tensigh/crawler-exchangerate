# -*- coding: utf-8 -*-

# Only looking for one thing, the JPY -> USD rate.
# Grabbing the date, unit and rate from the site.

import scrapy


class ExchangerateItem(scrapy.Item):
    date = scrapy.Field()
    todaysrate = scrapy.Field()
    base = scrapy.Field()
