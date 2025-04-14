---
title: Créer un livret à partir d'un PDF
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 80
url: /fr/net/make-booklet-of-pdf/
description: Cette section explique comment créer un livret à partir d'un PDF avec Aspose.PDF Facades en utilisant la classe PdfFileEditor.
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Make Booklet of PDF",
    "alternativeHeadline": "Create Booklets from PDFs with Enhanced Flexibility",
    "abstract": "La fonctionnalité Créer un livret à partir d'un PDF dans Aspose.PDF permet aux utilisateurs de créer facilement des livrets à partir de fichiers PDF en utilisant la classe PdfFileEditor. Cette fonctionnalité prend en charge à la fois les chemins de fichiers et les flux, permettant la personnalisation des tailles de page et la spécification des pages gauche et droite pour un contrôle de sortie amélioré. Cet outil puissant rationalise le processus de création de livrets, en faisant une ressource essentielle pour la manipulation de PDF.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "946",
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
    "url": "/net/make-booklet-of-pdf/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/make-booklet-of-pdf/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF peut effectuer non seulement des tâches simples et faciles, mais aussi faire face à des objectifs plus complexes. Consultez la section suivante pour les utilisateurs avancés et les développeurs."
}
</script>

## Créer un livret à partir d'un PDF en utilisant des chemins de fichiers

La méthode [MakeBooklet](https://reference.aspose.com/pdf/fr/net/aspose.pdf.facades/pdffileeditor/methods/makebooklet/index) de la classe [PdfFileEditor](https://reference.aspose.com/pdf/fr/net/aspose.pdf.facades/pdffileeditor) vous permet de créer un livret à partir du fichier PDF d'entrée et de l'enregistrer dans le fichier PDF de sortie. Cette surcharge vous permet de créer un livret en utilisant des chemins de fichiers. Le code suivant montre comment créer un livret en utilisant des chemins de fichiers.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void MakeBookletOfPdfUsingFilePaths()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Pages();
    // Create PdfFileEditor object
    var pdfEditor = new Aspose.Pdf.Facades.PdfFileEditor();
    // Make booklet
    pdfEditor.MakeBooklet(dataDir + "MakeBookletInput.pdf", dataDir + "MakeBookletUsingPaths_out.pdf");
}
```

## Créer un livret à partir d'un PDF en utilisant la taille de page et des chemins de fichiers

La méthode [MakeBooklet](https://reference.aspose.com/pdf/fr/net/aspose.pdf.facades/pdffileeditor/methods/makebooklet/index) de la classe [PdfFileEditor](https://reference.aspose.com/pdf/fr/net/aspose.pdf.facades/pdffileeditor) vous permet de créer un livret à partir du fichier PDF d'entrée et de l'enregistrer dans le fichier PDF de sortie. Cette surcharge vous permet de créer un livret en utilisant des chemins de fichiers. Vous pouvez également définir la taille de page du fichier PDF de sortie avec cette surcharge. Le code suivant montre comment créer un livret en utilisant la taille de page et des chemins de fichiers.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void MakeBookletOfPdfUsingPageSizeAndFilePaths()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Pages();
    // Create PdfFileEditor object
    var pdfEditor = new Aspose.Pdf.Facades.PdfFileEditor();
    // Make booklet
    pdfEditor.MakeBooklet(dataDir + "MakeBookletInput.pdf", dataDir + "MakeBookletUsingPageSizeAndPaths_out.pdf", PageSize.A5);
}
```

## Créer un livret à partir d'un PDF en utilisant la taille de page, des pages gauche et droite spécifiées, et des chemins de fichiers

