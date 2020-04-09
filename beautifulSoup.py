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
print("all 'p' texts:")
for paragraph in soup.find_all('p'):
    #print(paragraph.string)
    print(str(paragraph.text))

#get all <a> tags
print("a tags:")
for url in soup.find_all('a'):
    print(url.get('href'))