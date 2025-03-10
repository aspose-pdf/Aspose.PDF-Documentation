---
title: Convertir PDF en PowerPoint dans .NET
linktitle: Convertir PDF en PowerPoint
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 30
url: /fr/net/convert-pdf-to-powerpoint/
lastmod: "2021-11-01"
description: Aspose.PDF vous permet de convertir des PDF en format PPT (PowerPoint) en utilisant .NET. Une façon d'y parvenir est de convertir des PDF en PPTX avec des diapositives en tant qu'images.
lastmod: "2021-10-18"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Convert PDF to PowerPoint in .NET",
    "alternativeHeadline": "Convert PDF Documents to PowerPoint Presentations Efficiently in C#",
    "abstract": "Aspose.PDF for .NET introduit une fonctionnalité puissante permettant la conversion transparente de documents PDF en format PowerPoint (PPTX), permettant à chaque page PDF de se transformer en une diapositive distincte. Avec l'option de rendre le texte sélectionnable ou sous forme d'images, les utilisateurs peuvent facilement personnaliser leurs présentations tout en suivant efficacement l'avancement de la conversion. Optimisez votre flux de travail documentaire en tirant parti de cette fonctionnalité innovante pour une productivité accrue.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "1174",
    "proficiencyLevel": "Beginner",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF for .NET",
        "url": "https://products.aspose.com/pdf",
        "logo": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-net.svg",
        "alternateName": "Aspose",
        "sameAs": [
            "https://facebook.com/aspose.pdf/",
            "https://twitter.com/asposepdf",
            "https://www.youtube.com/channel/UCmV9sEg_QWYPi6BJJs7ELOg/featured",
            "https://www.linkedin.com/company/aspose",
            "https://stackoverflow.com/questions/tagged/aspose",
            "https://aspose.quora.com/",
            "https://aspose.github.io/"
        ],
        "contactPoint": [
            {
                "@type": "ContactPoint",
                "telephone": "+1 903 306 1676",
                "contactType": "sales",
                "areaServed": "US",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "sales",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "sales",
                "areaServed": "AU",
                "availableLanguage": "en"
            }
        ]
    },
    "url": "/net/convert-pdf-to-powerpoint/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/convert-pdf-to-powerpoint/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF peut effectuer non seulement des tâches simples et faciles, mais aussi faire face à des objectifs plus complexes. Consultez la section suivante pour les utilisateurs avancés et les développeurs."
}
</script>

## Aperçu

Cet article explique comment **convertir PDF en PowerPoint en utilisant C#**. Il couvre ces sujets.

