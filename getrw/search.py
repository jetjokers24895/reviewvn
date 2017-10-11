# -*- coding: utf-8 -*-
import requests
#import sys
#
import re
from bs4 import BeautifulSoup
#from bs4 import UnicodeDammit
#sys.stdout = codecs.getwriter("iso-8859-8")(sys.stdout, 'xmlcharrefreplace')
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

class lazada(object):
    pass       
class tiki(object):
    pass
class sendo(object):
    pass
class enbac(object):
    pass
class zalora(object):
    pass
class thegioididong(object):
    pass
class yahoo(object):
    pass
class yahooansw(object):
    pass
######### start lazada######################
def getcomment(link): #lazada
    r= requests.get(link)
    soup = BeautifulSoup(r.text,'html.parser')
    fnd = soup.find_all("div","c-review__comment")
    #print len(fnd)
    c = list()
    if len(fnd)!= 0:
        for i in fnd:
            comment = i.string
            c.append(comment)
    return c
link= '''http://www.lazada.vn/chuot-e-blue-puntero-ems146-1155624.html?spm=a2o4n.search.0.0.td3RpJ&ff=1'''
getcomment(link)
def get_src(input): # get link src tu html element lazada
    rexp='("src": ")(.*)"' #lay link cua the span
    f = re.compile(str(rexp)).findall(str(input))
    return str(f[0][1])




def search_lazada(keywords):
    payload={
        'q' : keywords 
        }# tao url
    r = requests.get("http://lazada.vn/catalog/",params=payload)# send request den lazada
    soup = BeautifulSoup(r.text,"html.parser")
    fclass = soup.find_all("div","c-product-card__img-placeholder")
    return fclass
    #print fclass.name
    # f = open("text.txt","w")
    #for i in fclass :
        #print 'http:lazada.vn/'+i.a.get("href")
        #img= get_src(i.span)
        #print img
        #print i.a.get("string")
        #print "####################"
    #print type(i)
    #print "####################"
    #f.write(str(i.span))
    #f.write("#################\n")
    #print "###############"
    #print r.url


#######################end lazada################################
