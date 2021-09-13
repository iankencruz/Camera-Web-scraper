
from bs4 import BeautifulSoup as soup
from urllib.request import Request, urlopen

my_url = "https://www.georges.com.au/digital-cameras/mirrorless-cameras.html"



req = Request(my_url, headers={'User-Agent': 'XYZ/3.0'})
webpage = urlopen(req, timeout=10).read()




# parse as a bs4 object
page_soup = soup(webpage, 'html.parser')

#grabs each product
#! NOT FINDING ALL ITEMS
items = page_soup.find_all("div", {'class': "product details product-item-details"})

 


# Get product name
for container in items:
    try:
        product_name = container.h5.text
        print(f"Product: {product_name}")
        priceList = container.find_all("span", {"class":"price"})

        oldprice = priceList[0].text
        newprice = priceList[1].text
        print("Top Price: " + oldprice)
        print("New Price: " + newprice)
    except:
        print("NO SALE PRICE FOUND!")
#         # oldprice = priceList[0].text
#         print("Top Price: " + oldprice)
#     else:
#         # oldprice = priceList[0].text
#         print("Top Price: " + oldprice)


#     print("\n")



#TODO: write a try, except, else block for items that dont have special discount price