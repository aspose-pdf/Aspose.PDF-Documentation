---
title: Aspose.PDF Java pour Ruby  
type: docs  
weight: 20  
url: fr/java/aspose-pdf-java-for-ruby/  
lastmod: "2021-06-05"  
---
## Introduction

### Rjb - Ruby Java Bridge

RJB est un programme de pont qui connecte Ruby et Java avec l'interface native Java. Rake + Rjb est l'outil de construction plus puissant et utile que Maven et Ant. Vous pouvez tester votre classe de logique métier Java elle-même avec le mock de Rjb. Il aide à migrer l'objet modèle de Struts dans votre application RoR. Mais attention à construire une application Swing, Ruby (et Rjb) ne prend pas en compte la gestion des threads natifs de la JVM.

### Aspose.PDF pour Java

Aspose.PDF pour Java est un composant de création de documents PDF qui permet à vos applications Java de lire, écrire et manipuler des documents PDF sans utiliser Adobe Acrobat.

Aspose.PDF pour Java est un composant à prix abordable qui offre une incroyable richesse de fonctionnalités, y compris : des options de compression PDF, la création et la manipulation de tableaux, la prise en charge des graphiques, des fonctions d'image, une fonctionnalité de lien hypertexte étendue, des contrôles de sécurité avancés et une gestion personnalisée des polices.

Aspose.PDF for Java vous permet de créer des fichiers PDF directement via l'API fournie et les modèles XML. Utiliser Aspose.PDF for Java vous permettra également d'ajouter des fonctionnalités PDF à vos applications en un rien de temps.

### Aspose.PDF Java pour Ruby

Le projet Aspose.PDF Java pour Ruby montre comment différentes tâches peuvent être réalisées en utilisant les API Aspose.PDF Java dans Ruby. Ce projet vise à fournir des exemples utiles pour les développeurs Ruby qui souhaitent utiliser Aspose.PDF for Java dans leurs projets Ruby en utilisant Rjb (Ruby Java Bridge).

## Configuration système requise et plateformes supportées

### Configuration système requise

Voici les configurations système requises pour utiliser Aspose.PDF Java pour Ruby :

- Gem Rjb est configuré
- Composant Aspose.PDF téléchargé

### Plateformes supportées

Voici les plateformes supportées :

- Ruby 2.2.x ou supérieur et DevKit respectif.
- Java 1.5 ou supérieur

## Téléchargements

### Télécharger les bibliothèques requises

Téléchargez les bibliothèques requises mentionnées ci-dessous. Celles-ci sont nécessaires pour exécuter les exemples Aspose.PDF Java pour Ruby.

- [Composant Aspose.PDF pour Java](https://repository.aspose.com/webapp/#/artifacts/browse/tree/General/repo/com/aspose/aspose-pdf)

### Télécharger des exemples depuis des sites de codage social

Les versions suivantes d'exemples fonctionnels sont disponibles au téléchargement sur les sites de codage social mentionnés ci-dessous :

GitHub

- [Aspose.PDF Java pour Ruby](https://github.com/aspose-pdf/Aspose.PDF-for-Java/tree/master/Plugins/Aspose_Pdf_Java_for_Ruby)

## Installation et utilisation

### Installation

Il est très simple et facile d'installer la gem Aspose.PDF Java pour Ruby, veuillez suivre ces étapes simples :

1. Exécutez la commande suivante.

{{< highlight java >}}

 $ gem install aspose-pdfjava

{{< /highlight >}}

1. Téléchargez le composant Aspose.PDF pour Java requis à partir du lien suivant.
   <https://downloads.aspose.com/pdf/java>
1. Créez un dossier "jars" à la racine de la gem Aspose.PDF Java pour Ruby et copiez-y le composant téléchargé.

### Utilisation

Incluez les fichiers requis pour travailler avec l'exemple helloworld.

{{< highlight java >}}

 require File.dirname(File.dirname(File.dirname(__FILE__))) + '/lib/aspose-pdfjava'

include Asposepdfjava

include Asposepdfjava::HelloWorld


initialize_aspose_pdf

{{< /highlight >}}

Comprenons le code ci-dessus.

1. La première ligne s'assure que le pdf aspose est chargé et disponible.
1. Inclure les fichiers nécessaires pour accéder au pdf aspose.
1. Initialiser les bibliothèques. Les classes JAVA aspose sont chargées à partir du chemin fourni dans le fichier aspose.yml.

## Support, Élargir et Contribuer

### Support

Dès les premiers jours d'Aspose, nous savions que donner simplement de bons produits à nos clients ne suffirait pas. Nous devions également offrir un bon service. Nous sommes nous-mêmes des développeurs et comprenons combien il est frustrant qu'un problème technique ou une bizarrerie dans le logiciel vous empêche de faire ce que vous devez faire. Nous sommes ici pour résoudre les problèmes, pas pour en créer.

C'est pourquoi nous offrons un support gratuit. Toute personne utilisant notre produit, qu'elle l'ait acheté ou qu'elle utilise une évaluation, mérite toute notre attention et notre respect.

Vous pouvez enregistrer tout problème ou suggestion lié à Aspose.PDF Java pour Ruby en utilisant l'une des plateformes suivantes :

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/issues)

### Étendre et Contribuer

Aspose.PDF Java pour Ruby est open source et son code source est disponible sur les principaux sites de codage social listés ci-dessous. Les développeurs sont encouragés à télécharger le code source et à contribuer en suggérant ou ajoutant de nouvelles fonctionnalités ou en améliorant les existantes, afin que d'autres puissent également en bénéficier.

### Code Source

Vous pouvez obtenir le dernier code source à partir de l'un des emplacements suivants :

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/tree/master/Plugins/Aspose_Pdf_Java_for_Ruby)

