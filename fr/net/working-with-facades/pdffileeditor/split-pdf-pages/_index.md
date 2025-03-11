---
title: Diviser les pages PDF
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 60
url: /fr/net/split-pdf-pages/
description: Cette section explique comment diviser les pages PDF avec Aspose.PDF Facades en utilisant la classe PdfFileEditor.
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Split PDF pages",
    "alternativeHeadline": "Effortlessly Split PDF Pages via File Paths and Streams",
    "abstract": "La nouvelle fonctionnalité Diviser les pages PDF dans Aspose.PDF for .NET permet aux utilisateurs de diviser efficacement les documents PDF en divers segments en utilisant la classe PdfFileEditor. Cette fonctionnalité prend en charge la division de la première page à une page spécifiée, la division en ensembles en vrac, et même l'isolement de pages individuelles, le tout via des chemins de fichiers ou des flux, offrant des options polyvalentes pour la manipulation de PDF.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "1017",
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
    "url": "/net/split-pdf-pages/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/split-pdf-pages/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF peut effectuer non seulement des tâches simples et faciles mais aussi faire face à des objectifs plus complexes. Consultez la section suivante pour les utilisateurs avancés et les développeurs."
}
</script>

## Diviser les pages PDF depuis le début en utilisant des chemins de fichiers

La méthode [SplitFromFirst](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdffileeditor/splitfromfirst/methods/1) de la classe [PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor) vous permet de diviser le fichier PDF en commençant par la première page et en terminant à un numéro de page spécifié. Si vous souhaitez manipuler les fichiers PDF depuis le disque, vous pouvez passer les chemins de fichiers des fichiers PDF d'entrée et de sortie à cette méthode. Le code suivant vous montre comment diviser les pages PDF depuis le début en utilisant des chemins de fichiers.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SplitPdfPagesFromFirstUsingFilePaths()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Pages();
    // Create PdfFileEditor object
    var pdfEditor = new Aspose.Pdf.Facades.PdfFileEditor();
    // Split pages
    pdfEditor.SplitFromFirst(dataDir + "MultiplePages.pdf", 3, dataDir + "SplitPagesUsingPaths_out.pdf");
}
```

## Diviser les pages PDF depuis le début en utilisant des flux de fichiers

La méthode [SplitFromFirst](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdffileeditor/splitfromfirst/methods/1) de la classe [PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor) vous permet de diviser le fichier PDF en commençant par la première page et en terminant à un numéro de page spécifié. Si vous souhaitez manipuler les fichiers PDF depuis les flux, vous pouvez passer les flux PDF d'entrée et de sortie à cette méthode. Le code suivant vous montre comment diviser les pages PDF depuis le début en utilisant des flux de fichiers.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SplitPdfPagesFromFirstUsingFileStreams()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Pages();
    // Create PdfFileEditor object
    var pdfEditor = new Aspose.Pdf.Facades.PdfFileEditor();
    // Create streams
    using (var inputStream = new FileStream(dataDir + "MultiplePages.pdf", FileMode.Open))
    {
        using (var outputStream = new FileStream(dataDir + "SplitPagesUsingStreams_out.pdf", FileMode.Create))
        {
            // Split pages
            pdfEditor.SplitFromFirst(inputStream, 3, outputStream);
        }
    }
}
```

## Diviser les pages PDF en plusieurs ensembles en utilisant des chemins de fichiers

