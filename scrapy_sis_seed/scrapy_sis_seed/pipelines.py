# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.exceptions import DropItem 
import sqlite3

class ScrapySisSeedPipeline(object):
    def process_item(self, item, spider):
        return item

class DuplicatesPipeline(object): 
    def __init__(self): 
        self.car_seen = set() 

    def process_item(self, item, spider): 
        if item['idurl'] in self.car_seen: 
            raise DropItem("Duplicate item found: %s" % item) 
        else: 
            self.car_seen.add(item['idurl']) 
            return item 

class SeedUrlPipeline(object):

    #打开数据库
    def open_spider(self, spider):
        db_name = spider.settings.get('SQLITE_DB_NAME', 'scrapy.db')

        self.db_conn = sqlite3.connect(db_name)
        self.db_cur = self.db_conn.cursor()

    #关闭数据库
    def close_spider(self, spider):
        self.db_conn.commit()
        self.db_conn.close()

    #对数据进行处理
    def process_item(self, item, spider):
        self.insert_db(item)
        return item

    #插入数据
    def insert_db(self, item):
       # NOTE:  Use "INSERT OR IGNORE", if you also use: "AdId TEXT NOT NULL UNIQUE"
        # "INSERT INTO ads ( AdId, DateR, AdURL ) VALUES (?, ?, ?)"
        sql = "INSERT INTO SeedItems ({0}) VALUES ({1})".format(','.join(item.keys()), ','.join(['?'] * len(item.keys())) )

        # (item.get('AdId',''),item.get('DateR',''),item.get('AdURL',''), ...)
        #itkeys = ','.join(item.keys())      # item keys as a list
        #itvals = ','.join(item.values())    # item values as a list
        ivals  = tuple(item.values())       # item values as a tuple

        #print (sql)
        #print("  itkeys: \t%s" % itkeys, flush=True)
        #print("  itvals: \t%s" % itvals, flush=True)
        self.db_cur.execute(sql, ivals)     # WARNING: Does NOT handle '[]'s ==> use: '' in spider

class ThreadUrlPipeline(object):

    #打开数据库
    def open_spider(self, spider):
        db_name = spider.settings.get('SQLITE_DB_NAME', 'scrapy.db')

        self.db_conn = sqlite3.connect(db_name)
        self.db_cur = self.db_conn.cursor()

    #关闭数据库
    def close_spider(self, spider):
        self.db_conn.commit()
        self.db_conn.close()

    #对数据进行处理
    def process_item(self, item, spider):
        self.insert_db(item)
        return item

    #插入数据
    def insert_db(self, item):
        # NOTE:  Use "INSERT OR IGNORE", if you also use: "AdId TEXT NOT NULL UNIQUE"
        # "INSERT INTO ads ( AdId, DateR, AdURL ) VALUES (?, ?, ?)"
        sql = "INSERT INTO ThreadItems ({0}) VALUES ({1})".format(','.join(item.keys()), ','.join(['?'] * len(item.keys())) )

        # (item.get('AdId',''),item.get('DateR',''),item.get('AdURL',''), ...)
        #itkeys = ','.join(item.keys())      # item keys as a list
        #itvals = ','.join(item.values())    # item values as a list
        ivals  = tuple(item.values())       # item values as a tuple

        #print (sql)
        #print("  itkeys: \t%s" % itkeys, flush=True)
        #print("  itvals: \t%s" % itvals, flush=True)
        self.db_cur.execute(sql, ivals)     # WARNING: Does NOT handle '[]'s ==> use: '' in spider