## Exemples de Code

Cette section comprend les sujets suivants :

- [Télécharger et configurer Aspose.Pdf en Ruby](/pdf/java/download-and-configure-aspose-pdf-in-ruby/)
- [Guide du programmeur Ruby](/pdf/java/ruby-programmers-guide/)
  - [Travailler avec l'objet Document en Ruby](/pdf/java/working-with-document-object-in-ruby/)
    - [Ajouter du JavaScript en Ruby](/pdf/java/adding-javascript-in-ruby/)
    - [Ajouter des calques au fichier PDF en Ruby](/pdf/java/add-layers-to-pdf-file-in-ruby/)

    - [Ajouter une table des matières à un PDF existant en Ruby](/pdf/java/add-toc-to-existing-pdf-in-ruby/)
- [Obtenir les propriétés de la fenêtre du document et de l'affichage des pages en Ruby](/pdf/java/get-document-window-and-page-display-properties-in-ruby/)
- [Obtenir des informations sur le fichier PDF en Ruby](/pdf/java/get-pdf-file-information-in-ruby/)
- [Obtenir les métadonnées XMP d'un fichier PDF en Ruby](/pdf/java/get-xmp-metadata-from-pdf-file-in-ruby/)
- [Optimiser le document PDF pour le Web en Ruby](/pdf/java/optimize-pdf-document-for-the-web-in-ruby/)
- [Optimiser la taille du fichier PDF en Ruby](/pdf/java/optimize-pdf-file-size-in-ruby/)
- [Supprimer les métadonnées du PDF en Ruby](/pdf/java/remove-metadata-from-pdf-in-ruby/)
- [Définir les propriétés de la fenêtre du document et de l'affichage des pages en Ruby](/pdf/java/set-document-window-and-page-display-properties-in-ruby/)
- [Définir l'expiration du PDF en Ruby](/pdf/java/set-pdf-expiration-in-ruby/)
- [Définir des informations sur le fichier PDF en Ruby](/pdf/java/set-pdf-file-information-in-ruby/)
- [Travailler avec les pages en Ruby](/pdf/java/working-with-pages-in-ruby/)

- [Concaténer des fichiers PDF en Ruby](/pdf/java/concatenate-pdf-files-in-ruby/)
- [Supprimer une page particulière d'un fichier PDF en Ruby](/pdf/java/delete-a-particular-page-from-the-pdf-file-in-ruby/)
- [Obtenir une page particulière dans un fichier PDF en Ruby](/pdf/java/get-a-particular-page-in-a-pdf-file-in-ruby/)
- [Obtenir le nombre de pages d'un PDF en Ruby](/pdf/java/get-page-count-of-pdf-in-ruby/)
- [Obtenir les propriétés de la page en Ruby](/pdf/java/get-page-properties-in-ruby/)
- [Insérer une page vide à la fin d'un fichier PDF en Ruby](/pdf/java/insert-an-empty-page-at-end-of-pdf-file-in-ruby/)
- [Insérer une page vide dans un fichier PDF en Ruby](/pdf/java/insert-an-empty-page-into-a-pdf-file-in-ruby/)
- [Diviser un fichier PDF en pages individuelles en Ruby](/pdf/java/split-pdf-file-into-individual-pages-in-ruby/)
- [Mettre à jour les dimensions de la page en Ruby](/pdf/java/update-page-dimensions-in-ruby/)
- [Travailler avec du texte en Ruby](/pdf/java/working-with-text-in-ruby/)
- [Ajouter une chaîne HTML en utilisant DOM en Ruby](/pdf/java/add-html-string-using-dom-in-ruby/)
- [Ajouter du texte à un fichier PDF existant en Ruby](/pdf/java/add-text-to-an-existing-pdf-file-in-ruby/)
- [Extraire le texte de toutes les pages d'un document PDF en Ruby](/pdf/java/extract-text-from-all-the-pages-of-a-pdf-document-in-ruby/)
  - [Travailler avec la conversion de documents en Ruby](/pdf/java/working-with-document-conversion-in-ruby/)
    - [Convertir HTML en format PDF en Ruby](/pdf/java/convert-html-to-pdf-format-in-ruby/)
    - [Convertir des pages PDF en images en Ruby](/pdf/java/convert-pdf-pages-to-images-in-ruby/)
    - [Convertir PDF en format DOC ou DOCX en Ruby](/pdf/java/convert-pdf-to-doc-or-docx-format-in-ruby/)
    - [Convertir PDF en classeur Excel en Ruby](/pdf/java/convert-pdf-to-excel-workbook-in-ruby/)
    - [Convertir PDF en format SVG en Ruby](/pdf/java/convert-pdf-to-svg-format-in-ruby/)
    - [Convertir un fichier SVG en format PDF en Ruby](/pdf/java/convert-svg-file-to-pdf-format-in-ruby/)
- [Supporter, étendre et contribuer à Aspose.Pdf en Ruby](/pdf/java/support-extend-and-contribute-to-aspose-pdf-in-ruby/)