La méthode [SplitToBulks](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/splittobulks/index) de la classe [PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor) vous permet de diviser le fichier PDF en plusieurs ensembles de pages. Dans cet exemple, nous avons besoin de deux ensembles de pages (1, 2) et (5, 6). Si vous souhaitez accéder au fichier PDF depuis le disque, vous devez passer le PDF d'entrée en tant que chemin de fichier. Cette méthode renvoie un tableau de MemoryStream. Vous pouvez parcourir ce tableau et enregistrer les ensembles de pages individuels en tant que fichiers séparés. Le code suivant vous montre comment diviser les pages PDF en plusieurs ensembles en utilisant des chemins de fichiers.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SplitPdfPagesToBulkUsingFilePaths()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Pages();
    // Create PdfFileEditor object
    var pdfEditor = new Aspose.Pdf.Facades.PdfFileEditor();
    var fileNumber = 1;
    // Create array of pages to split
    var numberOfPages = new int[][] { new int[] { 1, 2 }, new int[] { 3, 4 } };
    // Split to bulk
    var outBuffer = pdfEditor.SplitToBulks(dataDir + "MultiplePages.pdf", numberOfPages);
    // Save individual files
    foreach (var outStream in outBuffer)
    {
        using (var outFileStream = new FileStream(dataDir + "File_" + fileNumber.ToString() + "_out.pdf", FileMode.Create))
        {
            outStream.WriteTo(outFileStream);
            fileNumber++;
        }
    }
}
```

## Diviser les pages PDF en plusieurs ensembles en utilisant des flux

La méthode [SplitToBulks](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/splittobulks/index) de la classe [PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor) vous permet de diviser le fichier PDF en plusieurs ensembles de pages. Dans cet exemple, nous avons besoin de deux ensembles de pages (1, 2) et (5, 6). Vous pouvez passer un flux à cette méthode au lieu d'accéder au fichier depuis le disque. Cette méthode renvoie un tableau de MemoryStream. Vous pouvez parcourir ce tableau et enregistrer les ensembles de pages individuels en tant que fichiers séparés. Le code suivant vous montre comment diviser les pages PDF en plusieurs ensembles en utilisant des flux.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SplitPdfPagesToBulkUsingStreams()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Pages();
    // Create PdfFileEditor object
    var pdfEditor = new Aspose.Pdf.Facades.PdfFileEditor();
    // Create input stream
    using (var inputStream = new FileStream(dataDir + "MultiplePages.pdf", FileMode.Open))
    {
        var fileNumber = 1;
        // Create array of pages to split
        var numberOfPages = new int[][] { new int[] { 1, 2 }, new int[] { 3, 4 } };
        // Split to bulk
        var outBuffer = pdfEditor.SplitToBulks(inputStream, numberOfPages);
        // Save individual files
        foreach (var outStream in outBuffer)
        {
            using (var outFileStream = new FileStream(dataDir + "File_" + fileNumber.ToString() + "_out.pdf", FileMode.Create))
            {
                outStream.WriteTo(outFileStream);
                fileNumber++;
            }
        }
    }
}
```

## Diviser les pages PDF jusqu'à la fin en utilisant des chemins de fichiers

La méthode [SplitToEnd](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/splittoend/index) de la classe [PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor) vous permet de diviser le PDF à partir d'un numéro de page spécifié jusqu'à la fin du fichier PDF et de l'enregistrer en tant que nouveau PDF. Pour ce faire, en utilisant des chemins de fichiers, vous devez passer les chemins de fichiers d'entrée et de sortie ainsi que le numéro de page à partir duquel la division doit commencer. Le PDF de sortie sera enregistré sur le disque. Le code suivant vous montre comment diviser les pages PDF jusqu'à la fin en utilisant des chemins de fichiers.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SplitPdfPagesToEndUsingFilePaths()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Pages();
    // Create PdfFileEditor object
    var pdfEditor = new Aspose.Pdf.Facades.PdfFileEditor();
    // Split pages
    pdfEditor.SplitToEnd(dataDir + "MultiplePages.pdf", 3, dataDir + "SplitPagesToEndUsingPaths_out.pdf");
}
```

## Diviser les pages PDF jusqu'à la fin en utilisant des flux

La méthode [SplitToEnd](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/splittoend/index) de la classe [PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor) vous permet de diviser le PDF à partir d'un numéro de page spécifié jusqu'à la fin du fichier PDF et de l'enregistrer en tant que nouveau PDF. Pour ce faire, en utilisant des flux, vous devez passer les flux d'entrée et de sortie ainsi que le numéro de page à partir duquel la division doit commencer. Le PDF de sortie sera enregistré dans le flux de sortie. Le code suivant vous montre comment diviser les pages PDF jusqu'à la fin en utilisant des flux.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SplitPdfPagesToEndUsingStreams()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Pages();
    // Create PdfFileEditor object
    var pdfEditor = new Aspose.Pdf.Facades.PdfFileEditor();
    // Create streams
    using (var inputStream = new FileStream(dataDir + "MultiplePages.pdf", FileMode.Open))
    {
        using (var outputStream = new FileStream(dataDir + "SplitPagesToEndUsingStreams_out.pdf", FileMode.Create))
        {
            // Split pages
            pdfEditor.SplitToEnd(inputStream, 3, outputStream);   
        }
    }
}
```

