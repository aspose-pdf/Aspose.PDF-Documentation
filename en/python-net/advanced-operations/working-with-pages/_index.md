---
title: Working with PDF Pages in Python
linktitle: Working with Pages
type: docs
weight: 20
url: /python-net/working-with-pages/
description: How to add pages, add headers and footers, add watermarks  you can know in this section. Aspose.PDF for Python via .NET explain to you all details on this topic.
lastmod: "2025-02-27"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true 
AlternativeHeadline: How to work with PDF Pages in Python 
Abstract: The article titled "Working with PDF Pages in Python", published by the Aspose.PDF Doc Team, provides a comprehensive guide on manipulating PDF documents using the Aspose.PDF for Python via .NET library. Aimed at beginners, the article covers a variety of tasks such as adding, moving, and deleting pages within a PDF. It explains how to insert pages at specific locations or append them to the document's end, as well as how to modify page properties like size and orientation. Additionally, the article details methods for enhancing PDFs with headers, footers, watermarks, and background images using classes such as `Artifact`, `PageNumberStamp`, `ImageStamp`, and `TextStamp`. Users can also learn how to split PDF files, crop pages, and work with page numbering. The library supports cross-platform use on Windows, MacOS, and Linux, and the article includes links to relevant resources and code snippets to demonstrate these capabilities.
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Working with PDF Pages in Python",
    "alternativeHeadline": "How to work with PDF Pages",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "pdf, python, pdf page, add pdf page, add page number, rotate page, delete page",
    "wordcount": "302",
    "proficiencyLevel":"Beginner",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF Doc Team",
        "url": "https://products.aspose.com/pdf",
        "logo": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-python-net.svg",
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
    "url": "/python-net/working-with-pages/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/python-net/working-with-pages/"
    },
    "dateModified": "2023-02-04",
    "description": "How to add pages, add headers and footers, add watermarks  you can know in this section. Aspose.PDF for Python via .NET explain to you all details on this topic."
}
</script>

**Aspose.PDF for Python via .NET** lets you insert a page to a PDF document at any location in the file as well as add pages to the end of a PDF file. This section shows how to add pages to a PDF without Acrobat Reader.
You can add text or images in the headers and footers of your PDF file, and choose different headers in your document with Python library by Aspose.
Also, try to crop pages in PDF document programmatically using Python.

This section learn you how to add watermarks in your PDF file using Artifact class. You will check the programming sample for this task.
Add Page number using [PageNumberStamp](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagenumberstamp/) class. For adding a Stamp in your document use [ImageStamp](https://reference.aspose.com/pdf/python-net/aspose.pdf/imagestamp/) and [TextStamp](https://reference.aspose.com/pdf/python-net/aspose.pdf/textstamp/) classes. Use adding a watermark for creating background images in your PDF file with **Aspose.PDF for Python via .NET**.

You are able to do the following:

- [Add Pages](/pdf/python-net/add-pages/) - add pages at desired location or to the end of a PDF file and delete a page from you document.
- [Move Pages](/pdf/python-net/move-pages/) - move pages from one document to another.
- [Delete Pages](/pdf/python-net/delete-pages/) - delete page from your PDF file using PageCollection collection.
- [Change Page size](/pdf/python-net/change-page-size/) - you can change PDF page size with code snippet using Aspose.PDF library.
- [Rotate Pages](/pdf/python-net/rotate-pages/) - you can change the page orientation of pages in an existing PDF file.
- [Split Pages](/pdf/python-net/split-document/) - you can split PDF files into one or multiple PDF.
- [Add Headers and/or Footers](/pdf/python-net/add-headers-and-footers-of-pdf-file/) - add text or images in the headers and footers of your PDF file .
- [Crop Pages](/pdf/python-net/crop-pages/) - you can crop pages in PDF document programmatically with different Page Properties.
- [Add Watermarks](/pdf/python-net/add-watermarks/) - add watermarks in your PDF file with Artifact Class.
- [Add Page Numbering in PDF File](/pdf/python-net/add-page-number/) - PageNumberStamp class will help you to add a Page Number in your PDF file.
- [Add Backgrounds](/pdf/python-net/add-backgrounds/) - background images can be used to add a watermark.
- [Stamping](/pdf/python-net/stamping/) - you can use the ImageStamp class to add an image stamp to a PDF file and TextStamp class for adding a text.
- [Get and Set Page Properties](/pdf/python-net/get-and-set-page-properties/) - this section shows how to get the number of pages in a PDF file, get information about PDF page properties such as color and set page properties.

<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Aspose.PDF for Python via .NET Library",
    "image": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-python-net.svg",
    "url": "https://www.aspose.com/",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF",
        "url": "https://products.aspose.com/pdf",
        "logo": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-python-net.svg",
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
    "applicationCategory": "PDF Manipulation Library for Python",
    "downloadUrl": "https://www.nuget.org/packages/Aspose.PDF/",
    "operatingSystem": "Windows, MacOS, Linux",
    "screenshot": "https://docs.aspose.com/pdf/python-net/create-pdf-document/example.png",
    "softwareVersion": "2022.1",
    "aggregateRating": {
        "@type": "AggregateRating",
        "ratingValue": "5",
        "ratingCount": "16"
    }
}
</script>
