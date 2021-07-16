from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

#Coordenadas fuera de rango, cómo hacer para cargar la info de los articulos ?


url2 = "https://www.idealista.com/alquiler-viviendas/madrid/hortaleza/valdebebas-valdefuentes/"
url ="https://www.fotocasa.es/es/alquiler/viviendas/madrid-capital/valdebebas-valdefuentes/l?latitude=40.4907&longitude=-3.6255&combinedLocationIds=724,14,28,173,0,28079,0,678,92"
driver = webdriver.Chrome()

driver.get(url)

#Maximize de window 
driver.maximize_window()


#click accept button
button_accept = driver.find_element_by_xpath("//button[@data-testid='TcfAccept']")
button_accept.click()



# driver.find_element(By.NAME, "q").send_keys(texto_google + Keys.ENTER)


#coordinates to use x and y offset
def get_coordinates(class_name):
    ele= driver.find_element_by_class_name(class_name)
    point = ele.location
    return point
def x_coordinate(class_name):
     point = get_coordinates(class_name)
     return point['x']
     
def y_coordinate(class_name):
    point = get_coordinates(class_name)
    return point['y']

    


#Find each article and get the url 
#Problem: Can't access the href's of articles until they're loaded
    #Solutions:
        #1. Wait until the page is loaded ----> Still can't access
        #2. Scroll to the button ----> Still can't access
        #3. In the loop when obtaining each article, scroll to them
def get_href():

    section = driver.find_element_by_class_name('re-Searchresult')
    articles = section.find_elements_by_xpath("//*[@class='re-Searchresult-itemRow']")
    for article in articles:

        print(article.text)
    #Solution 1 ----> not working
    #wait until the page is loaded, otherwise we can't access the href's of articles
    # try:
    #     myElem = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CLASS_NAME, 're-Searchpage-subtitle')))
    #     print ("Page is ready!")
    # except TimeoutError:
    #     print("Loading took too much time!")
    

    #Page seems to be loaded, but still can't access the href's ---> scroll to the button
    
    #Solution 2 -------> not working 
    # class_name = "re-SharedFooter-legalWrapper"
    # footer = driver.find_element_by_class_name(class_name)
    actions = ActionChains(driver)
    #xoffset, yoffset
    # x = x_coordinate(class_name)
    # y = y_coordinate(class_name)
    # actions.move_to_element_with_offset(footer,x,y).perform()
    #Scroll to the top
    # top = driver.find_element_by_class_name('re-SearchTitle-title')
    # actions.move_to_element
    #WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CLASS_NAME, 're-Card-link')))
    
#Solution 3 ----> xpath for each article isn't working
#Solution 4 ----> keyDown to footer
    
    
    contador = 0
    for article in articles:
        driver.find_element_by_xpath('//body').send_keys(Keys.CONTROL+Keys.END)
        
        #Scroll to the article
        #article_scroll = driver.find_element_by_xpath("/")
        #actions.move_to_element(article_scroll)
        #child_class = article.find_element_by_class_name('re-Card-link')
        child_class = article.find_element_by_xpath("//*[@class='re-Card-link']")
        contador+= 1
        print(contador)
        print(child_class.get_attribute('href'))
    
    
        



get_href()
driver.close()