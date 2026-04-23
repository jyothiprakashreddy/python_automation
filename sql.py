import pymysql

conn = pymysql.connect(
    host = 'localhost',
    user = 'root',
    password = 'root',
)
print('connected')