_Format_: **PPTX**
- [C# PDF en PPTX](#csharp-pdf-to-pptx)
- [C# Convertir PDF en PPTX](#csharp-pdf-to-pptx)
- [C# Comment convertir un fichier PDF en PPTX](#csharp-pdf-to-pptx)

_Format_: **PowerPoint**
- [C# PDF en PowerPoint](#csharp-pdf-to-powerpoint)
- [C# Convertir PDF en PowerPoint](#csharp-pdf-to-powerpoint)
- [C# Comment convertir un fichier PDF en PowerPoint](#csharp-pdf-to-powerpoint)

Le code suivant fonctionne également avec la bibliothèque [Aspose.PDF.Drawing](/pdf/net/drawing/).

## Conversion C# PDF en PowerPoint et PPTX

**Aspose.PDF for .NET** vous permet de suivre l'avancement de la conversion de PDF en PPTX.

Nous avons une API nommée Aspose.Slides qui offre la fonctionnalité de créer ainsi que de manipuler des présentations PPT/PPTX. Cette API fournit également la fonctionnalité de convertir des fichiers PPT/PPTX en format PDF. Récemment, nous avons reçu des demandes de nombreux clients pour prendre en charge la capacité de transformation de PDF en format PPTX. À partir de la version Aspose.PDF for .NET 10.3.0, nous avons introduit une fonctionnalité pour transformer des documents PDF en format PPTX. Lors de cette conversion, les pages individuelles du fichier PDF sont converties en diapositives séparées dans le fichier PPTX.

Lors de la conversion de PDF en <abbr title="Microsoft PowerPoint 2007 XML Presentation">PPTX</abbr>, le texte est rendu en tant que texte que vous pouvez sélectionner/met à jour. Veuillez noter que pour convertir des fichiers PDF en format PPTX, Aspose.PDF fournit une classe nommée [`PptxSaveOptions`](https://reference.aspose.com/pdf/net/aspose.pdf/pptxsaveoptions). Un objet de la classe PptxSaveOptions est passé comme deuxième argument à la [`Document.Save(..) méthode`](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save). Le code suivant montre le processus de conversion des fichiers PDF en format PPTX.

## Conversion simple PDF en PowerPoint en utilisant C# et Aspose.PDF .NET

Pour convertir PDF en PPTX, Aspose.PDF for .NET conseille d'utiliser les étapes de code suivantes.

<a name="csharp-pdf-to-powerpoint"><strong>Étapes : Convertir PDF en PowerPoint en C#</strong></a> | <a name="csharp-pdf-to-pptx"><strong>Étapes : Convertir PDF en PPTX en C#</strong></a>

1. Créez une instance de la classe [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document).
2. Créez une instance de la classe [PptxSaveOptions](https://reference.aspose.com/pdf/net/aspose.pdf/pptxsaveoptions).
3. Utilisez la méthode **Save** de l'objet **Document** pour enregistrer le PDF en tant que PPTX.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertPDFToPPTX()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
    {
        // Instantiate PptxSaveOptions object
        var saveOptions = new Aspose.Pdf.PptxSaveOptions();

        // Save the file in PPTX format
        document.Save(dataDir + "PDFToPPT_out.pptx", saveOptions);
    }
}
```

## Convertir PDF en PPTX avec des diapositives en tant qu'images

{{% alert color="success" %}}
**Essayez de convertir PDF en PowerPoint en ligne**

Aspose.PDF for .NET vous présente une application gratuite en ligne ["PDF en PPTX"](https://products.aspose.app/pdf/conversion/pdf-to-pptx), où vous pouvez essayer d'explorer la fonctionnalité et la qualité de son fonctionnement.

[![Aspose.PDF Conversion PDF en PPTX avec l'application gratuite](pdf_to_pptx.png)](https://products.aspose.app/pdf/conversion/pdf-to-pptx)
{{% /alert %}}

Dans le cas où vous devez convertir un PDF consultable en PPTX sous forme d'images au lieu de texte sélectionnable, Aspose.PDF fournit une telle fonctionnalité via la classe [Aspose.Pdf.PptxSaveOptions](https://reference.aspose.com/pdf/net/aspose.pdf/pptxsaveoptions). Pour ce faire, définissez la propriété [SlidesAsImages](https://reference.aspose.com/pdf/net/aspose.pdf/pptxsaveoptions/properties/slidesasimages) de la classe [PptxSaveOptios](https://reference.aspose.com/pdf/net/aspose.pdf/pptxsaveoptions) sur 'true' comme indiqué dans l'exemple de code suivant.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertPDFToPPTWithSlidesAsImages()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
    {
        // Instantiate PptxSaveOptions object
        var saveOptions = new Aspose.Pdf.PptxSaveOptions
        {
            SlidesAsImages = true
        };

        // Save the file in PPTX format with slides as images
        document.Save(dataDir + "PDFToPPT_out.pptx", saveOptions);
    }
}
```

## Détails de progression de la conversion PPTX

Aspose.PDF for .NET vous permet de suivre l'avancement de la conversion de PDF en PPTX. La classe [Aspose.Pdf.PptxSaveOptions](https://reference.aspose.com/pdf/net/aspose.pdf/pptxsaveoptions) fournit la propriété [CustomProgressHandler](https://reference.aspose.com/pdf/net/aspose.pdf/pptxsaveoptions/properties/customprogresshandler) qui peut être spécifiée à une méthode personnalisée pour suivre l'avancement de la conversion comme indiqué dans l'exemple de code suivant.

```csharp
 // For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertPDFToPPTWithCustomProgressHandler()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
    {

        // Instantiate PptxSaveOptions object
        var saveOptions = new Aspose.Pdf.PptxSaveOptions();

        // Specify custom progress handler
        saveOptions.CustomProgressHandler = ShowProgressOnConsole;

        // Save the file in PPTX format with progress tracking
        document.Save(dataDir + "PDFToPPTWithProgressTracking_out.pptx", saveOptions);
    }
}

 // Define the method to handle progress events and display them on the console
private static void ShowProgressOnConsole(Aspose.Pdf.UnifiedSaveOptions.ProgressEventHandlerInfo eventInfo)
{
    switch (eventInfo.EventType)
    {
        case Aspose.Pdf.ProgressEventType.TotalProgress:
            // Display overall progress of the conversion
            Console.WriteLine($"{DateTime.Now.TimeOfDay}  - Conversion progress: {eventInfo.Value}%.");
            break;

        case Aspose.Pdf.ProgressEventType.ResultPageCreated:
            // Display progress of the page layout creation
            Console.WriteLine($"{DateTime.Now.TimeOfDay}  - Result page {eventInfo.Value} of {eventInfo.MaxValue} layout created.");
            break;

        case Aspose.Pdf.ProgressEventType.ResultPageSaved:
            // Display progress of the page being exported
            Console.WriteLine($"{DateTime.Now.TimeOfDay}  - Result page {eventInfo.Value} of {eventInfo.MaxValue} exported.");
            break;

        case Aspose.Pdf.ProgressEventType.SourcePageAnalysed:
            // Display progress of the source page analysis
            Console.WriteLine($"{DateTime.Now.TimeOfDay}  - Source page {eventInfo.Value} of {eventInfo.MaxValue} analyzed.");
            break;

        default:
            break;
    }
}
```

## Voir aussi 

Cet article couvre également ces sujets. Les codes sont les mêmes que ci-dessus.

_Format_: **PowerPoint**
- [C# Code PDF en PowerPoint](#csharp-pdf-to-powerpoint)
- [C# API PDF en PowerPoint](#csharp-pdf-to-powerpoint)
- [C# PDF en PowerPoint par programmation](#csharp-pdf-to-powerpoint)
- [C# Bibliothèque PDF en PowerPoint](#csharp-pdf-to-powerpoint)
- [C# Enregistrer PDF en tant que PowerPoint](#csharp-pdf-to-powerpoint)
- [C# Générer PowerPoint à partir de PDF](#csharp-pdf-to-powerpoint)
- [C# Créer PowerPoint à partir de PDF](#csharp-pdf-to-powerpoint)
- [C# Convertisseur PDF en PowerPoint](#csharp-pdf-to-powerpoint)

_Format_: **PPTX**
- [C# Code PDF en PPTX](#csharp-pdf-to-pptx)
- [C# API PDF en PPTX](#csharp-pdf-to-pptx)
- [C# PDF en PPTX par programmation](#csharp-pdf-to-pptx)
- [C# Bibliothèque PDF en PPTX](#csharp-pdf-to-pptx)
- [C# Enregistrer PDF en tant que PPTX](#csharp-pdf-to-pptx)
- [C# Générer PPTX à partir de PDF](#csharp-pdf-to-pptx)
- [C# Créer PPTX à partir de PDF](#csharp-pdf-to-pptx)
- [C# Convertisseur PDF en PPTX](#csharp-pdf-to-pptx)