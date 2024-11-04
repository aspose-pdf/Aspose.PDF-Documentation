---
title: Añadir y Eliminar un Marcador 
linktitle: Añadir y Eliminar un Marcador
type: docs
weight: 10
url: /java/add-and-delete-bookmark/
description: Puedes añadir un marcador a un documento PDF con Java. Es posible eliminar todos o algunos marcadores de un documento PDF.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Añadir un Marcador a un Documento PDF

Los marcadores se mantienen en la colección [OutlineItemCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/OutlineItemCollection) del objeto Document, que a su vez está en la colección [OutlineCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/OutlineCollection).

Para añadir un marcador a un PDF:

1. Abre un documento PDF usando el objeto [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document).
1. Crea un marcador y define sus propiedades.
1. Añade la colección [OutlineItemCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/OutlineItemCollection) a la colección Outlines.

El siguiente fragmento de código te muestra cómo añadir un marcador en un documento PDF.

```java
package com.aspose.pdf.examples;

import java.io.IOException;

import com.aspose.pdf.*;
import com.aspose.pdf.facades.Bookmark;
import com.aspose.pdf.facades.Bookmarks;
import com.aspose.pdf.facades.PdfBookmarkEditor;

public class ExampleBookmarks {

    private static String _dataDir = "/home/aspose/pdf-examples/Samples/Bookmarks/";

    private static String GetDataDir() {
        String os = System.getProperty("os.name");
        if (os.startsWith("Windows"))
            _dataDir = "C:\\Samples\\Bookmarks\\";
        return _dataDir;
    }

    public static void AddBookmarks() throws IOException {

        Document pdfDocument = new Document(GetDataDir() + "AddBookmark.pdf");

        // Crear un objeto de marcador
        OutlineItemCollection pdfOutline = new OutlineItemCollection(pdfDocument.getOutlines());
        pdfOutline.setTitle("Esquema de Prueba");
        pdfOutline.setItalic(true);
        pdfOutline.setBold(true);

        // Establecer el número de página de destino
        pdfOutline.setAction(new GoToAction(pdfDocument.getPages().get_Item(2)));

        // Añadir un marcador en la colección de esquemas del documento.
        pdfDocument.getOutlines().add(pdfOutline);

        // Guardar el documento actualizado
        pdfDocument.save(_dataDir + "AddBookmark_out.pdf");
    }
```


## Añadir un Marcador Hijo al Documento PDF

Los marcadores pueden estar anidados, indicando una relación jerárquica con marcadores padre e hijo. Este artículo explica cómo añadir un marcador hijo, es decir, un marcador de segundo nivel, a un PDF.

Para añadir un marcador hijo a un archivo PDF, primero añade un marcador padre:

1. Abre un documento.
1. Añade un marcador a la [OutlineItemCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/OutlineItemCollection), definiendo sus propiedades.
1. Añade la OutlineItemCollection a la colección [OutlineCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/OutlineCollection) del objeto Document.

El marcador hijo se crea de la misma manera que el marcador padre, explicado anteriormente, pero se añade a la colección de Outlines del marcador padre.

Los siguientes fragmentos de código muestran cómo añadir un marcador hijo a un documento PDF.

```java
    public static void AddChildBookmark() {
        // Abrir documento
        Document pdfDocument = new Document(GetDataDir() + "AddChildBookmark.pdf");

        // Crear un objeto de marcador padre
        OutlineItemCollection pdfOutline = new OutlineItemCollection(pdfDocument.getOutlines());
        pdfOutline.setTitle("Parent Outline");
        pdfOutline.setItalic(true);
        pdfOutline.setBold(true);

        // Crear un objeto de marcador hijo
        OutlineItemCollection pdfChildOutline = new OutlineItemCollection(pdfDocument.getOutlines());
        pdfChildOutline.setTitle("Child Outline");
        pdfChildOutline.setItalic(true);
        pdfChildOutline.setBold(true);

        // Añadir marcador hijo en la colección de marcadores padre
        pdfOutline.add(pdfChildOutline);
        // Añadir marcador padre en la colección de contornos del documento.
        pdfDocument.getOutlines().add(pdfOutline);

        // Guardar salida
        pdfDocument.save(_dataDir + "AddChildBookmark_out.pdf");
    }
```


## Eliminar todos los marcadores de un documento PDF

Todos los marcadores en un PDF se mantienen en la colección [OutlineCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/OutlineCollection). Este artículo explica cómo eliminar todos los marcadores de un archivo PDF.

Para eliminar todos los marcadores de un archivo PDF:

1. Llame al método Delete de la colección [OutlineCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/OutlineCollection).
1. Guarde el archivo modificado usando el método Save del objeto [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document).

Los siguientes fragmentos de código muestran cómo eliminar todos los marcadores de un documento PDF.

```java
    public static void DeleteAllBookmarksFromPDFDocument() {
        // Abrir documento
        Document pdfDocument = new Document(GetDataDir() + "DeleteAllBookmarks.pdf");

        // Eliminar todos los marcadores
        pdfDocument.getOutlines().delete();

        // Guardar archivo actualizado
        pdfDocument.save(_dataDir + "DeleteAllBookmarks_out.pdf");
    }
```

## Eliminar un marcador particular de un documento PDF

[Eliminar todos los adjuntos del documento PDF](https://docs.aspose.com/pdf/java/working-with-attachments/) mostró cómo eliminar todos los adjuntos de un archivo PDF. También es posible eliminar solo adjuntos específicos.

Para eliminar un marcador particular de un archivo PDF:

1. Pase el título del marcador como parámetro al método [Delete](https://reference.aspose.com/pdf/java/com.aspose.pdf/OutlineCollection#delete--) de la colección [OutlineCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/OutlineCollection).
1. Luego guarde el archivo actualizado con el método Save del objeto Document.

La clase [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) proporciona la colección [OutlineCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/OutlineCollection). El método [Delete](https://reference.aspose.com/pdf/java/com.aspose.pdf/OutlineCollection#delete--) elimina cualquier marcador con el título pasado al método.

Los siguientes fragmentos de código muestran cómo eliminar un marcador particular del documento PDF.

```java
    public static void DeleteParticularBookmarkPDFDocument() {
        // Abrir documento
        Document pdfDocument = new Document(GetDataDir() + "DeleteParticularBookmark.pdf");

        // Eliminar marcador específico por Título
        pdfDocument.getOutlines().delete("Child Outline");

        // Guardar archivo actualizado
        pdfDocument.save(_dataDir + "DeleteParticularBookmark_out.pdf");
    }
```