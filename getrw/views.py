# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from . import search

# Create your views here.
def createobj(keywords):
    fclass = search.search_lazada(keywords)
    listobj=list()
    for i in fclass:
        linkweb = 'http://lazada.vn'+i.a.get("href")
        comment = search.getcomment(linkweb)
        #print len(comment)
        if len(comment) == 0 :
            continue
        else:
            #print comment
            linkimg = search.get_src(i.span)
            obj= search.object(linkweb,comment,linkimg) 
            listobj.append(obj)
        
    return listobj


def getrw(request):
    return render(request,"getrw/form.html")



def mainaction(requests):
    keywords = requests.POST['keywords']
    lst= createobj(keywords)
    return render(requests,"getrw/review.html",{'lst':lst})   
