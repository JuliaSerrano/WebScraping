#create stats from the db
import sqlite3
from db import create_connection

def total_prop_location(conn,location):
    sql_total = '''SELECT COUNT(*) FROM properties WHERE location = ?;'''
    c = conn.cursor()
    c.execute(sql_total,[location])
    rows = c.fetchall()
    return rows[0][0]

def perc_buy_rent(conn,trans_type,location):
    sql = '''SELECT COUNT(*) FROM properties WHERE location = ? AND trans_type_id=?;'''
    c = conn.cursor()
    c.execute(sql,[location,trans_type])
    rows = c.fetchall()
    return rows[0][0]

def main():

    database = 'prices_tracker.db'

    # create a database connection
    conn = create_connection(database)
    total = total_prop_location(conn,'Majadahonda')
    num = perc_buy_rent(conn,1,'Majadahonda')
    print(f"{(num/total)*100}%")


main()
""" 
- [ ]  Cual es el porcentaje de viviendas en alquiler/venta

sql = SELECT COUNT(*) FROM properties WHERE location = 'Majadahonda' AND trans_type_id=3;
SELECT COUNT(*) FROM properties WHERE location = 'Majadahonda' AND trans_type_id=1;

- [ ]  Agencia mayoritaria en localidad
SELECT       agency
    FROM     properties
	WHERE    location = 'Alcobendas' AND trans_type_id = 3
    GROUP BY agency
    ORDER BY COUNT(*) DESC
    LIMIT    5;


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