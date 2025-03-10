---
title: Insérer des pages PDF
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 50
url: /fr/net/insert-pdf-pages/
description: Cette section explique comment insérer des pages PDF avec Aspose.PDF Facades en utilisant la classe PdfFileEditor.
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Insert PDF pages",
    "alternativeHeadline": "Insert Specific PDF Pages into Existing Documents",
    "abstract": "Optimisez votre gestion des PDF avec la nouvelle fonctionnalité permettant aux utilisateurs d'insérer des pages spécifiques d'un PDF dans un autre en utilisant la classe PdfFileEditor. Cette fonctionnalité prend en charge l'insertion de pages basée sur des plages et des tableaux, améliorant l'efficacité du flux de travail en combinant sans effort des documents via des chemins de fichiers ou des flux.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "751",
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
    "url": "/net/insert-pdf-pages/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/insert-pdf-pages/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF peut effectuer non seulement des tâches simples et faciles mais aussi faire face à des objectifs plus complexes. Consultez la section suivante pour les utilisateurs avancés et les développeurs."
}
</script>

## Insérer des pages PDF entre deux numéros en utilisant des chemins de fichiers

Une plage particulière de pages peut être insérée d'un PDF à un autre en utilisant la méthode [Insert](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/insert/index) de la classe [PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor). Pour ce faire, vous avez besoin d'un fichier PDF d'entrée dans lequel vous souhaitez insérer les pages, d'un fichier port à partir duquel les pages doivent être prises pour l'insertion, d'un emplacement où les pages doivent être insérées, et d'une plage de pages du fichier port qui doivent être insérées dans le fichier PDF d'entrée. Cette plage est spécifiée avec des paramètres de page de début et de page de fin. Enfin, le fichier PDF de sortie est enregistré avec la plage spécifiée de pages insérées dans le fichier d'entrée. Le code suivant vous montre comment insérer des pages PDF entre deux numéros en utilisant des flux de fichiers.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void InsertPdfPagesBetweenTwoNumbersUsingFilePaths()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Pages();
    // Create PdfFileEditor object
    var pdfEditor = new Aspose.Pdf.Facades.PdfFileEditor();
    // Insert pages
    pdfEditor.Insert(
        dataDir + "MultiplePages.pdf", 1, 
        dataDir + "InsertPages.pdf", 2, 5, 
        dataDir + "InsertPagesBetweenNumbers_out.pdf");
}
```

## Insérer un tableau de pages PDF en utilisant des chemins de fichiers

Si vous souhaitez insérer certaines pages spécifiées dans un autre fichier PDF, vous pouvez utiliser une surcharge de la méthode [Insert](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/insert/index) qui nécessite un tableau d'entiers de pages. Dans ce tableau, vous pouvez spécifier quelles pages particulières vous souhaitez insérer dans le fichier PDF d'entrée. Pour ce faire, vous avez besoin d'un fichier PDF d'entrée dans lequel vous souhaitez insérer les pages, d'un fichier port à partir duquel les pages doivent être prises pour l'insertion, d'un emplacement où les pages doivent être insérées, et d'un tableau d'entiers des pages du fichier port qui doivent être insérées dans le fichier PDF d'entrée. Ce tableau contient une liste de pages particulières que vous souhaitez insérer dans le fichier PDF d'entrée. Enfin, le fichier PDF de sortie est enregistré avec le tableau spécifié de pages insérées dans le fichier d'entrée. Le code suivant vous montre comment insérer un tableau de pages PDF en utilisant des chemins de fichiers.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void InsertArrayOfPdfPagesUsingFilePaths()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Pages();
    // Create PdfFileEditor object
    var pdfEditor = new Aspose.Pdf.Facades.PdfFileEditor();
    var pagesToInsert = new int[] { 2, 3 };
    // Insert pages
    pdfEditor.Insert(
        dataDir + "MultiplePages.pdf", 1, 
        dataDir + "InsertPages.pdf", pagesToInsert, 
        dataDir + "InsertArrayOfPages_out.pdf");
}
```

## Insérer des pages PDF entre deux numéros en utilisant des flux

Si vous souhaitez insérer la plage de pages en utilisant des flux, vous devez simplement utiliser la surcharge appropriée de la méthode [Insert](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/insert/index) de la classe [PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor). Pour ce faire, vous avez besoin d'un flux PDF d'entrée dans lequel vous souhaitez insérer les pages, d'un flux port à partir duquel les pages doivent être prises pour l'insertion, d'un emplacement où les pages doivent être insérées, et d'une plage de pages du flux port qui doivent être insérées dans le flux PDF d'entrée. Cette plage est spécifiée avec des paramètres de page de début et de page de fin. Enfin, le flux PDF de sortie est enregistré avec la plage spécifiée de pages insérées dans le flux d'entrée. Le code suivant vous montre comment insérer des pages PDF entre deux numéros en utilisant des flux.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void InsertPdfPagesBetweenTwoNumbersUsingStreams()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Pages();
    // Create PdfFileEditor object
    var pdfEditor = new Aspose.Pdf.Facades.PdfFileEditor();
    // Create streams
    using (var inputStream = new FileStream(dataDir + "MultiplePages.pdf", FileMode.Open))
    {
        using (var portStream = new FileStream(dataDir + "InsertPages.pdf", FileMode.Open))
        {
            using (var outputStream = new FileStream(dataDir + "InsertPagesBetweenNumbersUsingStreams_out.pdf", FileMode.Create))
            {
                // Insert pages
                pdfEditor.Insert(inputStream, 1, portStream, 1, 4, outputStream);
            }
        }
    }
}
```

## Insérer un tableau de pages PDF en utilisant des flux

Vous pouvez également insérer un tableau de pages dans un autre fichier PDF en utilisant des flux avec l'aide de la surcharge appropriée de la méthode Insert qui nécessite un tableau d'entiers de pages. Dans ce tableau, vous pouvez spécifier quelles pages particulières vous souhaitez insérer dans le flux PDF d'entrée. Pour ce faire, vous avez besoin d'un flux PDF d'entrée dans lequel vous souhaitez insérer les pages, d'un flux port à partir duquel les pages doivent être prises pour l'insertion, d'un emplacement où les pages doivent être insérées, et d'un tableau d'entiers des pages du flux port qui doivent être insérées dans le fichier PDF d'entrée. Ce tableau contient une liste de pages particulières que vous souhaitez insérer dans le flux PDF d'entrée. Enfin, le flux PDF de sortie est enregistré avec le tableau spécifié de pages insérées dans le fichier d'entrée. Le code suivant vous montre comment insérer un tableau de pages PDF en utilisant des flux.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void InsertArrayOfPdfPagesUsingStreams()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Pages();
    // Create PdfFileEditor object
    var pdfEditor = new Aspose.Pdf.Facades.PdfFileEditor();
    // Pages to insert
    var pagesToInsert = new int[] { 2, 3 };
    // Create streams
    using (var inputStream = new FileStream(dataDir + "MultiplePages.pdf", FileMode.Open))
    {
        using (var portStream = new FileStream(dataDir + "InsertPages.pdf", FileMode.Open))
        {
            using (var outputStream = new FileStream(dataDir + "InsertPagesUsingStreams_out.pdf", FileMode.Create))
            {
                // Insert pages
                pdfEditor.Insert(inputStream, 1, portStream, pagesToInsert, outputStream);
            }
        }
    }
}
```