import sqlite3

db = "scrapy.db"
drp_tb_sql = "drop table if exists ThreadItems"#sql语句：如果存在名为ThreadItems的表，则删除该表
drp_tb_sql2 = "drop table if exists SeedItems"#sql语句：如果存在名为SeedItems的表，则删除该表


crt_tb_sql = """
create table if not exists ThreadItems(
  idurl TEXT(256),
  forumpage TEXT(256),
  forumsubject TEXT(256),
  threadurl TEXT(256),
  threadtitle TEXT(256),
  uploaddate TEXT(256)
);
"""

crt_tb_sql2 = """
create table if not exists SeedItems(
  idurl TEXT(256),
  downloadurl TEXT(256),
  sizetype TEXT(256)
);
"""

#连接数据库
con = sqlite3.connect(db)#连接数据库，创建数据库连接对象
cur = con.cursor()#创建数据库的交互对象
 
#创建表staff
cur.execute(drp_tb_sql)#检查是否存在表，如存在，则删除
cur.execute(crt_tb_sql)#检查是否存在表，如不存在，则新创建表

cur.execute(drp_tb_sql2)#检查是否存在表，如存在，则删除
cur.execute(crt_tb_sql2)#检查是否存在表，如不存在，则新创建表

con.commit()#数据库对象启动事务提交
cur.close()#关闭数据库交互对象
con.close()#关闭数据库连接对象