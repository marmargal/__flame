from bs4 import BeautifulSoup
from selenium import webdriver


def seleniumFramework(url):
    driver = webdriver.Chrome("C:\Drivers\chromedriver.exe")
    driver.implicitly_wait(30)
    driver.get(url)
    return driver.page_source
    
def get_html(url):
    get_html = BeautifulSoup(seleniumFramework(url), 'lxml')
    return get_html