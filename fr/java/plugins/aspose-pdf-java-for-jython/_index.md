---
title: Aspose.PDF Java pour Jython
linktitle: Aspose.PDF Java pour Jython
type: docs
weight: 60
url: /java/aspose-pdf-java-for-jython/
description: Combinez la puissance d'Aspose.PDF pour Java avec Jython. Manipulez sans effort les fichiers PDF dans un environnement Java basé sur Python.
lastmod: "2026-06-09"
---
## 
Introduction


### 
Qu’est-ce que Jython ?

Jython est une implémentation Java de Python qui combine puissance expressive et clarté. Jython est disponible gratuitement pour une utilisation commerciale et non commerciale et est distribué avec le code source. Jython est complémentaire de Java et est particulièrement adapté aux tâches suivantes :


- 
**Scripts intégrés** : les programmeurs Java peuvent ajouter les bibliothèques Jython à leur système pour permettre aux utilisateurs finaux d'écrire des scripts simples ou compliqués qui ajoutent des fonctionnalités à l'application.

- 
**Expérimentation interactive** - Jython fournit un interpréteur interactif qui peut être utilisé pour interagir avec des packages Java ou avec des applications Java en cours d'exécution. Cela permet aux programmeurs d'expérimenter et de déboguer n'importe quel système Java utilisant Jython.

- 
**Développement rapide d'applications** - Les programmes Python sont généralement 2 à 10 fois plus courts que le programme Java équivalent. Cela se traduit directement par une productivité accrue des programmeurs. L'interaction transparente entre Python et Java permet aux développeurs de mélanger librement les deux langages à la fois pendant le développement et lors de l'expédition des produits.


### 
Aspose.PDF pour Java

Aspose.PDF pour Java est un composant de création de documents PDF qui permet à vos applications Java de lire, écrire et manipuler des documents PDF sans utiliser Adobe Acrobat.



Aspose.PDF pour Java est un composant à prix abordable qui offre une incroyable richesse de fonctionnalités, notamment : des options de compression PDF, la création et la manipulation de tableaux, la prise en charge de graphiques, des fonctions d'image, une fonctionnalité étendue de liens hypertexte, des contrôles de sécurité étendus et une gestion des polices personnalisées.



Aspose.PDF pour Java vous permet de créer des fichiers PDF directement via les modèles API et XML fournis. L'utilisation d'Aspose.PDF pour Java vous permettra également d'ajouter des fonctionnalités PDF à vos applications en un rien de temps.


### 
Aspose.PDF Java pour Jython



Aspose.PDF Java pour Jython est un projet qui démontre/fournit les exemples d'utilisation de l'API Aspose.PDF pour Java dans Jython.

## Configuration système requise et plates-formes prises en charge


### 
Configuration système requise



Voici la configuration système requise pour utiliser Aspose.PDF Java pour Jython :


- 
Java 1.5 ou supérieur installé

- 
Composant Aspose.PDF téléchargé
- Python 2.7.0


### 
Plateformes prises en charge



Voici les plates-formes prises en charge :


- 
Aspose.PDF 15.4 et supérieur.

- 
EDI Java (Eclipse, NetBeans...)

## Télécharger l'installation et l'utilisation


### 
Téléchargement



Les versions suivantes d'exemples en cours d'exécution peuvent être téléchargées depuis GitHub :


- 
[Github] (https://github.com/aspose-pdf/Aspose.PDF-for-Java/tree/master/Plugins/Aspose-Pdf-Java-for-Jython)



Téléchargez le composant Aspose.PDF pour Java :

- [Aspose.PDF pour Java] (https://downloads.aspose.com/pdf/java)


### 
Installation


- 
Placez le fichier jar Aspose.PDF pour Java téléchargé dans le répertoire "lib".

- 
Remplacez "your-lib" par le nom du fichier jar téléchargé dans le fichier _*init*_.py.


### 
Utilisation

Vous pouvez convertir un PDF en document doc à l'aide de l'exemple de code suivant :


```java
from aspose-pdf import Settings
from com.aspose.pdf import Document

class PdfToDoc:

    def __init__(self):
        dataDir = Settings.dataDir + 'WorkingWithDocumentConversion/PdfToDoc/'

        # Open the target document
        pdf = Document(dataDir + 'input1.pdf')

        # Save the concatenated output file (the target document)
        pdf.save(dataDir + "output.doc")

        print "Document has been converted successfully"

if __name__ == '__main__':

    PdfToDoc()
```

## 
Soutenir, étendre et contribuer


### 
Assistance



Dès les premiers jours d’Aspose, nous savions qu’offrir à nos clients de bons produits ne suffirait pas. Nous devions également offrir un bon service. Nous sommes nous-mêmes développeurs et comprenons à quel point il est frustrant lorsqu'un problème technique ou une bizarrerie dans le logiciel vous empêche de faire ce que vous devez faire. Nous sommes là pour résoudre les problèmes, pas pour les créer.



C'est pourquoi nous offrons une assistance gratuite. Quiconque utilise notre produit, qu'il l'ait acheté ou qu'il utilise une évaluation, mérite toute notre attention et notre respect.

Vous pouvez enregistrer tous les problèmes ou suggestions liés à Aspose.PDF Java pour Jython en utilisant l'une des plates-formes suivantes :


- 
[Github] (https://github.com/aspose-pdf/Aspose.PDF-for-Java/issues)


### 
Prolongez et contribuez



Aspose.PDF Java pour Jython est open source et son code source est disponible sur les principaux sites Web de codage social répertoriés ci-dessous. Les développeurs sont encouragés à télécharger le code source et à contribuer en suggérant ou en ajoutant de nouvelles fonctionnalités ou en améliorant celles existantes, afin que d'autres puissent également en bénéficier.


### 
Code source

Vous pouvez obtenir le dernier code source à partir de l'un des emplacements suivants


- 
[Github] (https://github.com/aspose-pdf/Aspose.PDF-for-Java)
