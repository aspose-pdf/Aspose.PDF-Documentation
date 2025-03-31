---
title: Añadir Páginas en PDF con Python
linktitle: Añadir Páginas
type: docs
weight: 10
url: /es/python-net/add-pages/
description: Este artículo enseña cómo insertar (añadir) una página en la ubicación deseada de un archivo PDF. Aprenda cómo mover, eliminar (borrar) páginas de un archivo PDF usando C#.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Añadir Páginas en PDF con Python",
    "alternativeHeadline": "Cómo añadir Páginas en un documento PDF",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "generación de documentos pdf",
    "keywords": "pdf, python, añadir página pdf, insertar página pdf",
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
    "url": "/python-net/add-pages/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/python-net/add-pages/"
    },
    "dateModified": "2022-02-04",
    "description": "Este artículo enseña cómo insertar (añadir) una página en la ubicación deseada de un archivo PDF. Aprenda cómo mover, eliminar (borrar) páginas de un archivo PDF usando Python."
}
</script>


Aspose.PDF para Python a través de .NET API proporciona total flexibilidad para trabajar con páginas en un documento PDF usando Python. Mantiene todas las páginas de un documento PDF en [PageCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/) que se puede usar para trabajar con páginas PDF. Aspose.PDF para Python a través de .NET te permite insertar una página en un documento PDF en cualquier ubicación del archivo, así como agregar páginas al final de un archivo PDF. Esta sección muestra cómo agregar páginas a un PDF usando Python.

## Agregar o Insertar Página en un Archivo PDF

Aspose.PDF para Python a través de .NET te permite insertar una página en un documento PDF en cualquier ubicación del archivo, así como agregar páginas al final de un archivo PDF.

### Insertar Página Vacía en un Archivo PDF en la Ubicación Deseada

Para insertar una página vacía en un archivo PDF:

1. Crea un objeto de la clase [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) con el archivo PDF de entrada.

1. Llame al método [insert](https://reference.aspose.com/pdf/es/net/aspose.pdf/pagecollection/methods/insert) de la colección [PageCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/) con el índice especificado.
1. Guarde el PDF de salida usando el método [save](https://reference.aspose.com/pdf/es/net/aspose.pdf.document/save/methods/4).

El siguiente fragmento de código le muestra cómo insertar una página en un archivo PDF.

```python

    import aspose.pdf as ap

    # Abrir documento
    document = ap.Document(input_pdf)
    # Insertar una página vacía en un PDF
    document.pages.insert(2)
    # Guardar archivo de salida
    document.save(output_pdf)
```

### Agregar una Página Vacía al Final de un Archivo PDF

A veces, desea asegurarse de que un documento termine en una página vacía. Este tema explica cómo insertar una página vacía al final del documento PDF.

Para insertar una página vacía al final de un archivo PDF:

1. Cree un objeto de la clase [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) con el archivo PDF de entrada.

1. Llame al método [add()](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/#methods) de la colección [PageCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/), sin ningún parámetro.
1. Guarde el PDF de salida usando el método [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods).

El siguiente fragmento de código le muestra cómo insertar una página vacía al final de un archivo PDF.

```python

    import aspose.pdf as ap

    # Abrir documento
    document = ap.Document(input_pdf)

    # Insertar una página vacía al final de un archivo PDF
    document.pages.add()

    # Guardar archivo de salida
    document.save(output_pdf)