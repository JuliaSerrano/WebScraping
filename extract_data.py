

link = 'https://www.fotocasa.es'

def extract_data(jsondata,url,mobile,real_estate,type_id,date,real_estate_id,price,trans_type_id,location,query_param):

    
    #iterate for each property
    for home in jsondata['realEstates']:
        #extract url
        url.append(link + home['detail']['es'])

        #extract mobile
        mobile.append(home['advertiser']['phone'])

        #extract real estate
        real_estate.append(home['advertiser']['clientAlias'])

        #type id (if 1 -> agency notlinked)
        type_id.append(home['advertiser']['typeId'])

        #date after T, it gets time. Only get date
        date.append((home['date']).partition("T")[0])

        #extract real estate id
        real_estate_id.append((home['id']))

        #extract price
        price.append(int(home['transactions'][0]['value'][0]))

        #transactionTypeId
        #1 -> Buy  3 -> Rent
        trans_type_id.append(home['transactions'][0]['transactionTypeId'])

        #location
        level5 =  home['address']['location']['level5']
        if level5 ==  " Madrid Capital":
            level7 = home['address']['location']['level7']
            location.append(level7)
        else:
            location.append(level5)



        
