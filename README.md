# atelier-initiation-TAL
Espace qui réunit des documents textuels et des scripts en Python permettant de réaliser une annotation morphosyntaxique de textes. 
## Les données
Le répositoire contient un répertoire nommé **corpus** qui contient 2 collections de textes: 
1. collection_aventure faire référence à une collection intitulée *Collection d'aventure* contenant des romans et nouvelles publiés entre 1916 et probablement 1926. Ce dossier est composé de 40 fichiers textes, dont certains contiennent plus de 300.000 mots. 
2. roman_aventure fait référence à une collection intitulée *Petit roman d'aventure* et publiée entre 1032 et 1937. Le dossier est composé de 70 fichiers. 

## Les scripts
Le répositoire contient 4 scripts en python.
1. *cleaning.py* contient une méthode qui permet de nettoyer les textes des caractères indésirables. 
2. *testLemmatiseOnePhrase.py* permet de lancer les scripts de lemmatisation sur une phrase de teste. Elle appelle la méthode de nettoyage du *cleaning.py*
3. *annotateText.py* contient une méthode qui génère un fichier xml pour chaque fichier de texte qu'on lui fournit. Elle peut-être exécutée sur un fichier de test (dans le répertoire **test**) 
4. *annotateMultipleFiles.py* appelle la methode définie dans *annotateText.py* pour réaliser une annotation morphosyntaxique par lot sur un ensemble de fichiers .txt d'un répertoire donné. 

La lemmatisation est réalisée grâce à la library [spacy](https://spacy.io/) de python et surtout à un pipeline appellé [Lefff](https://github.com/sammous/spacy-lefff) (Lexique des Formes Fléchies du Français), mis au point par l'equipe de l'INRIA. 
Pour en savoir plus, veuillez lire l'article publié sur HAL par les développeurs: https://hal.inria.fr/inria-00521242/

Pour tester la librarie standard de spacy pour le français, voir on line https://spacy.io/usage/spacy-101

### La liste des tags proposés par Lefff

```
ADJ 	   adjective
ADJWH	   interrogative adjective
ADV	   adverb
ADVWH	   interrogative adverb
CC	   coordination conjunction
CLO	   object clitic pronoun
CLR	   reflexive clitic pronoun
CLS	   subject clitic pronoun
CS	   subordination conjunction
DET	   determiner
DETWH	   interrogative determiner
ET	   foreign word
I	   interjection
NC	   common noun
NPP	   proper noun
P	   preposition
P+D	   preposition+determiner amalgam
P+PRO	   prepositon+pronoun amalgam
PONCT	   punctuation mark
PREF	   prefix
PRO	   full pronoun
PROREL	   relative pronoun
PROWH	   interrogative pronoun
V	   indicative or conditional verb form
VIMP	   imperative verb form
VINF	   infinitive verb form
VPP	   past participle
VPR	   present participle
VS	   subjunctive verb form
```

## Etapes à suivre pour installer les dépendances nécessaires au bon foncitonnement des scripts

* git clone https://github.com/MSH-Clermont/atelier-initiation-TAL.git

* Se placer dans le dossier créé et lancer un environnement virtuel avec les commandes suivantes :
	* python3 -m venv env
	* source ./env/bin/activate

* ecrire dans le terminal (dans le venv): pip install spacy
* ecrire dans le terminal (dans le venv): python -m spacy download fr_core_news_sm
* ecrire dans le terminal (dans le venv): pip install spacy-lefff

