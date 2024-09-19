---
title: Convertir des formats PDF en PDF/A
linktitle: Convertir des formats PDF en PDF/A
type: docs
weight: 100
url: /net/convert-pdf-to-pdfa/
lastmod: "2021-11-01"
description: Ce sujet vous montre comment Aspose.PDF permet de convertir un fichier PDF en un fichier PDF conforme au PDF/A.
sitemap:
    changefreq: "monthly"
    priority: 0.8
---

**Aspose.PDF pour .NET** vous permet de convertir un fichier PDF en un fichier PDF conforme au <abbr title="Portable Document Format / A">PDF/A</abbr>. Avant cela, le fichier doit être validé. Ce sujet explique comment.

{{% alert color="primary" %}}

Veuillez noter que nous suivons Adobe Preflight pour valider la conformité PDF/A. Tous les outils sur le marché ont leur propre "représentation" de la conformité PDF/A. Veuillez consulter cet article sur les outils de validation PDF/A pour référence. Nous avons choisi les produits Adobe pour vérifier comment Aspose.PDF produit des fichiers PDF parce qu'Adobe est au centre de tout ce qui est lié au PDF.

{{% /alert %}}

Convertissez le fichier en utilisant la méthode Convert de la classe Document.
{{% alert color="success" %}}
**Essayez de convertir un PDF en PDF/A en ligne**

Aspose.PDF pour .NET vous présente une application gratuite en ligne ["PDF to PDF/A-1A"](https://products.aspose.app/pdf/conversion/pdf-to-pdfa1a), où vous pouvez essayer d'explorer la fonctionnalité et la qualité de son fonctionnement.

[![Aspose.PDF Conversion PDF en PDF/A avec App Gratuite](pdf_to_pdfa.png)](https://products.aspose.app/pdf/conversion/pdf-to-pdfa1a)
{{% /alert %}}

Le code suivant fonctionne également avec la bibliothèque [Aspose.PDF.Drawing](/pdf/net/drawing/).

## Convertir un fichier PDF en PDF/A-1b

Le code suivant montre comment convertir des fichiers PDF en PDF conformes à PDF/A-1b.

```csharp
// Pour des exemples complets et des fichiers de données, veuillez aller à https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Le chemin vers le répertoire des documents.
string dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();

// Ouvrir le document
Document pdfDocument = new Document(dataDir + "PDFToPDFA.pdf");
           
// Convertir en document conforme à PDF/A
// Pendant le processus de conversion, la validation est également effectuée
pdfDocument.Convert(dataDir + "log.xml", PdfFormat.PDF_A_1B, ConvertErrorAction.Delete);

dataDir = dataDir + "PDFToPDFA_out.pdf";
// Sauvegarder le document de sortie
pdfDocument.Save(dataDir);
```
Pour effectuer uniquement la validation, utilisez la ligne de code suivante :

```csharp
// Pour des exemples complets et des fichiers de données, veuillez aller sur https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Le chemin vers le répertoire des documents.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

// Ouvrir le document
Document pdfDocument = new Document(dataDir + "ValidatePDFAStandard.pdf");

// Valider le PDF pour PDF/A-1a
pdfDocument.Validate(dataDir + "validation-result-A1A.xml", PdfFormat.PDF_A_1B);
```

## Convertir un fichier PDF en format PDF/A-3b

Aspose.PDF pour .NET prend également en charge la fonctionnalité de conversion d'un fichier PDF en format PDF/A-3b.

```csharp
// Pour des exemples complets et des fichiers de données, veuillez aller sur https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Le chemin vers le répertoire des documents.
string dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();

// Ouvrir le document
Document pdfDocument = new Document(dataDir + "input.pdf");           

pdfDocument.Convert(new MemoryStream(), PdfFormat.PDF_A_3B, ConvertErrorAction.Delete);

dataDir = dataDir + "PDFToPDFA3b_out.pdf";
// Sauvegarder le document de sortie
pdfDocument.Save(dataDir);
```
## Convertir un fichier PDF en format PDF/A-2u

Aspose.PDF pour .NET prend également en charge la fonctionnalité de convertir un fichier PDF en format PDF/A-2u.

```csharp
string inFile = "input.pdf";
string outFile = "output.pdf";
Aspose.PDF.Document doc = new Aspose.PDF.Document(inFile);
doc.Convert(new MemoryStream(), PdfFormat.PDF_A_2U, ConvertErrorAction.Delete);
doc.Save(outFile);
```

## Convertir un fichier PDF en format PDF/A-3u

Aspose.PDF pour .NET prend également en charge la fonctionnalité de convertir un fichier PDF en format PDF/A-3u.

```csharp
string inFile = "input.pdf";
string outFile = "output.pdf";
Aspose.PDF.Document doc = new Aspose.PDF.Document(inFile);
doc.Convert(new MemoryStream(), PdfFormat.PDF_A_3U, ConvertErrorAction.Delete);
doc.Save(outFile);
```

## Ajouter une pièce jointe à un fichier PDF/A

Si vous avez besoin d'attacher des fichiers au format de conformité PDF/A, nous recommandons d'utiliser la valeur PDF_A_3A de l'énumération Aspose.PDF.PdfFormat.
PDF/A_3a est le format qui offre la fonctionnalité d'attacher n'importe quel format de fichier en tant que pièce jointe à un fichier conforme PDF/A.

```csharp
```csharp
// Pour des exemples complets et des fichiers de données, veuillez vous rendre sur https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Le chemin vers le répertoire des documents.
string dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();

// Instancier Document pour charger un fichier existant
Aspose.Pdf.Document doc = new Document(dataDir + "input.pdf");
// Configurer le nouveau fichier à ajouter en tant que pièce jointe
FileSpecification fileSpecification = new FileSpecification(dataDir + "aspose-logo.jpg", "Fichier image de grande taille");
// Ajouter la pièce jointe à la collection de pièces jointes du document
doc.EmbeddedFiles.Add(fileSpecification);
// Effectuer la conversion en PDF/A_3a pour que la pièce jointe soit incluse dans le fichier résultant
doc.Convert(dataDir + "log.txt", Aspose.Pdf.PdfFormat.PDF_A_3A, ConvertErrorAction.Delete);
// Sauvegarder le fichier résultant
doc.Save(dataDir + "AddAttachmentToPDFA_out.pdf");
```

## Remplacer les polices manquantes par des polices alternatives

Conformément aux normes PDFA, les polices doivent être intégrées dans le document PDFA.
Selon les normes PDFA, les polices doivent être intégrées dans le document PDFA.

```csharp
// Pour des exemples complets et des fichiers de données, veuillez aller sur https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Le chemin vers le répertoire des documents.
string dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();

Aspose.Pdf.Text.Font originalFont = null;
try
{
    originalFont = FontRepository.FindFont("AgencyFB");
}
catch (Exception)
{
    // La police est manquante sur la machine de destination
    FontRepository.Substitutions.Add(new SimpleFontSubstitution("AgencyFB", "Arial"));
}
var fileNew = new FileInfo(dataDir + "newfile_out.pdf");
var pdf = new Document(dataDir + "input.pdf");
pdf.Convert(dataDir + "log.xml", PdfFormat.PDF_A_1B, ConvertErrorAction.Delete);
pdf.Save(fileNew.FullName);
```
