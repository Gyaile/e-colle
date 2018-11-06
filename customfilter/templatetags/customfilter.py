#-*- coding: utf-8 -*-
from django import template
from datetime import date, timedelta
from accueil.models import Classe, Config

register = template.Library()

@register.filter
def nometab(d):
	return Config.objects.get_config().nom_etablissement

@register.filter
def lookup(d,key):
    return "" if key not in d else d[key]

@register.filter
def integer(n):
    return int(n)

@register.filter
def addtime(temps, ajout):
    return temps+timedelta(days=ajout)

@register.filter
def heurecolle(temps):
	temps = temps or 0 # car une somme sur un ensemble vide peut renvoyer None
	return "{}h{:02d}".format(temps//60,temps%60)

@register.filter
def heure(heure):
	return "{}h{:02d}".format(heure//60,(heure%60))

@register.filter
def image(fichier):
    return fichier.replace('programme','image').replace('pdf','jpg')

@register.filter
def tzip(l1, l2):
    return zip(l1,l2)

@register.simple_tag
def get_mathjax():
    return Config.objects.get_config().mathjax

@register.simple_tag
def get_ects():
    return Config.objects.get_config().ects

@register.simple_tag
def get_modifgroupe():
    return Config.objects.get_config().modif_secret_groupe

@register.simple_tag
def get_classes():
    return Classe.objects.all()

@register.filter
def titer(obj):
    return iter(obj)

@register.filter
def tnext(iterable):
    try:
        return next(iterable)
    except Exception:
        return None