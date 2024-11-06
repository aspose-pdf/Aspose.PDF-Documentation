---
title: Hello World PHP via Java Exemple
linktitle: Hello World Exemple
type: docs
weight: 40
url: fr/php-java/hello-world-example/
description: Cette page montre comment utiliser une programmation simple pour créer un document PDF contenant le texte - Hello World en utilisant Aspose.PDF pour PHP via Java.
lastmod: "2024-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Hello World Exemple

Un exemple « Hello World » est généralement utilisé pour démontrer les fonctionnalités de base d'un langage de programmation ou d'un logiciel avec un cas d'utilisation simple.

Aspose.PDF pour PHP via Java API permet aux développeurs de créer, lire, éditer et manipuler des fichiers PDF dans leurs applications Java. Il prend en charge la lecture et la conversion de divers types de fichiers vers et à partir du format PDF. Cet article Hello World montre comment créer un fichier PDF en utilisant Aspose.PDF pour PHP via Java API. Après [avoir installé Aspose.PDF pour PHP via Java](/pdf/php-java/installation/) dans votre environnement, vous pouvez exécuter l'exemple de code ci-dessous pour voir comment fonctionne l'API Aspose.PDF.


L'extrait de code ci-dessous suit ces étapes :

1. Instancier un objet [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/class-use/Document)
1. Ajouter une [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/page) à l'objet document
1. Créer un objet [TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/TextFragment)
1. Ajouter TextFragment à la collection [Paragraph](https://reference.aspose.com/pdf/java/com.aspose.pdf/Paragraphs) de la page
1. Enregistrer le document PDF résultant

Le code suivant est un programme Hello World pour démontrer le fonctionnement de Aspose.PDF pour PHP via Java API.

```php
    $document = new Document();    
    $page = $document->getPages()->add();
    $textFragment = new TextFragment("Hello World!");    
    $page->getParagraphs()->add($textFragment);
    $document->save($outputFile);
```