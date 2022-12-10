# library
import psycopg2 as pg
import matplotlib.pyplot as plt
import pandas.io.sql as psql
connection = pg.connect(user="postgres",
                              password="2202",
                              host="localhost",
                              port="5432",
                              database="e3")
dataframe = psql.read_sql('SELECT * FROM reporte_cliente', connection)
print(dataframe)
# create data
names = ['groupA', 'groupB', 'groupC', 'groupD']
size = [12, 11, 3, 30]

# Create a circle at the center of the plot
my_circle = plt.Circle((0, 0), 0.7, color='white')

# Give color names
plt.pie(size, labels=names, colors=['red', 'green', 'blue', 'skyblue'])
p = plt.gcf()
p.gca().add_artist(my_circle)

# Show the graph
plt.show()