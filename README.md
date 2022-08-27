# Scraping Real Estate Properties
This web scraping project extracts real estate properties data from a given location by the API endpoint method.

All the data retrieved is extracted to an excel workbook and inserted to a database which is previously created.

## More in depth...

The API endpoint method directly gets the JSON data that is being sent from the server by making a request. 

I've used [Insomnia](https://github.com/Kong/insomnia) to check the query parameters needed to make the request and to get a preview of the response.

This project is divided in different files:

- [API Endpoint Method](API_endpoint_method.py)

    It's the main file. All the query parameters of the locations chosen are stored here, if you want to scrape another location, the parameters of this location will need to be added.

- [Request](request.py)

    It makes a GET request for the location given (by the query parameters), returning a json for each page.

- [Load Json](load_json.py) 

    This file consists of two methods:

    - `open_json`

    It opens and loads a json from the raw response exported from insomnia, instead of making a request.
    This method is created for test purposes, to avoid bombarding the web with requests. 

    - `open_json_request`

    It makes a request and loads the json response.

- [Extract Data](extract_data.py)

    It extracts from the jsondata:
    - Url of the property
    - Mobile
    - Real Estate Agency if apply
    - Type ID (to know if an agency is linked)
    - Date
    - Real Estate ID
    - Price
    - Transaction Type ID (to know if the property is open for sell or rent)
    - Location

- [Exports](exports.py)

    This file consists of two methods:

    - `export_csv`

    It exports the data retrieved to .csv file
    
    - `export_excel`

    It exports the data retrieved to .xlsx file

- [Database](db.py)

It creates a database connection to the SQLite database specified by a databse file, creates a table if not created and inserts the properties extracted.

## Quickstart


1. [Fork](https://docs.github.com/en/get-started/quickstart/fork-a-repo) and [Clone](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository) this repository and navigate into it
```
cd WebScraping
```

2. Install the dependencies
```
pip install -r requirements.txt
```

3. Run the script
```
python3 API_endpoint_method.py
```

