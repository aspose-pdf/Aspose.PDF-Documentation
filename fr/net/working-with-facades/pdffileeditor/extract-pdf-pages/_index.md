---
title: Extraire des pages PDF
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 40
url: /fr/net/extract-pdf-pages/
description: Cette section explique comment extraire des pages PDF avec Aspose.PDF Facades en utilisant la classe PdfFileEditor.
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Extract PDF pages",
    "alternativeHeadline": "Effortlessly Extract Selected Pages from PDF Files",
    "abstract": "La fonctionnalité Extraire des pages PDF dans Aspose.PDF for .NET Facades offre aux utilisateurs des capacités améliorées pour extraire sélectivement des pages de documents PDF. En utilisant la classe PdfFileEditor, les utilisateurs peuvent extraire efficacement une plage spécifiée ou un ensemble de pages via des chemins de fichiers ou des flux, rendant la manipulation des documents plus fluide et flexible. Cette fonctionnalité est particulièrement bénéfique pour les utilisateurs cherchant à personnaliser leur contenu PDF sans altérer les fichiers originaux.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "660",
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
    "url": "/net/extract-pdf-pages/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/extract-pdf-pages/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF peut effectuer non seulement des tâches simples et faciles mais aussi faire face à des objectifs plus complexes. Consultez la section suivante pour les utilisateurs avancés et les développeurs."
}
</script>

## Extraire des pages PDF entre deux numéros en utilisant des chemins de fichiers

La méthode [Extract](https://reference.aspose.com/pdf/fr/net/aspose.pdf.facades/pdffileeditor/methods/extract/index) de la classe [PdfFileEditor](https://reference.aspose.com/pdf/fr/net/aspose.pdf.facades/pdffileeditor) vous permet d'extraire une plage spécifiée de pages d'un fichier PDF. Cette surcharge vous permet d'extraire des pages tout en manipulant les fichiers PDF depuis le disque. Cette surcharge nécessite les paramètres suivants : chemin du fichier d'entrée, page de début, page de fin et chemin du fichier de sortie. Les pages de la page de début à la page de fin seront extraites et la sortie sera enregistrée sur le disque. Le code suivant vous montre comment extraire des pages PDF entre deux numéros en utilisant des chemins de fichiers.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void Extract_PDFPages_FilePaths()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Pages();

    // Create PdfFileEditor object
    PdfFileEditor pdfEditor = new PdfFileEditor();

    // Extract pages
    pdfEditor.Extract(dataDir + "MultiplePages.pdf", 1, 3, dataDir + "ExtractPagesBetweenNumbers_out.pdf");
}
```

## Extraire un tableau de pages PDF en utilisant des chemins de fichiers

Si vous ne souhaitez pas extraire une plage de pages, mais plutôt un ensemble de pages particulières, la méthode [Extract](https://reference.aspose.com/pdf/fr/net/aspose.pdf.facades/pdffileeditor/methods/extract/index) vous permet également de le faire. Vous devez d'abord créer un tableau d'entiers avec tous les numéros de pages qui doivent être extraits. Cette surcharge de la méthode [Extract](https://reference.aspose.com/pdf/fr/net/aspose.pdf.facades/pdffileeditor/methods/extract/index) prend les paramètres suivants : fichier PDF d'entrée, tableau d'entiers des pages à extraire et fichier PDF de sortie. Le code suivant vous montre comment extraire des pages PDF en utilisant des chemins de fichiers.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void Extract_PDFPages_Streams()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Pages();

    // Create PdfFileEditor object
    PdfFileEditor pdfEditor = new PdfFileEditor();

    // Create streams
    using (FileStream inputStream = new FileStream(dataDir + "MultiplePages.pdf", FileMode.Open))
    {
        using (FileStream outputStream = new FileStream(dataDir + "ExtractPagesBetweenTwoNumbers_out.pdf", FileMode.Create))
        {
            // Extract pages
            pdfEditor.Extract(inputStream, 1, 3, outputStream);
        }
    }
}
```

## Extraire des pages PDF entre deux numéros en utilisant des flux

La méthode [Extract](https://reference.aspose.com/pdf/fr/net/aspose.pdf.facades/pdffileeditor/methods/extract/index) de la classe [PdfFileEditor](https://reference.aspose.com/pdf/fr/net/aspose.pdf.facades/pdffileeditor) vous permet d'extraire une plage de pages en utilisant des flux. Vous devez passer les paramètres suivants à cette surcharge : flux d'entrée, page de début, page de fin et flux de sortie. Les pages spécifiées par la plage entre la page de début et la page de fin seront extraites du flux d'entrée et enregistrées dans le flux de sortie. Le code suivant vous montre comment extraire des pages PDF entre deux numéros en utilisant des flux.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void Extract_ArrayPDFPages_FilePaths()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Pages();

    // Create PdfFileEditor object
    PdfFileEditor pdfEditor = new PdfFileEditor();
    int[] pagesToExtract = new int[] { 1, 2 };
    // Extract pages
    pdfEditor.Extract(dataDir + "Extract.pdf", pagesToExtract, dataDir + "ExtractArrayOfPages_out.pdf");
}
```

## Extraire un tableau de pages PDF en utilisant des flux

Un tableau de pages peut être extrait du flux PDF et enregistré dans le flux de sortie en utilisant la surcharge appropriée de la méthode [Extract](https://reference.aspose.com/pdf/fr/net/aspose.pdf.facades/pdffileeditor/methods/extract/index). Si vous ne souhaitez pas extraire une plage de pages, mais plutôt un ensemble de pages particulières, la méthode [Extract](https://reference.aspose.com/pdf/fr/net/aspose.pdf.facades/pdffileeditor/methods/extract/index) vous permet également de le faire. Vous devez d'abord créer un tableau d'entiers avec tous les numéros de pages qui doivent être extraits. Cette surcharge de la méthode [Extract](https://reference.aspose.com/pdf/fr/net/aspose.pdf.facades/pdffileeditor/methods/extract/index) prend les paramètres suivants : flux d'entrée, tableau d'entiers des pages à extraire et flux de sortie. Le code suivant vous montre comment extraire des pages PDF en utilisant des flux.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void Extract_ArrayPDFPages_Streams()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Pages();
    
    // Create PdfFileEditor object
    PdfFileEditor pdfEditor = new PdfFileEditor();
    // Create streams
    using (FileStream inputStream = new FileStream(dataDir + "MultiplePages.pdf", FileMode.Open))
    {
        using (FileStream outputStream = new FileStream(dataDir + "ExtractArrayOfPagesUsingStreams_out.pdf", FileMode.Create))
        {
            int[] pagesToExtract = new int[] { 1, 2 };
            // Extract pages
            pdfEditor.Extract(inputStream, pagesToExtract, outputStream);
        }
    }
}
```