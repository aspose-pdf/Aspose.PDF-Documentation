---
title: Move PDF Pages programmatically via Python
linktitle: Move PDF Pages
type: docs
weight: 20
url: /python-net/move-pages/
description: Try to move pages at desired location or at the end of a PDF file using Aspose.PDF for Python via .NET.
lastmod: "2023-04-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Move PDF Pages programmatically Python",
    "alternativeHeadline": "How to move PDF Pages with Python",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "pdf, python, move pdf page",
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
    "url": "/python-net/move-pages/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/python-net/move-pages/"
    },
    "dateModified": "2023-04-04",
    "description": "Try to move pages at desired location or at the end of a PDF file using Aspose.PDF for Python via .NET."
}
</script>

## Moving a Page from one PDF Document to Another

This topic explains how to move page from one PDF document to the end of another document using Python.
To move an page we should:

1. Create a [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) class object with the source PDF file.
1. Create a [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) class object with the destination PDF file.
1. Get Page from the the [PageCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/) collection's.
1. [add()](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/#methods) page to the destination document.
1. Save the output PDF using the [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) method.
1. [delete()](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/#methods) page in source document.
1. Save the source PDF using the [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) method.

The following code snippet shows you how to move one page.

```python

    import aspose.pdf as ap

    srcDocument = ap.Document(src_file_name)
    dstDocument = ap.Document(dst_File_name)
    page = srcDocument.pages[2]
    dstDocument.pages.add(page)
    # Save output file
    dstDocument.save(dst_File_name_new)
    srcDocument.pages.delete(2)
    srcDocument.save(src_file_name_new)
```

## Moving bunch of Pages from one PDF Document to Another

1. Create a [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) class object with the source PDF file.
1. Create a [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) class object with the destination PDF file.
1. Define an array with page numbers to be moved.
1. Run loop through array:
    1. Get Page from the the [PageCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/) collection's.
    1. [add()](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/#methods) page to the destination document.
1. Save the output PDF using the [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) method.
1. [delete()](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/#methods) page in source document using array.
1. Save the source PDF using the [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) method.

The following code snippet shows you how to insert an empty page at the end of a PDF file.

```python

    import aspose.pdf as ap

    srcDocument = ap.Document(input_pdf)
    dstDocument = ap.Document()
    pages = [1, 3]
    for page_index in pages:
        page = srcDocument.pages[page_index]
        dstDocument.pages.add(page)
    # Save output files
    dstDocument.save(output_pdf_1)
    srcDocument.pages.delete(pages)
    srcDocument.save(output_pdf_2)
```

## Moving a Page in new location in the current PDF Document

1. Create a [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) class object with the source PDF file.
1. Get Page from the the [PageCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/) collection's.
1. [add()](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/#methods) page to the new location (for example to end).
1. [delete()](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/#methods) page in previous location.
1. Save the output PDF using the [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) method.

```python

    import aspose.pdf as ap

    srcDocument = ap.Document(input_pdf)

    page = srcDocument.pages[2]
    srcDocument.pages.add(page)
    srcDocument.pages.delete(2)

    # Save output file
    srcDocument.save(output_pdf)
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
