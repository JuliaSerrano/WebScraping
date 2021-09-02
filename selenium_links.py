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
import requests
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options


# Obtener todos los links de una pag                          ---- DONE  ---   
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




url = "https://www.fotocasa.es/es/alquiler/viviendas/la-moraleja/todas-las-zonas/l?latitude=40.5169&longitude=-3.6308&combinedLocationIds=724,14,28,167,282,28800,0,0,0"



driver = webdriver.Chrome()

driver.get(url)

time.sleep(5)
# Maximize de window
driver.maximize_window()


# click accept button
button_accept = driver.find_element_by_xpath(
    "//button[@data-testid='TcfAccept']")
button_accept.click()

#array result which is going to contain all the links
res = []


#returns the links of all the articles in one page
def get_href():

    #when NoSuchElementException, need 'element' for moving to it,
    # then xpath of child_class is found. No longer Exception.
    element = driver.find_element_by_class_name('re-SharedTopbar')
    action = ActionChains(driver)
    

    #articles we're going to get the href from
    articles = driver.find_elements_by_xpath(
        "//*[@class='re-Searchresult-itemRow re-Searchresult-itemRow--collageAYCE re-Searchresult-itemRow--simple']")
    
    
    
    #array with all the href's scraped
    
    
    #scroll down to find xpath of articles (otherwise, can't access)
    driver.find_element_by_xpath(
            '//body').send_keys(Keys.CONTROL+Keys.END)

    count = 1
    body = driver.find_element_by_css_selector('body')
    body.send_keys(Keys.PAGE_DOWN)
    for article in articles:
          
        time.sleep(3)
        
        try:
            #child class which contains the attribute href
            child_class = article.find_element_by_css_selector(
                'div > div > a')
            
        #Some of the articles may not have been activated when scrolling down,
        #so we scroll up
        except NoSuchElementException:
            print("NoSuchElementException")
            time.sleep(2)
            action.move_to_element(element).perform()
            driver.find_element_by_xpath(
            '//body').send_keys(Keys.CONTROL+Keys.END)
            time.sleep(3)    
        else:       
            href =  child_class.get_attribute('href')
            print(href)
            res.append(href)
            print("href appended " + str(count))
            count += 1
          

        
        
        
        
    
    return res

            
  

#scrapes each page by using get_href() method
def pages():
    
    driver.find_element_by_xpath(
                '//body').send_keys(Keys.CONTROL+Keys.END)
    time.sleep(1)

    #next page btn to click
    last_li = driver.find_element_by_xpath("//*[@class='sui-MoleculePagination']/li [last()]/a")
    
    #link of the last li
    last_link_li = last_li.get_attribute('href')
    
    page = 1
    for i in range(num_pages()):
        print("We're on page : ")
        print(page)
        
        #scrape
        get_href()
        
        #next page
        driver.get(last_link_li)
        time.sleep(1)
        page+= 1
        
    print(res) 
    
    

        
#exports to excel res with each link in a row
def export_excel(title):
    workbook = xlsxwriter.Workbook(title)
    worksheet = workbook.add_worksheet()
    pages()
    hrefs = res
    row = 0
    col = 0
    index = 1
    i = 0
    while i < len(hrefs):
        worksheet.write(row, col, index)
        worksheet.write(row, col + 1, hrefs[i])
        row += 1
        index += 1
        i += 1
    workbook.close()


#returns the number of pages the link has, so we can turn and scrape each one
def num_pages():
    driver.find_element_by_xpath(
                '//body').send_keys(Keys.CONTROL+Keys.END)
    time.sleep(1)
    last_page = driver.find_element_by_xpath("//*[@class='sui-MoleculePagination']/li [last()-1]/a/span")
    return int(last_page.text)
    





#get_href()
export_excel("LaMoraleja.xlsx")

#num_pages()




driver.close()