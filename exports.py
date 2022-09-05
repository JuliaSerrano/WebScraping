import pandas as pd
import xlsxwriter
import datetime

# create data frame and export to csv
# name_csv = "./file.csv"


def export_csv(name_csv, url, mobile, real_estate):

    df = pd.DataFrame(
        data={"link": url, "mobile": mobile, "real estate": real_estate})
    df.to_csv(name_csv, sep=',', index=False)
    print(df)


# export to excel, higlight when property not linked to a real estate agency
def export_excel(name_xlsx, url, mobile, real_estate, type_id, date, real_estate_id, price, trans_type_id, location, num_days):
    # open an Excel workbook
    workbook = xlsxwriter.Workbook(name_xlsx)

    # set up a format
    special_format = workbook.add_format(
        properties={'bold': True, 'font_color': 'red'})

    # Create a sheet
    worksheet = workbook.add_worksheet()

    # write headers
    header_format = workbook.add_format(
        properties={'bold': True, 'align': 'centre'})
    worksheet.write(0, 0, 'index', header_format)
    worksheet.write(0, 1, 'url', header_format)
    worksheet.write(0, 2, 'mobile', header_format)
    worksheet.write(0, 3, 'real_estate', header_format)
    worksheet.write(0, 4, 'typeId', header_format)
    worksheet.write(0, 5, 'date', header_format)
    worksheet.write(0, 6, 'retrieved date', header_format)
    worksheet.write(0, 7, 'real estate id', header_format)
    worksheet.write(0, 8, 'price', header_format)
    worksheet.write(0, 9, 'transaction type id', header_format)
    worksheet.write(0, 10, 'location', header_format)
    worksheet.write(0, 11, 'days on sale/rent', header_format)

    today_date = datetime.datetime.now().strftime("%Y-%m-%d")
    # write extracted data
    i = 1
    while i <= len(url):

        # highlight when real estate agency not linked
        if type_id[i-1] == 1:
            # index
            worksheet.write(i, 0, i, special_format)
            # url
            worksheet.write(i, 1, url[i-1], special_format)
            # mobile
            worksheet.write(i, 2, mobile[i-1], special_format)
            # real_estate
            worksheet.write(i, 3, real_estate[i-1], special_format)
            # type_id
            worksheet.write(i, 4, type_id[i-1], special_format)
            # date
            worksheet.write(i, 5, date[i-1], special_format)
            # retrieved date
            worksheet.write(i, 6, today_date, special_format)
            # real estate id
            worksheet.write(i, 7, real_estate_id[i-1], special_format)
            # price
            worksheet.write(i, 8, price[i-1], special_format)
            #transactionTypeId, Buy or Rent
            worksheet.write(i, 9, trans_type_id[i-1], special_format)
            # location
            worksheet.write(i, 10, location[i-1], special_format)
            # days on sale/rent
            worksheet.write(
                i, 11, num_days[i-1], special_format)

        # write as normal format when real estate agency already linked
        else:
            # index
            worksheet.write(i, 0, i)
            # url
            worksheet.write(i, 1, url[i-1])
            # mobile
            worksheet.write(i, 2, mobile[i-1])
            # real_estate
            worksheet.write(i, 3, real_estate[i-1])
            # type_id
            worksheet.write(i, 4, type_id[i-1])
            # date
            worksheet.write(i, 5, date[i-1])
            # retrieved date
            worksheet.write(i, 6, today_date)
            # real estate id
            worksheet.write(i, 7, real_estate_id[i-1])
            # price
            worksheet.write(i, 8, price[i-1])
            #transactionTypeId, Buy or Rent
            worksheet.write(i, 9, trans_type_id[i-1])
            # location
            worksheet.write(i, 10, location[i-1])
            # days on sale/rent
            worksheet.write(i, 11, num_days[i-1])
        i += 1

    workbook.close()
