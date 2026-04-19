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
Abstract: Este artículo proporciona instrucciones completas sobre la gestión de marcadores en documentos PDF usando la biblioteca Aspose.PDF para Python. Describe los procesos para agregar, modificar y eliminar marcadores dentro de un PDF. El artículo comienza con una guía sobre cómo añadir un marcador creando un objeto `OutlineItemCollection` y agregándolo a la `OutlineCollection` del documento. Incluye ejemplos de código que demuestran la creación y adición de marcadores tanto padre como hijo, resaltando una relación jerárquica. Además, el artículo cubre los métodos para eliminar todos los marcadores o un marcador específico por título. Cada sección incluye fragmentos de código Python para ilustrar las operaciones, asegurando que los lectores puedan implementar fácilmente las funcionalidades descritas en sus tareas de manipulación de PDF.
---

## Agregar un marcador a un documento PDF

Los marcadores se almacenan en el objeto Document [OutlineItemCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlineitemcollection/) colección, en sí misma en el [OutlineCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlinecollection/) colección.

Para agregar un marcador a un PDF:

1. Abrir un documento PDF usando [Documento](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) objeto.
1. Cree un marcador y defina sus propiedades.
1. Añada el [OutlineItemCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlineitemcollection/) colección a la colección Outlines.

El siguiente fragmento de código le muestra cómo agregar un marcador en un documento PDF.

```python

    import aspose.pdf as ap

    # Open document
    document = ap.Document(input_pdf)

    # Create a bookmark object
    outline = ap.OutlineItemCollection(document.outlines)
    outline.title = "Test Bookmark"
    outline.italic = True
    outline.bold = True
    # Set the destination page number
    outline.action = ap.annotations.GoToAction(document.pages[1])
    # Add bookmark in the document's outline collection.
    document.outlines.append(outline)

    # Save output
    document.save(output_pdf)
```

## Agregar un marcador hijo al documento PDF

Los marcadores pueden anidarse, indicando una relación jerárquica con marcadores padre e hijo. Este artículo explica cómo agregar un marcador hijo, es decir, un marcador de segundo nivel, a un PDF.

Para agregar un marcador hijo a un archivo PDF, primero agregue un marcador padre:

1. Abra un documento.
1. Agregar un marcador al [OutlineItemCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlineitemcollection/), definiendo sus propiedades.
1. Agregar el OutlineItemCollection al objeto Document [OutlineCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlinecollection/) colección.

El marcador hijo se crea igual que el marcador padre, explicado arriba, pero se agrega a la colección Outlines del marcador padre

Los siguientes fragmentos de código muestran cómo agregar un marcador secundario a un documento PDF.

```python

    import aspose.pdf as ap

    # Open document
    document = ap.Document(input_pdf)

    # Create a parent bookmark object
    outline = ap.OutlineItemCollection(document.outlines)
    outline.title = "Parent Outline"
    outline.italic = True
    outline.bold = True

    # Create a child bookmark object
    childOutline = ap.OutlineItemCollection(document.outlines)
    childOutline.title = "Child Outline"
    childOutline.italic = True
    childOutline.bold = True

    # Add child bookmark in parent bookmark's collection
    outline.append(childOutline)
    # Add parent bookmark in the document's outline collection.
    document.outlines.append(outline)

    # Save output
    document.save(output_pdf)
```

## Eliminar todos los marcadores de un documento PDF

Todos los marcadores en un PDF se almacenan en el [OutlineCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlinecollection/) colección. Este artículo explica cómo eliminar todos los marcadores de un archivo PDF.

Para eliminar todos los marcadores de un archivo PDF:

1. Llame al [OutlineCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlinecollection/) Método Delete de la colección.
1. Guarde el archivo modificado usando el [Documento](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) del objeto [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) método.

Los siguientes fragmentos de código muestran cómo eliminar todos los marcadores de un documento PDF.

```python

    import aspose.pdf as ap

    # Open document
    document = ap.Document(input_pdf)

    # Delete all bookmarks
    document.outlines.delete()

    # Save updated file
    document.save(output_pdf)

```

## Eliminar un marcador específico de un documento PDF

Para eliminar un marcador específico de un archivo PDF:

1. Pase el título del marcador como parámetro a la [OutlineCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlinecollection/) Método Delete de la colección.
1. Entonces guarde el archivo actualizado con el método Save del objeto Document.

El [Documento](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) La clase proporciona el [OutlineCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlinecollection/) colección. El [delete()](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlinecollection/#methods) el método elimina cualquier marcador con el título pasado al método.

Los siguientes fragmentos de código muestran cómo eliminar un marcador específico del documento PDF.

```python

    import aspose.pdf as ap

    # Open document
    document = ap.Document(input_pdf)

    # Delete particular outline by Title
    document.outlines.delete("Child Outline")

    # Save updated file
    document.save(output_pdf)
```

## Temas relacionados con marcadores

- [Trabajar con marcadores PDF en Python](/pdf/es/python-net/bookmarks/)
- [Obtener, actualizar y expandir los marcadores de PDF en Python](/pdf/es/python-net/get-update-and-expand-bookmark/)
- [Navegación e interacción en PDF usando Python](/pdf/es/python-net/navigation-and-interaction/)

