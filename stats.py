#create stats from the db
import sqlite3
import matplotlib.pyplot as plt
from db import create_connection

#- [1]  Percentage of properties open for buy/rent in a location

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

#- [2]  Majority agency in a location
def majority_agency(conn,location,num):
    sql = ''' SELECT agency,COUNT(*) FROM properties WHERE location = ?
    GROUP BY agency
    ORDER BY COUNT(*) DESC
    LIMIT ?;'''
    c = conn.cursor()
    c.execute(sql,[location,num])
    rows = c.fetchall()
    print(rows)

    #plot
    labels = []
    sizes = []
    for agency in rows:
        #agency name
        labels.append(agency[0])
        #number of properties with this agency
        sizes.append(agency[1]) 

    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, labels=labels, autopct='%1.1f%%',
            shadow=True, startangle=90)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    plt.show()   

#- [3] Average price of sell/rent in location (1 -> Sell, 3 -> Rent)
def avg_price(conn,location,trans_type):
    sql = '''SELECT avg(price) FROM properties WHERE location =? AND trans_type_id = ?;'''
    c = conn.cursor()
    c.execute(sql,[location,trans_type])
    rows =c.fetchall()

    #format currency output 
    fractional_separator = ","  
    currency = "€{:,.2f}".format(rows[0][0])
    main_currency, fractional_currency = currency.split(".")[0], currency.split(".")[1]
    new_main_currency = main_currency.replace(",", ".")
    currency = new_main_currency + fractional_separator + fractional_currency
    print(currency)

#- [4]  Properties with agency not linked in a location
def no_agency(conn,location,trans_type):
    sql = '''SELECT DISTINCT url,price FROM properties WHERE location = ? AND type_id = ? '''
    c = conn.cursor()
    c.execute(sql,[location,trans_type])
    rows = c.fetchall()
    for row in rows:
        print('{0:<10} {1:>8}€'.format(*row))





def main():

    database = 'prices_tracker.db'

    # create a database connection
    conn = create_connection(database)

# - [1]  Percentage of properties open for buy/rent in a location
    perc_buy_rent(conn,'Majadahonda')

#- [2]  Majority agency in a location
    majority_agency(conn,'Majadahonda',10)

#- [3]  Average price of sell/rent in location (1 -> Sell, 3 -> Rent)
    avg_price(conn,'Majadahonda',3)

#- [4]  Properties with agency not linked in a location
    no_agency(conn,'Majadahonda',1)




if __name__ == '__main__':
    main()


""" 
More stats to be added...
- [ ]  Numero de viviendas que salen a venta/alquiler /mes /semana en zona…

- [ ]  Tiempo que tarda en venderse/alquilarse 

- [ ]  Nuevas viviendas/viviendas mas recientes

"""