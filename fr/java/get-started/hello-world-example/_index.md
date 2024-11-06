---
title: Hello World Java Example
linktitle: Hello World Example
type: docs
weight: 40
url: fr/java/hello-world-example/
description: Cette page montre comment utiliser une programmation simple pour créer un document PDF contenant le texte - Hello World en utilisant Aspose.PDF pour Java.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Exemple Hello World

Un exemple « Hello World » est traditionnellement utilisé pour présenter les fonctionnalités d'un langage de programmation ou d'un logiciel avec un cas d'utilisation simple.

Aspose.PDF pour Java API permet aux développeurs d'applications Java de créer, lire, éditer et manipuler des fichiers PDF dans leurs applications. Il vous permet de lire et de convertir plusieurs types de fichiers différents vers et depuis le format de fichier PDF. Cet article Hello World montre comment créer un fichier PDF en Java en utilisant Aspose.PDF pour Java API. Après [avoir installé Aspose.PDF pour Java](/pdf/java/installation/) dans votre environnement, vous pouvez exécuter l'exemple de code ci-dessous pour voir comment fonctionne l'API Aspose.PDF.

L'extrait de code ci-dessous suit ces étapes :

1. Instancier un objet [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/class-use/Document)
1. Ajouter une [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/page) à l'objet document
1. Créer un objet [TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/TextFragment)
1. Ajouter TextFragment à la collection de [Paragraph](https://reference.aspose.com/pdf/java/com.aspose.pdf/Paragraphs) de la page
1. Enregistrer le document PDF résultant

Le code suivant est un programme Hello World pour démontrer le fonctionnement de l'API Aspose.PDF pour Java.

```java
// Initialiser l'objet document
Document document = new Document();
 
// Ajouter une page
Page page = document.getPages().add();
 
// Ajouter du texte à la nouvelle page
page.getParagraphs().add(new TextFragment("Hello World!"));
 
// Enregistrer le PDF mis à jour
document.save("HelloWorld_out.pdf");
```