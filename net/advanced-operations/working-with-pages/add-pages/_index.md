---
title: Add Pages in PDF with C#
linktitle: Add Pages
type: docs
weight: 10
url: /net/add-pages/
description: This article teaches how to insert (add) a page at the desired location PDF file. Learn how to move, remove (delete) pages from a PDF file using C#.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
aliases:
    - /net/insert-pdf-pages/
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Add Pages in PDF with C#",
    "alternativeHeadline": "How to add Pages in PDF document",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "pdf, c#, add pdf page, insert pdf page",
    "wordcount": "302",
    "proficiencyLevel":"Beginner",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF Doc Team",
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
    "url": "/net/add-pages/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/add-pages/"
    },
    "dateModified": "2022-02-04",
    "description": "This article teaches how to insert (add) a page at the desired location PDF file. Learn how to move, remove (delete) pages from a PDF file using C#."
}
</script>

Aspose.PDF for .NET API provides full flexibility to work with pages in a PDF document using C# or any other .NET language. It maintains all the pages of a PDF document in [PageCollection](https://reference.aspose.com/pdf/net/aspose.pdf/pagecollection) that can be used to work with PDF pages.
Aspose.PDF for .NET lets you insert a page to a PDF document at any location in the file as well as add pages to the end of a PDF file.
This section shows how to add pages to a PDF using C#.

## Add or Insert Page in a PDF File

Aspose.PDF for .NET lets you insert a page to a PDF document at any location in the file as well as add pages to the end of a PDF file.

The following code snippet also work with [Aspose.PDF.Drawing](/pdf/net/drawing/) library.

### Insert Empty Page in a PDF File at Desired Location

To insert an empty page in a PDF file:

1. Create a [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) class object with the input PDF file.
1. Call the [PageCollection](https://reference.aspose.com/pdf/net/aspose.pdf/pagecollection) collection's [Insert](https://reference.aspose.com/pdf/net/aspose.pdf/pagecollection/methods/insert) method with specified index.
1. Save the output PDF using the [Save](https://reference.aspose.com/pdf/net/aspose.pdf.document/save/methods/4) method.

The following code snippet shows you how to insert a page in a PDF file.

{{< gist "aspose-pdf" "7e1330795d76012fcb04248bb81d45b3" "Examples-CSharp-AsposePDF-Pages-InsertEmptyPage-InsertEmptyPage.cs" >}}

In example above, we added empty page with default parameters. If you need to make page size the same as another page in document you shold add
a few lines of code:

```csharp
var page = pdfDocument.Pages.Insert(2);
//copy page parameters from page 1
page.ArtBox = pdfDocument.Pages[1].ArtBox;
page.BleedBox = pdfDocument.Pages[1].BleedBox;
page.CropBox = pdfDocument.Pages[1].CropBox;
page.MediaBox = pdfDocument.Pages[1].MediaBox;
page.TrimBox = pdfDocument.Pages[1].TrimBox;
```

### Add an Empty Page at the End of a PDF File

Sometimes, you want to ensure that a document ends on an empty page. This topic explains how to insert an empty page at the end of the PDF document.

To insert an empty page at the end of a PDF file:

1. Create a [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) class object with the input PDF file.
1. Call the [PageCollection](https://reference.aspose.com/pdf/net/aspose.pdf/pagecollection) collection's [Add](https://reference.aspose.com/pdf/net/aspose.pdf.pagecollection/add/methods/1) method, without any parameters.
1. Save the output PDF using the [Save](https://reference.aspose.com/pdf/net/aspose.pdf.document/save/methods/4) method.

The following code snippet shows you how to insert an empty page at the end of a PDF file.

{{< gist "aspose-pdf" "7e1330795d76012fcb04248bb81d45b3" "Examples-CSharp-AsposePDF-Pages-InsertEmptyPageAtEnd-InsertEmptyPageAtEnd.cs" >}}

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
