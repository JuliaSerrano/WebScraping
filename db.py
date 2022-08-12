import sqlite3
from sqlite3 import Error



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
    sql =  ''' INSERT INTO properties(date, retrieved_date, url, mobile, agency, real_estate_id)
              VALUES(?,?,?,?,?,?) '''

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
    sql =  ''' INSERT INTO price_history(price, retrieved_date, createdAt, updatedAt)
              VALUES(?,?,?,?) '''

    c = conn.cursor()
    c.execute(sql,price_history)
    c.commit()
    return c.lastrowid
    

def main():
    database = 'realEstateTracker.db'

    sql_create_properties_table = """ CREATE TABLE IF NOT EXISTS properties(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        date DATETIME,
        retrieved_date DATETIME,
        url TEXT NOT NULL,
        mobile INTEGER,
        agency TEXT,
        real_estate_id INTEGER NOT NULL
    ); """

    
    sql_create_price_history_table=""" CREATE TABLE IF NOT EXISTS price_history(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        price INTEGER,
        retrieved_date DATETIME,
        createdAt DATETIME,
        updatedAt DATETIME,
		FOREIGN KEY(retrieved_date) REFERENCES properties(retrieved_date),
		FOREIGN KEY(id) REFERENCES properties(id)
    ); """


    # create a database connection
    conn = create_connection(database)

    # create tables
    if conn is not None:
        # create properties table
        create_table(conn, sql_create_properties_table)

        #create price_history table
        create_table(conn, sql_create_price_history_table)

    else:
        print("Error! cannot create the database connection.")

    #insert into tables
    
    #create elements to test the functions
        #date, retrieved_date, url, mobile, agency, real_estate_id)
    property = (('2007-01-01 10:00:00','2021-04-02 10:00:00','www.youtube.com',6431345,'Engelk',987643))
    property_id = insert_property(conn,property)
    print(property_id)


if __name__ == '__main__':
    main()



