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
        last_bar_du_monde = BarDuMonde.objects.last()
        couv = last_bar_du_monde.illustration.url.split('/')
        last_bar_du_monde.illustration = couv[-1]
    except:
        print('no BlogPost or BarDuMonde')
    return locals()

