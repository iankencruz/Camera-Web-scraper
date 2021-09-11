import time
from bs4 import BeautifulSoup as soup
from selenium import webdriver
import pandas as pd

_digi_url = 'https://www.digidirect.com.au/cameras/mirrorless-cameras'
_georges_url = 'https://www.georges.com.au/digital-cameras/mirrorless-cameras.html'

#TODO Scrape Georges camera aswell
#TODO refactor in to a function to reuse scraping code


def ScrollPage(driver, scrollPauseTime, screenHeight, iter):
    while True:
    # scroll one screen height each time
        driver.execute_script("window.scrollTo(0, {scrollHeight}*{i});".format(scrollHeight=screenHeight, i=iter))  
        iter += 1
        time.sleep(scrollPauseTime)

    # update scroll height each time after scrolled, as the scroll height can change after we scrolled the page
        scrollHeight = driver.execute_script("return document.body.scrollHeight;")  
    
    # Break the loop when the height we need to scroll to is larger than the total scroll height
        if (screenHeight) * iter > scrollHeight:
            print ("Finished Scrolling!")
            break 
    
        print("Scrolling!")




def LoadPage(sel_driver, dest):        
    # Load webpage
    sel_driver.get(dest)    

    # Wait before scrolling
    time.sleep(0.3)

  

def ParseHTML(sel_driver, html_tag : str, id : str, id_name : str):
    # parse as a bs4 object
    page_soup = soup(sel_driver.page_source, 'html.parser')

    #grabs each product
    result_items = page_soup.findAll(html_tag, {id: id_name}) 

    return result_items



# Load webdriver
driver = webdriver.Chrome()


# Pause time in between scrolls
_scrollPauseTime = .5 

# get the screen height of the web
screenHeight = driver.execute_script("return window.screen.height;")   
i = 1




# Load The desired webpage
LoadPage(driver, _digi_url)

# function refactor
ScrollPage(driver, _scrollPauseTime, screenHeight, i)







items = ParseHTML(driver, 'li','class','item product product-item')







top_price = ''
new_price = ''



# Write to file setup
filename = 'product_cameras.csv'
file = open(filename, 'w')


#* WRITE THE HEADERS OF THE CSV FILE
headers = 'Product Name, Brand,Top Price, Sale Price \n'
file.write(headers)





def GetProductInfo(bs4_item, html : str, id : str, id_name : str):
    product_name = bs4_item.strong.a['title'] 





#* Filter by brand
search_target = ["Fujifilm", "Sony", "Canon"]

# Get product name
for container in items:
    for i in range(len(search_target)):
        if (search_target[i] in container.strong.a['title'] ):

            try:
                product_name = container.strong.a['title'] 
                print("Product: " + product_name)

                priceList = container.find_all("span", {"class":"price"})

                brand_name = search_target[i]


                # Grab old and new price from span class
                # Format text to remove comma
                top_price = priceList[0].text.replace(',', '')
                new_price = priceList[1].text.replace(',', '')

                print("New Price: " + new_price)




            except:
                print("NO SALE PRICE FOUND!")
                print("Top Price: " + top_price)
            else:
                print("Top Price: " + top_price)

            # file.write(product_name + ',' +  oldprice + ',' +  newprice + '\n')
            file.write(f'{product_name},{brand_name},{top_price},{new_price} \n')
            print("\n")


print("Total items found: " + str(len(items)) + '\n')

file.close()

driver.quit()


