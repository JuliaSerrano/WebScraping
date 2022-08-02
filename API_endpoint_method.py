import requests
import pandas as pd
import json
import math
from request import request

link = 'https://www.fotocasa.es'



#open and load json from raw responde (obtained with insomnia)
with open('fotocasa_1_alcobendas.json') as f:
    jsondata = json.load(f)


#numero de viviendas
num_viv = jsondata['count']

#numero de paginas
num_pags = math.ceil(num_viv/30)

# data = request(num_pags)
# jsondata = data[0]


#data to extract
url =[]
mobile = []
real_estate = []

#iterate for each property
for home in jsondata['realEstates']:
    #extract url
    url.append(link + home['detail']['es'])

    #extract mobile
    mobile.append(home['advertiser']['phone'])

    #extract real estate
    real_estate.append(home['advertiser']['clientAlias'])

#create data frame and export to csv
df = pd.DataFrame(data={"link":url,"mobile":mobile})
df.to_csv("./file.csv", sep=',',index=False)
print(df)


