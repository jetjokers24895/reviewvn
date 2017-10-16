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


class object_tiki:
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

def search_tiki(keywords):
    payload={
        'q' : keywords 
        }# tao url
    r = requests.get("https://tiki.vn/search",params=payload)# send request den lazada
    soup = BeautifulSoup(r.text,"html.parser") 
    fclass = soup.find_all("div","product-item")
    return fclass[0:2] # tra ve 5 phan tu

def get_comment(link):
    
    client.get(link)
    soup = BeautifulSoup(client.page_source,"html.parser")
    fclass = soup.find_all("div","description js-description")
    c = list()
    for i in fclass:
        c.append(i.p.text)
    return c
    '''
    with open("text.txt","w") as p:
        p.write(client.page_source.encode('utf-8'))
        p.close()
with open("text.txt","r") as fd:
    text = fd.read()
    soup = BeautifulSoup(text,"html.parser")
    fclass = soup.find_all("div","description js-description")
    a = open("string.txt","w")
    for i in fclass :
        a.write(i.p.text.encode('utf-8')+"\n")
'''
#get_comment('''https://tiki.vn/dac-nhan-tam-kho-nho-p517031.html''')

def get_src(input): # get link src tu html element lazada
    rexp='(src=")(.*)"' #lay link cua the span
    f = re.compile(str(rexp)).findall(str(input))
    return f[0][1]
#search_tiki("iphone 7")
