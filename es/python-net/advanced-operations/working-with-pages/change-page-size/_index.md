---
title: Cambiar el Tamaño de la Página PDF con Python
linktitle: Cambiar el Tamaño de la Página PDF
type: docs
weight: 60
url: es/python-net/change-page-size/
description: Cambia el tamaño de la página de tu documento PDF usando la biblioteca Aspose.PDF para Python a través de .NET.
lastmod: "2023-04-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Cambiar el Tamaño de la Página PDF con Python",
    "alternativeHeadline": "Redimensionar Página PDF con Python",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "generación de documentos pdf",
    "keywords": "pdf, python, cambiar tamaño pdf, redimensionar pdf",
    "wordcount": "302",
    "proficiencyLevel":"Principiante",
    "publisher": {
        "@type": "Organization",
        "name": "Equipo de Documentación de Aspose.PDF",
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
    "url": "/python-net/change-page-size/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/python-net/change-page-size/"
    },
    "dateModified": "2023-04-04",
    "description": "Cambia el tamaño de la página de tu documento PDF usando la biblioteca Aspose.PDF para Python a través de .NET."
}
</script>


## Cambiar el Tamaño de Página del PDF

Aspose.PDF para Python a través de .NET te permite cambiar el tamaño de página del PDF con simples líneas de código en tus aplicaciones Python. Este tema explica cómo actualizar/cambiar las dimensiones de página (tamaño) de un archivo PDF existente.

La clase [Page](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) contiene el método [set_page_size()](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/#methods) que te permite establecer el tamaño de la página. El fragmento de código a continuación actualiza las dimensiones de la página en unos pocos pasos fáciles:

1. Cargar el archivo PDF de origen.
1. Obtener las páginas en el objeto [PageCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/).
1. Obtener una página dada.
1. Llamar al método set_page_size() para actualizar sus dimensiones.
1. Llamar al método [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) de la clase [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) para generar el archivo PDF con dimensiones de página actualizadas.

```python

    import aspose.pdf as ap

    document = ap.Document(input_pdf)

    # Obtener una página en particular
    page = document.pages[1]

    # Establecer el tamaño de la página como A4 (11.7 x 8.3 in) y en Aspose.Pdf, 1 pulgada = 72 puntos
    # Así que las dimensiones A4 en puntos serán (842.4, 597.6)
    page.set_page_size(597.6, 842.4)

    # Guardar el documento actualizado
    document.save(output_pdf)
```


<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Aspose.PDF para la Biblioteca .NET",
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
    "offers": {
        "@type": "Offer",
        "price": "1199",
        "priceCurrency": "USD"
    },
    "applicationCategory": "Biblioteca de Manipulación de PDF para Python",
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