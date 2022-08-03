import requests
import pandas as pd
import json
import math
from request import request
import xlsxwriter

link = 'https://www.fotocasa.es'

#data to extract
url =[]
mobile = []
real_estate = []

#number of pages
num_pags = -1

#open and load json from raw responde (obtained with insomnia)
# raw = 'fotocasa_1_alcobendas.json'
def open_json(raw_json):

    with open(raw_json) as f:
        jsondata = json.load(f)

    #numero de viviendas
    num_viv = jsondata['count']

    #numero de paginas
    num_pags = math.ceil(num_viv/30)
    return jsondata
    # data = request(num_pags)
    # jsondata = data[0]

def extract_data(jsondata,url,mobile,real_estate):

    #iterate for each property
    for home in jsondata['realEstates']:
        #extract url
        url.append(link + home['detail']['es'])

        #extract mobile
        mobile.append(home['advertiser']['phone'])

        #extract real estate
        real_estate.append(home['advertiser']['clientAlias'])


#create data frame and export to csv
# name_csv = "./file.csv"
def export_csv(name_csv,url,mobile,real_estate):

    df = pd.DataFrame(data={"link":url,"mobile":mobile,"real estate":real_estate})
    df.to_csv(name_csv, sep=',',index=False)
    print(df)


#export to excel, higlight when property not linked to a real estate agency
def export_excel(name_xlsx,url,mobile,real_estate):
    # open an Excel workbook
    workbook = xlsxwriter.Workbook(name_xlsx)

    # set up a format
    special_format = workbook.add_format(properties={'bold': True, 'font_color': 'red'})

    # Create a sheet
    worksheet = workbook.add_worksheet()

    #write headers
    worksheet.write(0,0,'index')
    worksheet.write(0,1,'url')
    worksheet.write(0,2,'mobile')
    worksheet.write(0,3,'real_estate')   

    #write extracted data
    i = 1
    while i <= len(url):

        #highlight when real estate agency not linked
        if not real_estate[i-1]:
            #index
            worksheet.write(i,0,i,special_format)
            #url
            worksheet.write(i,1,url[i-1],special_format)
            #mobile
            worksheet.write(i,2,mobile[i-1],special_format)
            #real_estate
            worksheet.write(i,3,real_estate[i-1],special_format)

        #write as normal format
        else:
            #index
            worksheet.write(i,0,i)

            #url
            worksheet.write(i,1,url[i-1])

            #mobile
            worksheet.write(i,2,mobile[i-1])

            #real_estate
            worksheet.write(i,3,real_estate[i-1])

        i += 1
    workbook.close()

        




def main():
    jsondata = open_json('fotocasa_1_alcobendas.json')
    extract_data(jsondata,url,mobile,real_estate)
    # export_csv("./file.csv",url,mobile,real_estate)
    export_excel('file.xlsx',url,mobile,real_estate)
    
if __name__ == '__main__':
    main()