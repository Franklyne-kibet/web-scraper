#Create a beautifulsoup object 
from bs4 import BeautifulSoup
from urllib.request import urlopen 

url = 'http://olympus.realpython.org/profiles/dionysus'
page = urlopen(url)
html = page.read().decode('utf-8')
soup = BeautifulSoup(html, "html.parser") 

#Use BeautifulSoup Object 
print(soup.get_text())

print(soup.find_all("img")) 

#find all images 
image1, image2 = soup.find_all("img")

#get the image name 
print(image1.name)

#get the image source
print(image1['src'])

#get the title
print(soup.title.string)