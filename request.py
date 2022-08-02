import requests

data = []
url = "https://api.fotocasa.es/PropertySearch/Search"

#makes a request for each page, returning json/page
def request(number_pages):

    for x in range(1,number_pages+1):
        querystring = {
        "combinedLocationIds":"724,14,28,167,282,28006,0,0,0",
        "culture":"es-ES",
        "hrefLangCultures":"ca-ES;es-ES;de-DE;en-GB",
        "isMap":"false",
        "isNewConstructionPromotions":"false",
        "latitude":"40.5423",
        "longitude":"-3.63104",
        "pageNumber":f"{number_pages}",
        "platformId":"1",
        "sortOrderDesc":"true",
        "sortType":"scoring",
        "transactionTypeId":"1",
        "propertyTypeId":"2"
        }

        payload = ""
        headers = {
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:101.0) Gecko/20100101 Firefox/101.0",
            "Accept": "application/json, text/plain, */*",
            "Accept-Language": "en-US,en;q=0.5",
            "Accept-Encoding": "gzip, deflate, br",
            "Referer": "https://www.fotocasa.es/",
            "Origin": "https://www.fotocasa.es",
            "Connection": "keep-alive",
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-site",
            "TE": "trailers"
        }

        r = requests.request("GET", url, data=payload, headers=headers, params=querystring)

        data.append(r.json()) 

    return data  



