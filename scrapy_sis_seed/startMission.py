import scrapy
from datetime import datetime
from datetime import timedelta
from scrapy.crawler import CrawlerRunner
from scrapy.utils.log import configure_logging
from twisted.internet import reactor

from configstring import urls_prefix
from scrapy_sis_seed.spiders import (AAS_Spider, ACAS_Spider, ACS_Spider,
                                     ASR_Spider, AUS_Spider, WAS_Spider)

_a = input('请输入日期，格式为yyyy-mm-dd: ')
_startdate = datetime.strptime(_a, "%Y-%m-%d")
#startTime = datetime(2019, 9, 22, 0, 0)
_enddate = _startdate - timedelta(days=6)

#_startdate = startTime
#_enddate = endTime
_urlprefix = urls_prefix

configure_logging()
runner = CrawlerRunner()
runner.crawl(AAS_Spider.AAS_Spider,startdate=_startdate,enddate=_enddate,urlprefix=_urlprefix)
runner.crawl(ACAS_Spider.ACAS_Spider,startdate=_startdate,enddate=_enddate,urlprefix=_urlprefix)
runner.crawl(ACS_Spider.ACS_Spider,startdate=_startdate,enddate=_enddate,urlprefix=_urlprefix)
runner.crawl(ASR_Spider.ASR_Spider,startdate=_startdate,enddate=_enddate,urlprefix=_urlprefix)
runner.crawl(AUS_Spider.AUS_Spider,startdate=_startdate,enddate=_enddate,urlprefix=_urlprefix)
runner.crawl(WAS_Spider.WAS_Spider,startdate=_startdate,enddate=_enddate,urlprefix=_urlprefix)
d = runner.join()
d.addBoth(lambda _: reactor.stop())

reactor.run() # the script will block here until all crawling jobs are finished
