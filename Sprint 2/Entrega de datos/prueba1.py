import psycopg2
import unittest
conexion = psycopg2.connect(user="postgres",
                              password="2202",
                              host="localhost",
                              port="5432",
                              database="e3")
cursor = conexion.cursor()
pgmonto=''
#cursor.execute('SELECT cli_nombre FROM cliente where cli_id=1412; ')
#pgmonto = cursor.fetchall()
def nombrecliente(x):
    cursor.execute('SELECT cli_nombre FROM cliente where cli_id=' + str(x) + '; ')
    pgmonto = cursor.fetchall()
    return(pgmonto)
cursor = conexion.cursor()
cursor.execute('SELECT pg_fecha FROM pago ')
pgfecha = cursor.fetchall()
class TestCalc(unittest.TestCase):
    def test_add(self):
        self.assertEqual(nombrecliente(1410), [('NATURA COSMETICOS',)])
if __name__ == '__main__':
    unittest.main()