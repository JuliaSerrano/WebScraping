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

#Obtenidos todos los links de la 1ª pag:
    #Obtener los de las demás páginas
    #Filtrar según sean de profesional o de propietario
    #Exportar links a excel  --DONE--
    #Obtener info. según búsqueda/link proporcionado


url2 = "https://www.idealista.com/alquiler-viviendas/madrid/hortaleza/valdebebas-valdefuentes/"
url ="https://www.fotocasa.es/es/alquiler/viviendas/madrid-capital/valdebebas-valdefuentes/l?latitude=40.4907&longitude=-3.6255&combinedLocationIds=724,14,28,173,0,28079,0,678,92"
driver = webdriver.Chrome()

driver.get(url)

#Maximize de window 
driver.maximize_window()


#click accept button
button_accept = driver.find_element_by_xpath("//button[@data-testid='TcfAccept']")
button_accept.click()




#devuelve true si en la pag hay min una vivienda
#en caso contrario false
def exist_house():
    try:
        child_class = driver.find_element_by_xpath("//*[@class='re-Card-link']")
        child_class.get_attribute('href')
        return True
    except NoSuchElementException:
        return False

    





#Find each article and get the url 
#Problem: Can't access the href's of articles until they're loaded
#Solution: we load the articles by scrolling down 
        
def get_href():

    section = driver.find_element_by_class_name('re-Searchresult')
    articles = section.find_elements_by_xpath("//*[@class='re-Searchresult-itemRow']")
    
    
    res = []
    def get_href_page():
        contador = 0
        for article in articles:
            #scroll down
            driver.find_element_by_xpath('//body').send_keys(Keys.CONTROL+Keys.END)
            #child class which contains the attribute href 
            child_class = article.find_element_by_xpath("//*[@class='re-Card-link']")
            child_class_aux = article.find_element_by_xpath("//*[@class='re-Card-link']")
            contador += 1
            #print(contador)
            #print(child_class.get_attribute('href'))
            res.append(child_class_aux.get_attribute('href'))
    
        

    num = "2"
    url_aux = url
    #There is min 1 house ---> 
    while exist_house():
        get_href_page()
        url_aux.replace("/l?", "/l/" + num + "?")
        print(url_aux)
        driver.get(url_aux)
        #String to int (to add 1)
        num_aux = int(num)
        num_aux += 1
        #int to String 
        num = str(num_aux)
        
    return res















def export_excel(title):
    workbook = xlsxwriter.Workbook(title)
    worksheet = workbook.add_worksheet()
    hrefs = get_href()
    row = 0
    col = 0
    index = 1
    for href in hrefs:
        worksheet.write(row,col,index)
        worksheet.write(row, col + 1, href)
        row+=1
        index+=1
    workbook.close()    
    
    




get_href()
export_excel("prueba.xlsx")
driver.close()