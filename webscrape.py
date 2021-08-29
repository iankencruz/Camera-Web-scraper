import time
from typing import Container
# from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


my_url = 'https://www.digidirect.com.au/lenses/mirrorless-lenses'



browser = webdriver.Chrome()


#load webpage
browser.get(my_url)
time.sleep(0.5)

# Get the body element to scroll
elem = browser.find_element_by_tag_name("body")

scrollAmount = 10

while scrollAmount:
    
    elem.send_keys(Keys.PAGE_DOWN)
    time.sleep(.2)
    scrollAmount-=1
    print("Scrolling!  #" + str(scrollAmount))
    
    


print ("Finished Scrolling!")


# parse as a bs4 object
page_soup = soup(browser.page_source, 'html.parser')

#grabs each product
#! NOT FINDING ALL ITEMS
items = page_soup.findAll("li", {'class': 'item product product-item'})


# Get product name
for container in items:
    try:
        product_name = container.strong.a['title']
        print("Product: " + product_name)
        priceList = container.find_all("span", {"class":"price"})

        oldprice = priceList[0].text
        newprice = priceList[1].text
        print("New Price: " + newprice)
    except:
        print("NO SALE PRICE FOUND!")
        # oldprice = priceList[0].text
        print("Top Price: " + oldprice)
    else:
        # oldprice = priceList[0].text
        print("Top Price: " + oldprice)


    print("\n")

    
print("Total items found: " + str(len(items)))

browser.quit()
