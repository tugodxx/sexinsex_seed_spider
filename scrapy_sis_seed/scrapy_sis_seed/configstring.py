import os
from datetime import datetime
from datetime import timedelta

# Crawler Configurations
urls_prefix = 'http://bababa.live/bbs/'
startTime = datetime(2019, 9, 22, 0, 0)
endTime = startTime - timedelta(days=6)
encoding = 'gbk'
sleeptime = 0

# Credentials
username = ''
password = ''