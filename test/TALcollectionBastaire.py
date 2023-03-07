#!/usr/bin/env python
# coding:utf-8
"""
Name : TALcollectionBastaire.py
Author : Aurelia Vasile, MSH, UCA

Created on : 18/01/2023 13:36

"""
# installer spacy avec pip install spacy
import spacy
# importer la langue française avec la commande suivante:  python -m spacy download fr_core_news_sm

# installer la librairie d'amélioration du français pip install spacy-lefff form here https://github.com/sammous/spacy-lefff

from spacy_lefff import LefffLemmatizer, POSTagger
from spacy.language import Language

@Language.factory('french_lemmatizer')
def create_french_lemmatizer(nlp, name):
    return LefffLemmatizer(after_melt=True, default=True)

@Language.factory('melt_tagger')
def create_melt_tagger(nlp, name):
    return POSTagger()

nlp = spacy.load('fr_core_news_sm')
nlp.add_pipe('melt_tagger', after='parser')
nlp.add_pipe('french_lemmatizer', after='melt_tagger')

# phrase de test
#doc = nlp(u"Allons-nous partir en vacances ? Le mot qui tue. Ceux-ci me vont bien. Tout à l'heure, elle n'aura pas de café. Y a-t-il un problème")

# ouvrir et lire un fichier text (le chercher dans l'arborescence des dossiers)
myFileText = open("./BUCA_Bastaire_Collection_Aventures/BUCA_Bastaire_Collection_Aventures_C91953_reconnuV2.txt", "rt").read()

# remplace les apostrophes du type ’ par des apostrophes du type ' et remplace les retours à la ligne par rien
docAvecBonApostrophe = myFileText.replace("’", "'").replace("\n", " ")

# Quand on appelle la fonction nlp sur un text,
# tout d'abord spaCy le tokenise (le sépare en mots en fonction de l'espace) et produit un resultat de type objet "doc" qu'il va falloir mannipuler ensuite

doc = nlp(docAvecBonApostrophe)
outputFile = "BUCA_Bastaire_Collection_Aventures_C91953_reconnuV2_ConcatSTR.xml"

from xml.sax.saxutils import escape, quoteattr

def write_xml(doc, outputFile):
    with open(outputFile, 'w') as ofile:
        ofile.write('<?xml version="1.0" encoding="UTF-8"?>\n<text>\n')
        for token in doc:
            word = '  <w pos="{}" lem={}>{}</w>\n'.format(token._.melt_tagger, quoteattr(token._.lefff_lemma), escape(token.text))
            ofile.write(word)
        ofile.write('</text>\n')

write_xml(doc, outputFile)
