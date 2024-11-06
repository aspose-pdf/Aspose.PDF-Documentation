---
title: Ajout d'une pièce jointe à un document PDF
linktitle: Ajout d'une pièce jointe à un document PDF
type: docs
weight: 10
url: fr/java/ajouter-une-pièce-jointe-à-un-document-pdf/
description: Cette page décrit comment ajouter une pièce jointe à un fichier PDF avec Java.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Les pièces jointes peuvent contenir une grande variété d'informations et peuvent être de différents types de fichiers. Cet article explique comment ajouter une pièce jointe à un fichier PDF.

1. Créez un objet [FileSpecification](https://reference.aspose.com/pdf/java/com.aspose.pdf/FileSpecification) qui contient le fichier que vous souhaitez joindre, et la description du fichier.

1. Ajoutez l'objet [FileSpecification](https://reference.aspose.com/pdf/java/com.aspose.pdf/FileSpecification) à la collection [EmbeddedFiles](https://reference.aspose.com/pdf/java/com.aspose.pdf/EmbeddedFileCollection) de l'objet [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) en utilisant la méthode [add(..)](https://reference.aspose.com/pdf/java/com.aspose.pdf/FileSpecification). La collection [EmbeddedFiles](https://reference.aspose.com/pdf/java/com.aspose.pdf/EmbeddedFileCollection) contient toutes les pièces jointes ajoutées à un fichier PDF.

Le snippet de code suivant vous montre comment ajouter une pièce jointe dans un document PDF.

```java
public class ExampleAttachments {
    
    private static String _dataDir = "/home/aspose/pdf-examples/Samples/Attachments/";

    public static void AddingAttachment() {
        // Ouvrir un document
  Document pdfDocument = new Document(_dataDir+"input.pdf");
  // Configurer un nouveau fichier à ajouter en tant que pièce jointe
  FileSpecification fileSpecification = new FileSpecification("sample.txt", "Fichier texte d'exemple");
  // Ajouter une pièce jointe à la collection de pièces jointes du document
  pdfDocument.getEmbeddedFiles().add(fileSpecification);
  // Enregistrer le document mis à jour
  pdfDocument.save("output.pdf");
    }
}
```