La méthode [MakeBooklet](https://reference.aspose.com/pdf/fr/net/aspose.pdf.facades/pdffileeditor/methods/makebooklet/index) de la classe [PdfFileEditor](https://reference.aspose.com/pdf/fr/net/aspose.pdf.facades/pdffileeditor) vous permet de créer un livret à partir du fichier PDF d'entrée et de l'enregistrer dans le fichier PDF de sortie. Cette surcharge vous permet de créer un livret en utilisant des chemins de fichiers. Vous pouvez également définir la taille de page du fichier PDF de sortie et spécifier des pages particulières pour les côtés gauche et droit du fichier PDF de sortie avec cette surcharge. Le code suivant montre comment créer un livret en utilisant la taille de page, des pages gauche et droite spécifiées et des chemins de fichiers.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void MakeBookletOfPdfUsingPageSizeSpecifiedLeftAndRightPagesAndFilePaths()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Pages();
    // Create PdfFileEditor object
    var pdfEditor = new Aspose.Pdf.Facades.PdfFileEditor();
    // Set left and right pages
    var leftPages = new int[] { 1, 5 };
    var rightPages = new int[] { 2, 3 };
    // Make booklet
    pdfEditor.MakeBooklet(dataDir + "MakeBookletMultiplePagesInput.pdf", dataDir + "MakeBookletUsingLeftRightPagesAndPaths_out.pdf", PageSize.A5, leftPages, rightPages);
}
```

## Créer un livret à partir d'un PDF en utilisant des pages gauche et droite spécifiées, et des chemins de fichiers

La méthode [MakeBooklet](https://reference.aspose.com/pdf/fr/net/aspose.pdf.facades/pdffileeditor/methods/makebooklet/index) de la classe [PdfFileEditor](https://reference.aspose.com/pdf/fr/net/aspose.pdf.facades/pdffileeditor) vous permet de créer un livret à partir du fichier PDF d'entrée et de l'enregistrer dans le fichier PDF de sortie. Cette surcharge vous permet de créer un livret en utilisant des chemins de fichiers. Vous pouvez également spécifier des pages particulières pour les côtés gauche et droit du fichier PDF de sortie avec cette surcharge. Le code suivant montre comment créer un livret en utilisant des pages gauche et droite spécifiées et des chemins de fichiers.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void MakeBookletOfPdfUsingSpecifiedLeftAndRightPagesAndFilePaths()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Pages();
    // Create PdfFileEditor object
    var pdfEditor = new Aspose.Pdf.Facades.PdfFileEditor();
    // Set left and right pages
    var leftPages = new int[] { 1, 5 };
    var rightPages = new int[] { 2, 3 };
    // Make booklet
    pdfEditor.MakeBooklet(dataDir + "MakeBookletMultiplePagesInput.pdf", dataDir + "MakeBookletUsingLeftRightPagesAndPaths_out.pdf", leftPages, rightPages);
}
```

## Créer un livret à partir d'un PDF en utilisant des flux

La méthode [MakeBooklet](https://reference.aspose.com/pdf/fr/net/aspose.pdf.facades/pdffileeditor/methods/makebooklet/index) de la classe [PdfFileEditor](https://reference.aspose.com/pdf/fr/net/aspose.pdf.facades/pdffileeditor) vous permet de créer un livret à partir du flux PDF d'entrée et de l'enregistrer dans les flux PDF de sortie. Cette surcharge vous permet de créer un livret en utilisant des flux au lieu de chemins de fichiers. Le code suivant montre comment créer un livret en utilisant des flux.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void MakeBookletOfPdfUsingStreams()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Pages();
    // Create PdfFileEditor object
    var pdfEditor = new Aspose.Pdf.Facades.PdfFileEditor();
    // Create streams
    using (var inputStream = new FileStream(dataDir + "MakeBookletInput.pdf", FileMode.Open))
    {
        using (var outputStream = new FileStream(dataDir + "MakeBookletUsingStreams_out.pdf", FileMode.Create))
        {
            // Make booklet
            pdfEditor.MakeBooklet(inputStream, outputStream);
        }
    }
}
```

## Créer un livret à partir d'un PDF en utilisant la taille de page et des flux

La méthode [MakeBooklet](https://reference.aspose.com/pdf/fr/net/aspose.pdf.facades/pdffileeditor/methods/makebooklet/index) de la classe [PdfFileEditor](https://reference.aspose.com/pdf/fr/net/aspose.pdf.facades/pdffileeditor) vous permet de créer un livret à partir du flux PDF d'entrée et de l'enregistrer dans le flux PDF de sortie. Cette surcharge vous permet de créer un livret en utilisant des flux au lieu de chemins de fichiers. Vous pouvez également définir la taille de page du flux PDF de sortie avec cette surcharge. Le code suivant montre comment créer un livret en utilisant la taille de page et des flux.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void MakeBookletOfPdfUsingPageSizeAndStreams()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Pages();
    // Create PdfFileEditor object
    var pdfEditor = new Aspose.Pdf.Facades.PdfFileEditor();
    // Create streams
    using (var inputStream = new FileStream(dataDir + "MakeBookletInput.pdf", FileMode.Open))
    {
        using (var outputStream = new FileStream(dataDir + "MakeBookletUsingPageSizeAndStreams_out.pdf", FileMode.Create))
        {
            // Make booklet
            pdfEditor.MakeBooklet(inputStream, outputStream, PageSize.A5);
        }
    }
}
```

