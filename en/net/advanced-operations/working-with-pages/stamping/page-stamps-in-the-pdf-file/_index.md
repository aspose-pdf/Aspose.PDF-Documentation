---
title: Add PDF Page Stamps in PDF using C#
linktitle: Page stamps in PDF File
type: docs
weight: 30
url: /net/page-stamps-in-the-pdf-file/
description: Add a page stamp to a PDF document using the PdfPageStamp class with Aspose.PDF for .NET library.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Add PDF Page Stamps in PDF using C#",
    "alternativeHeadline": "Enhance PDFs with Custom Page Stamps in C#",
    "abstract": "Unlock powerful PDF editing capabilities with the new page stamp feature in Aspose.PDF for .NET. Easily add customizable composite stamps incorporating graphics, text, and tables directly onto your PDF documents, enhancing their visual appeal and functionality. Ideal for creating professional stationery-like designs, this feature simplifies document generation and manipulation in C#",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "212",
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
    "url": "/net/page-stamps-in-the-pdf-file/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/page-stamps-in-the-pdf-file/"
    },
    "dateModified": "2024-11-26",
    "description": "Add a page stamp to a PDF document using the PdfPageStamp class with Aspose.PDF for .NET library."
}
</script>

## Add Page Stamp with C\#

A [PdfPageStamp](https://reference.aspose.com/pdf/net/aspose.pdf/PdfPageStamp) can be used when you need to apply a composite stamp containing graphics, text, tables. The following example shows how to use a stamp to create stationery like in using Adobe InDesign, Illustrator, Microsoft Word. Assume we have some input document and we want apply 2 kinds of border with blue and plum color.

The following code snippet also work with [Aspose.PDF.Drawing](/pdf/net/drawing/) library.

```csharp
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddPageStamp()
{
    // The path to the documents directory
    string dataDir = RunExamples.GetDataDir_AsposePdf_StampsWatermarks();

    var inputFileName = "AddPageStampInput.pdf";
    var outputFileName = "AddPageStamp_out.pdf";
    var pageStampFileName = "AddPageStamp.pdf";

    //Open document
    using (var document = new Aspose.Pdf.Document(dataDir + inputFileName))
    {
        //Create PdfPageStamps
        var bluePageStamp = new Aspose.Pdf.PdfPageStamp(dataDir + pageStampFileName, 1)
        {
            Height = 800,
            Background = true
        };
        // Add stamps
        document.Pages[1].AddStamp(bluePageStamp);
        // Save updated document
        document.Save(dataDir + outputFileName);
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
