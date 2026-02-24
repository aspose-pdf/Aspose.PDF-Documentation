---
title: Obtener, actualizar y expandir un marcador usando Python
linktitle: Obtener, actualizar y expandir un marcador
type: docs
weight: 20
url: /es/python-net/get-update-and-expand-bookmark/
description: Este artículo describe cómo usar marcadores en un archivo PDF con nuestra biblioteca Aspose.PDF para Python.
lastmod: "2025-02-27"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Cómo usar marcadores en PDF con Python
Abstract: Este artículo ofrece una guía completa sobre la gestión de marcadores dentro de un documento PDF utilizando la biblioteca Aspose.PDF en Python. Comienza explicando cómo recuperar marcadores de un archivo PDF a través de `OutlineCollection`, que contiene todos los marcadores, y detalla el acceso a los atributos de los marcadores mediante `OutlineItemCollection`. Luego describe el proceso de determinar el número de página asociado a un marcador usando `PdfBookmarkEditor`. Además explica cómo manejar estructuras jerárquicas de marcadores recuperando los marcadores hijos dentro de cada `OutlineItemCollection`. También cubre la actualización de propiedades de los marcadores, mostrando cómo modificar los atributos de los marcadores y guardar los cambios en un PDF. Por último, el artículo aborda la necesidad de expandir los marcadores al visualizar un documento, mostrando cómo establecer el estado abierto de cada marcador para que se expandan por defecto. Los fragmentos de código acompañan cada sección, proporcionando ejemplos prácticos de la implementación de estas funcionalidades.
---

## Obtener marcadores

El objeto [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) de la [OutlineCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlinecollection/) contiene todos los marcadores de un archivo PDF. Este artículo explica cómo obtener marcadores de un archivo PDF y cómo averiguar en qué página está un marcador en particular.

Para obtener los marcadores, recorra la colección [OutlineCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlinecollection/) y obtenga cada marcador en el OutlineItemCollection. La [OutlineItemCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlineitemcollection/) proporciona acceso a todos los atributos del marcador. El siguiente fragmento de código muestra cómo obtener marcadores del archivo PDF.

```python

    import aspose.pdf as ap

    # Open document
    document = ap.Document(input_pdf)

    # Loop through all the bookmarks
    for i in range(len(document.outlines)):
        outline_item = document.outlines[i + 1]
        print(outline_item.title)
        print(outline_item.italic)
        print(outline_item.bold)
        print(outline_item.color)
```

## Obtener el número de página de un marcador

Una vez que haya añadido un marcador, puede averiguar en qué página está obteniendo el número de página de destino asociado al objeto Bookmark.

```python

    import aspose.pdf as ap

    # Create PdfBookmarkEditor
    bookmarkEditor = ap.facades.PdfBookmarkEditor()
    # Open PDF file
    bookmarkEditor.bind_pdf(input_pdf)
    # Extract bookmarks
    bookmarks = bookmarkEditor.extract_bookmarks()
    for bookmark in bookmarks:
        str_level_seprator = ""
        for i in range(bookmark.level):
            str_level_seprator += "----"

        print(str_level_seprator, "Title:", bookmark.title)
        print(str_level_seprator, "Page Number:", bookmark.page_number)
        print(str_level_seprator, "Page Action:", bookmark.action)
```

## Obtener marcadores hijos de un documento PDF

Los marcadores pueden organizarse en una estructura jerárquica, con padres e hijos. Para obtener todos los marcadores, recorra las colecciones Outlines del objeto Document. Sin embargo, para obtener también los marcadores hijos, recorra también todos los marcadores en cada objeto [OutlineItemCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlineitemcollection/) obtenido en el primer bucle. Los siguientes fragmentos de código muestran cómo obtener marcadores hijos de un documento PDF.

```python

    import aspose.pdf as ap

    # Open document
    document = ap.Document(input_pdf)

    # Loop through all the bookmarks
    for i in range(len(document.outlines)):
        outline_item = document.outlines[i + 1]
        print(outline_item.title)
        print(outline_item.italic)
        print(outline_item.bold)
        print(outline_item.color)
        count = len(outline_item)
        if count > 0:
            print("Child Bookmarks")
            # There are child bookmarks then loop through that as well
            for j in range(len(outline_item)):
                child_outline_item = outline_item[i + 1]
                print(child_outline_item.title)
                print(child_outline_item.italic)
                print(child_outline_item.bold)
                print(child_outline_item.color)
```

## Actualizar marcadores en un documento PDF

Para actualizar un marcador en un archivo PDF, primero obtenga el marcador específico de la colección OutlineColletion del objeto Document especificando el índice del marcador. Una vez que haya recuperado el marcador en el objeto [OutlineItemCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlineitemcollection/), puede actualizar sus propiedades y luego guardar el archivo PDF actualizado usando el método Save. Los siguientes fragmentos de código muestran cómo actualizar marcadores en un documento PDF.

```python

    import aspose.pdf as ap

    # Open document
    document = ap.Document(input_pdf)

    # Get a bookmark object
    outline = document.outlines[1]

    # Get child bookmark object
    child_outline = outline[1]
    child_outline.title = "Updated Outline"
    child_outline.italic = True
    child_outline.bold = True

    # Save output
    document.save(output_pdf)
```

## Marcadores expandidos al visualizar el documento

Los marcadores se encuentran en la colección [OutlineItemCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlineitemcollection/) del objeto Document, que a su vez está en la colección [OutlineCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlinecollection/). Sin embargo, podríamos tener el requisito de que todos los marcadores estén expandidos al visualizar el archivo PDF.

Para cumplir con este requisito, podemos establecer el estado abierto de cada elemento de contorno/marcador como Abierto. El siguiente fragmento de código muestra cómo establecer el estado abierto de cada marcador como expandido en un documento PDF.

```python

    import aspose.pdf as ap

    # Open document
    document = ap.Document(input_pdf)

    # Set page view mode i.e. show thumbnails, full-screen, show attachment panel
    document.page_mode = ap.PageMode.USE_OUTLINES
    # Traverse through each Ouline item in outlines collection of PDF file
    for i in range(len(document.outlines)):
        item = document.outlines[i + 1]
        # Set open status for outline item
        item.open = True

    # Save output
    document.save(output_pdf)
```


