#!/usr/bin/env python
# coding:utf-8
"""
Name : annotateMultipleFiles.py
Author : Aurelia Vasile, MSH, UCA

Created on : 07/03/2023 11:20

"""
import argparse
from annotateText import write_xml

# library to move through the folders
import os



INPUTFOLDER = input("renseigner le chemin du dossier contenant des fichiers textes : \n")

# test if the path gave by users exists
while os.path.exists(INPUTFOLDER) == False:
    #if not, a message will be shown
    INPUTFOLDER = input("chemin incorrect. renseigner le chemin du dossier contenant des fichiers textes : \n")

# if the path is correct, the treatment of text files starts
else:
    # for each text file
    for fileText in os.listdir(INPUTFOLDER):
        # test if file exists
        if fileText.endswith(".txt"):
            # get the name without the extension .txt and add the xml extension instead
            outputXmlFile = fileText[:-4] + ".xml"
            # call write_xml method
            write_xml(INPUTFOLDER+"/"+fileText, "outputXml/"+outputXmlFile)
            # indicate for users the path of output xml
            print("Le fichier xml se trouve dans outputXml/"+outputXmlFile)



