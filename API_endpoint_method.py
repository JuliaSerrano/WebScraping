import requests
import pandas as pd
import json
import math


with open('fotocasa_1_alcobendas.json') as f:
    jsondata = json.load(f)




#numero de viviendas
num_viv = jsondata['count']
print(num_viv)

#numero de paginas
num_pags = math.ceil(num_viv/30)
print(num_pags)