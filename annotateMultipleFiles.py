#!/usr/bin/env python
# coding:utf-8
"""
Name : annotateMultipleFiles.py
Author : Aurelia Vasile, MSH, UCA

Created on : 07/03/2023 11:20

"""
import argparse
from annotateText import write_xml

# library for fetching the path names of files
import glob
# library to move through the folders
import os


"""
parser = argparse.ArgumentParser()

parser.add_argument("inputTextsFolder", help="dossier dans lequel se trouve tous les fichiers txt à lemmatiser. A ajouter en tant que nom de chemin")

parser.add_argument("outputXmlFolder", help="dossier dans lequel seront sauvegarder les fichiers xml en sortie. A ajouter en tant que nom de chemin")

args = parser.parse_args()

inputTextFolder = args.inputTextsFolder
outputXmlFolder = args.outputXmlFolder
"""


INPUTFOLDER = input("ajouter le chemin du dossier avec des textes")
OUTPUFOLDER = input("ajouter le chemin des dossiers de sortie des xml")

for fileText in os.listdir(INPUTFOLDER):

    # for each text file
    if fileText.endswith(".txt"):
        # get the name without the extension .txt and add the xml extension instead
        outputXmlFile = fileText[:-4] + ".xml"

        write_xml(INPUTFOLDER+"/"+fileText, OUTPUFOLDER+"/"+outputXmlFile)
        print(outputXmlFile)
