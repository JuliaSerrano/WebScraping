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


def insert_property(conn, property):
    """ insert property into the property table
    :param conn: Connection object
    :param property: 
    :return property id
    """
    sql = ''' INSERT INTO properties(retrieved_date,created_date,url,mobile,agency,real_estate_id,price,type_id,trans_type_id,location,num_days)
              VALUES(?,?,?,?,?,?,?,?,?,?,?) '''

    c = conn.cursor()
    c.execute(sql, property)
    conn.commit()
    return c.lastrowid


def update_particular(conn):
    sql = '''  UPDATE properties SET agency = 'Particular' WHERE type_id = 1; '''
    c = conn.cursor()
    c.execute(sql)
    conn.commit()


def export_to_db(conn, url, mobile, real_estate, date, real_estate_id, price, type_id, trans_type_id, location, num_days):
    today_date = datetime.datetime.now().strftime("%Y-%m-%d")
    for i in range(0, len(url)):
        # properties
        prop = (today_date, date[i], url[i], mobile[i], real_estate[i],
                real_estate_id[i], price[i], type_id[i], trans_type_id[i], location[i], num_days[i])
        id_product = insert_property(conn, prop)
    return id_product
