#!/usr/bin/env python
# coding:utf-8
"""
Name : annotateText.py
Author : Aurelia Vasile, MSH, UCA

Created on : 07/03/2023 10:11

"""

from cleaning import remove_messy_char
import xml.etree.ElementTree as ET
from xml.sax.saxutils import escape, quoteattr

import spacy

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



def write_xml(inputText, outputFile):
    '''
    open a txt file, add French part of speach and lemma for each character and output an xml file
    :param inputText: .txt file
    :param outputFile: .xml file
    :return: ElementTree object with xml hierarchy : <text><w pos=pos, lefffLemma=lefffLemma, spacyLemma=spacyLemma> text <w>
    '''

    # open and read a text file
    myFileText = open(inputText, "rt").read()

    # call the method remove_messy_char to clean the text
    cleanedText = remove_messy_char(myFileText)

    # generate an object nlp
    doc = nlp(cleanedText)

    # build the xml structure with <text> as element root
    racine = ET.Element("text")
    for token in doc:
        lefffLemma = token._.lefff_lemma
        pos = token._.melt_tagger
        spacyLemma = token.lemma_
        if lefffLemma is not None and pos is not None and spacyLemma is not None:
            # xml structure for each character <w lefffLemma=chercher, pos=V, spacyLemma=cherche> cherche
            word = ET.SubElement(racine, "w", pos=pos, lefffLemma=lefffLemma, spacyLemma=spacyLemma)
            word.text = escape(token.text)

    tree = ET.ElementTree(racine)
    tree.write(outputFile, encoding="UTF-8", xml_declaration=True,  default_namespace=None, method="xml")


