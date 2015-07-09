#-*- coding: utf-8 -*-

from django.db import models
from mezzanine.pages.models import Page, RichTextPage
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

class Ville_BarDuMonde(Page):
    """
        Modèle parent des BarDuMonde 
        Le champ Page.titre suffit
    """
    illustration = models.ImageField(upload_to=MEDIA_ROOT, verbose_name="Illustration de la ville; Taille recommandée: 1000x400; Poids maximal recommandé: 150 Ko")
    # that's all folks ? 

class BarDuMonde(Page):
    ville = models.ForeignKey(Ville_BarDuMonde,verbose_name='Ville du bar')
    date_derniere_visite = models.DateField(null=True,blank=True)
    illustration = models.ImageField(upload_to=MEDIA_ROOT, verbose_name="Illustration du Bar; Taille recommandée: 800x450; Poids maximal recommandé: 100 Ko")
    site_web = models.URLField(verbose_name='Site internet',null=True,blank=True,help_text='entrez une adresse URL valide')
    facebook = models.URLField(null=True,blank=True)
    twitter = models.URLField(null=True,blank=True)
    adresse = models.CharField(max_length=200,null=True,blank=False)
    barman_vedette = models.TextField(verbose_name='Barman Vedette',null=True,blank=True)
    cocktail = models.TextField(null=True,blank=True)
    decoration = models.TextField(verbose_name='décoration',null=True,blank=True)



