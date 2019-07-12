import sqlite3
from tkinter import Toplevel, Scrollbar, Listbox, Tk, Button
from tkinter.constants import Y, END, LEFT, BOTH

from pattern.db import RIGHT

from Scraping.Frameworks import Soup


urlZara = "https://www.zara.com/es/"
urlCategoria = "https://www.zara.com/es/es/mujer-chaquetas-l1114.html?v1=1180323"
urlPrenda = "https://www.zara.com/es/es/jeans-skinny-camuflaje-p00327022.html?v1=8142582&v2=1295745"

# devuelve hombre/mujer, categoria y url a categoria
def obtener_enlaces_Zara(url): 
    res = []
    get_html = Soup.get_html(url)
    
    try:
        for item in get_html.find_all("a", attrs={"class":"_category-link"}):
            nombre = item.find("span", attrs={"class":"cat-name"}).text
            enlace = item.get('href')
            if(type(enlace) == str):
                if("es/es/mujer" in enlace):
                    res.append(['WOMEN', nombre, enlace])
                if("es/es/hombre" in enlace):
                    res.append(['MEN', nombre, enlace])
    except:
        print("Something went wrong")            
#     for r in res: print(r)
    return res

def obtener_enlace_prenda(urlCategoria):
    # product-list _productList  
    res = []
    get_html = Soup.get_html(urlCategoria)
    
    try:
        for item in get_html.find_all("li", attrs={"class":"product _product"}):
            res.append(item.find('a')['href'])
    except:
        print("Something went wrong")
#     for r in res: print(r)
#     print(len(res))
    return res

def obtener_detalles_prenda(urlPrenda):
    res = []
    images = []
    sizes = []
    
    try:
        get_html_prenda = Soup.get_html(urlPrenda)
        
        # Name
        productName = get_html_prenda.find(attrs={"class":"product-name"}).text 
            
        # Price
        price = get_html_prenda.find(attrs={"class":"_product-price"}).text
        
        # Color
        color = get_html_prenda.find(attrs={"class":"_colorName"}).text
        
        # Description
        description = get_html_prenda.find(attrs={"id":"description"}).text
        
        # Sizes
        for size in get_html_prenda.find(attrs={"class":"size-select"}):
            for s in size.findAll(attrs={"class":"product-size"}):
                if('_disabled' not in s.attrs['class']):                    # tallas disponibles  
                    sizes.append(s.find("span", attrs={"class":"size-name"}).text)
        
        # Images
        for item in get_html_prenda.find_all(attrs={"id":"main-images"}):
            for i in item.find_all('img'):
                images.append(i['src']) 
                
        
        res.append(productName)
        res.append(description)
        res.append(color)
        res.append(price)
        res.append(sizes)
        res.append(images)
    
    except:
        print("Something went wrong")

#     for r in res: print(r)
    return res

def imprimir_etiqueta(cursor):
    v = Toplevel()
    sc = Scrollbar(v)
    sc.pack(side=RIGHT, fill=Y)
    lb = Listbox(v, width=150, yscrollcommand=sc.set)
    for row in cursor:
        lb.insert(END,row[0])
        lb.insert(END,row[1])
        lb.insert(END,row[2])
        lb.insert(END,row[3])
        lb.insert(END,row[4])
        lb.insert(END,row[5])
        lb.insert(END,row[6])
        lb.insert(END,row[7])
        lb.insert(END,row[8])
        lb.insert(END,'')
    lb.pack(side = LEFT, fill = BOTH)
    sc.config(command = lb.yview)

def populate_Zara(url):
    conn = sqlite3.connect('../populate.db')
    conn.text_factory = str
#     sql_insert_query = """ INSERT INTO 'zara_db' 
#                         ('id', 'sex', 'cat', 
#                         'name', 'price', 'color', 'description', 'sizes', 'images')

    conn.execute("DROP TABLE IF EXISTS ZARA_DB")
    conn.execute(''' CREATE TABLE ZARA_DB
                        (ZARA_ID INTEGER PRIMARY KEY AUTOINCREMENT,
                        SEX TEXT,
                        CATEGORY TEXT,
                        LINK TEXT UNIQUE,
                        NAME TEXT,
                        PRICE TEXT,
                        COLOR TEXT,
                        DESCRIPTION TEXT,
                        SIZES TEXT,
                        IMAGES TEXT ); ''')
                        

    
#                             SEX TEXT,
#                         CATEGORY TEXT,
    for a in obtener_enlaces_Zara(urlZara):
        sex = a[0]
        cat = a[1]
        for b in obtener_enlace_prenda(a[2]):
            link = b
            prenda = obtener_detalles_prenda(b)

#             check = conn.execute(""" SELECT link FROM ZARA_DB WHERE LINK = ? """, (link))
#             conn.commit
#             
#             if len(check) == 0:
            try:
                conn.execute(""" INSERT INTO ZARA_DB (SEX, CATEGORY, LINK, NAME, PRICE, COLOR, DESCRIPTION, SIZES, IMAGES)
                        VALUES (?,?,?,?,?,?,?,?,?) """, (sex, cat, link, prenda[0], prenda[1], prenda[2], prenda[3], str(prenda[4]), str(prenda[5]) ))
                conn.commit()
                print(sex, cat, link, prenda)
            except:
                print("Something went wrong")

         
    
                    
                    #         
#                     (prenda[0], prenda[1], prenda[2], prenda[3], prenda[4], prenda[5]))
#     args = prenda[0:4]
#     conn.execute(sql, args)
    conn.commit()
    
    cursor = conn.execute("SELECT SEX, CATEGORY, LINK, NAME, PRICE, COLOR, DESCRIPTION, SIZES, IMAGES FROM ZARA_DB") 
#                             , SIZES, IMAGES FROM ZARA_DB")
    imprimir_etiqueta(cursor)
    
    conn.close()

def listar_bd():
    conn = sqlite3.connect('populate.db')
    conn.text_factory = str  
    cursor = conn.execute("SELECT NAME, PRICE, COLOR, DESCRIPTION, SIZES, IMAGES FROM ZARA_DB")
    imprimir_etiqueta(cursor)
    conn.close() 

def ventana():
    top = Tk()
    almacenar = Button(top, text="Almacenar libros", command=populate_Zara(urlZara))
    almacenar.pack(side=LEFT)
    listar = Button(top, text="Listar libros", command=listar_bd)
    listar.pack(side=LEFT)
    salir = Button(top,text="Salir", command=exit)
    salir.pack(side=LEFT)
    top.mainloop()  


ventana()

# for a in obtener_enlaces_Zara(urlZara):
#     sex = a[0]
#     cat = a[1]
#     link = a[2]
#     for b in obtener_enlace_prenda(a[2]):
#         for c in obtener_detalles_prenda(b):
#             print(c)
#             print(sex, cat, link, c)

# print(obtener_detalles_prenda(urlPrenda))
    










