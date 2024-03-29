import requests
import json
import pandas as pd
import brotlicffi
import brotli
import gzip
from io import BytesIO
import zlib

data = []
url = "https://web.gw.fotocasa.es/v2/propertysearch/search?"

# makes a request for each page, returning json/page


def request(location, number_pages, query_param, trans_type):

    # change majadahonda por zona elegida
    for x in range(1, number_pages+1):
        querystring = {
            "combinedLocationIds": f"{query_param[location][0]}",
            "culture": "es-ES",
            "hrefLangCultures": "ca-ES;es-ES;de-DE;en-GB",
            "isMap": "false",
            "isNewConstructionPromotions": "false",
            "latitude": f"{query_param[location][1]}",
            "longitude": f"{query_param[location][2]}",
            "pageNumber": f"{x}",
            "platformId": "1",
            "sortOrderDesc": "true",
            "sortType": "scoring",
            "transactionTypeId": f"{trans_type}",
            "propertyTypeId": "2"
        }

        payload = ""
        headers = {
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/110.0",
            "Accept": "application/json, text/plain, */*",
            "Accept-Language": "en-US,en;q=0.5",
            "Accept-Encoding": "gzip, deflate, br",
            "Origin": "https://www.fotocasa.es",
            "Connection": "keep-alive",
            "Referer": "https://www.fotocasa.es/",
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-site",
            "Pragma": "no-cache",
            "Cache-Control": "no-cache",
            "TE": "trailers"
        }

        r = requests.request("GET", url, data=payload,
                             headers=headers, params=querystring)
        data.append(r.json())
    return data
