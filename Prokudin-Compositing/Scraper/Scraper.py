#!/usr/bin/env python3

import urllib.request
from bs4 import BeautifulSoup
import csv

# http://www.loc.gov/pictures/search/?q=Prokudin+negative&fa=displayed%3Aanywhere&sp=1
# ^ is the website that I will be pulling from, sp=n at the end is the page number
# if I want, I should be using their json api
# https://libraryofcongress.github.io/data-exploration/responses.html


def getHTML(url):
    req = urllib.request.Request(url, headers={'User-Agent': 'Magic Browser'})
    con = urllib.request.urlopen(req)
    html = con.read()
    return html

url_search_base = 'http://www.loc.gov/pictures/search/?q=Prokudin+negative&fa=displayed%3Aanywhere&sp='

# returns a list of links from a page in the results of the search
def getLinks(pagenum):
    list_of_links = []
    url = url_search_base+str(pagenum)
    html = getHTML(url)
    soup = BeautifulSoup(html, 'html.parser')
    for link in soup.find_all('a', href=True):
        url = 'http:'+link['href']
        if 'item' in url and url not in list_of_links:
            list_of_links.append(url)
    return list_of_links

# given a item link, returns the link to download of the uncomposited image
def getDownload(link):
    list_of_links = []
    html = getHTML(link)
    soup = BeautifulSoup(html, 'html.parser')
    for link in soup.find_all('a', href=True):
        url = 'http:'+link['href']
        if '.jpg' in url and url not in list_of_links:
            list_of_links.append(url)
    if len(list_of_links) == 6:
        return list_of_links[-1]
    return 0


def download(link, fname):
    if len(str(link)) < 8:
        return
    req = urllib.request.Request(link, headers={'User-Agent': 'Magic Browser'})
    con = urllib.request.urlopen(req)
    file = open('../data-sets/test-set/'+fname, 'wb')
    file.write(con.read())
    file.close()

list_of_links = []
for i in range(1,96):
    list_of_links = list_of_links + getLinks(i)
    print('parsing ' + str(i) + "th page of results")

iter = 1
for link in list_of_links:
    # to counter weird error with '0' being a link
    if len(str(link)) < 8:
        iter = iter + 1
        continue
    link = getDownload(link)
    fname =  'img'+str(iter)+'.jpg'
    download(link,fname)
    print('downloaded ' + fname + ' from ' + str(link))
    iter = iter + 1
