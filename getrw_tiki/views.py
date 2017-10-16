# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import search_tiki
from django.shortcuts import render

    

# Create your views here.
def getrw_tiki(requests):
    return render(requests,"getrw_tiki/form.html")

def createobj(keywords):
    fclass = search_tiki.search_tiki(keywords)
    listobj=list()
    for i in fclass:
        linkweb = i.a.get("href")
        comment = search_tiki.get_comment(linkweb)
        #print len(comment)
        if len(comment) == 0 :
            continue
        else:
            #print comment
            linkimg = search_tiki.get_src(i.span)
            obj= search_tiki.object_tiki(linkweb,comment,linkimg) 
            listobj.append(obj)
        
    return listobj

def mainaction(requests):
    keywords = requests.POST['keywords']
    lst= createobj(keywords)
    return render(requests,"getrw_tiki/review.html",{'lst':lst})