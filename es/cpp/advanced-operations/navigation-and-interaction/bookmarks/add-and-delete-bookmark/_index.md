---
title: Añadir y Eliminar un Marcador
linktitle: Añadir y Eliminar un Marcador
type: docs
weight: 10
url: es/cpp/add-and-delete-bookmark/
description: Este tema explica cómo añadir un marcador a un documento PDF con la biblioteca C++. También puedes eliminar todos o ciertos marcadores de un documento PDF.
lastmod: "2022-01-31"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Añadir un Marcador a un Documento PDF

Los marcadores se mantienen en la colección [OutlineItemCollection](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.outline_item_collection/) del objeto Documento, que a su vez está en la colección [OutlineCollection](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.outline_collection/).

Para añadir un marcador a un PDF:

1. Abre un documento PDF usando el objeto [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document/).
1. Crea un marcador y define sus propiedades.
1. Agregue la colección [OutlineItemCollection](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.outline_collection/) a la colección Outlines.

El siguiente fragmento de código le muestra cómo agregar un marcador en un documento PDF.

```cpp
void AddBookmarks() {


String _dataDir("C:\\Samples\\Bookmarks\\");

auto pdfDocument = MakeObject<Document>(_dataDir + u"AddBookmark.pdf");


// Crear un objeto marcador

auto pdfOutline = MakeObject<OutlineItemCollection>(pdfDocument->get_Outlines());

pdfOutline->set_Title(u"Test Outline");

pdfOutline->set_Italic(true);

pdfOutline->set_Bold(true);


// Establecer el número de página de destino

pdfOutline->set_Action(MakeObject<Aspose::Pdf::Annotations::GoToAction>(pdfDocument->get_Pages()->idx_get(2)));


// Agregar un marcador en la colección de esquemas del documento.

pdfDocument->get_Outlines()->Add(pdfOutline);


// Guardar el documento actualizado

pdfDocument->Save(_dataDir + u"AddBookmark_out.pdf");
}
```

## Agregar un marcador hijo al documento PDF

Los marcadores pueden anidarse, indicando una relación jerárquica con marcadores padre e hijo. Este artículo explica cómo añadir un marcador secundario, es decir, un marcador de segundo nivel, a un PDF.

Para añadir un marcador secundario a un archivo PDF, primero añada un marcador principal:

1. Abra un documento.
1. Añada un marcador a la [OutlineItemCollection](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.outline_item_collection/), definiendo sus propiedades.
1. Añada la OutlineItemCollection a la colección [OutlineCollection](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.outline_collection/) del objeto Document.

El marcador secundario se crea igual que el marcador principal, explicado anteriormente, pero se añade a la colección de Contornos del marcador principal.

Los siguientes fragmentos de código muestran cómo añadir un marcador secundario a un documento PDF.

```cpp
void AddChildBookmark() {


String _dataDir("C:\\Samples\\Bookmarks\\");

// Open document

auto pdfDocument = MakeObject<Document>(_dataDir + u"AddChildBookmark.pdf");


// Create a parent bookmark object

auto pdfOutline = MakeObject<OutlineItemCollection>(pdfDocument->get_Outlines());

pdfOutline->set_Title(u"Parent Outline");

pdfOutline->set_Italic(true);

pdfOutline->set_Bold(true);


// Create a child bookmark object

auto pdfChildOutline = MakeObject<OutlineItemCollection>(pdfDocument->get_Outlines());

pdfChildOutline->set_Title(u"Child Outline");

pdfChildOutline->set_Italic(true);

pdfChildOutline->set_Bold(true);


// Add child bookmark in parent bookmark's collection

pdfOutline->Add(pdfChildOutline);

// Add parent bookmark in the document's outline collection.

pdfDocument->get_Outlines()->Add(pdfOutline);


// Save output

pdfDocument->Save(_dataDir + u"AddChildBookmark_out.pdf");
}
```
## Eliminar todos los marcadores de un documento PDF

Todos los marcadores en un PDF se encuentran en la colección [OutlineCollection](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.outline_collection/). Este artículo explica cómo eliminar todos los marcadores de un archivo PDF.

Para eliminar todos los marcadores de un archivo PDF:

1. Llame al método Delete de la colección [OutlineCollection](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.outline_collection/).
1. Guarde el archivo modificado usando el método Save del objeto [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document/).

Los siguientes fragmentos de código muestran cómo eliminar todos los marcadores de un documento PDF.

```cpp
void DeleteAllBookmarksFromPDFDocument() {


String _dataDir("C:\\Samples\\Bookmarks\\");

// Abrir documento

auto pdfDocument = MakeObject<Document>(_dataDir + u"DeleteAllBookmarks.pdf");


// Eliminar todos los marcadores

pdfDocument->get_Outlines()->Delete();


// Guardar archivo actualizado

pdfDocument->Save(_dataDir + u"DeleteAllBookmarks_out.pdf");
}
```


## Eliminar un marcador particular de un documento PDF

[Eliminar todos los adjuntos del documento PDF](https://docs.aspose.com/pdf/cpp/working-with-attachments/) mostró cómo eliminar todos los adjuntos de un archivo PDF. También es posible eliminar solo adjuntos específicos.

Para eliminar un marcador específico de un archivo PDF:

1. Pase el título del marcador como parámetro al método Delete de la colección [OutlineCollection](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.outline_collection/).
2. Luego guarde el archivo actualizado con el método Save del objeto Document.

La clase [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document/) proporciona la colección [OutlineCollection](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.outline_collection/). El método [Delete](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.outline_collection#a04f36a1f4f7c4fde3189399eb046a98b) elimina cualquier marcador con el título pasado al método.

Los siguientes fragmentos de código muestran cómo eliminar un marcador específico del documento PDF.

```cpp
void DeleteParticularBookmarkPDFDocument() {


String _dataDir("C:\\Samples\\Bookmarks\\");

// Abrir documento

auto pdfDocument = MakeObject<Document>(_dataDir + u"DeleteParticularBookmark.pdf");


// Eliminar marcador específico por título

pdfDocument->get_Outlines()->Delete(u"Child Outline");


// Guardar archivo actualizado

pdfDocument->Save(_dataDir + u"DeleteParticularBookmark_out.pdf");
}
```