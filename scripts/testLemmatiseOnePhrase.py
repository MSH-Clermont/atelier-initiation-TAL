#!/usr/bin/env python
# coding:utf-8
"""
Name : testLemmatiseOnePhrase.py
Author : Aurelia Vasile, MSH, UCA

Created on : 07/03/2023 09:45

"""

# installer spacy avec pip install spacy
import spacy

# download the trained pipelines for French with :  python -m spacy download fr_core_news_sm

# install the lefff library (Lexique des Formes Fléchies du Français) pip install spacy-lefff form here https://github.com/sammous/spacy-lefff

from spacy_lefff import LefffLemmatizer, POSTagger
from spacy.language import Language
from scripts.cleaning import remove_messy_char

@Language.factory('french_lemmatizer')
def create_french_lemmatizer(nlp, name):
    return LefffLemmatizer(after_melt=True, default=True)

@Language.factory('melt_tagger')
def create_melt_tagger(nlp, name):
    return POSTagger()

nlp = spacy.load('fr_core_news_sm')
nlp.add_pipe('melt_tagger', after='parser')
nlp.add_pipe('french_lemmatizer', after='melt_tagger')

# test phrase
phrase = "Que je sache. Bien qu'il soupçonnât le président, il se décida. Elle soupçonna son père.\n" \
         "Allons-nous < partir ^en vacances ? Y \"a-t-il\" <> un problème. ___ I	,	------- - . ....... —	" \
         "Oui !... où allons-nous? Il s'est assis sur ses genoux. " \
         "—	A toi de faire mieux. " \
         "Ceux-ci me vont bien. " \
         "Tout à l’heure, elle n’aura pas de café. "

# call the method remove_messy_char
cleanedText = remove_messy_char(phrase)

# generate an object nlp
doc = nlp(cleanedText)

for token in doc:
    # generate the lefff lemma
    lefffLemma = token._.lefff_lemma
    # generate the part of speach
    pos = token._.melt_tagger
    # generate the spacy standard lemma (different from the lefff lemma)
    spacyLemma = token.lemma_

    if lefffLemma is not None and pos is not None and spacyLemma is not None:
        print(f"token={token.text: <10} pos={pos: <5} spacyLemma={spacyLemma: <10} lefffLemma={lefffLemma}")
