import sqlite3

conn = sqlite3.connect(
    'scrapy.db',
    timeout=20,
)
conn.row_factory = lambda cursor, row: row[0]

cursor = conn.cursor()
cursor.execute('SELECT threadurl FROM ThreadItems')
urlrows = cursor.fetchall()

cursorf = conn.cursor()
cursorf.execute('select threadurl from ThreadItems where  ThreadItems.idurl not in(select SeedItems.idurl from SeedItems)')
urlfailedrows = cursorf.fetchall()