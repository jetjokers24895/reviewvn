# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
#from . import search_vatgia
from . import search_vatgia

# Create your views here.
def getrw_vatgia(requests):
    return render(requests,"getrw_vatgia/form.html")

def createobj(keywords):
    fclass = search_vatgia.search_vatgia(keywords)
    listobj=list()
    for i in fclass:
        linkweb = 'http://vatgia.com'+i.get("href")
        comment = search_vatgia.get_comment(linkweb)
        #print len(comment)
        if len(comment) == 0 :
            continue
        else:
            #print comment
            linkimg = search_vatgia.get_src(i)
            obj= search_vatgia.object(linkweb,comment,linkimg) 
            listobj.append(obj)
    return listobj

def mainaction(requests):
    keywords = requests.POST['keywords']
    lst= createobj(keywords)
    if lst == []:
        return render(requests,'getrw_vatgia/nocomment.html')
    return render(requests,"getrw_vatgia/review.html",{'lst':lst})
