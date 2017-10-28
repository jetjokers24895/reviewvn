# -*- coding: utf-8 -*-
import requests
import re
from bs4 import BeautifulSoup
from selenium import webdriver
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
class object_adayroi:
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

def search_adayroi(keywords):
    payload={
        'q' : keywords,
        's': '5'
        }# tao url
    r = requests.get("https://www.adayroi.com/tim-kiem",params=payload)# send request den lazada
    #print r.url
    #with open("text.txt","w") as p:
        #p.write(r.text.encode('utf-8'))
        #p.close()
    soup = BeautifulSoup(r.text,"html.parser") 
    fclass = soup.find_all("span","mask",limit=2)
    return fclass # tra ve 2phan tu
#search_adayroi('samsung galaxy s8')
def get_comment(link):
    client.get(link)
    soup = BeautifulSoup(client.page_source,'html.parser')
    fclass = soup.find_all('div','comment-body')
    c = list()
    for i in fclass:
        text=i.p.text.encode('utf-8').replace('Xem thêmThu gọn','')
        c.append(text)
    return c
    #soup = BeautifulSoup(client.page_source,'html.parser')
#link='''https://www.adayroi.com/samsung-galaxy-s8-plus-g955f-vang-p-KlPR0-f1-2?pi=yv5zP&w=rMl&mc=wn4M'''
#get_comment(link)
#search_adayroi("samsung galaxy s8")