#!/usr/bin/env python
# coding:utf-8
"""
Name : annotateOneFile.py
Author : Aurelia Vasile, MSH, UCA

Created on : 13/03/2023 15:00

"""
import argparse
from annotateText import write_xml

parser = argparse.ArgumentParser()
parser.add_argument("inputTextFile", help="fichier texte en format .txt destiné à être lemmatisé. A ajouter en tant que nom de chemin")
args = parser.parse_args()
# paramètre à rajouter par l'utilisateur avec le chemin vers le dossier contenant le fichier txt comme dans l'exemple
#inputTextFile = "test/BUCA_Bastaire_Roman_Aventures_C95455.txt"
inputTextFile = args.inputTextFile

# sur le chemin récupéré, remplace l'extension .txt avec l'extension .xml (la sauvegarde du xml se fera dans le même dossier que le .txt
outputXMLFile = inputTextFile[:-4] + ".xml"

# appelle la fonction write_xml pour générer un fichier xml sur un seul fichier txt.
write_xml(inputTextFile, outputXMLFile)