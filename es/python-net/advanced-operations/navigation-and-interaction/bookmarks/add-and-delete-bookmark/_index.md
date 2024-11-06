---
title: Añadir y Eliminar un Marcador usando Python
linktitle: Añadir y Eliminar un Marcador
type: docs
weight: 10
url: es/python-net/add-and-delete-bookmark/
description: Puede añadir un marcador a un documento PDF con Python. Es posible eliminar todos o algunos marcadores de un documento PDF.
lastmod: "2023-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Añadir y Eliminar un Marcador",
    "alternativeHeadline": "Cómo añadir y eliminar un Marcador de un PDF",
    "author": {
        "@type": "Person",
        "name":"Andriy Andrukhovskiy",
        "givenName": "Andriy",
        "familyName": "Andrukhovskiy",
        "url":"https://www.linkedin.com/in/andruhovski/"
    },
    "genre": "generación de documentos pdf",
    "keywords": "pdf, python, eliminar marcador, añadir marcador",
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
    "url": "/python-net/add-and-delete-bookmark/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/python-net/add-and-delete-bookmark/"
    },
    "dateModified": "2023-02-04",
    "description": "Puede añadir un marcador a un documento PDF con Python. Es posible eliminar todos o algunos marcadores de un documento PDF."
}
</script>


## Añadir un Marcador a un Documento PDF

Los marcadores se mantienen en la colección [OutlineItemCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlineitemcollection/) del objeto Document, que a su vez está en la colección [OutlineCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlinecollection/).

Para añadir un marcador a un PDF:

1. Abra un documento PDF usando el objeto [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. Cree un marcador y defina sus propiedades.
1. Añada la colección [OutlineItemCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlineitemcollection/) a la colección de Outlines.

El siguiente fragmento de código muestra cómo añadir un marcador en un documento PDF.

```python

    import aspose.pdf as ap

    # Abrir documento
    document = ap.Document(input_pdf)

    # Crear un objeto de marcador
    outline = ap.OutlineItemCollection(document.outlines)
    outline.title = "Marcador de Prueba"
    outline.italic = True
    outline.bold = True
    # Establecer el número de página de destino
    outline.action = ap.annotations.GoToAction(document.pages[1])
    # Añadir marcador en la colección de esquemas del documento.
    document.outlines.append(outline)

    # Guardar salida
    document.save(output_pdf)
```


## Añadir un Marcador Hijo al Documento PDF

Los marcadores pueden estar anidados, indicando una relación jerárquica con marcadores padre e hijo. Este artículo explica cómo añadir un marcador hijo, es decir, un marcador de segundo nivel, a un PDF.

Para añadir un marcador hijo a un archivo PDF, primero añada un marcador padre:

1. Abra un documento.
1. Añada un marcador a la [OutlineItemCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlineitemcollection/), definiendo sus propiedades.
1. Añada la OutlineItemCollection a la colección [OutlineCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlinecollection/) del objeto Document.

El marcador hijo se crea igual que el marcador padre, explicado arriba, pero se agrega a la colección de Contornos del marcador padre.

Los siguientes fragmentos de código muestran cómo añadir un marcador hijo a un documento PDF.

```python

    import aspose.pdf as ap

    # Abrir documento
    document = ap.Document(input_pdf)

    # Crear un objeto de marcador padre
    outline = ap.OutlineItemCollection(document.outlines)
    outline.title = "Contorno Padre"
    outline.italic = True
    outline.bold = True

    # Crear un objeto de marcador hijo
    childOutline = ap.OutlineItemCollection(document.outlines)
    childOutline.title = "Contorno Hijo"
    childOutline.italic = True
    childOutline.bold = True

    # Añadir marcador hijo en la colección del marcador padre
    outline.append(childOutline)
    # Añadir marcador padre en la colección de contornos del documento.
    document.outlines.append(outline)

    # Guardar salida
    document.save(output_pdf)
```


## Eliminar todos los Marcadores de un Documento PDF

Todos los marcadores en un PDF se mantienen en la colección [OutlineCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlinecollection/). Este artículo explica cómo eliminar todos los marcadores de un archivo PDF.

Para eliminar todos los marcadores de un archivo PDF:

1. Llame al método Delete de la colección [OutlineCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlinecollection/).
2. Guarde el archivo modificado usando el método [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) del objeto [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).

Los siguientes fragmentos de código muestran cómo eliminar todos los marcadores de un documento PDF.

```python

    import aspose.pdf as ap

    # Abrir documento
    document = ap.Document(input_pdf)

    # Eliminar todos los marcadores
    document.outlines.delete()

    # Guardar archivo actualizado
    document.save(output_pdf)

```

## Eliminar un Marcador Particular de un Documento PDF

Para eliminar un marcador particular de un archivo PDF:

1. Pase el título del marcador como parámetro al método Delete de la colección [OutlineCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlinecollection/).
1. Luego guarde el archivo actualizado con el método Save del objeto Document.

La clase [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) proporciona la colección [OutlineCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlinecollection/). El método [delete()](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlinecollection/#methods) elimina cualquier marcador con el título pasado al método.

Los siguientes fragmentos de código muestran cómo eliminar un marcador particular del documento PDF.

```python

    import aspose.pdf as ap

    # Abrir documento
    document = ap.Document(input_pdf)

    # Eliminar un esquema particular por título
    document.outlines.delete("Child Outline")

    # Guardar archivo actualizado
    document.save(output_pdf)