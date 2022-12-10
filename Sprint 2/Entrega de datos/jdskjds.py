import mysql.connector as sql
import pandas as pd

db_connection = sql.connect(host='192.168.1.211', database='sist_boleta', user='root', password='wcs2019.,')
db_cursor = db_connection.cursor()
db_cursor.execute('SELECT * FROM Deuda_Memorial;')

table_rows = db_cursor.fetchall()

df = pd.DataFrame(table_rows)
print(df)