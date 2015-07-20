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
    class Meta:
        verbose_name = ("Ville (Bars du Monde)")

class BarDuMonde(Page):

    ville = models.ForeignKey(Ville_BarDuMonde,verbose_name='Ville du bar')
    date_derniere_visite = models.DateField(null=True,blank=True)
    illustration = models.ImageField(upload_to=MEDIA_ROOT, verbose_name="Illustration du Bar; Taille recommandée: 800x450; Poids maximal recommandé: 100 Ko")
    site_web = models.URLField(verbose_name='Site internet',null=True,blank=True,help_text='entrez une adresse URL valide')
    facebook = models.URLField(null=True,blank=True)
    twitter = models.URLField(null=True,blank=True)
    adresse = models.CharField(max_length=200,null=True,blank=False)
    barman_vedette = models.TextField(verbose_name='Barman Vedette',help_text='Description du Barman',null=True,blank=True)
    cocktail = models.TextField(help_text='Description du cocktail vedette',null=True,blank=True)
    decoration = models.TextField(verbose_name='décoration',help_text='Description de la décoration',null=True,blank=True)

    class Meta:
        verbose_name = ("Bar Du Monde")

class IBDM(models.Model):
    bar = models.ForeignKey(BarDuMonde)
    illustration = models.ImageField(upload_to=MEDIA_ROOT+'/bar_du_monde')
    legende = models.CharField(max_length=400,verbose_name='légende',help_text='400 caractères max',null=True,blank=True)

    def save(self, *args, **kwargs):
        """
            try to override save() for illustration.url purposes
        """
        self.illustration = self.illustration.name.replace(' ','_')
        super(IBDM, self).save(*args, **kwargs)

class IBDM_BarmanVedette(IBDM):
    category = "barman_vedette"
class IBDM_Cocktail(IBDM):
    category = "cocktail"
class IBDM_Decoration(IBDM):
    category = "deco"




