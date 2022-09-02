
# import methods from files
from load_json import open_json, open_json_request
from exports import export_csv, export_excel
from extract_data import extract_data
from db import export_to_db, create_connection, create_table, update_particular


# data to be extracted
url = []
mobile = []
real_estate = []
type_id = []
date = []
real_estate_id = []
price = []
trans_type_id = []
location = []

# dic with query parametres from search
# combinedLocationIds,latitude,longitude
# we need this info to make the request
query_param = {
    "alcobendas": ['724,14,28,167,282,28006,0,0,0', '40.5423', '-3.63104'],
    "majadahonda": ['724,14,28,172,221,28080,0,0,0', '40.4733', '-3.87275'],
    "valdebebas - valdefuentes, madrid capital": ['724,14,28,173,0,28079,0,678,92', '40.4907', '-3.62553'],
    "cercanias valdebebas, madrid": ['724,14,28,173,0,28079,0,668,25', '40.48224', '-3.6165'],
    "sanchinarro": ['724,14,28,173,0,28079,0,678,91', '40.4935', '-3.65437'],
    "las tablas": ['724,14,28,173,0,28079,0,187,11', '40.5043', '-3.67112'],
    "soto de la moraleja": ['724,14,28,167,282,28800,0,3168,0', '40.52467', '-3.64149'],
    "arroyo de la vega": ['724,14,28,167,282,28800,0,3170,0', '40.53585', '-3.62636'],
    "san sebastian de los reyes": ['724,14,28,167,281,28134,0,0,0', '40.5483', '-3.62536'],
    "barajas": ['724,14,28,173,0,28079,0,668,0', '40.468037022265854', '-3.582424716280453'],
    "timon": ['724,14,28,173,0,28079,0,668,25', '40.4846', '-3.59714'],
    "alameda del valle": ['724,14,28,167,250,28003,0,0,0', '40.9178', '-3.8423'],
    "el molar (madrid)": ['724,14,28,167,168,28086,0,0,0', '40.7341', '-3.58141'],
    "la moraleja": ['724,14,28,167,282,28800,0,0,0', '40.51687', '-3.63076'],
    "lozoya": ['724,14,28,167,250,28076,0,0,0', '40.9532', '-3.79199'],
    "pinilla": ['24,14,28,167,250,28112,0,0,0', '40.9282,', '-3.8163'],
    "rascafria": ['724,14,28,167,250,28120,0,0,0', '40.9069', '-3.87959'],
    "soto del real": ['724,14,28,167,167,28144,0,0,0', '40.7542', '-3.7869']
}


def main():
    # scan input from user:
    # while True:
    #     location = input('Which location do you want to scrape?\n').lower()

    #     if(location not in query_param):
    #         print("Invalid location, try again")
    #         continue
    #     else:
    #         print("Valid location")
    #         print('Type the transaction type(number):\n 1:Buy\n 3:Rent')
    #         trans_type = int(input())
    #         number_pages = int(input('What are the number of pages?\n'))
    #         break
    trans_type = [1, 3]
    for key, value in query_param.items():
        for transaction in trans_type:
            data = open_json_request(key, 10, query_param, transaction)

    # request for each page, store in data
    # data = open_json_request(location,number_pages,query_param,trans_type)

    # for each page, extract data and export to excel
    for jsondata in data:
        extract_data(jsondata, url, mobile, real_estate, type_id, date,
                     real_estate_id, price, trans_type_id, location, query_param)
        # print(f"{url}\n")
        # export_csv("./file.csv",url,mobile,real_estate)
    export_excel('todoJunto.xlsx', url, mobile, real_estate, type_id,
                 date, real_estate_id, price, trans_type_id, location)
    print("Location scraped and exported to excel")

    # # #database
    database = 'prices_tracker.db'

    sql_create_properties_table = """ CREATE TABLE IF NOT EXISTS properties(
        id_product INTEGER PRIMARY KEY AUTOINCREMENT,
        retrieved_date DATETIME NOT NULL,
        created_date DATETIME,
        url TEXT NOT NULL,
        mobile INTEGER,
        agency TEXT,
        real_estate_id INTEGER NOT NULL,
        price INTEGER,
        type_id INTEGER,
        trans_type_id INTEGER,
        location TEXT
        
    ); """

    # create a database connection
    conn = create_connection(database)

    # create tables
    if conn is not None:
        # create properties table
        create_table(conn, sql_create_properties_table)

    else:
        print("Error! cannot create the database connection.")

    # insert into tables
    export_to_db(conn, url, mobile, real_estate, date,
                 real_estate_id, price, type_id, trans_type_id, location)
    update_particular(conn)
    print('Data exported to database succesfully')


if __name__ == '__main__':
    main()
