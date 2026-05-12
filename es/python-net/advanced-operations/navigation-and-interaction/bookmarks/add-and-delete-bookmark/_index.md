---
title: Agregar y eliminar marcadores PDF en Python
linktitle: Agregar y eliminar un marcador
type: docs
weight: 10
url: /es/python-net/add-and-delete-bookmark/
description: Aprende cómo agregar y eliminar marcadores en documentos PDF usando Python.
lastmod: "2026-04-15"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Cómo agregar y eliminar marcadores usando Python
Abstract: Este artículo proporciona instrucciones exhaustivas sobre la gestión de marcadores en documentos PDF usando la biblioteca Aspose.PDF for Python via .NET. Describe los procesos para agregar, modificar y eliminar marcadores dentro de un PDF. El artículo comienza con una guía sobre cómo añadir un marcador creando un objeto `OutlineItemCollection` y añadiéndolo a la `OutlineCollection` del documento. Incluye ejemplos de código que demuestran la creación y adición de marcadores tanto padre como hijo, resaltando una relación jerárquica. Además, el artículo cubre métodos para eliminar todos los marcadores o un marcador específico por título. Cada sección incluye fragmentos de código Python para ilustrar las operaciones, asegurando que los lectores puedan implementar fácilmente las funcionalidades descritas en sus tareas de manipulación de PDF.
---

## Agregar un marcador a un documento PDF

Los marcadores se guardan en el objeto Document [OutlineItemCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlineitemcollection/) colección, en sí misma en el [OutlineCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlinecollection/) colección.

Para agregar un marcador a un PDF:

1. Abra un documento PDF usando [Documento](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) objeto.
1. Crea un marcador y define sus propiedades.
1. Añade el [OutlineItemCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlineitemcollection/) colección a la colección Outlines.

El siguiente fragmento de código le muestra cómo agregar un marcador en un documento PDF.

```python
import aspose.pdf as ap
import sys
from os import path

def add_bookmark(infile, outfile):
    # Open PDF document
    document = ap.Document(infile)

    # Create a bookmark object
    pdf_outline = ap.OutlineItemCollection(document.outlines)
    pdf_outline.title = "Test Outline"
    pdf_outline.italic = True
    pdf_outline.bold = True

    # Set the destination page number
    pdf_outline.action = ap.annotations.GoToAction(document.pages[1])

    # Add bookmark to the document's outline collection
    outlines = document.outlines
    outlines.append(pdf_outline)

    # Save PDF document
    document.save(outfile)
```

## Agregar un marcador hijo al documento PDF

Los marcadores pueden anidarse, indicando una relación jerárquica con marcadores padre e hijo. Este artículo explica cómo agregar un marcador hijo, es decir, un marcador de segundo nivel, a un PDF.

Para agregar un marcador hijo a un archivo PDF, primero agregue un marcador padre:

1. Abrir un documento.
1. Agregar un marcador a la [OutlineItemCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlineitemcollection/), definiendo sus propiedades.
1. Agregar el OutlineItemCollection al objeto Document [OutlineCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlinecollection/) colección.

El marcador hijo se crea igual que el marcador padre, explicado arriba, pero se agrega a la colección Outlines del marcador padre

Los siguientes fragmentos de código muestran cómo agregar un marcador hijo a un documento PDF.

```python
import aspose.pdf as ap
import sys
from os import path

def add_child_bookmark(infile, outfile):
    # Open PDF document
    document = ap.Document(infile)

    # Create a parent bookmark object
    pdf_outline = ap.OutlineItemCollection(document.outlines)
    pdf_outline.title = "Parent Outline"
    pdf_outline.italic = True
    pdf_outline.bold = True

    # Create a child bookmark object
    pdf_child_outline = ap.OutlineItemCollection(document.outlines)
    pdf_child_outline.title = "Child Outline"
    pdf_child_outline.italic = True
    pdf_child_outline.bold = True

    # Add child bookmark to parent bookmark's collection
    pdf_outline.append(pdf_child_outline)

    # Add parent bookmark to the document's outline collection
    document.outlines.append(pdf_outline)

    # Save PDF document
    document.save(outfile)
```

## Eliminar todos los marcadores de un documento PDF

Todos los marcadores en un PDF se almacenan en el [OutlineCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlinecollection/) colección. Este artículo explica cómo eliminar todos los marcadores de un archivo PDF.

Para eliminar todos los marcadores de un archivo PDF:

1. Llame al [OutlineCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlinecollection/) método Delete de la colección.
1. Guarda el archivo modificado usando el [Documento](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) del objeto [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) método.

Los siguientes fragmentos de código muestran cómo eliminar todos los marcadores de un documento PDF.

```python
import aspose.pdf as ap
import sys
from os import path

def delete_bookmarks(infile, outfile):
    # Open PDF document
    document = ap.Document(infile)

    # Delete all bookmarks in the PDF document
    document.outlines.delete()

    # Save PDF document
    document.save(outfile)
```

## Eliminar un marcador específico de un documento PDF

Para eliminar un marcador específico de un archivo PDF:

1. Pase el título del marcador como parámetro a la [OutlineCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlinecollection/) método Delete de la colección.
1. Luego guarde el archivo actualizado con el método Save del objeto Document.

El [Documento](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) la clase’ proporciona el [OutlineCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlinecollection/) colección. El [delete()](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlinecollection/#methods) el método elimina cualquier marcador con el título pasado al método.

Los siguientes fragmentos de código muestran cómo eliminar un marcador específico del documento PDF.

```python
import aspose.pdf as ap
import sys
from os import path

def delete_bookmark(infile, outfile):
    # Open PDF document
    document = ap.Document(infile)

    # Delete a specific bookmark by title.
    # Note: If multiple bookmarks have the same title, only the first matching bookmark will be deleted.
    document.outlines.delete("Child Outline")

    # Save PDF document
    document.save(outfile)
```

## Temas relacionados de marcadores

- [Trabajar con marcadores PDF en Python](/pdf/es/python-net/bookmarks/)
- [Obtener, actualizar y expandir marcadores PDF en Python](/pdf/es/python-net/get-update-and-expand-bookmark/)
- [Navegación e interacción en PDF usando Python](/pdf/es/python-net/navigation-and-interaction/)

