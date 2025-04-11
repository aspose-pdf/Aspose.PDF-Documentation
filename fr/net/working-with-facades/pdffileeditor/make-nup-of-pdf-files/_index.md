---
title: Faire NUp de fichiers PDF
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 90
url: /fr/net/make-nup-of-pdf-files/
description: Cet article montre comment faire fonctionner NUp de fichiers PDF avec Aspose.PDF Facades en utilisant la classe PdfFileEditor.
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Make NUp of PDF files",
    "alternativeHeadline": "Create NUp PDFs with Flexible Input Methods",
    "abstract": "La fonctionnalité NUp dans Aspose.PDF for .NET permet aux utilisateurs de combiner efficacement plusieurs fichiers PDF en un seul document de sortie, en personnalisant la taille des pages et les configurations de mise en page. Cette fonctionnalité prend en charge à la fois les chemins de fichiers et les flux, permettant une intégration flexible dans divers flux de travail tout en améliorant la présentation des documents.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "895",
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
    "url": "/net/make-nup-of-pdf-files/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/make-nup-of-pdf-files/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF peut effectuer non seulement des tâches simples et faciles mais aussi faire face à des objectifs plus complexes. Consultez la section suivante pour les utilisateurs avancés et les développeurs."
}
</script>

## Faire NUp de PDF en utilisant des chemins de fichiers

La méthode [MakeNUp](https://reference.aspose.com/pdf/fr/net/aspose.pdf.facades/pdffileeditor/methods/makenup/index) de la classe [PdfFileEditor](https://reference.aspose.com/pdf/fr/net/aspose.pdf.facades/pdffileeditor) vous permet de faire NUp du fichier PDF d'entrée et de l'enregistrer dans le fichier PDF de sortie. Cette surcharge vous permet de faire NUp en utilisant des chemins de fichiers. L'extrait de code suivant vous montre comment faire NUP en utilisant des chemins de fichiers.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void MakeNupOfPdfUsingFilePaths()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Pages();
    // Create PdfFileEditor object
    var pdfEditor = new Aspose.Pdf.Facades.PdfFileEditor();
    // Make NUp
    pdfEditor.MakeNUp(dataDir + "MakeNupInput.pdf", dataDir + "MakeNupInput2.pdf", "MakeNUpUsingPaths_out.pdf");
}
```

## Faire NUp en utilisant la taille de page et des chemins de fichiers

La méthode [MakeNUp](https://reference.aspose.com/pdf/fr/net/aspose.pdf.facades/pdffileeditor/methods/makenup/index) de la classe [PdfFileEditor](https://reference.aspose.com/pdf/fr/net/aspose.pdf.facades/pdffileeditor) vous permet de faire NUp du fichier PDF d'entrée et de l'enregistrer dans le fichier PDF de sortie. Cette surcharge vous permet de faire NUp en utilisant des chemins de fichiers. Vous pouvez également définir la taille de page du fichier PDF de sortie en utilisant cette surcharge. L'extrait de code suivant vous montre comment faire NUp en utilisant la taille de page et des chemins de fichiers.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void MakeNupUsingPageSizeAndFilePaths()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Pages();
    // Create PdfFileEditor object
    var pdfEditor = new Aspose.Pdf.Facades.PdfFileEditor();
    // Make NUp
    pdfEditor.MakeNUp(dataDir + "MakeNupMultiplePagesInput.pdf", dataDir + "MakeNUpUsingPageSizeAndPaths_out.pdf", 2, 3, PageSize.A5);
}
```

## Faire NUp de PDF en utilisant la taille de page, des valeurs horizontales et verticales, et des chemins de fichiers

