import json
import math
from request import request

#open and load json from raw response (obtained with insomnia)
# raw = 'fotocasa_1_alcobendas.json'
def open_json(raw_json):

    with open(raw_json) as f:
        jsondata = json.load(f)

    #numero de viviendas
    num_viv = jsondata['count']

    #numero de paginas
    num_pags = math.ceil(num_viv/30)
    return jsondata

#!when functionning only use open_json, not make a request each time

#open and load json from request 
def open_json_request(location,number_pages,query_param,trans_type):
    data = []
    data = request(location,number_pages,query_param,trans_type)
    return data