---
title: Move PDF Pages programmatically C#
linktitle: Move PDF Pages
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 20
url: /net/move-pages/
description: Try to move pages at desired location or at the end of a PDF file using Aspose.PDF for .NET.
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Move PDF Pages programmatically C#",
    "alternativeHeadline": "Programmatically Rearrange PDF Pages with .NET",
    "abstract": "Aspose.PDF for .NET introduces a powerful new feature that allows users to programmatically move PDF pages between documents or rearrange them within the same document. This functionality enhances PDF manipulation capabilities by enabling developers to insert pages at designated locations and effortlessly manage page organization while maintaining document integrity",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "668",
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
    "url": "/net/move-pages/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/move-pages/"
    },
    "dateModified": "2024-11-26",
    "description": "Try to move pages at desired location or at the end of a PDF file using Aspose.PDF for .NET."
}
</script>

## Moving a Page from one PDF Document to Another

This topic explains how to move page from one PDF document to the end of another document using C#.

The following code snippet also work with [Aspose.PDF.Drawing](/pdf/net/drawing/) library.

To move an page we should:

1. Create a [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) class object with the source PDF file.
1. Create a [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) class object with the destination PDF file.
1. Get Page from the the [PageCollection](https://reference.aspose.com/pdf/net/aspose.pdf/pagecollection) collection's.
1. [Add](https://reference.aspose.com/pdf/net/aspose.pdf.pagecollection/add/methods/1) page to the destination document.
1. Save the output PDF using the [Save](https://reference.aspose.com/pdf/net/aspose.pdf.document/save/methods/4) method.
1. [Delete](https://reference.aspose.com/pdf/net/aspose.pdf.pagecollection/delete/methods/1) page in source document.
1. Save the source PDF using the [Save](https://reference.aspose.com/pdf/net/aspose.pdf.document/save/methods/4) method.

The following code snippet shows you how to move one page.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void MovingAPageFromOnePdfDocumentToAnother()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Pages();

    // Open PDF documents
    using (var srcDocument = new Aspose.Pdf.Document(dataDir + "MovingPageInput.pdf"))
    {
        using (var dstDocument = new Aspose.Pdf.Document())
        {
            var page = srcDocument.Pages[2];
            dstDocument.Pages.Add(page);
            // Save PDF document
            dstDocument.Save(dataDir + "MovingPage_out.pdf");
            srcDocument.Pages.Delete(2);
            // Save PDF document
            srcDocument.Save(dataDir + "MovingPageInput_out.pdf");
        }
    }
}
```

## Moving bunch of Pages from one PDF Document to Another

1. Create a [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) class object with the source PDF file.
1. Create a [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) class object with the destination PDF file.
1. Define an array with page numbers to be moved.
1. Run loop through array:
    1. Get Page from the the [PageCollection](https://reference.aspose.com/pdf/net/aspose.pdf/pagecollection) collection's.
    1. [Add](https://reference.aspose.com/pdf/net/aspose.pdf.pagecollection/add/methods/1) page to the destination document.
1. Save the output PDF using the [Save](https://reference.aspose.com/pdf/net/aspose.pdf.document/save/methods/4) method.
1. [Delete](https://reference.aspose.com/pdf/net/aspose.pdf.pagecollection/delete/methods/2) page in source document using array.
1. Save the source PDF using the [Save](https://reference.aspose.com/pdf/net/aspose.pdf.document/save/methods/4) method.

The following code snippet shows you how to move a bunch of pages from one PDF document to another.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void MovingBunchOfPagesFromOnePdfDocumentToAnother()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Pages();

    // Open PDF documents
    using (var srcDocument = new Aspose.Pdf.Document(dataDir + "MovingBunchOfPagesInput.pdf"))
    {
        using (var dstDocument = new Aspose.Pdf.Document())
        {
            var pages = new[] { 1, 3 };
            foreach (int pageIndex in pages)
            {
                var page = srcDocument.Pages[pageIndex];
                dstDocument.Pages.Add(page);
            }
            // Save PDF document
            dstDocument.Save(dataDir + "MovingBunchOfPages_out.pdf");
            srcDocument.Pages.Delete(pages);
            // Save PDF document
            srcDocument.Save(dataDir + "MovingBunchOfPagesInput_out.pdf";
        }
    }
}
```

## Moving a Page in new location in the current PDF Document

1. Create a [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) class object with the source PDF file.
1. Get Page from the the [PageCollection](https://reference.aspose.com/pdf/net/aspose.pdf/pagecollection) collection's.
1. [Add](https://reference.aspose.com/pdf/net/aspose.pdf.pagecollection/add/methods/1) page to the new location (for example to end).
1. [Delete](https://reference.aspose.com/pdf/net/aspose.pdf.pagecollection/delete/methods/1) page in previous location.
1. Save the output PDF using the [Save](https://reference.aspose.com/pdf/net/aspose.pdf.document/save/methods/4) method.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void MovingAPageInNewLocationInTheCurrentPdfDocument()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Pages();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "MovingAPageInNewLocationInTheCurrentPdfDocumentInput.pdf"))
    {
        var page = document.Pages[2];
        document.Pages.Add(page);
        document.Pages.Delete(2);
        // Save PDF document
        document.Save(dataDir + "MovingAPageInNewLocationInTheCurrentPdfDocument_out.pdf");
    }
}
```

<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Aspose.PDF for .NET Library",
    "image": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-net.svg",
    "url": "https://www.aspose.com/",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF",
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
    "offers": {
        "@type": "Offer",
        "price": "1199",
        "priceCurrency": "USD"
    },
    "applicationCategory": "PDF Manipulation Library for .NET",
    "downloadUrl": "https://www.nuget.org/packages/Aspose.PDF/",
    "operatingSystem": "Windows, MacOS, Linux",
    "screenshot": "https://docs.aspose.com/pdf/net/create-pdf-document/screenshot.png",
    "softwareVersion": "2022.1",
    "aggregateRating": {
        "@type": "AggregateRating",
        "ratingValue": "5",
        "ratingCount": "16"
    }
}
</script>
