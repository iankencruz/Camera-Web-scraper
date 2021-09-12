import time
from bs4 import BeautifulSoup as soup
from bs4.element import PageElement
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pandas as pd

_digi_url = 'https://www.digidirect.com.au/cameras/mirrorless-cameras'
_georges_url = 'https://www.georges.com.au/digital-cameras/mirrorless-cameras.html'

#TODO Scrape Georges camera aswell
#TODO refactor in to a function to reuse scraping code


#* FUNCTION DEFINITIONS
def LoadPage(sel_driver, dest):        
    # Load webpage
    sel_driver.get(dest)    

    # Wait before scrolling
    time.sleep(0.3)

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

def ParseHTML(sel_driver, html_tag : str, id : str, id_name : str):
    
    # parse as a bs4 object
    page_soup = soup(sel_driver.page_source, 'html.parser')

    #grabs each product
    result_items = page_soup.findAll(html_tag, {id: id_name}) 

    return result_items

def GetProductInfo(tar_list : list, bs4_item : soup, html : str, id : str, id_name : str):
    product_name = bs4_item.strong.a['title'] 
    prices = bs4_item.find_all(html, {id:id_name})
    brand_name = tar_list[i]
    top_p = prices[0].text.replace(',', '')
    new_p = 'NO SALE'                       #* Default value

    #* Handling of prices when no sale is on
    if (len(prices) >= 2 ):
        new_p = prices[1].text.replace(',', '')

    #* DEBUG LOGS    
    print(product_name, brand_name)
    print(top_p, new_p)
    print ('\n')


    return product_name, brand_name, top_p, new_p




op = Options()
op.add_argument("--headless")
# Load webdriver
driver = webdriver.Chrome(options=op)





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




##############
#TODO create a write file function

# Write to file setup
filename = 'product_cameras.csv'
file = open(filename, 'w')


#* WRITE THE HEADERS OF THE CSV FILE
headers = 'Product Name, Brand,Top Price, Sale Price \n'
file.write(headers)













#* Filter by brand
search_target = ["Fujifilm", "Sony", "Canon"]

# Get product name
for container in items:
    for i in range(len(search_target)):
        if (search_target[i] in container.strong.a['title'] ):

            try:


                prod_name, brand_name, top_price, new_price = GetProductInfo(search_target, container, 'span', 'class', 'price')

            except FileNotFoundError:
                print("Error")

            file.write(f'{prod_name},{brand_name},{top_price},{new_price} \n')

            


print("Total items found: " + str(len(items)) + '\n')

file.close()


try:
    driver.quit()
    print("Driver Closed Successfully!")
except MemoryError:
    print('Failed to quit driver!')

