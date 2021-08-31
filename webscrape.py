import time
from bs4 import BeautifulSoup as soup
from selenium import webdriver

my_url = 'https://www.digidirect.com.au/cameras/mirrorless-cameras/filters/brand/fujifilm-3'

#TODO Use request instead of selenium to load the rest of the items



# Load webdriver
driver = webdriver.Chrome()

# Load webpage
driver.get(my_url)

# Wait before scrolling
time.sleep(0.3)

# Get the body element to scroll
elem = driver.find_element_by_tag_name("body")

# Pause time in between scrolls
scrollPauseTime = .5 

# get the screen height of the web
screenHeight = driver.execute_script("return window.screen.height;")   
i = 1


filename = 'products.csv'
f = open(filename, 'w')


headers = 'Product Name, Top Price, Sale Price\n'

f.write(headers)

while True:
    # scroll one screen height each time
    driver.execute_script("window.scrollTo(0, {scrollHeight}*{i});".format(scrollHeight=screenHeight, i=i))  
    i += 1
    time.sleep(scrollPauseTime)

    # update scroll height each time after scrolled, as the scroll height can change after we scrolled the page
    scrollHeight = driver.execute_script("return document.body.scrollHeight;")  
    
    # Break the loop when the height we need to scroll to is larger than the total scroll height
    if (screenHeight) * i > scrollHeight:
        break 
    
    print("Scrolling!")

print ("Finished Scrolling!")

# parse as a bs4 object
page_soup = soup(driver.page_source, 'html.parser')

#grabs each product
items = page_soup.findAll("li", {'class': 'item product product-item'})

print(len(items))


# Get product name
for container in items:
    try:
        product_name = container.strong.a['title']
        print("Product: " + product_name)
        priceList = container.find_all("span", {"class":"price"})

        # Grab old and new price from span class
        # oldprice = priceList[0].text
        # newprice = priceList[1].text
        
        # Format text to remove comma
        oldprice = priceList[0].text.replace(',', '')
        newprice = priceList[1].text.replace(',', '')

        print("New Price: " + newprice)
    except:
        print("NO SALE PRICE FOUND!")
        print("Top Price: " + oldprice)
    else:
        print("Top Price: " + oldprice)

    f.write(product_name + ',' +  oldprice + ',' +  newprice + '\n')
    print("\n")

print("Total items found: " + str(len(items)))
f.close()

driver.quit()

#TODO Implement into a csv file and organise to low-high pricing

