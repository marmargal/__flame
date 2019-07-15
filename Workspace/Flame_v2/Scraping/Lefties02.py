import sys 
import urllib.request

from PyQt5.QtCore import QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEnginePage  # Webkit
from PyQt5.QtWidgets import QApplication 

import bs4 as bs


class Client(QWebEnginePage):

    def __init__(self, url):
        self.app = QApplication(sys.argv)
        # QWebEnginePage.__init__(self)
        QWebEngineView.__init__(self)
        self.loadFinished.connect(self.on_page_load)
        self.load(QUrl(url))
        self.app.exec_()
        
    def on_page_load(self):
        self.app.quit()

        
url = 'https://pythonprogramming.net/parsememcparseface/'  # 'https://www.lefties.com/es/#woman'
client_response = Client(url)
# source = client_response.toHtml()
# soup = bs.BeautifulSoup(source,'lxml')
print(client_response.toHtml())
# print(soup.prettify())
    
