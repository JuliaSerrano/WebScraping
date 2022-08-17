#create stats from the db
import sqlite3
import matplotlib.pyplot as plt
from db import create_connection

def total_prop_location(conn,location):
    sql_total = '''SELECT COUNT(*) FROM properties WHERE location = ?;'''
    c = conn.cursor()
    c.execute(sql_total,[location])
    rows = c.fetchall()
    return rows[0][0]

def perc_buy_rent(conn,location):
    perc_buy = 0
    perc_rent = 0
    sql = '''SELECT COUNT(*) FROM properties WHERE location = ? AND trans_type_id=1;'''
    c = conn.cursor()
    c.execute(sql,[location])
    rows = c.fetchall()
    perc =  ((rows[0][0]/total_prop_location(conn,location))*100)

    #plot
    labels = 'Buy', 'Rent'

    perc_buy = perc
    perc_rent = 100 - perc_buy

    sizes = [perc_buy,perc_rent]
    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, labels=labels, autopct='%1.1f%%',
            shadow=True, startangle=90)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    plt.show()

def majority_agency(conn,location):
    sql = ''' SELECT agency,COUNT(*) FROM properties WHERE location = ?
    GROUP BY agency
    ORDER BY COUNT(*) DESC
    LIMIT    5;'''
    c = conn.cursor()
    c.execute(sql,[location])
    rows = c.fetchall()
    print(rows)

def main():

    database = 'prices_tracker.db'

    # create a database connection
    conn = create_connection(database)

#- [1]  Cual es el porcentaje de viviendas en alquiler/venta
    perc_buy_rent(conn,'Majadahonda')

#- [2]  Agencia mayoritaria en localidad
    majority_agency(conn,'Majadahonda')



main()


""" 





- [ ]  Precio medio en localidad de compra/alquiler

SELECT avg(price) FROM properties WHERE location = 'La Moraleja' AND trans_type_id = 1;
       min(price)
       max(price)

- [ ]  Numero de viviendas que salen a venta/alquiler /mes /semana en zona…

- [ ]  Tiempo que tarda en venderse/alquilarse 

- [ ]  Nuevas viviendas

- [ ]  Viviendas sin agencia en una zona, mostrar datos
SELECT COUNT(*) FROM properties WHERE location = 'Majadahonda' AND type_id = 1

"""