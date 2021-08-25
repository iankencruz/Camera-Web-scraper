#! python 3
#mapit.py - Launches a map in the browser using an address from 
#command line or clipboard

import webbrowser, sys, pyperclip

if len(sys.argv) > 1:
    #get address from command line
    address = ' '.join(sys.argv[1:])            # sys.argv[1:] = Chop off first element of array ("mapit.py")
else:
    # Get Address from clipboard
    address = pyperclip.paste()

webbrowser.open('https://www.google.com/maps/place/'+address)



# --------------------------------------------------------------------------------------------------------------------------------
# Ideas for Similar Programs
# As long as you have a URL, the webbrowser module lets users cut 
# out the step of opening the browser and directing themselves to a website. 
# Other programs could use this functionality to do the following:# 


# -Open all links on a page in separate browser tabs.# 

# -Open the browser to the URL for your local weather.# 

# -Open several social network sites that you regularly check.

# --------------------------------------------------------------------------------------------------------------------------------


