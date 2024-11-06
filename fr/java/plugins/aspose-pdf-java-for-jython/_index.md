---
title: Aspose.PDF Java pour Jython
type: docs
weight: 60
url: fr/java/aspose-pdf-java-for-jython/
lastmod: "2021-06-05"
---

## Introduction

### Qu'est-ce que Jython ?

Jython est une implémentation Java de Python qui combine puissance expressive et clarté. Jython est librement disponible pour une utilisation commerciale et non commerciale et est distribué avec le code source. Jython est complémentaire à Java et est particulièrement adapté aux tâches suivantes :

- **Script embarqué** - Les programmeurs Java peuvent ajouter les bibliothèques Jython à leur système pour permettre aux utilisateurs finaux d'écrire des scripts simples ou compliqués qui ajoutent des fonctionnalités à l'application.
- **Expérimentation interactive** - Jython fournit un interpréteur interactif qui peut être utilisé pour interagir avec des packages Java ou avec des applications Java en cours d'exécution. Cela permet aux programmeurs d'expérimenter et de déboguer tout système Java en utilisant Jython.
- **Développement rapide d'applications** - Les programmes Python sont généralement 2 à 10 fois plus courts que le programme Java équivalent.
 Cela se traduit directement par une augmentation de la productivité des programmeurs. L'interaction transparente entre Python et Java permet aux développeurs de mélanger librement les deux langages à la fois pendant le développement et dans les produits livrés.

### Aspose.PDF pour Java

Aspose.PDF pour Java est un composant de création de documents PDF qui permet à vos applications Java de lire, écrire et manipuler des documents PDF sans utiliser Adobe Acrobat.

Aspose.PDF pour Java est un composant à prix abordable qui offre une incroyable richesse de fonctionnalités, notamment : options de compression PDF, création et manipulation de tables, prise en charge des graphiques, fonctions d'image, fonctionnalité étendue des hyperliens, contrôles de sécurité avancés et gestion des polices personnalisées.

Aspose.PDF pour Java vous permet de créer des fichiers PDF directement via l'API fournie et des modèles XML. Utiliser Aspose.PDF pour Java vous permettra également d'ajouter des capacités PDF à vos applications en un rien de temps.

### Aspose.PDF Java pour Jython

Aspose.PDF Java pour Jython est un projet qui démontre / fournit des exemples d'utilisation de l'API Aspose.PDF pour Java dans Jython.
## Exigences du système et plates-formes prises en charge

### Exigences du système

Voici les exigences du système pour utiliser Aspose.PDF Java pour Jython :

- Java 1.5 ou supérieur installé
- Composant Aspose.PDF téléchargé
- Jython 2.7.0

### Plates-formes prises en charge

Voici les plates-formes prises en charge :

- Aspose.PDF 15.4 et supérieur.
- IDE Java (Eclipse, NetBeans ...)

## Téléchargement, installation et utilisation

### Téléchargement

Les versions suivantes des exemples d'exécution sont disponibles pour téléchargement à partir de GitHub :

- [Github](https://github.com/aspose-pdf/Aspose.PDF-for-Java/tree/master/Plugins/Aspose-Pdf-Java-for-Jython)

Télécharger le composant Aspose.PDF pour Java :

- [Aspose.PDF for Java](https://downloads.aspose.com/pdf/java)

### Installation

- Placez le fichier jar Aspose.PDF pour Java téléchargé dans le répertoire "lib".
- Remplacez "your-lib" par le nom du fichier jar téléchargé dans le fichier _*init*_.py.

### Utilisation

Vous pouvez convertir un document Pdf en document doc en utilisant l'exemple de code suivant :

```java
from aspose-pdf import Settings
from com.aspose.pdf import Document

class PdfToDoc:

    def __init__(self):
        dataDir = Settings.dataDir + 'WorkingWithDocumentConversion/PdfToDoc/'


        # Ouvrir le document cible
        pdf = Document(dataDir + 'input1.pdf')

        # Enregistrer le fichier de sortie concaténé (le document cible)
        pdf.save(dataDir + "output.doc")

        print "Le document a été converti avec succès"


if __name__ == '__main__':       

    PdfToDoc()
```


## Support, Étendre et Contribuer

### Support

Dès les premiers jours d'Aspose, nous savions que donner à nos clients de bons produits ne suffirait pas. Nous devions également fournir un bon service. Nous sommes nous-mêmes développeurs et comprenons à quel point il est frustrant lorsqu'un problème technique ou une bizarrerie dans le logiciel vous empêche de faire ce que vous devez faire. Nous sommes ici pour résoudre des problèmes, pas pour en créer.

C'est pourquoi nous offrons un support gratuit. Toute personne qui utilise notre produit, qu'elle l'ait acheté ou qu'elle utilise une version d'évaluation, mérite toute notre attention et notre respect.

Vous pouvez signaler tout problème ou suggestion lié à Aspose.PDF Java pour Jython en utilisant l'une des plateformes suivantes :

- [Github](https://github.com/aspose-pdf/Aspose.PDF-for-Java/issues)

### Étendre et Contribuer

Aspose.PDF Java pour Jython est open source et son code source est disponible sur les principaux sites de codage social répertoriés ci-dessous.
 Les développeurs sont encouragés à télécharger le code source et à contribuer en suggérant ou en ajoutant de nouvelles fonctionnalités ou en améliorant celles existantes, afin que d'autres puissent également en bénéficier.

### Code Source

Vous pouvez obtenir le dernier code source à partir de l'un des emplacements suivants

- [Github](https://github.com/aspose-pdf/Aspose.PDF-for-Java)