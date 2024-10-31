---
title: Cómo Crear PDF usando Python
linktitle: Crear Documento PDF
type: docs
weight: 10
url: /python-net/create-pdf-document/
description: Crear y dar formato al Documento PDF con Aspose.PDF para Python a través de .NET.
lastmod: "2023-04-12"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Cómo Crear PDF usando Python",
    "alternativeHeadline": "Crear documento PDF desde cero a través de Python",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "generación de documentos pdf",
    "keywords": "pdf, python, dotnet, crear documento pdf",
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
    "url": "/python-net/create-pdf-document/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/python-net/create-pdf-document/"
    },
    "dateModified": "2022-02-04",
    "description": "Crear y dar formato al Documento PDF con Aspose.PDF para Python a través de .NET."
}
</script>


**Aspose.PDF para Python a través de .NET** es una API de manipulación de PDF que permite a los desarrolladores crear, cargar, modificar y convertir archivos PDF directamente desde aplicaciones de Python para .NET con solo unas pocas líneas de código.

## Cómo Crear un Archivo PDF Simple

Para crear un PDF usando Python a través de .NET con Aspose.PDF, puedes seguir estos pasos:

1. Crear un objeto de la clase [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/)
1. Agregar un objeto [Page](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) a la colección [pages](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#properties) del objeto Document
1. Agregar [TextFragment](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragment/) a la colección [paragraphs](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/#properties) de la página
1. Guardar el documento PDF resultante

```python

    import aspose.pdf as ap

    # Inicializar objeto de documento
    document = ap.Document()
    # Agregar página
    page = document.pages.add()
    # Agregar texto a la nueva página
    page.paragraphs.add(ap.text.TextFragment("¡Hola Mundo!"))
    # Guardar PDF actualizado
    document.save(output_pdf)
```