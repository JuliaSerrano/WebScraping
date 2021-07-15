import pickle
from selenium import webdriver
import time


url = "https://www.idealista.com/alquiler-viviendas/madrid/hortaleza/valdebebas-valdefuentes/"

driver = webdriver.Chrome()

driver.get(url)

def cookies(url):
    #open ----> open 'filename' to write in binary mode (wb)
    #.dump ----> pickle an object and saves it in 'oufile'
    
    filename = 'cookies.pkl'
    outfile = open(filename,"wb")
    pickle.dump(driver.get_cookies() , outfile)



#load cookies to avoid the captcha
def load_cookies(filename):
    cookies = pickle.load(open(filename, "rb"))
    for cookie in cookies:
        driver.add_cookie(cookie)
