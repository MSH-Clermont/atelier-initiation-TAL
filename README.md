# Atelier d'initiation au Traitement Automatique des textes
Espace qui réunit des documents textuels et des scripts en Python permettant de réaliser une annotation morphosyntaxique de textes. 
Ces documents sont utilisés dans le cadre de l'atelier d'initiation aux traitements automatiques des textes organisé à la MSH de Clermont-Ferrand.   

## Les données textuelles
Le répository contient un répertoire nommé **corpus** qui contient 2 collections de textes : 
1. collection_aventure faire référence à une collection intitulée *Collection d'aventure* contenant des romans et nouvelles publiés entre 1916 et probablement 1926. Ce dossier est composé de 40 fichiers textes, dont certains contiennent plus de 300.000 mots. 
2. roman_aventure fait référence à une collection intitulée *Petit roman d'aventure* et publiée entre 1932 et 1937. Le dossier est composé de 70 fichiers. 
3. le dossier **xml** est le dossier contenant tous les fichiers annotés en formats xml prétraités pour l'atelier. 
4. le fichier **metadata.csv** contient les métadonnées des deux collections (en Dubin Core) extraites depuis la bibliothèque virtuelle de l'UCA qui met à disposition les deux collections: https://bibliotheque-virtuelle.bu.uca.fr/collection-tree/browse?collection=39. Pour un usage à destination de TXM, le fichier **metadata.csv** doit être placé dans le même dossier que les fichiers xml; il doit également contenir une colonne *id* avec les identifiants des fichiers xml annotés. 

## Les scripts
Le répository contient un répertoire nommé **scripts** qui contient 3 scripts en python.
1. *cleaning.py* contient une méthode qui permet de nettoyer les textes des caractères indésirables. 
2. *testLemmatiseOnePhrase.py* permet de lancer les scripts de lemmatisation sur une phrase de test. Elle appelle la méthode de nettoyage du *cleaning.py* et génère un fichier xml
3. *annotateText.py* est le script principal qui génère un ou plusieurs fichiers xml pour chaque fichier .txt qu'on lui fournit. Le script a besoin d'un paramètre obligatoire, à savoir le chemin vers le fichier .txt. Il a un paramètre optionnel à savoir le chemin du dossier de sortie.

Le dossier **test** contient des scripts python de test utilisés pour la première version de production des annotations.

La lemmatisation est réalisée grâce à la library [spacy](https://spacy.io/) de python et surtout à un pipeline appellé [Lefff](https://github.com/sammous/spacy-lefff) (Lexique des Formes Fléchies du Français), mis au point par l'equipe de l'INRIA. 
Pour en savoir plus, veuillez lire l'article publié sur HAL par les auteurs: https://hal.inria.fr/inria-00521242/

Tester la librairie standard de spacy pour le français en ligne: https://spacy.io/usage/spacy-101

### La liste des étiquettes proposées par Lefff

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

## Etapes à suivre pour lancer les traitements et installer les dépendances nécessaires au bon fonctionnement des scripts

* Dans le terminal (ou git bash), exécuter la commande
`git clone https://github.com/MSH-Clermont/atelier-initiation-TAL.git`

* Se placer dans le dossier créé et lancer un environnement virtuel avec la commande suivante (à exécuter seulement la première fois). [sur certaines machines, remplacer la commande *python* par la commande *py* ] :
    ```
    python -m venv venv
    ```
Activer l'environnement virtuel à chaque nouvelle connexion avec la commande suivante en fonction du système d'opération :
  * Windows : 
    ```
    source ./venv/Scripts/activate
    ```
    
  * Linux/Mac OS :
    ```
    source ./venv/bin/activate
    ```
Installation des bibliothèques python : 
* ecrire dans le terminal (en mode venv) : `pip install -r requirements.txt`
* ecrire dans le terminal (en mode venv) : `python -m spacy download fr_core_news_sm`

## Lancer le traitement

Exécuter une commande selon le modèle suivant pour annoter un fichier :
`python annotateText.py [monFichier.txt] -o [monDossierDeSortie]`

Exécuter une commande selon le modèle suivant pour annoter plusieurs fichiers :
`python annotateText.py [monDossier]/*.txt -o [monDossierDeSortie]` 