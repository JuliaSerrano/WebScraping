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




url = "https://www.fotocasa.es/es/alquiler/viviendas/madrid-capital/valdebebas-valdefuentes/l?latitude=40.4907&longitude=-3.6255&combinedLocationIds=724,14,28,173,0,28079,0,678,92"



driver = webdriver.Chrome()

driver.get(url)

time.sleep(5)
# Maximize de window
driver.maximize_window()


# click accept button
button_accept = driver.find_element_by_xpath(
    "//button[@data-testid='TcfAccept']")
button_accept.click()


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
    print(len(articles))
    
    
    #array with all the href's scraped
    
    
    #scroll down to find xpath of articles (otherwise, can't access)
    driver.find_element_by_xpath(
            '//body').send_keys(Keys.CONTROL+Keys.END)

    count = 0
    body = driver.find_element_by_css_selector('body')
    body.send_keys(Keys.PAGE_DOWN)
    for article in articles:
          
        time.sleep(3)
          

            #child class which contains the attribute href

        try:
            child_class = article.find_element_by_css_selector(
                'div > div > a')
            
        #Some of the articles may not been activated when scrolling down,
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
          

        
        
        
        
    print(res)
    #print(len(res))
    return res

            
  

#scrapes by using get_href() method, and turns to the next
#page (until the last one) and scrapes it 
def pages():
    driver.find_element_by_xpath(
                '//body').send_keys(Keys.CONTROL+Keys.END)
    time.sleep(1)
        
        
    curr_url = driver.current_url
    lis = driver.find_elements_by_class_name('sui-MoleculePagination-item')
    num_lis = len(lis)
    time.sleep(1)
    #next page btn to click
    last_li = driver.find_element_by_xpath("//*[@class='sui-MoleculePagination']/li [last()]/a")
    #link of the last li
    last_link_li = last_li.get_attribute('href')
    finished = False
    while not finished :
        if(curr_url == last_link_li): #estamos en la ultima pag
            print("Last page")
            get_href()
            finished = True
        else:
            print("not last page")
            get_href()
            driver.get(last_link_li)
            time.sleep(1)
            curr_url = driver.current_url
        
    print(res) 
    
    
   # btn_next = driver.find_element_by_class_name("//*[@class='sui-LinkBasic sui-AtomButton sui-AtomButton--primary sui-AtomButton--outline sui-AtomButton--center sui-AtomButton--small sui-AtomButton--link sui-AtomButton--empty']").get_attribute('href')
   # while curr_url != last_link_li: #not last page, scrape and turn to the next one
    #    get_href()
     #   print("todavia no estamos en la ultima pag, pasar pag")
      #  last_li.click()
       # curr_url = driver.current_url
        
        #last_li = driver.find_element_by_xpath("//*[@class='sui-MoleculePagination']/li [last()]/a")
        
    #last page, scrape and finish
    #get_href()
    #print("Hemos llegado a la ultima pag")
    #return res
        
            


def export_excel(title):
    workbook = xlsxwriter.Workbook(title)
    worksheet = workbook.add_worksheet()
    hrefs = pages()
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




#pages()


#get_href()
export_excel("prueba.xlsx")





driver.close()