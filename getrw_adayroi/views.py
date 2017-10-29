# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import search_adayroi
from django.shortcuts import render

# Create your views here.
def getrw_adayroi(request):
    return render(request,"getrw_adayroi/form.html")
    

def createobj(keywords):
    fclass = search_adayroi.search_adayroi(keywords)
    print len(fclass)
    listobj=list()
    for i in fclass:
        linkweb ='https://www.adayroi.com'+ i.a.get("href")
        comment = search_adayroi.get_comment(linkweb)
        #print len(comment)
        if len(comment) == 0 :
            continue
        else:
            #print comment
            linkimg = i.a.img.get('data-src')
            obj= search_adayroi.object_adayroi(linkweb,comment,linkimg) 
            listobj.append(obj)
        
    return listobj

def mainaction(requests):
    keywords = requests.POST['keywords']
    lst= createobj(keywords)
    if lst == []:
        return render(requests,'getrw_adayroi/nocomment.html')
    return render(requests,"getrw_adayroi/review.html",{'lst':lst})