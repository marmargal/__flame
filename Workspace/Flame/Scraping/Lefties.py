import re
import json
import string
import sys
#from PyQt4 import QtGui
from bs4 import BeautifulSoup
from pip._vendor import requests


prendaLefties = "https://www.lefties.com/es/women/novedades-woman/camiseta-mickey-c1029507p501184069.html"
prendaHM = "https://www2.hm.com/es_es/productpage.0651110001.html"
prendaZara = "https://www.zara.com/es/es/cazadora-acolchada-estampado-animal-p04968020.html?v1=7781001&v2=1074507"

urlLefties = "https://www.lefties.com/es/#woman"


# javascript
def obtener_prenda(urlPrenda):
    req = requests.get(urlPrenda)
    data = req.text
    get_html = BeautifulSoup(data,'html.parser')
    
    prenda = []
    return prenda


def obtener_todas_las_prendas(urlWeb):
    req = requests.get(urlWeb)
    data = req.text
    get_html = BeautifulSoup(data,'html.parser')
    
    res = [] # almacenamos las URLS
    
#     for i in get_html.find_all("script", type="text/javascript"):
#         print i
#         print ("=======================================")
#     script = get_html.html.find_next_sibling('script', re.compile(r"\$\(document\)\.ready"))
#     pattern = re.compile("(\w+): '(.*?)'")
#     fields = dict(re.findall(pattern, script.text))
#     print fields['woman']
    
    #"sidemenu-list-item new-collection parent"
    #"sidemenu-list-item"
    for i in get_html.find_all(class_="sidemenu-list-item new-collection parent"):
        print (i.gettext())
      
    for r in res:
        print r
    print res
    return res

obtener_todas_las_prendas(urlLefties)

# div id = "product-container"
# por el json del javascript
def obtener_prenda_lefties(urlPrenda):
    req = requests.get(urlPrenda)
    data = req.text
    get_html = BeautifulSoup(data,'html.parser')
    
    res = []
    
    for j in get_html.find_all("script", type="application/ld+json"):
        prenda = j.get_text().split(",")
        
        res.append(prenda[3])
        res.append(prenda[4])
        res.append(prenda[5])
        res.append(prenda[10])
        res.append(prenda[12])        
    
#     print res
    return res

