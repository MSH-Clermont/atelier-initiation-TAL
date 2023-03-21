#!/usr/bin/env python
# coding:utf-8
"""
Name : annotateText.py
Author : Aurelia Vasile, MSH, UCA

Created on : 07/03/2023 10:11

"""

import os
import spacy
import argparse
import xml.etree.ElementTree as ET

from cleaning import remove_messy_char
from xml.sax.saxutils import escape
from spacy_lefff import LefffLemmatizer, POSTagger
from spacy.language import Language


@Language.factory('french_lemmatizer')
def create_french_lemmatizer(nlp, name):
    return LefffLemmatizer(after_melt=True, default=True)


@Language.factory('melt_tagger')
def create_melt_tagger(nlp, name):
    return POSTagger()


def create_nlp_pipe():
    """make a custom nlp pipe for processing French text"""
    nlp = spacy.load('fr_core_news_sm')
    nlp.add_pipe('melt_tagger', after='parser')
    nlp.add_pipe('french_lemmatizer', after='melt_tagger')
    return nlp


def write_xml(inputFile, outputFile, nlp):
    '''
    open a txt file, add French part of speach and lemma for each token and output an xml file
    :param inputText: .txt file
    :param outputFile: .xml file
    :return: ElementTree object with xml hierarchy : <text><w pos=pos, lefffLemma=lefffLemma, spacyLemma=spacyLemma> text <w>
    '''

    # open and read a text file
    with open(inputFile, "r") as txtfile:
        txt = txtfile.read()

    # call the method remove_messy_char to clean the text
    cleanedText = remove_messy_char(txt)

    # generate an object nlp
    doc = nlp(cleanedText)

    # build the xml structure with <text> as element root
    racine = ET.Element("text")
    for token in doc:
        lefffLemma = token._.lefff_lemma
        pos = token._.melt_tagger
        spacyLemma = token.lemma_
        if lefffLemma is not None and pos is not None and spacyLemma is not None:
            # xml structure for each character <w lefffLemma=chercher, pos=V, spacyLemma=cherche> cherche </w>
            word = ET.SubElement(racine, "w", pos=pos, lefffLemma=escape(lefffLemma), spacyLemma=escape(spacyLemma))
            word.text = escape(token.text)

    tree = ET.ElementTree(racine)
    ET.indent(tree, space="  ", level=0)
    tree.write(outputFile, encoding="UTF-8", xml_declaration=True,  default_namespace=None, method="xml")


def parse_arguments():
    parser = argparse.ArgumentParser(description='Lemmatize text file(s), output XML')
    parser.add_argument('infiles', nargs='+',
                        help='List of text files to lemmatize')
    parser.add_argument('-o', '--outdir', default=os.path.curdir,
                        help='Output directory (where to place XML files)')
    return parser.parse_args()


def main():
    args = parse_arguments()
    nlp = create_nlp_pipe()
    for infile in args.infiles:
        print(f"Processing {infile}...")
        basename = os.path.splitext(os.path.basename(infile))[0]
        outfile = os.path.join(args.outdir, f"{basename}.xml")
        write_xml(infile, outfile, nlp)


if __name__ == '__main__':
    main()
