from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup


my_url = 'https://www.digidirect.com.au/cameras/mirrorless-cameras/filters/brand/fujifilm-2'

uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()
# parse as a bs4 object
page_soup = soup(page_html, 'html.parser')

#grabs each product
containers = page_soup.find_all("div", {"class": "product-item-info -grid"})
container = containers[0]

# Get product name
for container in containers:
    product_name = container.strong.a['title']
    print(product_name)
    oldprice = oldprice = container.findAll("div", {"class":"current-price-wrapper"})
    oldprice[0].text
    print(oldprice[0].text)
    





#TODO: write a try and except block for items that dont have special discount price