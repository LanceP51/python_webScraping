import bs4 as bs
import urllib.request

#grab the source as raw data response
source = urllib.request.urlopen('https://pythonprogramming.net/parsememcparseface/').read()

#make some object Soup
soup = bs.BeautifulSoup(source,'lxml')

#let's get some items

# title of the page
print("soup title component:")
print(soup.title)

# get attributes:
print("soup title attribute:")
print(soup.title.name)

# get values:
print("soup title string value:")
print(soup.title.string)

# beginning navigation:
print("beginning nav component:")
print(soup.title.parent.name)

# getting specific values:
print("p component:")
print(soup.p)

#print all the <p>'s
#print("all 'p' texts:")
for paragraph in soup.find_all('p'):
#    #print(paragraph.string)
    print(str(paragraph.text))

#get all <a> tags
print("a tags:")
for url in soup.find_all('a'):
    print(url.get('href'))

#specific Soup Nav item
nav = soup.nav
#get all nav a tags
for url in nav.find_all('a'):
    print(url.get('href'))

#get text from body
body = soup.body
for paragraph in body.find_all('p'):
    print(paragraph.text)

#print similar text but when it's a given class name.
for div in soup.find_all('div', class_='body'):
    print(div.text)

#scrape tables

table = soup.find('table')
#find the rows in the table
table_rows = table.find_all('tr')
#iterate through rows to print data
for tr in table_rows:
    td = tr.find_all('td')
    row = [i.text for i in td]
    print(row)

#same with Pandas, will get into Pandas in another Lesson
import pandas as pd

dfs = pd.read_html('https://pythonprogramming.net/parsememcparseface/',header=0)
for df in dfs:
    print(df)

#scrape xml

#get source
xsource = urllib.request.urlopen('https://pythonprogramming.net/sitemap.xml').read()
xsoup = bs.BeautifulSoup(xsource,'xml')

#get the url's
for url in xsoup.find_all('loc'):
    print(url.text)

#parsing dynamically updated data via javascript

js_test = soup.find('p', class_='jstest')

print(js_test.text)

#mimic a client
import sys
from PyQt5.QtGui import QApplication
from PyQt5.QtCore import QUrl
from PyQt5.QtWebKit import QWebPage

class Client(QWebPage):

    def __init__(self, url):
        self.app = QApplication(sys.argv)
        QWebPage.__init__(self)
        self.loadFinished.connect(self.on_page_load)
        self.mainFrame().load(QUrl(url))
        self.app.exec_()

    def on_page_load(self):
        self.app.quit()

url = 'https://pythonprogramming.net/parsememcparseface/'
client_response = Client(url)
jsource = client_response.mainFrame().toHtml()
jsoup = bs.BeautifulSoup(jsource, 'lxml')
js_test = jsoup.find('p', class_='jstest')
print(js_test.text)