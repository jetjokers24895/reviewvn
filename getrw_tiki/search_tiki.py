import requests
import re
from bs4 import BeautifulSoup

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

def search_tiki(keywords):
    payload={
        'q' : keywords 
        }# tao url
    r = requests.get("https://tiki.vn/search",params=payload)# send request den lazada
    with open("text.txt","r") as p:
        text = p.read()
        p.close()
    soup = BeautifulSoup(str(text),"html.parser") 
    fclass = soup.find_all("div","product-item")
    for i in fclass:
        link = get_src(i.span)
        print link
        print "###################"

def get_comment(link):
    r = requests.get(link)
    with open("text.txt","w") as p:
        p.write(r.text.encode('utf-8'))
        p.close()
get_comment('''https://tiki.vn/tai-nghe-apple-earpods-iphone-7-7-plus-lightning-earpods7-hang-nhap-khau-p587550.html?src=search&q=iphone+7''')

def get_src(input): # get link src tu html element lazada
    rexp='(src=")(.*)"/>' #lay link cua the span
    f = re.compile(str(rexp)).findall(str(input))
    return f[0][1]
search_tiki("iphone 7")
