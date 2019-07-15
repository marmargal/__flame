'''
Created on 9 feb. 2019

@author: inmam
'''
from Scraping.Frameworks import Soup

urlLefties = "https://www.lefties.com/es/#woman"


def obtener_enlaces_Lefties(url):
    
    res = []
    get_html = Soup.get_html(url)

    for item in get_html.find_all("li", attrs={"class":"sidemenu-list-item parent"}):
        for a in item.find_all("a"):
            nombre = a.get_text()
            enlace = a.get('href')
            if(('/es/women/') in enlace):
                res.append(['WOMEN', nombre, enlace])
            if(('/es/men/') in enlace):
                res.append(['MEN', nombre, enlace])
            
    return res


def obtener_enlace_prendas(urlCategoria):
    
    res = []
    get_html = Soup.get_html(urlCategoria)
    
    for item in get_html.find_all(class_="grid-product-standard grid-product2"):  # sacamos la url de la prenda
        enlace_prenda = item['href']
        res.append(enlace_prenda)
        
#     for i in res: print(i)
    return res

#     for item in get_html_prenda.find_all(attrs={"id":"product-container"}):
#         print(item)
#         images =  item.find_all("img", attrs={"class":"product-image"})
#         for i in images: print(i['src'])
# #         print(images)


def obtener_detalles_prenda(urlPrenda):  #                     NO FUNCIONA!!!!!!
    
    res = []
    get_html_prenda = Soup.get_html(urlPrenda) 
    
#     for img in get_html_prenda.find(attrs={"id":"product-image-container"}):
#         images = img.find_all('img')
    
    for prenda in get_html_prenda.find(attrs={"id":"product-info-container"}):
        name = prenda.find("info-name").text
        print(name)
        
#     print(images)
#     for i in images: print(i)
    return res;


obtener_detalles_prenda('https://www.lefties.com/es/women/colecci%C3%B3n/vestidos-y-monos/vestido-asim%C3%A9trico-c1029510p501376839.html?colorId=800')

###################################################################################################################################

# for enlace in obtener_enlaces_Lefties(urlLefties):
#     for enlacePrenda in obtener_enlace_prendas(enlace[2]):
#         print(enlacePrenda)

# for item in get_html.find_all(class_="sidemenu-list-item parent"):#, attrs="href"): ## ENLACES
#     print(item.get('a').get('href'))
