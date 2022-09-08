import sqlite3
from sqlite3 import Error
from datetime import datetime, date


def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)

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
    sql = ''' INSERT INTO properties(retrieved_date,created_date,url,mobile,agency,real_estate_id,price,type_id,trans_type_id,location,num_days,updated_date)
              VALUES(?,?,?,?,?,?,?,?,?,?,?,?) '''

    c = conn.cursor()
    c.execute(sql, property)
    conn.commit()
    return c.lastrowid


def update_particular(conn):
    sql = '''  UPDATE properties SET agency = 'Particular' WHERE type_id = 1; '''
    c = conn.cursor()
    c.execute(sql)
    conn.commit()

# output boolean    T: property already in db


def exist_db(conn, prop):
    sql = '''SELECT COUNT(1) FROM properties WHERE url = ?;'''
    c = conn.cursor()
    c.execute(sql, [prop[2]])
    rows = c.fetchall()
    # property doesn't exist
    if(rows[0][0] < 1):
        return False
    # property exists
    return True


# output boolean     T:diff price
def change_price(conn, prop):
    sql = '''SELECT price FROM properties WHERE url = ?;'''
    c = conn.cursor()
    c.execute(sql, [prop[2]])
    rows = c.fetchall()
    # same price
    if(rows[0][0] == prop[6]):
        return False
    # diff price
    return True

# output: created_date of a prop, given by the url


def get_created_date(conn, prop):
    sql = '''SELECT created_date FROM PROPERTIES WHERE url = ?'''
    c = conn.cursor()
    c.execute(sql, [prop[2]])
    rows = c.fetchall()
    return rows[0][0]


def update_prop(conn, prop):

    c = conn.cursor()

    # num days since created_date (original, may be changed when update)
    today = datetime.now()
    date_time_obj = datetime.strptime(get_created_date(conn, prop), '%Y-%m-%d')
    num_days = ((today - date_time_obj).days)

    # if same price -> update retrieved_date,num days on sale/rent
    if(change_price(conn, prop) == False):
        # print(
        #     f'same price, update retrieved_date: {prop[0]}, num_days: {prop[10]}, where url: {prop[2]}')
        sql_samep = '''UPDATE properties SET retrieved_date = ?, num_days = ?, updated_date = ? WHERE url = ?'''
        c.execute(sql_samep, [prop[0], num_days, prop[1], prop[2]])
    # if diff price -> update retrieved_date, price and num_days
    else:
        # print(
        #     f'diff price, update retrieved_date: {prop[0]}, price: {prop[6]}, num_days: {prop[10]} where url: {prop[2]}')
        sql_diffp = '''UPDATE properties SET retrieved_date = ?,price = ?, num_days = ?, updated_date = ? WHERE url = ?'''
        c.execute(sql_diffp, [prop[0], prop[6], num_days, prop[1], prop[2]])
    conn.commit()


def export_to_db(conn, url, mobile, real_estate, date, real_estate_id, price, type_id, trans_type_id, location, num_days):
    today_date = datetime.now().strftime("%Y-%m-%d")
    for i in range(0, len(url)):
        # properties
        """ 
        prop[0] = today_date
        prop[1]= date
        prop[2]= url
        prop[3]= mobile
        prop[4]= real_estate
        prop[5]= real_estate_id
        prop[6]= price
        prop[7]= type_id
        prop[8]= trans_type_id
        prop[9]= location
        prop[10]= num_days
        prop[11]= date
         """
        prop = (today_date, date[i], url[i], mobile[i], real_estate[i],
                real_estate_id[i], price[i], type_id[i], trans_type_id[i], location[i], num_days[i], date[i])
        # new property
        if(exist_db(conn, prop) == False):
            insert_property(conn, prop)

        # already in db -> update prop (not store again)
        else:
            update_prop(conn, prop)
