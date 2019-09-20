# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapySisSeedItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class SISThreadUrlItem(scrapy.Item):
    idurl = scrapy.Field()
    forumpage = scrapy.Field()
    forumsubject = scrapy.Field()
    threadurl = scrapy.Field()
    threadtitle = scrapy.Field()
    uploaddate = scrapy.Field()


class SISSeedUrlItem(scrapy.Item):
    idurl = scrapy.Field()
    downloadurl = scrapy.Field()
    sizetype = scrapy.Field()