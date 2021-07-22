from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from openpyxl import Workbook
import xlsxwriter
import time
from selenium.common.exceptions import NoSuchElementException

#! Obtener todos los links de una pag                         ---NOT DONE---   error en la iteracion de articulos, solo devuelve el 1º
# Obtener los de las demás páginas                            ---  DONE  ---
#! Filtrar según sean de profesional o de propietario         ---NOT DONE---   filtrar inicialmente, en get_href()
# Exportar links a excel                                      ---  DONE  ---
#! Obtener info. según link proporcionado                     ---NOT DONE---   basic tkinter GUI for: 
#                                                                                          -link de fotocasa a scrapear
#                                                                                          -nombre del archivo excel al que importar info. (se crea uno nuevo cada vez)
#                                                                                           -??
#?Consulta diaria: Se ha añadido alguna casa nueva?
#?          primera idea: como en cada excel pone el numero de casas conseguidas (tkinter output).
#?          solicitar al usuario dichas casas y compararlas con un nuevo scrapeo sobre el mismo link.  (meter en el excel la fecha y el link)



url2 = "https://www.idealista.com/alquiler-viviendas/madrid/hortaleza/valdebebas-valdefuentes/"
url = "https://www.fotocasa.es/es/alquiler/viviendas/madrid-capital/valdebebas-valdefuentes/l?latitude=40.4907&longitude=-3.6255&combinedLocationIds=724,14,28,173,0,28079,0,678,92"
driver = webdriver.Chrome()

driver.get(url)

# Maximize de window
driver.maximize_window()


# click accept button
button_accept = driver.find_element_by_xpath(
    "//button[@data-testid='TcfAccept']")
button_accept.click()





#returns the links of all the articles in one page
def get_href():

    section = driver.find_element_by_class_name('re-Searchresult')
    articles = section.find_elements_by_xpath(
        "//*[@class='re-Searchresult-itemRow']")
    res = []
    
    #Solo me da el primer elemento, arreglar for
    for article in articles:
        
        # scroll down
        driver.find_element_by_xpath(
            '//body').send_keys(Keys.CONTROL+Keys.END)

        # child class which contains the attribute href
        child_class = article.find_element_by_xpath(
            "//*[@class='re-Searchresult-itemRow']/div/div[last()]/a")
        #child_class_aux = article.find_element_by_xpath(
            #   "//*[@class='re-Card-link']")
            
        print(child_class.get_attribute('href'))
        res.append(child_class.get_attribute('href'))

    #print(res)
    


            
  
#scrapes by using get_href() method, and turns to the next
#page (until the last one) and scrapes it 
def pages():
    driver.find_element_by_xpath(
                '//body').send_keys(Keys.CONTROL+Keys.END)
    time.sleep(1)
        
        
    curr_url = driver.current_url
        
    #next page btn to click
    last_li = driver.find_element_by_xpath("//*[@class='sui-MoleculePagination']/li [last()]/a")
        
    #link of the last li
    last_link_li = last_li.get_attribute('href')
        
    while curr_url != last_link_li: #not last page, scrape and turn to the next one
        #get_href()
        print("todavia no estamos en la ultima pag, pasar pag")
        last_li.click()
        
    #last page, scrape and finish
    #get_href()
    print("Hemos llegado a la ultima pag")
    #return res
        
            


def export_excel(title):
    workbook = xlsxwriter.Workbook(title)
    worksheet = workbook.add_worksheet()
    hrefs = get_href()
    row = 0
    col = 0
    index = 1
    i = 0
    while i < len(hrefs):
        worksheet.write(row, col, index)
        worksheet.write(row, col + 1, i)
        row += 1
        index += 1
        i += 1
    workbook.close()



#pages()
get_href()

# print(get_href())
# export_excel("prueba.xlsx")
driver.close()
