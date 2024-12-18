---
title: Convertir PDF en PowerPoint en .NET
linktitle: Convertir PDF en PowerPoint
type: docs
weight: 30
url: /fr/net/convert-pdf-to-powerpoint/
lastmod: "2021-11-01"
description: Aspose.PDF vous permet de convertir un PDF au format PPT (PowerPoint) en utilisant .NET. Il est possible de convertir un PDF en PPTX avec des diapositives sous forme d'images.
lastmod: "2021-10-18"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
## Aperçu

Cet article explique comment **convertir un PDF en PowerPoint en utilisant C#**. Il couvre ces sujets.

_Format_ : **PPTX**
- [C# PDF en PPTX](#csharp-pdf-to-pptx)
- [C# Convertir PDF en PPTX](#csharp-pdf-to-pptx)
- [C# Comment convertir un fichier PDF en PPTX](#csharp-pdf-to-pptx)

_Format_ : **PowerPoint**
- [C# PDF en PowerPoint](#csharp-pdf-to-powerpoint)
- [C# Convertir PDF en PowerPoint](#csharp-pdf-to-powerpoint)
- [C# Comment convertir un fichier PDF en PowerPoint](#csharp-pdf-to-powerpoint)

Le fragment de code suivant fonctionne également avec la bibliothèque [Aspose.PDF.Drawing](/pdf/fr/net/drawing/).

## Conversion de PDF en PowerPoint et PPTX en C#
## Conversion de PDF en PowerPoint et PPTX en C#

**Aspose.PDF pour .NET** vous permet de suivre la progression de la conversion de PDF en PPTX.

Nous disposons d'une API nommée Aspose.Slides qui offre la fonctionnalité de créer et de manipuler des présentations PPT/PPTX. Cette API fournit également la fonctionnalité de convertir des fichiers PPT/PPTX en format PDF. Récemment, nous avons reçu des demandes de nombreux clients pour supporter la capacité de transformation de PDF en format PPTX. À partir de la version Aspose.PDF pour .NET 10.3.0, nous avons introduit une fonctionnalité pour transformer des documents PDF en format PPTX. Lors de cette conversion, les pages individuelles du fichier PDF sont converties en diapositives séparées dans le fichier PPTX.

Lors de la conversion de PDF en <abbr title="Microsoft PowerPoint 2007 XML Presentation">PPTX</abbr>, le texte est rendu en tant que Texte où vous pouvez le sélectionner/mettre à jour.
Lors de la conversion de PDF en <abbr title="Microsoft PowerPoint 2007 XML Presentation">PPTX</abbr>, le texte est rendu en tant que Texte où vous pouvez le sélectionner/mettre à jour.

## Conversion simple de PDF en PowerPoint utilisant C# et Aspose.PDF .NET

Pour convertir un PDF en PPTX, Aspose.PDF pour .NET recommande d'utiliser les étapes de code suivantes.

<a name="csharp-pdf-to-powerpoint"><strong>Étapes : Convertir un PDF en PowerPoint en C#</strong></a> | <a name="csharp-pdf-to-pptx"><strong>Étapes : Convertir un PDF en PPTX en C#</strong></a>

1. Créer une instance de la classe [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document)
2. Créer une instance de la classe [PptxSaveOptions](https://reference.aspose.com/pdf/net/aspose.pdf/pptxsaveoptions)
3. Utiliser la méthode **Save** de l'objet **Document** pour enregistrer le PDF en tant que PPTX

```csharp
// Pour des exemples complets et des fichiers de données, veuillez aller à https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Le chemin vers le répertoire des documents.
string dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();
// Charger le document PDF
Aspose.Pdf.Document doc = new Aspose.Pdf.Document(dataDir + "input.pdf");
// Instancier une instance de PptxSaveOptions
Aspose.Pdf.PptxSaveOptions pptx_save = new Aspose.Pdf.PptxSaveOptions();
// Sauvegarder le résultat au format PPTX
doc.Save(dataDir + "PDFToPPT_out.pptx", pptx_save);
```
## Convertir PDF en PPTX avec des diapositives comme images

{{% alert color="success" %}}
**Essayez de convertir un PDF en PowerPoint en ligne**

Aspose.PDF pour .NET vous présente l'application gratuite en ligne ["PDF to PPTX"](https://products.aspose.app/pdf/conversion/pdf-to-pptx), où vous pouvez explorer la fonctionnalité et la qualité de son fonctionnement.

[![Aspose.PDF Conversion PDF en PPTX avec application gratuite](pdf_to_pptx.png)](https://products.aspose.app/pdf/conversion/pdf-to-pptx)
{{% /alert %}}

Dans le cas où vous avez besoin de convertir un PDF consultable en PPTX sous forme d'images plutôt que de texte sélectionnable, Aspose.PDF offre cette fonctionnalité via la classe [Aspose.Pdf.PptxSaveOptions](https://reference.aspose.com/pdf/net/aspose.pdf/pptxsaveoptions). Pour ce faire, définissez la propriété [SlidesAsImages](https://reference.aspose.com/pdf/net/aspose.pdf/pptxsaveoptions/properties/slidesasimages) de la classe [PptxSaveOptios](https://reference.aspose.com/pdf/net/aspose.pdf/pptxsaveoptions) à 'true' comme le montre l'exemple de code suivant.

```csharp
// Pour des exemples complets et des fichiers de données, veuillez aller sur https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Le chemin vers le répertoire des documents.
string dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();
// Charger le document PDF
Aspose.Pdf.Document doc = new Aspose.Pdf.Document(dataDir + "input.pdf");
// Instancier l'instance PptxSaveOptions
Aspose.Pdf.PptxSaveOptions pptx_save = new Aspose.Pdf.PptxSaveOptions();
// Sauvegarder le résultat au format PPTX
pptx_save.SlidesAsImages = true;
doc.Save(dataDir + "PDFToPPT_out_.pptx", pptx_save);
```
## Détail de la progression de la conversion PPTX

Aspose.PDF pour .NET vous permet de suivre la progression de la conversion de PDF en PPTX. La classe [Aspose.Pdf.PptxSaveOptions](https://reference.aspose.com/pdf/net/aspose.pdf/pptxsaveoptions) fournit une propriété [CustomProgressHandler](https://reference.aspose.com/pdf/net/aspose.pdf/pptxsaveoptions/properties/customprogresshandler) qui peut être spécifiée à une méthode personnalisée pour suivre la progression de la conversion comme illustré dans l'exemple de code suivant.

```csharp
// Pour des exemples complets et des fichiers de données, veuillez aller à https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Le chemin vers le répertoire des documents.
string dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();
// Charger le document PDF
Aspose.Pdf.Document doc = new Aspose.Pdf.Document(dataDir + "input.pdf");
// Instancier l'instance PptxSaveOptions
Aspose.Pdf.PptxSaveOptions pptx_save = new Aspose.Pdf.PptxSaveOptions();

// Spécifier le gestionnaire de progression personnalisé
pptx_save.CustomProgressHandler = ShowProgressOnConsole;
// Sauvegarder la sortie au format PPTX
doc.Save(dataDir + "PDFToPPTWithProgressTracking_out_.pptx", pptx_save);
```
Voici la méthode personnalisée pour afficher la progression de la conversion.

```csharp
// Pour des exemples complets et des fichiers de données, veuillez visiter https://github.com/aspose-pdf/Aspose.PDF-for-.NET
switch (eventInfo.EventType)
{
    case ProgressEventType.TotalProgress:
        Console.WriteLine(String.Format("{0}  - Progression de la conversion : {1}% .", DateTime.Now.TimeOfDay, eventInfo.Value.ToString()));
        break;
    case ProgressEventType.ResultPageCreated:
        Console.WriteLine(String.Format("{0}  - Page de résultat {1} sur {2} mise en page créée.", DateTime.Now.TimeOfDay, eventInfo.Value.ToString(), eventInfo.MaxValue.ToString()));
        break;
    case ProgressEventType.ResultPageSaved:
        Console.WriteLine(String.Format("{0}  - Page de résultat {1} sur {2} exportée.", DateTime.Now.TimeOfDay, eventInfo.Value.ToString(), eventInfo.MaxValue.ToString()));
        break;
    case ProgressEventType.SourcePageAnalysed:
        Console.WriteLine(String.Format("{0}  - Page source {1} sur {2} analysée.", DateTime.Now.TimeOfDay, eventInfo.Value.ToString(), eventInfo.MaxValue.ToString()));

        break;
    default:
        break;
}
```
## Voir aussi

Cet article couvre également ces sujets. Les codes sont les mêmes que ci-dessus.

_Format_ : **PowerPoint**
- [Code C# PDF vers PowerPoint](#csharp-pdf-to-powerpoint)
- [API C# PDF vers PowerPoint](#csharp-pdf-to-powerpoint)
- [C# PDF vers PowerPoint Programmation](#csharp-pdf-to-powerpoint)
- [Bibliothèque C# PDF vers PowerPoint](#csharp-pdf-to-powerpoint)
- [C# Enregistrer PDF en tant que PowerPoint](#csharp-pdf-to-powerpoint)
- [C# Générer un PowerPoint à partir d'un PDF](#csharp-pdf-to-powerpoint)
- [C# Créer un PowerPoint à partir d'un PDF](#csharp-pdf-to-powerpoint)
- [Convertisseur C# PDF vers PowerPoint](#csharp-pdf-to-powerpoint)

_Format_ : **PPTX**
- [Code C# PDF vers PPTX](#csharp-pdf-to-pptx)
- [API C# PDF vers PPTX](#csharp-pdf-to-pptx)
- [C# PDF vers PPTX Programmation](#csharp-pdf-to-pptx)
- [Bibliothèque C# PDF vers PPTX](#csharp-pdf-to-pptx)
- [C# Enregistrer PDF en tant que PPTX](#csharp-pdf-to-pptx)
- [C# Générer un PPTX à partir d'un PDF](#csharp-pdf-to-pptx)
- [C# Créer un PPTX à partir d'un PDF](#csharp-pdf-to-pptx)
- [Convertisseur C# PDF vers PPTX](#csharp-pdf-to-pptx)
