---
title: Extraire les pièces jointes d'un fichier PDF
type: docs
weight: 10
url: /fr/net/extract-attachments/
description: Cette section explique comment extraire des pièces jointes d'un PDF avec la classe PdfExtractor.
lastmod: "2021-06-05"
---

Une des principales catégories sous les capacités d'extraction du [namespace Aspose.Pdf.Facades](https://reference.aspose.com/pdf/net/aspose.pdf.facades) est l'extraction de pièces jointes. Cette catégorie fournit un ensemble de méthodes, qui non seulement aident à extraire les pièces jointes, mais fournissent également les méthodes qui peuvent vous donner les informations relatives aux pièces jointes, c'est-à-dire les méthodes [GetAttachmentInfo](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/methods/getattachmentinfo) et [GetAttachName](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/methods/getattachnames) fournissent respectivement les informations de pièce jointe et le nom de la pièce jointe. Afin d'extraire puis d'obtenir des pièces jointes, nous utilisons les méthodes [ExtractAttachment](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/methods/extractattachment) et [GetAttachment](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/methods/getattachment).

L'extrait de code suivant vous montre comment utiliser les méthodes PdfExtractor :

```csharp
public static void ExtractAttachments()
{
    PdfExtractor pdfExtractor = new PdfExtractor();
    pdfExtractor.BindPdf(_dataDir + "sample-attach.pdf");

    // Extraire les pièces jointes
    pdfExtractor.ExtractAttachment();

    // Obtenir les noms des pièces jointes
    if (pdfExtractor.GetAttachNames().Count > 0)
    {
         Console.WriteLine("Extraction et stockage...");
         // Obtenir les pièces jointes extraites
         pdfExtractor.GetAttachment(_dataDir);
    }
}
```