## Diviser le PDF en pages individuelles en utilisant des chemins de fichiers

{{% alert color="primary" %}}

Vous pouvez essayer de diviser le document PDF et de voir les résultats en ligne à ce lien :

[products.aspose.app/pdf/splitter](https://products.aspose.app/pdf/splitter) {{% /alert %}}

Pour diviser le fichier PDF en pages individuelles, vous devez passer le PDF en tant que chemin de fichier à la méthode [SplitToPages](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/splittopages/index). Cette méthode renverra un tableau de MemoryStream contenant les pages individuelles du fichier PDF. Vous pouvez parcourir ce tableau de MemoryStream et enregistrer les pages individuelles en tant que fichiers PDF individuels sur le disque. Le code suivant vous montre comment diviser le PDF en pages individuelles en utilisant des chemins de fichiers.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SplitPdfToIndividualPagesUsingFilePaths()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Pages();
    // Create PdfFileEditor object
    var pdfEditor = new Aspose.Pdf.Facades.PdfFileEditor();
    var fileNumber = 1;
    // Split to pages
    var outBuffer = pdfEditor.SplitToPages(dataDir + "splitPdfToIndividualPagesInput.pdf");
    // Save individual files
    foreach (var outStream in outBuffer)
    {
        using (var outFileStream = new FileStream(dataDir + "File_" + fileNumber.ToString() + "_out.pdf", FileMode.Create))
        {
            outStream.WriteTo(outFileStream);
            fileNumber++;
        }
    }
}
```

## Diviser le PDF en pages individuelles en utilisant des flux

Pour diviser le fichier PDF en pages individuelles, vous devez passer le PDF en tant que flux à la méthode [SplitToPages](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/splittopages/index). Cette méthode renverra un tableau de MemoryStream contenant les pages individuelles du fichier PDF. Vous pouvez parcourir ce tableau de MemoryStream et enregistrer les pages individuelles en tant que fichiers PDF individuels sur le disque, ou vous pouvez conserver ces pages individuelles dans le flux mémoire pour une utilisation ultérieure dans votre application. Le code suivant vous montre comment diviser le PDF en pages individuelles en utilisant des flux.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SplitPdfToIndividualPagesUsingStreams()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Pages();
    // Create PdfFileEditor object
    var pdfEditor = new Aspose.Pdf.Facades.PdfFileEditor();
    // Create input stream
    using (var inputStream = new FileStream(dataDir + "splitPdfToIndividualPagesInput.pdf", FileMode.Open))
    {
        var fileNumber = 1;
        // Split to pages
        var outBuffer = pdfEditor.SplitToPages(inputStream);
        // Save individual files
        foreach (var outStream in outBuffer)
        {
            using (var outFileStream = new FileStream(dataDir + "File_" + fileNumber.ToString() + "_out.pdf", FileMode.Create))
            {
                outStream.WriteTo(outFileStream);
                fileNumber++;
            }
        }
    }
}
```