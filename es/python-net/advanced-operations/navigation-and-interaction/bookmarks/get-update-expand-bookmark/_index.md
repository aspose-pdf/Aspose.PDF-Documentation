---
title: Obtener, Actualizar y Expandir un Marcador usando Python
linktitle: Obtener, Actualizar y Expandir un Marcador
type: docs
weight: 20
url: es/python-net/get-update-and-expand-bookmark/
description: Este artículo describe cómo usar marcadores en un archivo PDF con nuestra biblioteca Aspose.PDF para Python.
lastmod: "2023-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Obtener, Actualizar y Expandir un Marcador con Python",
    "alternativeHeadline": "Cómo obtener Marcadores de un archivo PDF",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "generación de documentos pdf",
    "keywords": "pdf, python, obtener marcadores",
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
    "url": "/python-net/get-update-and-expand-bookmark/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/python-net/get-update-and-expand-bookmark/"
    },
    "dateModified": "2023-02-04",
    "description": "Este artículo describe cómo usar marcadores en un archivo PDF con nuestra biblioteca Aspose.PDF para Python."
}
</script>


## Obtener Marcadores

La colección [OutlineCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlinecollection/) del objeto [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) contiene todos los marcadores de un archivo PDF. Este artículo explica cómo obtener marcadores de un archivo PDF y cómo determinar en qué página se encuentra un marcador en particular.

Para obtener los marcadores, recorre la colección [OutlineCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlinecollection/) y obtén cada marcador en la OutlineItemCollection. La [OutlineItemCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlineitemcollection/) proporciona acceso a todos los atributos del marcador. El siguiente fragmento de código muestra cómo obtener marcadores del archivo PDF.

```python

    import aspose.pdf as ap

    # Abrir documento
    document = ap.Document(input_pdf)

    # Recorrer todos los marcadores
    for i in range(len(document.outlines)):
        outline_item = document.outlines[i + 1]
        print(outline_item.title)
        print(outline_item.italic)
        print(outline_item.bold)
        print(outline_item.color)
```


## Obtener el Número de Página de un Marcador

Una vez que hayas añadido un marcador, puedes averiguar en qué página se encuentra obteniendo el número de página de destino asociado con el objeto Bookmark.

```python

    import aspose.pdf as ap

    # Crear PdfBookmarkEditor
    bookmarkEditor = ap.facades.PdfBookmarkEditor()
    # Abrir archivo PDF
    bookmarkEditor.bind_pdf(input_pdf)
    # Extraer marcadores
    bookmarks = bookmarkEditor.extract_bookmarks()
    for bookmark in bookmarks:
        str_level_seprator = ""
        for i in range(bookmark.level):
            str_level_seprator += "----"

        print(str_level_seprator, "Título:", bookmark.title)
        print(str_level_seprator, "Número de Página:", bookmark.page_number)
        print(str_level_seprator, "Acción de Página:", bookmark.action)
```

## Obtener Submarcadores de un Documento PDF

Los marcadores pueden organizarse en una estructura jerárquica, con padres e hijos.
 Para obtener todos los marcadores, recorra los colecciones de Outlines del objeto Document. Sin embargo, para obtener también los marcadores secundarios, recorra todos los marcadores en cada objeto [OutlineItemCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlineitemcollection/) obtenido en el primer ciclo. Los siguientes fragmentos de código muestran cómo obtener marcadores secundarios de un documento PDF.

```python

    import aspose.pdf as ap

    # Abrir documento
    document = ap.Document(input_pdf)

    # Recorrer todos los marcadores
    for i in range(len(document.outlines)):
        outline_item = document.outlines[i + 1]
        print(outline_item.title)
        print(outline_item.italic)
        print(outline_item.bold)
        print(outline_item.color)
        count = len(outline_item)
        if count > 0:
            print("Marcadores secundarios")
            # Hay marcadores secundarios, entonces recorrer también
            for j in range(len(outline_item)):
                child_outline_item = outline_item[i + 1]
                print(child_outline_item.title)
                print(child_outline_item.italic)
                print(child_outline_item.bold)
                print(child_outline_item.color)
```

## Actualizar Marcadores en un Documento PDF

Para actualizar un marcador en un archivo PDF, primero, obtén el marcador particular de la colección OutlineColletion del objeto Document especificando el índice del marcador. Una vez que hayas recuperado el marcador en el objeto [OutlineItemCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlineitemcollection/), puedes actualizar sus propiedades y luego guardar el archivo PDF actualizado usando el método Save. Los siguientes fragmentos de código muestran cómo actualizar marcadores en un documento PDF.

```python

    import aspose.pdf as ap

    # Abrir documento
    document = ap.Document(input_pdf)

    # Obtener un objeto de marcador
    outline = document.outlines[1]

    # Obtener objeto de marcador hijo
    child_outline = outline[1]
    child_outline.title = "Outline Actualizado"
    child_outline.italic = True
    child_outline.bold = True

    # Guardar salida
    document.save(output_pdf)
```

## Marcadores Expandidos al ver el documento

Los marcadores se mantienen en la colección [OutlineItemCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlineitemcollection/) del objeto Document, a su vez en la colección [OutlineCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlinecollection/).
 Sin embargo, es posible que tengamos un requisito de tener todos los marcadores expandidos al ver el archivo PDF.

Para cumplir con este requisito, podemos establecer el estado abierto para cada elemento de esquema/marcador como Abierto. El siguiente fragmento de código le muestra cómo establecer el estado abierto para cada marcador como expandido en un documento PDF.

```python

    import aspose.pdf as ap

    # Abrir documento
    document = ap.Document(input_pdf)

    # Establecer modo de vista de página, es decir, mostrar miniaturas, pantalla completa, mostrar panel de adjuntos
    document.page_mode = ap.PageMode.USE_OUTLINES
    # Recorrer cada elemento de esquema en la colección de esquemas del archivo PDF
    for i in range(len(document.outlines)):
        item = document.outlines[i + 1]
        # Establecer estado abierto para el elemento de esquema
        item.open = True

    # Guardar salida
    document.save(output_pdf)