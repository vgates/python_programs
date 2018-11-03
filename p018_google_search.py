## REQUIRED MODULES
# requests - requests will allow you to send HTTP/1.1 requests using Python. 
#   It also allows you to access the response data of Python

# sys - module provides access to some variables used or maintained by the interpreter 
#   and to functions that interact strongly with the interpreter

# webbrowser - provides an interface to display Web-based documents.

# bs4 - BeautifulSoup 4 is for parsing HTML and XML files  

import requests, sys, webbrowser, bs4


# sending get request and saving the response as res object 

# sys.argv is a list in Python, which contains the command-line arguments passed to the script.
#   first argument is the file name hence we discard the first element and fetch others, hence [1:]

# '+'.join(sys.argv[1:]) - joins elements of a list by '+' (here sys.argv[1:] is a list)
res = requests.get('https://google.com/search?q=' + '+'.join(sys.argv[1:]))

# raise_for_status - To check that a request is successful or not
res.raise_for_status()

# res.text is the content of the response in unicode
soup = bs4.BeautifulSoup(res.text,"html.parser") # creates a soup object

# Now from the parsed html structure we retrive the a tags under element which has class r
# If you inspect the google results page you would see that the actual links of the results lie there
linkElements = soup.select('.r a') # returns a list

linkToOpen = min(2,len(linkElements))

for i in range(linkToOpen):
    # Open url in a new window of the default browser
    webbrowser.open('https://google.com' + linkElements[i].get('href'))