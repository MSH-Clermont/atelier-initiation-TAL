#!/usr/bin/env python
# coding:utf-8
"""
Name : cleaning.py
Author : Aurelia Vasile, MSH, UCA

Created on : 07/03/2023 09:42

"""
import re

def remove_messy_char(text):
    '''
    cleans the text of messy characters and symbols
    :param text: text (str): String to which the function is to be applied
    :return: cleaned string
    '''

    # replaces slanted apostrophes with straight apostrophes, line breaks and tabulations with a space
    outputText = text.replace("’", "'").replace("\n", " ").replace("\t", " ")

    # replaces odd characters with a space
    charRemoved = re.sub(r'[<>$_*■/©/{}•\\•°®\^]', ' ', outputText)

    # deletes dashes that occur more than twice
    multipleLineRemoved = re.sub(r'[-]{2,}', '', charRemoved)

    # deletes points that occur more than 4 times
    multiplePointsRemoved = re.sub(r'[\.]{4,}', '', multipleLineRemoved)

    # replaces spaces that occur more than twice with a single space
    emptySpacesReplaced = re.sub(r'[\s]{2,}', ' ', multiplePointsRemoved)

    return emptySpacesReplaced
