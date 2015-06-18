#-*- coding: utf-8 -*-

from __future__ import unicode_literals
from models import *

class PubMiddleware(object):
    def process_template_response(self, request, response):
        try:
            habillage = Publicite.objects.get(formatPub='HABILLAGE')
            media = habillage.media.url.split('/')
            habillage.media = media[-1]
        except: 
            habillage = False
        response.context_data['habillage'] = habillage
        try:
            square = Publicite.objects.get(formatPub='SQUARE')
            media = square.media.url.split('/')
            square.media = media[-1]
        except:
            square = False
        response.context_data['square'] = square
        try:
            colonne = Publicite.objects.get(formatPub='COLONNE')
            media = colonne.media.url.split('/')
            colonne.media = media[-1]
        except:
            colonne = False
        response.context_data['colonne'] = colonne
        if habillage or colonne or square:
            response.context_data['pub'] = True
        if colonne or square:
            response.context_data['sidePub'] = True
        return response
