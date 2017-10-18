# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import search_vatgia
from django.shortcuts import render

# Create your views here.
def getrw_vatgia(requests):
    return render(requests,"getrw_vatgia/form.html")

def createobj(keywords):
    fclass = search_vatgia.search_vatgia(keywords)
    listobj=list()
    for i in range(len(fclass)):
        linkweb = 'http://vatgia.com/'+fclass[i].get("href")
        comment = search_vatgia.get_comment(linkweb)
        #print len(comment)
        if len(comment) == 0 :
            continue
        else:
            #print comment
            linkimg = fclass[i].img.get('src')
            obj= search_vatgia.object(linkweb,comment,linkimg) 
            listobj.append(obj)
        
    return listobj

def mainaction(requests):
    keywords = requests.POST['keywords']
    lst= createobj(keywords)
    return render(requests,"getrw_vatgia/review.html",{'lst':lst})