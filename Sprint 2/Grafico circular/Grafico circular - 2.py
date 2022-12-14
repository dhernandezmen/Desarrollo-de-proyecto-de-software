import matplotlib.pyplot as plt
import psycopg2 as pg
import pandas.io.sql as psql
import numpy as np

connection = pg.connect(user="postgres",
                              password="2202",
                              host="localhost",
                              port="5432",
                              database="e3")
def grafico3():
    col2 = []
    dataframe3 = psql.read_sql('SELECT * FROM reporte_cliente', connection)

    for a in dataframe3['ge_id']:
        col2.append(1)

    dataframe3.insert(1, "val1", col2, True)
    #Suma las gestiones segun cliente
    del dataframe3['es_nombre']
    del dataframe3['sub_tipo']

    df3=dataframe3.groupby(['cli_nombre'], as_index =False).sum()
    print(df3)

    #GRAFICO Circulo
    names = df3['cli_nombre']
    size = df3['val1']

    # Create a circle at the center of the plot
    my_circle = plt.Circle((0, 0), 0.7, color='white')

    # Give color names
    plt.pie(size, labels=names, colors=['red', 'green', 'blue', 'skyblue'])
    p = plt.gcf()
    p.gca().add_artist(my_circle)

    # Show the graph
    plt.show()

grafico3()
connection.close()