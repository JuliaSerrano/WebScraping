import sqlite3
from sqlite3 import Error
import datetime


def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return conn


def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)



def insert_property(conn,property):
    """ insert property into the property table
    :param conn: Connection object
    :param property: 
    :return property id
    """
    sql =  ''' INSERT INTO properties(retrieved_date,created_date,url,mobile,agency,real_estate_id,price)
              VALUES(?,?,?,?,?,?,?) '''

    c = conn.cursor()
    c.execute(sql,property)
    conn.commit()
    return c.lastrowid

def insert_price_history(conn,price_history):
    """ insert price_history into price_history table
    :param conn: Connection object
    :param price_history: 
    :return property id
    """
    sql =  ''' INSERT INTO price_history(id_price_date,id_product,retrieved_date,price)
              VALUES(?,?,?,?) '''

    c = conn.cursor()
    c.execute(sql,price_history)
    conn.commit()
    return c.lastrowid





def export_to_db(conn,url,mobile,real_estate,date,real_estate_id,price):
    today_date = datetime.datetime.now().strftime("%Y-%m-%d")
    for i in range(0,len(url)):
        #properties
        property = (today_date,date[i],url[i],mobile[i],real_estate[i],real_estate_id[i],price[i])
        id_product = insert_property(conn,property)

        #id_price_date, id_product,retrieved_date,price)
        price_history = (str(id_product)+today_date,id_product,today_date,price[i])
        insert_price_history(conn,price_history)
        