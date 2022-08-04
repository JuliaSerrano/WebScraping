import pandas as pd
import xlsxwriter

#create data frame and export to csv
# name_csv = "./file.csv"
def export_csv(name_csv,url,mobile,real_estate):

    df = pd.DataFrame(data={"link":url,"mobile":mobile,"real estate":real_estate})
    df.to_csv(name_csv, sep=',',index=False)
    print(df)


#export to excel, higlight when property not linked to a real estate agency
def export_excel(name_xlsx,url,mobile,real_estate,number_pages):
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

        #write as normal format when real estate agency already linked
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

        
