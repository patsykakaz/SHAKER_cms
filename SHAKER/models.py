#-*- coding: utf-8 -*-

from django.db import models
from mezzanine.pages.models import Page
from mezzanine.core.models import RichText
from settings import MEDIA_ROOT

class Publicite(Page):
    lien = models.CharField(max_length=255, null=True, blank=True)
    media = models.ImageField(upload_to=MEDIA_ROOT+'/publicite', null=True)
    OPTION_FORMAT_PUB = (
        ('HABILLAGE','HABILLAGE'),
        ('SQUARE', 'SQUARE'),
        ('COLONNE','COLONNE'),
    )
    formatPub = models.CharField(choices=OPTION_FORMAT_PUB, max_length=250, null=True)

class BarDuMonde(Page):
    date_derniere_visite = models.DateField(null=True,blank=True)
    ville = models.CharField(max_length=100,null=False,blank=False)
    illustration = models.ImageField(upload_to=MEDIA_ROOT+'/BarDuMonde/', verbose_name="Illustration du Bar; Taille recommandée: 800x450; Poids maximal recommandé: 100 Ko")
    site_web = models.URLField(verbose_name='Site web/facebook')
    adresse = models.CharField(max_length=200,null=True,blank=False)
    barman_vedette = models.TextField(verbose_name='Barman Vedette',null=True,blank=True)
    cocktail = models.TextField(null=True,blank=True)
    decoration = models.TextField(verbose_name='décoration',null=True,blank=True)



