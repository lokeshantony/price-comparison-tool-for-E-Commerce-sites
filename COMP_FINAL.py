#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

name='iphone 14 pro max'

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.68", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}


def amazon(name):
    URL = 'https://www.amazon.in/s?k='+name.replace(" ","+")
    URL = 'https://www.amazon.in/s?k='+name.replace(" ","+")+'&i=todays-deals'
    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.text, "html.parser")
    title = soup.select('.a-color-base.a-text-normal')[0].getText().strip().upper()
    price = soup.select('.a-price-whole')[0].getText().strip().upper()
    print(title)
    print(price)
    print(URL)
def flipkart(name):
    URL = 'https://www.flipkart.com/search?q='+name.replace(' ','%20')+'&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off'
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.set_window_size(1024, 600)
    driver.minimize_window()
    driver.get(URL)
    time.sleep(2)
    soup=BeautifulSoup(driver.page_source,'html.parser')
    title = soup.find_all('div',{'class':'_4rR01T'})[0].get_text()
    cost =  soup.find_all('div',{'class':'_30jeq3 _1_WHN1'})[0].get_text()
    print(title)
    print(cost)
    print(URL)
def croma(name):
    URL = 'https://www.croma.com/searchB?q=realme%20pad%20mini%3Arelevance&text=realme%20pad%20mini'
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.set_window_size(1024, 600)
    driver.minimize_window()
    driver.get(URL)
    time.sleep(2)
    soup=BeautifulSoup(driver.page_source,'html.parser')
    title = soup.find_all('h3',{'class':'product-title plp-prod-title'})[0].get_text()
    cost=soup.find_all('span',{'class':'amount','data-testid':'new-price'})[0].get_text()
    print(title)
    print(cost)
    print(URL)
def ebay(name):
    URL = 'https://www.ebay.com/sch/i.html?_from=R40&_trksid=p2380057.m570.l1313&_nkw='+name.replace(" ","+")+'&_sacat=0'
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.68", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}
    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.text, "html.parser")
    tags = soup.findAll('div', class_ = 's-item__title')
    title = tags[3].text
    price = soup.findAll('span', class_ = 's-item__price')
    cost = price[3].text
    print(title)
    print(cost)
    print(URL)
amazon(name)
flipkart(name)
croma(name)
ebay(name)

