---
title: Agregar y eliminar un marcador usando Python
linktitle: Agregar y eliminar un marcador
type: docs
weight: 10
url: /es/python-net/add-and-delete-bookmark/
description: Puedes agregar un marcador a un documento PDF con Python. Es posible eliminar todos o marcadores específicos de un documento PDF.
lastmod: "2025-02-27"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Cómo agregar y eliminar marcadores usando Python
Abstract: Este artículo proporciona instrucciones completas sobre la gestión de marcadores en documentos PDF utilizando la biblioteca Aspose.PDF para Python. Describe los procesos para agregar, modificar y eliminar marcadores dentro de un PDF. El artículo comienza con una guía sobre cómo agregar un marcador creando un objeto `OutlineItemCollection` y añadiéndolo a la `OutlineCollection` del documento. Incluye ejemplos de código que demuestran la creación y adición de marcadores tanto padre como hijo, resaltando una relación jerárquica. Además, el artículo cubre métodos para eliminar todos los marcadores o un marcador específico por título. Cada sección incluye fragmentos de código Python para ilustrar las operaciones, garantizando que los lectores puedan implementar fácilmente las funcionalidades descritas en sus tareas de manipulación de PDF.
---

## Agregar un marcador a un documento PDF

Los marcadores se guardan en la colección [OutlineItemCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlineitemcollection/) del objeto Document, que a su vez está en la colección [OutlineCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlinecollection/).

Para agregar un marcador a un PDF:

1. Abre un documento PDF usando el objeto [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. Crea un marcador y define sus propiedades.
1. Añade la colección [OutlineItemCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlineitemcollection/) a la colección Outlines.

El siguiente fragmento de código muestra cómo agregar un marcador en un documento PDF.

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

Los marcadores pueden anidarse, indicando una relación jerárquica entre marcadores padre e hijo. Este artículo explica cómo agregar un marcador hijo, es decir, un marcador de segundo nivel, a un PDF.

Para agregar un marcador hijo a un archivo PDF, primero agrega un marcador padre:

1. Abre un documento.
1. Añade un marcador a la [OutlineItemCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlineitemcollection/), definiendo sus propiedades.
1. Añade la [OutlineItemCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlineitemcollection/) a la colección [OutlineCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlinecollection/) del objeto Document.

El marcador hijo se crea de la misma manera que el marcador padre, explicado arriba, pero se agrega a la colección Outlines del marcador padre.

Los siguientes fragmentos de código muestran cómo agregar un marcador hijo a un documento PDF.

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

Todos los marcadores en un PDF se encuentran en la colección [OutlineCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlinecollection/). Este artículo explica cómo eliminar todos los marcadores de un archivo PDF.

Para eliminar todos los marcadores de un archivo PDF:

1. Llama al método Delete de la colección [OutlineCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlinecollection/).
1. Guarda el archivo modificado usando el método [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) del objeto [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).

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

1. Pasa el título del marcador como parámetro al método Delete de la colección [OutlineCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlinecollection/).
1. Luego guarda el archivo actualizado con el método Save del objeto Document.

La clase [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) proporciona la colección [OutlineCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlinecollection/). El método [delete()](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlinecollection/#methods) elimina cualquier marcador cuyo título se pase al método.

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


