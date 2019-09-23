import scrapy
import operator
from datetime import datetime
from datetime import timedelta
import re
import time
import scrapy
from scrapy_sis_seed.configstring import urls_prefix, startTime, endTime
from scrapy_sis_seed.items import SISThreadUrlItem

# <a href="forum-58-1.html">Asia Censored Section | 亚洲有码薄码区</a>

class QuotesSpider(scrapy.Spider):
    name = "ACS"
    start_urls = [
        urls_prefix + 'forum-58-1.html',
    ]

    custom_settings = {
        'ITEM_PIPELINES':{
                        'scrapy_sis_seed.pipelines.ThreadUrlPipeline': 400,
        }
    }


    def parse(self, response):
        tabless = response.xpath('//table[@id=$val]', val='forum_58')[-1]
        # response.css('table#forum_143')
        nexturl = response.css('div.pages a.next::attr(href)').get()
        nextpage = urls_prefix + nexturl
        pagename = response.url.split("/")[-1]

        threadlist = tabless.css('tbody')
        firstTime = datetime.strptime(threadlist[0].css('td.author em::text').get(), '%Y-%m-%d')
        finalTime = datetime.strptime(threadlist[-1].css('td.author em::text').get(), '%Y-%m-%d')
        if firstTime < endTime :
            exit()
        elif firstTime <= startTime and finalTime <= startTime and finalTime >= endTime :
            for thread in threadlist:
                    item = SISThreadUrlItem()
                    item['idurl'] = thread.css('th span a::attr(href)').get()
                    item['forumpage'] = pagename
                    item['forumsubject'] = tabless.css('b::text').get()
                    item['threadurl']= urls_prefix + thread.css('th span a::attr(href)').get()
                    item['threadtitle'] = thread.css('th span a::text').get()
                    item['uploaddate'] = thread.css('td.author em::text').get()
                    yield  item
        elif finalTime < endTime or (firstTime > startTime and finalTime <= startTime):
            for thread in threadlist:
                singledate = datetime.strptime(thread.css('td.author em::text').get(), '%Y-%m-%d')
                if singledate >= endTime and singledate <= startTime:
                    item = SISThreadUrlItem()
                    item['idurl'] = thread.css('th span a::attr(href)').get()
                    item['forumpage'] = pagename
                    item['forumsubject'] = tabless.css('b::text').get()
                    item['threadurl']= urls_prefix + thread.css('th span a::attr(href)').get()
                    item['threadtitle'] = thread.css('th span a::text').get()
                    item['uploaddate'] = thread.css('td.author em::text').get()
                    yield  item

        yield response.follow(nextpage, self.parse)