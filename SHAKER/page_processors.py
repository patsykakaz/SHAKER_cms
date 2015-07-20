#-*- coding: utf-8 -*-

from django import forms
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from mezzanine.pages.page_processors import processor_for
from mezzanine.blog.models import BlogPost, BlogCategory
from .models import *


@processor_for('/')
def processor_home(request,page):
    try: 
        blog_post_list = BlogPost.objects.all()
        last_bar_du_monde = BarDuMonde.objects.latest('date_derniere_visite')
        couv = last_bar_du_monde.illustration.url.split('/')
        last_bar_du_monde.illustration = couv[-1]
    except:
        print('FUCK')
        print('no BlogPost or BarDuMondex')
    return locals()

@processor_for(Ville_BarDuMonde)
def processor_Ville_BarDuMonde(request,page):
    try: 
        ville = Ville_BarDuMonde.objects.get(title=page.title)
        illustration = ville.illustration.url.split('/')
        ville.illustration = illustration[-1]
        bar_ville = BarDuMonde.objects.filter(ville=ville)
        print(bar_ville)
    except:
        print('no result for this query')
    return locals()

@processor_for(BarDuMonde)
def processor_AllBarDuMonde(request,page):
    try:
        bar = BarDuMonde.objects.filter(title=page.title)
        bar = bar[0]
        illustration = bar.illustration.url.split('/')
        bar.illustration = illustration[-1]
        # TODO: override save() for img.url
        barPics = IBDM.objects.filter(bar=bar)
    except:
        print("QueryError")
        pass
    return locals()





