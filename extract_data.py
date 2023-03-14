from datetime import datetime, date

link = 'https://www.fotocasa.es'


def extract_data(jsondata, url, mobile, real_estate, type_id, created_date, real_estate_id, price, trans_type_id, location, num_days):
    if 'realEstates' not in jsondata:
        return
    # iterate for each property
    for home in jsondata['realEstates']:
        # extract url
        url.append(link + home['detail']['es'])

        # extract mobile
        mobile.append(home['advertiser']['phone'])

        # extract real estate
        real_estate.append(home['advertiser']['clientAlias'])

        # type id (if 1 -> agency notlinked)
        type_id.append(home['advertiser']['typeId'])

        # date after T, it gets time. Only get date
        created_date.append((home['date']).partition("T")[0])

        # extract real estate id
        real_estate_id.append((home['id']))

        # extract price
        price.append(int(home['transactions'][0]['value'][0]))

        # transactionTypeId
        # 1 -> Buy  3 -> Rent
        trans_type_id.append(home['transactions'][0]['transactionTypeId'])

        # location
        level5 = home['address']['location']['level5']
        level7 = home['address']['location']['level7']
        level8 = home['address']['location']['level8']

        if level5 == " Madrid Capital":
            if level7 == "Hortaleza" or level7 == "Fuencarral - El Pardo":
                location.append(level8)
            elif level8 == "Timón":
                location.append(level8)
            else:
                location.append(level7)

        elif level5 == "La Moraleja" and level7 == "Arroyo de la Vega":
            location.append(level7)
        else:
            location.append(level5)

        # num days on sale/rent
        today = datetime.now()
        date_time_obj = datetime.strptime(created_date[-1], '%Y-%m-%d')
        num_days.append((today - date_time_obj).days)
