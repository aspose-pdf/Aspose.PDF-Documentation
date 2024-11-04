---
title: Convertir HTML en PDF
linktitle: Convertir HTML en PDF
type: docs
weight: 40
url: /php-java/convert-html-to-pdf/
lastmod: "2024-05-20"
description: Ce sujet vous montre comment Aspose.PDF permet de convertir les formats HTML et MHTML en fichier PDF.
sitemap:
    changefreq: "monthly"
    priority: 0.8
---

## Aperçu

Cet article explique comment convertir HTML en PDF en utilisant PHP. Le code est très simple, il suffit de charger le HTML dans la classe Document et de l'enregistrer en tant que PDF de sortie. Convertir MHTML en PDF en Java est également similaire. Il couvre les sujets suivants

## Bibliothèque Java pour convertir HTML en PDF

**Aspose.PDF pour PHP via Java** est une API de manipulation de PDF qui vous permet de convertir de manière transparente n'importe quel document HTML existant en PDF.
Le processus de conversion de HTML en PDF peut être personnalisé de manière flexible.

## Convertir HTML en PDF

L'exemple de code Java suivant montre comment convertir un document HTML en PDF.

1. Créez une instance de la classe [HtmlLoadOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/HtmlLoadOptions).

1. Initialiser l'objet [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Enregistrer le document PDF de sortie en appelant la méthode [Document.save(String)](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/#save-java.lang.String-).

```php
    // Créer une instance de HtmlLoadOptions pour spécifier les options de chargement pour le fichier HTML
    $loadOption = new HtmlLoadOptions();

    // Créer un nouvel objet Document et charger le fichier HTML
    $document = new Document($inputFile, $loadOption);

    // Enregistrer le document en tant que fichier PDF
    $document->save($outputFile);
```

## Conversion avancée de HTML en PDF

Le moteur de conversion HTML dispose de plusieurs options qui nous permettent de contrôler le processus de conversion.

### Support des Media Queries

1. Créer un [LoadOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/HtmlLoadOptions) HTML.
1. [Définir le mode Print ou Screen](https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlloadoptions/#setHtmlMediaType-int-).

1. Initialiser [objet Document](https://reference.aspose.com/page/java/com.aspose.page/document).
1. Enregistrer le document PDF de sortie.

Les requêtes média sont une technique populaire pour fournir une feuille de style adaptée à différents appareils. Nous pouvons définir le type d'appareil en utilisant la classe [HtmlMediaType](https://reference.aspose.com/pdf/java/com.aspose.pdf/HtmlMediaType).

```php

    // Créez une instance de HtmlLoadOptions pour spécifier les options de chargement pour le fichier HTML
    $htmlMediaType = new HtmlMediaType();

    // Définir le mode Imprimer ou Écran
    $loadOption->setHtmlMediaType($htmlMediaType->Print);

    // Créez un nouvel objet Document et chargez le fichier HTML
    $document = new Document($inputFile, $loadOption);

    // Enregistrez le document en tant que fichier PDF
    $document->save($outputFile);
```

### Activer (désactiver) l'intégration des polices

1. Ajouter de nouvelles [LoadOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/HtmlLoadOptions) Html.
1. Désactiver l'intégration des polices.
1. Enregistrer un nouveau document.

Les pages HTML utilisent souvent des polices (par exemple.
 fonts à partir d'un dossier local, Google Fonts, etc). Nous pouvons également contrôler l'intégration des polices dans un document en utilisant une propriété [setEmbedFonts](https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlloadoptions/#setEmbedFonts-boolean-).

```php

    // Créer une instance de HtmlLoadOptions pour spécifier les options de chargement pour le fichier HTML
    $loadOption = new HtmlLoadOptions();

    // Désactiver l'intégration des polices
    $loadOption->setEmbedFonts(true);

    // Créer un nouvel objet Document et charger le fichier HTML
    $document = new Document($inputFile, $loadOption);

    // Enregistrer le document en tant que fichier PDF
    $document->save($outputFile);
```

## Convertir MHTML en PDF

<abbr title="Encapsulation MIME de documents HTML agrégés">MHTML</abbr>, diminutif de MIME HTML, est un format d'archive de page web utilisé pour combiner des ressources qui sont généralement représentées par des liens externes (tels que des images, des animations Flash, des applets Java et des fichiers audio) avec du code HTML en un seul fichier. The content of an MHTML file is encoded as if it were an HTML email message, using the MIME type multipart/related.

Next code snippet show how to covert MHTML files to PDF format with Java:

```php

    // Créez une nouvelle instance de la classe MhtLoadOptions.
    $loadOption = new MhtLoadOptions();

    // Créez une nouvelle instance de la classe Document et chargez le fichier MHTML.
    $document = new Document($inputFile, $loadOption);

    // Enregistrez le document en tant que fichier PDF.
    $document->save($outputFile);
```