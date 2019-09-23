import sqlite3

conn = sqlite3.connect(
    'scrapy.db',
    timeout=20,
)
conn.row_factory = lambda cursor, row: row[0]

cursor = conn.cursor()
cursor.execute('select count(threadurl) from ThreadItems where  ThreadItems.idurl not in(select SeedItems.idurl from SeedItems)')
urlrows = cursor.fetchone()
print(urlrows)
#if urlrows > 0 :
#    cursorf = conn.cursor()
#    cursorf.execute('select threadurl from ThreadItems where  ThreadItems.idurl not in(select SeedItems.idurl from SeedItems)')
#    urlfailedrows = cursorf.fetchall()

#    for url in urlfailedrows :
#        print(url)