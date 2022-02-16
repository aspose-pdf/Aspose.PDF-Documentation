---
title: Working with PDF Pages in C#
linktitle: Working with Pages
type: docs
weight: 20
url: /net/working-with-pages/
description: How to add pages, add headers and footers, add watermarks  you can know in this section. Aspose.PDF for .NET explain to you all details on this topic.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
aliases:
    - /net/working-with-stamps-and-watermarks/
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Working with PDF Pages in C#",
    "alternativeHeadline": "Working with PDF Pages in C#",
    "author": {
        "@type": "Person",
        "name":"Andriy Andrukhovskiy",
        "givenName": "Andriy",
        "familyName": "Andrukhovskiy",
        "url":"https://www.linkedin.com/in/andruhovski/"
    },
    "genre": "pdf document generation",
    "keywords": "pdf, c#, document generation",
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
    "url": "/net/working-with-pages/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/working-with-pages/"
    },
    "dateModified": "2022-02-04",
    "description": "How to add pages, add headers and footers, add watermarks  you can know in this section. Aspose.PDF for .NET explain to you all details on this topic."
}
</script>

**Aspose.PDF for .NET** lets you insert a page to a PDF document at any location in the file as well as add pages to the end of a PDF file. This section shows how to add pages to a PDF without Acrobat Reader.
You can add text or images in the headers and footers of your PDF file, and choose different headers in your document with C# library by Aspose.
Also, try to crop pages in PDF document programmatically using C#.

This section learn you how to add watermarks in your PDF file using Artifact class. You will check the programming sample for this task.
Add Page number using PageNumberStamp class. For adding a Stamp in your document use ImageStamp and TextStamp classes. Use adding a watermark for creating background images in your PDF file with **Aspose.PDF for .NET**.

You are able to do the following:

- [Add Pages](/pdf/net/add-pages/) - add pages at desired location or to the end of a PDF file and delete a page from you document.
- [Move Pages](/pdf/net/move-pages/) - move pages from one document to another.
- [Delete Pages](/pdf/net/delete-pages/) - delete page from your PDF file using PageCollection collection.
- [Change Page size](/pdf/net/change-page-size/) - you can change PDF page size with code snippet using Aspose.PDF library.
- [Rotate Pages](/pdf/net/rotate-pages/) - you can change the page orientation of pages in an existing PDF file.
- [Split Pages](/pdf/net/split-document/) - you can split PDF files into one or multiple PDF.
- [Add Headers and/or Footers](/pdf/net/add-headers-and-footers-of-pdf-file/) - add text or images in the headers and footers of your PDF file .
- [Crop Pages](/pdf/net/crop-pages/) - you can crop pages in PDF document programmatically with different Page Properties.
- [Add Watermarks](/pdf/net/add-watermarks/) - add watermarks in your PDF file with Artifact Class.
- [Add Page Numbering in PDF File](/pdf/net/add-page-number/) - PageNumberStamp class will help you to add a Page Number in your PDF file.
- [Add Backgrounds](/pdf/net/add-backgrounds/) - background images can be used to add a watermark.
- [Stamping](/pdf/net/stamping/) - you can use the ImageStamp class to add an image stamp to a PDF file and TextStamp class for adding a text.

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
