import scrapy
import operator
from datetime import datetime
from datetime import timedelta
import re
import time
import scrapy
import sqlite3

from scrapy_sis_seed.getThreadurl import urlfailedrows
from scrapy_sis_seed.configstring import urls_prefix
from scrapy_sis_seed.items import SISSeedUrlItem

class QuotesSpider(scrapy.Spider):
    name = "GetSeedUrlFailed"
    start_urls = urlfailedrows

    custom_settings = {
        'DOWNLOAD_DELAY': 0.5,
        'CONCURRENT_REQUESTS_PER_IP': 10,
        'CONCURRENT_REQUESTS':20,
        'DOWNLOAD_TIMEOUT': 20,
        'ITEM_PIPELINES':{
                        'scrapy_sis_seed.pipelines.SeedUrlPipeline': 400,
        }
    }
    
    def parse(self, response):
        pagename = response.url.split("/")[-1]
        torrentlist = response.css('dl.t_attachlist a[target="_blank"]::attr(href)')
        sizetext = response.css('title::text').re_first(r'(\d+(\.|\,)?\d+ *?(G|g|M|m))')
        if sizetext is None :
            sizetext = response.css('div.t_msgfont::text').re_first(r'(\d+(\.|\,)?\d+ *?(G|g|M|m))')

        for torrent in torrentlist:
                    item = SISSeedUrlItem()
                    item['idurl'] = pagename
                    item['downloadurl'] = urls_prefix + torrent.get()
                    item['sizetype'] = sizetext                  
                    yield  item