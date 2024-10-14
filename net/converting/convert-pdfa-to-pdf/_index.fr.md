---
title: Convertir le format PDF/A en format PDF
linktitle: Convertir le format PDF/A en format PDF
type: docs
weight: 110
url: /net/convert-pdfa-to-pdf/
lastmod: "2021-11-01"
description: Ce sujet vous montre comment Aspose.PDF permet de convertir un fichier PDF/A en document PDF avec la bibliothèque .NET.
sitemap:
    changefreq: "monthly"
    priority: 0.8
---

Le snippet de code suivant fonctionne également avec la bibliothèque [Aspose.PDF.Drawing](/pdf/net/drawing/).

## Convertir un document PDF/A en PDF

Convertir un document PDF/A en PDF signifie retirer la restriction <abbr title="Portable Document Format Archive">PDF/A</abbr> du document original.
La classe [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) possède la méthode [RemovePdfaCompliance(..)](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/removepdfacompliance) pour retirer les informations de conformité PDF du fichier source.

```csharp
public static void ConvertPDFAtoPDF()
{
    // Pour des exemples complets et des fichiers de données, veuillez aller sur https://github.com/aspose-pdf/Aspose.PDF-for-.NET
    Document pdfDocument = new Document(_dataDir + "PDFAToPDF.pdf");
    // Retirer les informations de conformité PDF/A
    pdfDocument.RemovePdfaCompliance();
    // Enregistrer le document mis à jour
    pdfDocument.Save(_dataDir + "PDFAToPDF_out.pdf");
}
```
Cette info est également supprimée si vous apportez des modifications au document (par exemple, ajouter des pages). Dans l'exemple suivant, le document résultant perd la conformité PDF/A après l'ajout de pages.

```csharp
public static void ConvertPDFAtoPDFAdvanced()
{
    // Pour des exemples complets et des fichiers de données, veuillez aller sur https://github.com/aspose-pdf/Aspose.PDF-for-.NET
    Document pdfDocument = new Document(_dataDir + "PDFAToPDF.pdf");
    // Ajouter une nouvelle page (vide) supprime les informations de conformité PDF/A.
    pdfDocument.Pages.Add();
    // Enregistrer le document mis à jour
    pdfDocument.Save(_dataDir + "PDFAToPDF_out.pdf");
}
```
