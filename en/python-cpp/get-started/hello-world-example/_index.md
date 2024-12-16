---
title: Example of Hello World using Python language
linktitle: Hello World Example
type: docs
weight: 20
url: /python-cpp/hello-world-example/
description: This sample demonstrates how to create a simple PDF "Hello, World!" document using Aspose.PDF for Python
lastmod: "2023-07-27"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Example of Hello World using Python language",
    "alternativeHeadline": "Aspose.PDF Python (via C++) example",
    "author": {
        "@type": "Person",
        "givenName": "Andriy",
        "familyName": "Andrukhovskiy",
        "url":"https://www.linkedin.com/in/andruhovski/"
    },
    "genre": "pdf document generation",
    "keywords": "pdf, Python, document generation",
    "wordcount": "302",
    "proficiencyLevel":"Beginner",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF Doc Team",
        "url": "https://products.aspose.com/pdf",
        "logo": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-python-cpp.svg",
        "alternateName": "Aspose",
        "sameAs": [
            "https://facebook.com/aspose.pdf/",
            "https://twitter.com/asposepdf",
            "https://https://www.youtube.com/@AsposePDF",
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
    "url": "http://docs.aspose.com/pdf/python-cpp/hello-world-example/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "http://docs.aspose.com/pdf/python-cpp/hello-world-example/"
    },
    "dateModified": "2022-02-04",
    "description": "This sample demonstrates how to create a simple PDF document using Aspose.PDF for Python.",
    "articleBody": "A simple use case can help to demonstrate the features of a programming language or software. This is usually done with a "Hello World" example.\n\nAspose.PDF for Python via C++ is a powerful PDF API that enables the developers to create, manipulate and convert PDF documents in their Python applications. It supports working with various file formats such as PDF, XFA, TXT, HTML, PCL, XML, XPS, EPUB, TEX and image file formats. In this article, we will show you how to create a PDF document with the text "Hello World!" using Aspose.PDF API. You need to install Aspose.PDF for Python via C++ in your environment before running the following code sample.\n1. Import the AsposePdfPython module.\n2. Create a new PDF document object using the document_create function.\n3. Get the pages collection of the document using the document_get_pages function.\n4. Add a new page to the pages collection using the page_collection_add_page function.\n5. Get the paragraphs collection of the page using the page_get_paragraphs function.\n6. Creating a new image object using the image_create function.\n7. Setting the file name of the image object to "sample.jpg" using the image_set_file function.\n8. Adding the image object to the paragraphs collection using the paragraphs_add_image function.\n9. Saving the document to a file named "document.pdf" using the document_save function.\n10. Closing the document handle using the close_handle function."
}
</script>

A simple use case can help to demonstrate the features of a programming language or software. This is usually done with a "Hello World" example.

Aspose.PDF for Python via C++ is a powerful PDF API that enables the developers to create, manipulate and convert PDF documents in their Python applications. It supports working with various file formats such as PDF, XFA, TXT, HTML, PCL, XML, XPS, EPUB, TEX and image file formats. In this article, we will show you how to create a PDF document with the text "Hello World!" using Aspose.PDF API. You need to install Aspose.PDF for Python via C++ in your environment before running the following code sample.

1. Import the `AsposePdfPython` module.
1. Create a new PDF document object using the `document_create` function.
1. Get the pages collection of the document using the `document_get_pages` function.
1. Add a new page to the pages collection using the `page_collection_add_page` function.
1. Get the paragraphs collection of the page using the `page_get_paragraphs` function.
1. Creating a new image object using the `image_create` function.
1. Setting the file name of the image object to "sample.jpg" using the `image_set_file` function.
1. Adding the image object to the paragraphs collection using the `paragraphs_add_image` function.
1. Saving the document to a file named "document.pdf" using the `document_save` function.
1. Closing the document handle using the `close_handle function`.

The following code snippet is a Hello World program that demonstrates how to Aspose.PDF for Python via C++ works.

```python
from AsposePdfPython import *
 
doc = document_create()
pages = document_get_pages(doc)
page = page_collection_add_page(pages)
paragraphs = page_get_paragraphs(page)
image = image_create()
image_set_file(image,"sample.jpg")
paragraphs_add_image(paragraphs,image)
 
document_save(doc, "document.pdf")
close_handle(doc)
```
