# -*- coding: utf-8 -*-
import requests
#import sys
from selenium import webdriver
import re
from bs4 import BeautifulSoup
#from bs4 import UnicodeDammit
#sys.stdout = codecs.getwriter("iso-8859-8")(sys.stdout, 'xmlcharrefreplace')
import os
project_dir = os.path.dirname(os.path.abspath(__file__))
#project_dir = project_dir.replace('\\','/')
phantom_linuxdir = project_dir + '/phantom/linux/bin/phantomjs'
#phantom_linuxdir= '/app/getrw_tiki/phantom/linux/bin/phantomjs'
phantom_windir = project_dir + '/phantom/windows/bin/phantomjs'
#print phantom_linuxdir
#client = webdriver.PhantomJS(executable_path=r'/app/getrw_tiki/phantom/linux/bin/phantomjs') ### crawler js
client = webdriver.PhantomJS()
#client = webdriver.PhantomJS(phantom_windir) ### crawler js


class object:
    def __init__(self,lnkweb,comment,lnkImg):
        #comment co kieu la chuoi
        self.lnkweb = lnkweb
        self.comment = comment
        self.lnkImg = lnkImg
    def returnvalue(self): # tra ve cac gia tri cua doi tuong
        obj = list() # tao mang rong
        obj.append(self.lnkweb) #them cac gia tri thuoc tinh vao list
        obj.append(self.comment)
        obj.append(self.lnkImg)
        return obj #tra ve list chua cac gia tri doi tuong

######### start lazada######################
def get_comment(link): #lazada
    r= requests.get(link)
    soup = BeautifulSoup(r.text,'html.parser')
    fnd = soup.find_all("div","review_criteria")
    #print len(fnd)
    c = list()
    if len(fnd)!= 0:
        for i in range(len(fnd)):
            comment = fnd[i].span.text
            c.append(comment)
    return c

#link= '''http://vatgia.com/bantoanquoc&module=product&view=detail&record_id=5958125'''
#get_comment(link)
print range(5)

def search_vatgia(keywords):
    link = 'http://vatgia.com/home/quicksearch.php?keyword='+keywords.replace(' ','+')+'&sort=5'
    client.get(link)
    soup = BeautifulSoup(client.page_source,"html.parser")
    fclass = soup.find_all("a","picture_link")
    return fclass[0:6]
    #print i.img.get('src')
 


#######################end lazada################################
#search_vatgia("iphone 7")
