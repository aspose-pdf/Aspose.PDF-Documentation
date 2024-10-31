---
title: Dividir PDF programáticamente en Python
linktitle: Dividir archivos PDF
type: docs
weight: 60
url: /python-net/split-pdf-document/
keywords: dividir pdf en múltiples archivos, dividir pdf en pdfs separados, dividir pdf python
description: Este tema muestra cómo dividir páginas de PDF en archivos PDF individuales en tus aplicaciones de Python.
lastmod: "2023-04-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Dividir PDF programáticamente",
    "alternativeHeadline": "Cómo dividir PDF con Python",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "generación de documentos pdf",
    "keywords": "pdf, python, dividir pdf",
    "wordcount": "302",
    "proficiencyLevel":"Principiante",
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
                "contactType": "ventas",
                "areaServed": "US",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "ventas",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "ventas",
                "areaServed": "AU",
                "availableLanguage": "en"
            }
        ]
    },
    "url": "/python-net/split-pdf-document/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/python-net/split-pdf-document/"
    },
    "dateModified": "2022-02-04",
    "description": "Este tema muestra cómo dividir páginas de PDF en archivos PDF individuales en tus aplicaciones de Python."
}
</script>


Dividir páginas de PDF puede ser una función útil para aquellos que desean separar un archivo grande en páginas individuales o grupos de páginas.

## Ejemplo en Vivo

[Aspose.PDF Splitter](https://products.aspose.app/pdf/splitter) es una aplicación web gratuita en línea que te permite investigar cómo funciona la funcionalidad de división de presentaciones.

[![Aspose Split PDF](splitter.png)](https://products.aspose.app/pdf/splitter)

Este tema muestra cómo dividir páginas de PDF en archivos PDF individuales en tus aplicaciones de Python. Para dividir páginas de PDF en archivos PDF de una sola página usando Python, se pueden seguir los siguientes pasos:

1. Recorre las páginas del documento PDF a través de la colección [PageCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/) del objeto [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/)
1. Para cada iteración, crea un nuevo objeto Document y añade el objeto [Page](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) individual al documento vacío

1. Guarda el nuevo PDF usando el método [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods)

## Dividir PDF en múltiples archivos o pdfs separados en Python

El siguiente fragmento de código en Python te muestra cómo dividir las páginas de un PDF en archivos PDF individuales.

```python

    import aspose.pdf as ap

    # Abrir documento
    document = ap.Document(input_pdf)

    page_count = 1

    # Bucle a través de todas las páginas
    for pdfPage in document.pages:
        new_document = ap.Document()
        new_document.pages.add(pdfPage)
        new_document.save(output_path + "_page_" + str(page_count) + ".pdf")
        page_count = page_count + 1
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