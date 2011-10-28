# coding: utf-8
import re
import unicodedata
from django.template.defaultfilters import date

from django import template
register = template.Library()

def multiwordReplace(text, wordDic):
    rc = re.compile('|'.join(map(re.escape, wordDic)))
    def translate(match):
        return wordDic[match.group(0)]
    return rc.sub(translate, text)

@register.filter
def replace(string):
    return multiwordReplace(string, {' / ': '<br />',
                                     '\'': '&rsquo;',})

def remove_diacritics(string):
    return unicodedata.normalize('NFKD', string).encode('ASCII', 'ignore')

def is_vowel(string):
    return remove_diacritics(string.lower()) in list('aeiouy')

@register.filter
def abbreviate(string, limit=0):
    out = ''
    for i, sub in enumerate(re.split('-', string)): # TODO: créer un catalogue de ponctuations de séparation.
        tmp_limit = limit
        for j in range(len(sub)):
            try:
                if is_vowel(sub[j]):
                    if tmp_limit == 0:
                        if j == 0:
                            sub = sub[:1]
                        else:
                            sub = sub[:j]
                        sub += '.'
                        break
                    try:
                        if not is_vowel(sub[j+1]):
                            tmp_limit -= 1
                    except:
                        tmp_limit -= 1
            except:
                ''
        if i > 0:
            out += '-'
        out += sub
    return out

@register.filter
def naissance(obj):
    out = ''
    if obj.date_naissance:
        out += date(obj.date_naissance, 'SHORT_DATE_FORMAT').encode('utf-8')
    elif obj.date_naissance_approx:
        out += obj.date_naissance_approx
    else:
        return None
    if obj.lieu_naissance:
        out += ', ' + obj.lieu_naissance.nom.encode('utf-8')
    elif obj.lieu_naissance_approx:
        out += ', ' + obj.lieu_naissance_approx
    return out

@register.filter
def mort(obj):
    out = ''
    if obj.date_mort:
        out += date(obj.date_mort, 'SHORT_DATE_FORMAT').encode('utf-8')
    elif obj.date_mort_approx:
        out += obj.date_mort_approx
    else:
        return None
    if obj.lieu_mort:
        out += ', ' + obj.lieu_mort.nom.encode('utf-8')
    elif obj.lieu_naissance_approx:
        out += ', ' + obj.lieu_mort_approx
    return out

