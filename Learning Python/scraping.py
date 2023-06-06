# basic components of a website

# 1. HTML= Hypertext Markup Language used to display content on website 

# 2. need to grab information by extrcating html tags 

# 3. CSS= cascading style sheets that are used to give style to a website

# pip install requests
# pip install laxl
# pip install bs4

import requests

#res= requests.get("http://www.example.com")
''''
print(type(res)) # check the type 

print(res.text) # this will get the html page with its elements
'''
# we will use python BeautifulSoup to extract web pages
# Beautiful soup has alot of built in libraries 

import bs4
'''
soup= bs4.BeautifulSoup(res.text, "lxml")
print(soup)

print(soup.select('title')) # extractting the title name of webpage

title_tag= soup.select('title')
print(title_tag[0]) #since the results returns as a list so we can extract the list using indexing 
print(type(title_tag[0]))
'''

# grabbing all elements of a class
''''
res= requests.get("https://en.wikipedia.org/wiki/Grace_Hopper")

soup=bs4.BeautifulSoup(res.text, "lxml")

#print(soup) # grabs all elements

print(soup.select(".mw-headline"))

for items in soup.select(".mw-headline"): # extrcated headlines
    print(items.text)
'''
# can grab images from a website as well 

res= requests.get("Https://en.wikipedia.org/wiki/Deep_Blue_(chess_computer)")

soup=bs4.BeautifulSoup(res.text, "lxml")

image_info= soup.select('.thumbimage') # getting image

print(image_info)

print(len(image_info))

comp= image_info[0]
print(type(comp))
print(comp['src'])

