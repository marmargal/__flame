'''
Created on 9 feb. 2019

@author: inmam
'''
from bs4 import BeautifulSoup
from selenium import webdriver;import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

urlLefties = "https://www.lefties.com/es/#woman"

driver = webdriver.Chrome("C:\Drivers\chromedriver.exe")
driver.implicitly_wait(30)
driver.get(urlLefties)

soup = BeautifulSoup(driver.page_source, 'lxml')

# for item in soup.find_all(class_="sidemenu-list-item parent"):#, attrs="href"): ## ENLACES
#     print(item.get('a').get('href'))

def obtener_enlaces_Lefties():
    
    res = []

    for item in soup.find_all("li", attrs={"class":"sidemenu-list-item parent"}):
        for a in item.find_all("a"):
            nombre = a.get_text()
            enlace = a.get('href')
            res.append([nombre,enlace])
            

    for i in res: print(i)
    return res;

obtener_enlaces_Lefties()
        

# for items in wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".sidemenu-list-item"))):
#     link = items.find_element_by_css_selector(".reviewdata a")
#     link.click()
#     time.sleep(2)
# 
# soup = BeautifulSoup(driver.page_source,"lxml")
# print(soup)

# for item in wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".sidemenu-list-item"))):
#     link = item.get_attribute("href")
#     link.click()
#     time.sleep(2)
#     
#     print(link)

#     name = item.find_element_by_css_selector("p a").text
#     review_title = item.find_element_by_css_selector("strong a[id^=ctl00_ctl00_ContentPlaceHolderFooter_ContentPlaceHolderBody_rptreviews]").text
#     review_data = ' '.join([' '.join(items.text.split()) for items in item.find_elements_by_css_selector(".reviewdata")])
#     print("Name: {}\nReview_Title: {}\nReview_Data: {}\n".format(name, review_title, review_data))

# driver.quit()