La méthode [MakeNUp](https://reference.aspose.com/pdf/fr/net/aspose.pdf.facades/pdffileeditor/methods/makenup/index) de la classe [PdfFileEditor](https://reference.aspose.com/pdf/fr/net/aspose.pdf.facades/pdffileeditor) vous permet de faire NUp du fichier PDF d'entrée et de l'enregistrer dans le fichier PDF de sortie. Cette surcharge vous permet de faire NUp en utilisant des chemins de fichiers. Vous pouvez également définir la taille de page du fichier PDF de sortie et le nombre horizontal et vertical de pages sur chaque page de sortie en utilisant cette surcharge. L'extrait de code suivant vous montre comment faire NUp en utilisant la taille de page, des valeurs horizontales et verticales, et des chemins de fichiers.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void MakeNupOfPdfUsingPageSizeHorizontalAndVerticalValuesAndFilePaths()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Pages();
    // Create PdfFileEditor object
    var pdfEditor = new Aspose.Pdf.Facades.PdfFileEditor();
    // Make NUp
    pdfEditor.MakeNUp(dataDir + "MakeNupInput.pdf", "MakeNUpUsingPageSizeHorizontalAndVerticalValues_out.pdf", 2, 3);
}
```

## Faire NUp de PDF en utilisant un tableau de fichiers PDF et des chemins de fichiers

La méthode [MakeNUp](https://reference.aspose.com/pdf/fr/net/aspose.pdf.facades/pdffileeditor/methods/makenup/index) de la classe [PdfFileEditor](https://reference.aspose.com/pdf/fr/net/aspose.pdf.facades/pdffileeditor) vous permet de faire NUp d'un tableau de fichiers PDF d'entrée et de les enregistrer dans un seul fichier PDF de sortie. Cette surcharge vous permet de faire NUp en utilisant des chemins de fichiers. L'extrait de code suivant vous montre comment faire NUp en utilisant un tableau de fichiers PDF et des chemins de fichiers.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void MakeNupOfPdfUsingArrayOfPdfFilesAndFilePaths()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Pages();
    // Create PdfFileEditor object
    var pdfEditor = new Aspose.Pdf.Facades.PdfFileEditor();
    // Create array of files
    string[] filesArray = new string[2];
    filesArray[0] = dataDir + "MakeNupInput.pdf";
    filesArray[1] = dataDir + "MakeNupInput2.pdf";
    // Make NUp
    pdfEditor.MakeNUp(filesArray, dataDir + "MakeNupUsingArrayOfFilesAndPaths_out.pdf", true);
}
```

## Faire NUp de PDF en utilisant des flux

La méthode [MakeNUp](https://reference.aspose.com/pdf/fr/net/aspose.pdf.facades/pdffileeditor/methods/makenup/index) de la classe [PdfFileEditor](https://reference.aspose.com/pdf/fr/net/aspose.pdf.facades/pdffileeditor) vous permet de faire NUp du flux PDF d'entrée et de l'enregistrer dans le flux PDF de sortie. Cette surcharge vous permet de faire NUp en utilisant des flux au lieu de chemins de fichiers. L'extrait de code suivant vous montre comment faire NUp en utilisant des flux.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void MakeNupOfPdfUsingStreams()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Pages();
    // Create PdfFileEditor object
    var pdfEditor = new Aspose.Pdf.Facades.PdfFileEditor();
    // Create streams
    using (var inputStream1 = new FileStream(dataDir + "MakeNupInput.pdf", FileMode.Open))
    {
        using (var inputStream2 = new FileStream(dataDir + "MakeNupInput2.pdf", FileMode.Open))
        {
            using (var outputStream = new FileStream(dataDir + "MakeNUpUsingStreams_out.pdf", FileMode.Create))
            {
                // Make NUp
                pdfEditor.MakeNUp(inputStream1, inputStream2, outputStream);
            }
        }
    }
}
```

## Faire NUp de PDF en utilisant la taille de page et des flux

La méthode [MakeNUp](https://reference.aspose.com/pdf/fr/net/aspose.pdf.facades/pdffileeditor/methods/makenup/index) de la classe [PdfFileEditor](https://reference.aspose.com/pdf/fr/net/aspose.pdf.facades/pdffileeditor) vous permet de faire NUp du flux PDF d'entrée et de l'enregistrer dans le flux PDF de sortie. Cette surcharge vous permet de faire NUp en utilisant des flux au lieu de chemins de fichiers. Vous pouvez également définir la taille de page du flux PDF de sortie en utilisant cette surcharge. L'extrait de code suivant vous montre comment faire NUp en utilisant la taille de page et des flux.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void MakeNupOfPdfUsingPageSizeAndStreams()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Pages();
    // Create PdfFileEditor object
    var pdfEditor = new Aspose.Pdf.Facades.PdfFileEditor();
    // Create streams
    using (var inputStream = new FileStream(dataDir + "MakeNupInput.pdf", FileMode.Open))
    {
        using (var outputStream = new FileStream(dataDir + "MakeNUpUsingPageSizeAndStreams_out.pdf", FileMode.Create))
        {
            // Make NUp
            pdfEditor.MakeNUp(inputStream, outputStream, 2, 3, PageSize.A5);    
        }    
    }
}
```

