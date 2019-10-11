import scrapy
import operator
from datetime import datetime
from datetime import timedelta
import re
import time
import scrapy
#from configstring import urls_prefix, startTime, endTime
from scrapy_sis_seed.items import SISThreadUrlItem

# <a href="forum-25-1.html">Asia Uncensored Section | 亚洲无码区</a>

class AUS_Spider(scrapy.Spider):
    name = "AUS"
    def __init__(self, startdate=None, enddate=None, urlprefix='', *args, **kwargs):
        super(AUS_Spider, self).__init__(*args, **kwargs) 
        self._startdate = startdate
        self._enddate = enddate
        self._urlprefix = urlprefix
        self.start_urls = [ urlprefix + 'forum-25-1.html',]

    custom_settings = {
        'ITEM_PIPELINES':{
                        'scrapy_sis_seed.pipelines.ThreadUrlPipeline': 400,
        }
    }


    def parse(self, response):
        tabless = response.xpath('//table[@id=$val]', val='forum_25')[-1]
        # response.css('table#forum_143')
        nexturl = response.css('div.pages a.next::attr(href)').get()
        nextpage = self._urlprefix + nexturl
        pagename = response.url.split("/")[-1]

        threadlist = tabless.css('tbody')
        firstTime = datetime.strptime(threadlist[0].css('td.author em::text').get(), '%Y-%m-%d')
        finalTime = datetime.strptime(threadlist[-1].css('td.author em::text').get(), '%Y-%m-%d')
        if firstTime < self._enddate :
            self.crawler.engine.close_spider(self, 'Asia Uncensored Section | 亚洲无码区, job done!')
        elif firstTime <= self._startdate and finalTime <= self._startdate and finalTime >= self._enddate :
            for thread in threadlist:
                item = SISThreadUrlItem()
                item['idurl'] = thread.css('th span a::attr(href)').get()
                item['forumpage'] = pagename
                item['forumsubject'] = 'AUS'
                item['threadurl']= self._urlprefix + thread.css('th span a::attr(href)').get()
                item['threadtitle'] = thread.css('th span a::text').get()
                item['uploaddate'] = thread.css('td.author em::text').get()
                yield  item  
        elif finalTime < self._enddate or (firstTime > self._startdate and finalTime <= self._startdate) :
            for thread in threadlist:
                singledate = datetime.strptime(thread.css('td.author em::text').get(), '%Y-%m-%d')
                if singledate >= self._enddate and singledate <= self._startdate:
                    item = SISThreadUrlItem()
                    item['idurl'] = thread.css('th span a::attr(href)').get()
                    item['forumpage'] = pagename
                    item['forumsubject'] = 'AUS'
                    item['threadurl']= self._urlprefix + thread.css('th span a::attr(href)').get()
                    item['threadtitle'] = thread.css('th span a::text').get()
                    item['uploaddate'] = thread.css('td.author em::text').get()
                    yield  item  

        yield response.follow(nextpage, self.parse)