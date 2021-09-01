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


url = "https://www.fotocasa.es/es/alquiler/viviendas/madrid-capital/san-blas/l?latitude=40.4346&longitude=-3.6117&combinedLocationIds=724,14,28,173,0,28079,0,676,0"



driver = webdriver.Chrome()

driver.get(url)

# Maximize de window
driver.maximize_window()


# click accept button
button_accept = driver.find_element_by_xpath(
    "//button[@data-testid='TcfAccept']")
button_accept.click()

driver.find_element_by_xpath(
                '//body').send_keys(Keys.CONTROL+Keys.END)
time.sleep(1)

def num_pages():
    last = 0
    lis = driver.find_elements_by_class_name('sui-MoleculePagination-item')
    for li in lis:
        child_class = li.find_element_by_class_name(
                'sui-AtomButton-inner').get_attribute("value")
        print(child_class)
        if child_class > last:

            last = child_class
        
    print(last)


num_pages()
driver.close()

