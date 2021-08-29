from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

my_url = 'https://www.digidirect.com.au/lenses/mirrorless-lenses'

uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

# parse as a bs4 object
page_soup = soup(page_html, 'html.parser')

#grabs each product
#! NOT FINDING ALL ITEMS
items = page_soup.find_all("li", {'class': 'item product product-item'})

 
print (len(items))


# # Get product name
# for container in items:
#     try:
#         product_name = container.strong.a['title']
#         print("Product: " + product_name)
#         priceList = container.find_all("span", {"class":"price"})

#         oldprice = priceList[0].text
#         newprice = priceList[1].text
#         print("New Price: " + newprice)
#     except:
#         print("NO SALE PRICE FOUND!")
#         # oldprice = priceList[0].text
#         print("Top Price: " + oldprice)
#     else:
#         # oldprice = priceList[0].text
#         print("Top Price: " + oldprice)


#     print("\n")



#TODO: write a try, except, else block for items that dont have special discount price