## Faire NUp de PDF en utilisant la taille de page, des valeurs horizontales et verticales, et des flux

La méthode [MakeNUp](https://reference.aspose.com/pdf/fr/net/aspose.pdf.facades/pdffileeditor/methods/makenup/index) de la classe [PdfFileEditor](https://reference.aspose.com/pdf/fr/net/aspose.pdf.facades/pdffileeditor) vous permet de faire NUp du flux PDF d'entrée et de l'enregistrer dans le flux PDF de sortie. Cette surcharge vous permet de faire NUp en utilisant des flux au lieu de chemins de fichiers. Vous pouvez également définir la taille de page du flux PDF de sortie et le nombre horizontal et vertical de pages sur chaque page de sortie en utilisant cette surcharge. L'extrait de code suivant vous montre comment faire NUp en utilisant la taille de page, des valeurs horizontales et verticales, et des flux.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void MakeNupOfPdfUsingPageSizeHorizontalAndVerticalValuesAndStreams()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Pages();
    // Create PdfFileEditor object
    var pdfEditor = new Aspose.Pdf.Facades.PdfFileEditor();
    // Create streams
    using (var inputStream = new FileStream(dataDir + "MakeNupInput.pdf", FileMode.Open))
    {
        using (var outputStream = new FileStream(dataDir + "MakeNUpUsingPageSizeHorizontalVerticalValuesAndStreams_out.pdf", FileMode.Create))
        {
            // Make NUp
            pdfEditor.MakeNUp(inputStream, outputStream, 2, 3); 
        }
    }
}
```

## Faire NUp de PDF en utilisant un tableau de fichiers PDF et des flux

La méthode [MakeNUp](https://reference.aspose.com/pdf/fr/net/aspose.pdf.facades/pdffileeditor/methods/makenup/index) de la classe [PdfFileEditor](https://reference.aspose.com/pdf/fr/net/aspose.pdf.facades/pdffileeditor) vous permet de faire NUp d'un tableau de flux PDF d'entrée et de les enregistrer dans un seul flux PDF de sortie. Cette surcharge vous permet de faire NUp en utilisant des flux au lieu de chemins de fichiers. L'extrait de code suivant vous montre comment faire NUp en utilisant un tableau de fichiers PDF en utilisant des flux.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void MakeNupOfPdfUsingArrayOfPdfFilesAndStreams()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Pages();
    // Create PdfFileEditor object
    var pdfEditor = new Aspose.Pdf.Facades.PdfFileEditor();
    // Create streams
    using (var stream1 = new FileStream(dataDir + "MakeNupInput.pdf", FileMode.Open))
    {
        using (var stream2 = new FileStream(dataDir + "MakeNupInput2.pdf", FileMode.Open))
        {
            using (var outputStream = new FileStream(dataDir + "MakeNUpUsingArrayOfFilesAndStreams_out.pdf", FileMode.Create))
            {
                var fileStreams = new Stream[2];
                fileStreams[0] = stream1;
                fileStreams[1] = stream2;
                // Make NUp
                pdfEditor.MakeNUp(fileStreams, outputStream, true);
            }
        }
    }
}
```