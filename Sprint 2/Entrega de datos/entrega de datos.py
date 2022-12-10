import psycopg2

conexion = psycopg2.connect(user="postgres",
                              password="2202",
                              host="localhost",
                              port="5432",
                              database="e3")
cursor = conexion.cursor()

cursor.execute('SELECT pg_monto FROM pago ')
pgmonto = cursor.fetchall()

cursor = conexion.cursor()
cursor.execute('SELECT pg_fecha FROM pago ')
pgfecha = cursor.fetchall()

print(pgmonto)
print(pgfecha)