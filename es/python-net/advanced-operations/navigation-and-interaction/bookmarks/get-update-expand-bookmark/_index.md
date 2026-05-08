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
Abstract: Este artículo ofrece una guía completa sobre la gestión de marcadores dentro de un documento PDF utilizando la biblioteca Aspose.PDF en Python. Comienza explicando cómo recuperar los marcadores de un archivo PDF a través de la `OutlineCollection`, que contiene todos los marcadores, y detalla el acceso a los atributos del marcador mediante la `OutlineItemCollection`. Luego, el artículo describe el proceso de determinar el número de página asociado a un marcador usando el `PdfBookmarkEditor`. Además, explica cómo manejar estructuras jerárquicas de marcadores recuperando los marcadores secundarios dentro de cada `OutlineItemCollection`. También cubre la actualización de las propiedades de los marcadores, demostrando cómo modificar los atributos del marcador y guardar los cambios en un PDF. Finalmente, el artículo aborda el requisito de expandir los marcadores al visualizar un documento, mostrando cómo establecer el estado abierto de cada marcador para asegurarse de que se expandan por defecto. Los fragmentos de código acompañan a cada sección, proporcionando ejemplos prácticos de la implementación de estas funcionalidades.
---

## Obtener marcadores

El [Documento](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) del objeto [OutlineCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlinecollection/) la colección contiene todos los marcadores de un archivo PDF. Este artículo explica cómo obtener marcadores de un archivo PDF y cómo obtener en qué página está un marcador en particular.

Para obtener los marcadores, recorra la [OutlineCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlinecollection/) colección y obtenga cada marcador en el OutlineItemCollection. El [OutlineItemCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlineitemcollection/) proporciona acceso a todos los atributos del marcador. El siguiente fragmento de código muestra cómo obtener marcadores del archivo PDF.

```python
from os import path
import sys
import aspose.pdf as ap

def get_bookmarks(input_pdf):
    document = ap.Document(input_pdf)
    for i in range(len(document.outlines)):
        outline_item = document.outlines[i + 1]
        print(outline_item.title)
        print(outline_item.italic)
        print(outline_item.bold)
        print(outline_item.color)
```

## Obteniendo el número de página de un marcador

Una vez que hayas agregado un marcador, puedes averiguar en qué página está obteniendo el número de página (PageNumber) de destino asociado al objeto Bookmark.

```python
from os import path
import sys
import aspose.pdf as ap

def get_bookmark_page_number(input_pdf):
    # Create PdfBookmarkEditor
    bookmark_editor = ap.facades.PdfBookmarkEditor()
    # Open PDF file
    bookmark_editor.bind_pdf(input_pdf)
    # Extract bookmarks
    bookmarks = bookmark_editor.extract_bookmarks()
    for bookmark in bookmarks:
        str_level_separator = ""
        for i in range(bookmark.level):
            str_level_separator += "----"

        print(str_level_separator, "Title:", bookmark.title)
        print(str_level_separator, "Page Number:", bookmark.page_number)
        print(str_level_separator, "Page Action:", bookmark.action)
```

## Obtener marcadores secundarios de un documento PDF

Los marcadores pueden organizarse en una estructura jerárquica, con padres e hijos. Para obtener todos los marcadores, recorra las colecciones Outlines del objeto Document. Sin embargo, para obtener también los marcadores secundarios, recorra también todos los marcadores en cada [OutlineItemCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlineitemcollection/) objeto obtenido en el primer bucle. Los siguientes fragmentos de código muestran cómo obtener marcadores secundarios de un documento PDF.

```python
from os import path
import sys
import aspose.pdf as ap

def get_child_bookmarks(input_pdf):
    document = ap.Document(input_pdf)
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
                child_outline_item = outline_item[j + 1]
                print(child_outline_item.title)
                print(child_outline_item.italic)
                print(child_outline_item.bold)
                print(child_outline_item.color)
```

## Actualizar marcadores en un documento PDF

Para actualizar un marcador en un archivo PDF, primero obtenga el marcador particular de la colección OutlineColletion del objeto Document especificando el índice del marcador. Una vez que haya recuperado el marcador en [OutlineItemCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlineitemcollection/) objeto, puede actualizar sus propiedades y luego guardar el archivo PDF actualizado usando el método Save. Los siguientes fragmentos de código muestran cómo actualizar marcadores en un documento PDF.

```python
from os import path
import sys
import aspose.pdf as ap

def update_bookmarks(input_pdf, output_pdf):
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

## Marcadores ampliados al visualizar el documento

Los marcadores se guardan en el objeto Document [OutlineItemCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlineitemcollection/) colección, en sí misma en el [OutlineCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlinecollection/) colección. Sin embargo, puede que tengamos un requisito de que todos los marcadores estén ampliados al visualizar el archivo PDF.

Para cumplir con este requisito, podemos establecer el estado abierto para cada elemento de esquema/marcador como Open. El siguiente fragmento de código le muestra cómo establecer el estado abierto para cada marcador como ampliado en un documento PDF.

```python
from os import path
import sys
import aspose.pdf as ap

def expanded_bookmarks(input_pdf, output_pdf):
    document = ap.Document(input_pdf)
    document.page_mode = ap.PageMode.USE_OUTLINES
    for i in range(len(document.outlines)):
        item = document.outlines[i + 1]
        item.open = True
    document.save(output_pdf)
```

## Temas relacionados de marcadores

- [Trabajar con marcadores PDF en Python](/pdf/es/python-net/bookmarks/)
- [Agregar y eliminar marcadores PDF en Python](/pdf/es/python-net/add-and-delete-bookmark/)
- [Navegación e interacción en PDF usando Python](/pdf/es/python-net/navigation-and-interaction/)

