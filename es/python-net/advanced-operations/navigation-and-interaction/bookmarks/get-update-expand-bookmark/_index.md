---
title: Obtener, actualizar y expandir marcadores PDF en Python
linktitle: Obtener, actualizar y expandir un marcador
type: docs
weight: 20
url: /es/python-net/get-update-and-expand-bookmark/
description: Aprende cómo recuperar, actualizar y expandir marcadores en documentos PDF usando Python.
lastmod: "2026-04-15"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Cómo usar marcadores en PDF con Python
Abstract: Este artículo ofrece una guía completa sobre la gestión de marcadores dentro de un documento PDF usando la biblioteca Aspose.PDF para Python. Comienza explicando cómo recuperar los marcadores de un archivo PDF a través de la `OutlineCollection`, que contiene todos los marcadores, y detalla el acceso a los atributos de los marcadores mediante la `OutlineItemCollection`. Luego el artículo describe el proceso de determinar el número de página asociado a un marcador usando el `PdfBookmarkEditor`. Además explica cómo manejar estructuras jerárquicas de marcadores recuperando los marcadores hijos dentro de cada `OutlineItemCollection`. También cubre la actualización de las propiedades de los marcadores, demostrando cómo modificar los atributos de los marcadores y guardar los cambios en un PDF. Finalmente, el artículo aborda el requisito de expandir los marcadores al visualizar un documento, mostrando cómo establecer el estado abierto de cada marcador para garantizar que se expandan por defecto. Los fragmentos de código acompañan cada sección, proporcionando ejemplos prácticos de la implementación de estas funcionalidades.
---

## Obtener marcadores

El [Documento](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) del objeto [OutlineCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlinecollection/) collection contiene todos los marcadores de un archivo PDF. Este artículo explica cómo obtener marcadores de un archivo PDF y cómo averiguar en qué página se encuentra un marcador en particular.

Para obtener los marcadores, recorra el [OutlineCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlinecollection/) collection y obtenga cada marcador en el OutlineItemCollection. The [OutlineItemCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlineitemcollection/) proporciona acceso a todos los atributos del marcador. El siguiente fragmento de código muestra cómo obtener marcadores del archivo PDF.

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

Una vez que hayas añadido un marcador, puedes averiguar en qué página está obteniendo el PageNumber de destino asociado al objeto Bookmark.

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

Los marcadores pueden organizarse en una estructura jerárquica, con padres e hijos. Para obtener todos los marcadores, recorra las colecciones Outlines del objeto Document. Sin embargo, para obtener también los marcadores hijos, recorra también todos los marcadores en cada [OutlineItemCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlineitemcollection/) objeto obtenido en el primer bucle. Los siguientes fragmentos de código muestran cómo obtener marcadores hijos de un documento PDF.

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

Para actualizar un marcador en un archivo PDF, primero obtenga el marcador específico de la colección OutlineColletion del objeto Document especificando el índice del marcador. Una vez que haya recuperado el marcador en [OutlineItemCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlineitemcollection/) objeto, puede actualizar sus propiedades y luego guardar el archivo PDF actualizado usando el método Save. Los siguientes fragmentos de código muestran cómo actualizar marcadores en un documento PDF.

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

Los marcadores se almacenan en el objeto Document [OutlineItemCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlineitemcollection/) colección, en sí misma en el [OutlineCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlinecollection/) collection. Sin embargo, puede que tengamos un requisito de que todos los marcadores estén expandidos al visualizar el archivo PDF.

Para cumplir con este requisito, podemos establecer el estado abierto para cada elemento de outline/bookmark como Open. El siguiente fragmento de código le muestra cómo establecer el estado abierto para cada marcador como expandido en un documento PDF.

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

## Temas relacionados con marcadores

- [Trabajar con marcadores PDF en Python](/pdf/es/python-net/bookmarks/)
- [Agregar y eliminar marcadores PDF en Python](/pdf/es/python-net/add-and-delete-bookmark/)
- [Navegación e interacción en PDF usando Python](/pdf/es/python-net/navigation-and-interaction/)

