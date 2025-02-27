---
title: Delete Images from PDF File using Python
linktitle: Delete Images
type: docs
weight: 20
url: /python-net/delete-images-from-pdf-file/
description: This section explain how to delete Images from PDF File using Aspose.PDF for Python via .NET.
lastmod: "2025-02-27"
TechArticle: true 
AlternativeHeadline: How to Delete Images from PDF File using Python
Abstract: The article, authored, provides a beginner-level guide on how to delete images from PDF files using the Aspose.PDF for Python via .NET library. It addresses the need for removing images to protect privacy, reduce file size, and prepare PDFs for text extraction or compression. The article includes step-by-step instructions and code snippets for both deleting specific images and removing all images from a PDF document. The tutorial demonstrates the use of Python code to open a PDF, access and delete images from pages, and save the updated document. This guide is published by Aspose.PDF Doc Team, which provides resources for PDF manipulation and offers support across multiple platforms.
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Delete Images from PDF File using Python",
    "alternativeHeadline": "How to remove Images from PDF",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "pdf, python, delete, remove image from pdf",
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
    "url": "/python-net/delete-images-from-pdf-file/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/python-net/delete-images-from-pdf-file/"
    },
    "dateModified": "2023-02-04",
    "description": "This section explain how to delete Images from PDF File using Aspose.PDF for Python via .NET."
}
</script>

There are many reasons for removing all or specific images from PDFs.

Sometimes a PDF file may contain important images that need to be removed to protect privacy or prevent unauthorized access to certain information.

Removing unwanted or redundant images can help reduce file size, making it easier to share or store PDFs. 

If necessary, you can reduce the number of pages by removing all images from the document.
Also, deleting images from the document will help prepare the PDF for compression or extraction of text information.

**Aspose.PDF for Python via .NET** will help you with this task.

## Delete Images from PDF File

To delete an image from a PDF file:

1. Open existing PDF Document.
1. Delete a particular image.
1. Save updated PDF file.

The following code snippet shows how to delete an image from a PDF file.

```python

    import aspose.pdf as ap

    # Open document
    document = ap.Document(input_file)

    # Delete particular image
    document.pages[2].resources.images.delete(1)

    # Save updated PDF file
    document.save(output_pdf)
```

## Delete all images from input PDF 

```python

    import aspose.pdf as ap

    # Open document
    document = ap.Document(input_file)

    # Delete all images on all pages
    for i in range(len(document.pages)):
        while len(document.pages[i + 1].resources.images) != 0:
            document.pages[i + 1].resources.images.delete(1)

    # Save updated PDF file
    document.save(output_file)
```


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
    "applicationCategory": "PDF Manipulation Library for Python via .NET",
    "downloadUrl": "https://www.nuget.org/packages/Aspose.PDF/",
    "operatingSystem": "Windows, MacOS, Linux",
    "screenshot": "https://docs.aspose.com/pdf/python-net/create-pdf-document/screenshot.png",
    "softwareVersion": "2022.1",
    "aggregateRating": {
        "@type": "AggregateRating",
        "ratingValue": "5",
        "ratingCount": "16"
    }
}
</script>
