---
title: Extraire les Pièces Jointes d'un Fichier PDF
type: docs
weight: 10
url: /java/extract-attachments/
description: Cette section explique comment extraire les pièces jointes d'un PDF avec la classe PdfExtractor.
lastmod: "2021-06-05"
draft: false
---

Une des principales catégories sous les capacités d'extraction de [com.aspose.pdf.facades](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/package-frame) est l'extraction de pièces jointes.

 Cette catégorie fournit un ensemble de méthodes, qui non seulement aident à extraire les pièces jointes, mais fournissent également des méthodes qui peuvent vous donner les informations relatives aux pièces jointes, c'est-à-dire que les méthodes [GetAttachmentInfo](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfExtractor#getAttachmentInfo--) et [GetAttachName](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfExtractor#getAttachNames--) fournissent respectivement des informations sur les pièces jointes et le nom des pièces jointes. Afin d'extraire puis d'obtenir les pièces jointes, nous utilisons les méthodes [ExtractAttachment](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfExtractor#extractAttachment--) et [GetAttachment](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfExtractor#getAttachment--).

L'extrait de code suivant vous montre comment utiliser les méthodes PdfExtractor :

```java
  public static void ExtractAttachments() {
        PdfExtractor pdfExtractor = new PdfExtractor();
        pdfExtractor.bindPdf(_dataDir + "sample-attach.pdf");

        // Extraire les pièces jointes
        pdfExtractor.extractAttachment();

        // Obtenir les noms des pièces jointes
        if (pdfExtractor.getAttachNames().size() > 0) {
            System.out.println("Extraction et stockage...");
            // Obtenir les pièces jointes extraites
            pdfExtractor.getAttachment(_dataDir);
        }
    }
```