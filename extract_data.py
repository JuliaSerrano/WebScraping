

link = 'https://www.fotocasa.es'

def extract_data(jsondata,url,mobile,real_estate,type_id,date):

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


