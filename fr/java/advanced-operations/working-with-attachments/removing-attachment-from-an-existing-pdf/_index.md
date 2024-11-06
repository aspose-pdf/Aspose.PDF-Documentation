---
title: Suppression de pièce jointe d'un PDF existant
linktitle: Suppression de pièce jointe d'un PDF existant
type: docs
weight: 30
url: fr/java/removing-attachment-from-an-existing-pdf/
description: Aspose.PDF peut supprimer des pièces jointes de vos documents PDF. Utilisez l'API Java PDF pour supprimer des pièces jointes dans les fichiers PDF avec la bibliothèque Aspose.PDF.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Aspose.PDF peut supprimer des pièces jointes des fichiers PDF. Les pièces jointes d'un document PDF sont conservées dans la collection EmbeddedFiles de l'objet Document.

Les pièces jointes d'un document PDF sont conservées dans la collection [EmbeddedFiles](https://reference.aspose.com/pdf/java/com.aspose.pdf/EmbeddedFileCollection) de l'objet [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document).

Pour supprimer toutes les pièces jointes associées à un fichier PDF :

1. Appelez la méthode delete(..) de la collection [EmbeddedFiles](https://reference.aspose.com/pdf/java/com.aspose.pdf/EmbeddedFileCollection).

1. Enregistrez le fichier mis à jour en utilisant la méthode save de l'objet [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document).

Le code suivant montre comment supprimer toutes les pièces jointes d'un document PDF.

```java
   public static void DeleteAllAttachmentsFromPDF(){
  // Ouvrir un document
  Document pdfDocument = new Document(_dataDir+"input.pdf");
  // Supprimer toutes les pièces jointes
  pdfDocument.getEmbeddedFiles().delete();
  // Enregistrez le fichier mis à jour
  pdfDocument.save("output.pdf");

    }
```