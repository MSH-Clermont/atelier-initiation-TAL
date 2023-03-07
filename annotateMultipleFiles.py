#!/usr/bin/env python
# coding:utf-8
"""
Name : annotateMultipleFiles.py
Author : Aurelia Vasile, MSH, UCA

Created on : 07/03/2023 11:20

"""

from annotateText import write_xml

# library for fetching the path names of files
import glob
# library to move through the folders
import os


for root, directories, files in os.walk('corpus/roman_aventure/text', topdown=False):
    # add into a list the absolute path of text files.
    path = glob.glob (root + "/" + "*.txt", recursive=True)
    # for each text file
    for fichierText in path:
        # if the file is in .txt format
        if os.path.isfile(fichierText):
            # get the name without the extension .txt and add the xml extension instead
            outputFile = fichierText[:-4] + ".xml"

            callMyFunctionThatGeneratesXML = write_xml(fichierText, outputFile)
            print(outputFile)
