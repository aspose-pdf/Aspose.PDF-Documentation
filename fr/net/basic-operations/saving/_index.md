---
title: Sauvegarder un document PDF de manière programmatique
linktitle: Sauvegarder PDF
type: docs
weight: 30
url: fr/net/save-pdf-document/
description: Apprenez à sauvegarder un fichier PDF en C# avec la bibliothèque PDF Aspose.PDF pour .NET. Sauvegardez le document PDF sur le système de fichiers, dans un flux, et dans des applications Web.
aliases:
    - /net/saving/
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

Le prochain extrait de code fonctionne également avec une nouvelle interface graphique [Aspose.Drawing](/pdf/net/drawing/).

## Sauvegarder un document PDF sur le système de fichiers

Vous pouvez sauvegarder le document PDF créé ou manipulé sur le système de fichiers en utilisant la méthode `Save` de la classe `Document`.
Lorsque vous ne fournissez pas le type de format (options), le document est sauvegardé au format Aspose.PDF v.1.7 (*.pdf).

```csharp
public static void SaveDocument()
{
    var originalFileName = Path.Combine(_dataDir, "SimpleResume.pdf");
    var modifiedFileName = Path.Combine(_dataDir, "SimpleResumeModified.pdf");

    var pdfDocument = new Aspose.Pdf.Document(originalFileName);
    // faire quelques manipulations, par exemple ajouter une nouvelle page vide
    pdfDocument.Pages.Add();
    pdfDocument.Save(modifiedFileName);
}
```
## Enregistrer le document PDF dans un flux

Vous pouvez également enregistrer le document PDF créé ou manipulé dans un flux en utilisant les surcharges des méthodes `Save`.

```csharp
public static void SaveDocumentStream()
{
    var originalFileName = Path.Combine(_dataDir, "SimpleResume.pdf");
    var modifiedFileName = Path.Combine(_dataDir, "SimpleResumeModified.pdf");

    var pdfDocument = new Aspose.Pdf.Document(originalFileName);
    // faire quelques manipulations, par exemple ajouter une nouvelle page vide
    pdfDocument.Pages.Add();
    pdfDocument.Save(System.IO.File.OpenWrite(modifiedFileName));
}
```

## Enregistrer le document PDF dans les applications Web

Pour enregistrer des documents dans les applications Web, vous pouvez utiliser les méthodes proposées ci-dessus. De plus, la classe `Document` dispose d'une méthode surchargée `Save` pour une utilisation avec la classe [HttpResponse](https://docs.microsoft.com/en-us/dotnet/api/system.web.httpresponse?view=netframework-4.8).

```csharp
var originalFileName = Path.Combine(_dataDir, "SimpleResume.pdf");
var pdfDocument = new Aspose.Pdf.Document(originalFileName);
// faire quelques manipulations, par exemple ajouter une nouvelle page vide
pdfDocument.Pages.Add();
pdfDocument.Save(Response, originalFileName, ContentDisposition.Attachment, new PdfSaveOptions());
```

Pour une explication plus détaillée, veuillez suivre la section [Vitrine](/pdf/net/showcases/).

## Enregistrer au format PDF/A ou PDF/X

Le PDF/A est une version normalisée ISO du format de document portable (PDF) utilisée pour l'archivage et la conservation à long terme des documents électroniques.
Le PDF/A se distingue du PDF en ce qu'il interdit les fonctionnalités non adaptées à l'archivage à long terme, telles que la liaison de polices (par opposition à l'incorporation de polices) et le chiffrement. Les exigences de l'ISO pour les visionneuses PDF/A comprennent des directives de gestion des couleurs, la prise en charge des polices incorporées et une interface utilisateur pour la lecture des annotations incorporées.

Le PDF/X est un sous-ensemble de la norme ISO PDF. Le but du PDF/X est de faciliter l'échange de graphiques, et il a donc une série d'exigences liées à l'impression qui ne s'appliquent pas aux fichiers PDF standard.

Dans les deux cas, la méthode `Save` est utilisée pour stocker les documents, tandis que les documents doivent être préparés à l'aide de la méthode `Convert`.

```csharp
public static void SaveDocumentAsPDFx()
{
    var pdfDocument = new Aspose.Pdf.Document("..\\..\\..\\Samples\\SimpleResume.pdf");
    pdfDocument.Pages.Add();
    pdfDocument.Convert(new PdfFormatConversionOptions(PdfFormat.PDF_X_3));
    pdfDocument.Save("..\\..\\..\\Samples\\SimpleResume_X3.pdf");
}
```