## Créer un livret à partir d'un PDF en utilisant la taille de page, des pages gauche et droite spécifiées, et des flux

La méthode [MakeBooklet](https://reference.aspose.com/pdf/fr/net/aspose.pdf.facades/pdffileeditor/methods/makebooklet/index) de la classe [PdfFileEditor](https://reference.aspose.com/pdf/fr/net/aspose.pdf.facades/pdffileeditor) vous permet de créer un livret à partir du flux PDF d'entrée et de l'enregistrer dans le flux PDF de sortie. Cette surcharge vous permet de créer un livret en utilisant des flux au lieu de chemins de fichiers. Vous pouvez également définir la taille de page du fichier PDF de sortie et spécifier des pages particulières pour les côtés gauche et droit du flux PDF de sortie avec cette surcharge. Le code suivant montre comment créer un livret en utilisant la taille de page, des pages gauche et droite spécifiées, et des flux.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void MakeBookletOfPdfUsingPageSizeSpecifiedLeftAndRightPagesAndStreams()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Pages();
    // Create PdfFileEditor object
    var pdfEditor = new Aspose.Pdf.Facades.PdfFileEditor();
    // Create streams
    using (var inputStream = new FileStream(dataDir + "MakeBookletMultiplePagesInput.pdf", FileMode.Open))
    {
        using (var outputStream = new FileStream(dataDir + "MakeBookletUsingPageSizeLeftRightPagesAndStreams_out.pdf", FileMode.Create))
        {
            // Set left and right pages
            var leftPages = new int[] { 1, 5 };
            var rightPages = new int[] { 2, 3 };
            // Make booklet
            pdfEditor.MakeBooklet(inputStream, outputStream, PageSize.A5, leftPages, rightPages);
        }
    }
}
```

## Créer un livret à partir d'un PDF en utilisant des pages gauche et droite spécifiées, et des flux

La méthode [MakeBooklet](https://reference.aspose.com/pdf/fr/net/aspose.pdf.facades/pdffileeditor/methods/makebooklet/index) de la classe [PdfFileEditor](https://reference.aspose.com/pdf/fr/net/aspose.pdf.facades/pdffileeditor) vous permet de créer un livret à partir du flux PDF d'entrée et de l'enregistrer dans le flux PDF de sortie. Cette surcharge vous permet de créer un livret en utilisant des flux au lieu de chemins de fichiers. Vous pouvez également spécifier des pages particulières pour les côtés gauche et droit du flux PDF de sortie avec cette surcharge. Le code suivant montre comment créer un livret en utilisant des pages gauche et droite spécifiées et des flux.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void MakeBookletOfPdfUsingSpecifiedLeftAndRightPagesAndStreams()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Pages();
    // Create PdfFileEditor object
    var pdfEditor = new Aspose.Pdf.Facades.PdfFileEditor();
    // Create streams
    using (var inputStream = new FileStream(dataDir + "MakeBookletMultiplePagesInput.pdf", FileMode.Open))
    {
        using (var outputStream = new FileStream(dataDir + "MakeBookletUsingLeftRightPagesAndStreams_out.pdf", FileMode.Create))
        {
            // Set left and right pages
            var leftPages = new int[] { 1, 5 };
            var rightPages = new int[] { 2, 3 };
            // Make booklet
            pdfEditor.MakeBooklet(inputStream, outputStream, leftPages, rightPages);
        }
    }
}
```