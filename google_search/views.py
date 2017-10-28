# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
def view_google_search(requests):
    return render(requests,"google_search/google_search.html")