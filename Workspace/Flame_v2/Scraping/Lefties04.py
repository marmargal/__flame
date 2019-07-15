'''
Created on 2 jul. 2019

@author: inmam
'''
from bs4.diagnose import diagnose

from Scraping.Frameworks import Soup

url = 'https://www.lefties.com/es/women/colecci%C3%B3n/vestidos-y-monos/vestido-estampado-bolsillos-c1029510p501312829.html?colorId=061&SALES=1'


def obtener_detalles_prenda(urlPrenda, nombreDoc):  #                     NO FUNCIONA!!!!!!
    
    res = []
#     get_html_prenda = Soup.get_html(urlPrenda).prettify(formatter="xml", encoding="utf-8") 
    get_html_prenda = Soup.get_html(urlPrenda) 
    
#     print(get_html_prenda.prettify(formatter="xml", encoding="utf-8"))
#     print(get_html_prenda.html)

#     f = open('html/'+ nombreDoc + '.txt', 'w')
#     f.write(str(get_html_prenda.html))

    with open('html/' + nombreDoc + '.html', "w", encoding="utf-8") as f:
        f.write(str(get_html_prenda))
    f.close
    
    with open('html/' + nombreDoc + '.html') as fp:
        data = fp.read()
    diagnose(data)
    
#     for prenda in get_html_prenda.find(attrs={"id":"product-info-container"}):
#         name = prenda.find("info-name").text
#         print(name)
        
#     print(images)
#     for i in images: print(i)
    
    return res;


obtener_detalles_prenda(url, 'prueba_lefties_01')

