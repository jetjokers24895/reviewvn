# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from search import *
from django.shortcuts import render, render_to_response
# Create your views here.
def createobj(keywords):
    fclass = search_lazada(keywords)
    listobj=list()
    for i in fclass:
        linkweb = 'http://lazada.vn'+i.a.get("href")
        comment = getcomment(linkweb)
        print len(comment)
        if len(comment) == 0 :
            continue
        else:
            print comment
            linkimg = get_src(i.span)
            obj=object(linkweb,comment,linkimg) 
            listobj.append(obj)
        
    return listobj


def getrw(request):
    return render(request,"getrw/form.html")

def mainaction(requests):
    keywords = requests.POST['keywords']
    if keywords is not None:
        lst= createobj(keywords=keywords)
        return render(requests,"getrw/rewiew.html",{'lst':lst})
    else:
        return render_to_response("get-review")
    
