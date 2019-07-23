from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import json
import os
import argparse
import urllib

def webscrape(searchterm):

    #searchterm = 'bananas' # will also be the name of the folder
    url = "https://www.google.co.in/search?q="+searchterm+"&source=lnms&tbm=isch"
    browser = webdriver.Chrome(r"C:\Users\Andrew\Documents\UCBEL201902DATA2 HOMEWORK\ImageProcessing\chromedriver.exe")
    browser.get(url)
    header={'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.134 Safari/537.36"}
    counter = 0
    succounter = 0

    for x in browser.find_elements_by_xpath('//div[contains(@class,"rg_meta")]'):
        counter = counter + 1
        print ("Total Count:", counter)
        print ("Succsessful Count:", succounter)
        print ("URL:",json.loads(x.get_attribute('innerHTML'))["ou"])
    
        img = json.loads(x.get_attribute('innerHTML'))["ou"]
        imgtype = json.loads(x.get_attribute('innerHTML'))["ity"]
        if imgtype == 'jpg' or imgtype == 'jpeg':
            try:
                print(os.path.join('static','images', 'webscraped',str(succounter)+".jpg"))
                urllib.request.urlretrieve(img, os.path.join('static','images', 'webscraped',str(succounter)+".jpg"))
                succounter = succounter + 1
            except:
                    print ("can't get img")
        if succounter == 3:
            break
            
    
    print (succounter, "pictures succesfully downloaded")
    browser.close()
