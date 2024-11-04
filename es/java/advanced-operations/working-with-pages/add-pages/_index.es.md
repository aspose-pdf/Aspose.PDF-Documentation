---
title: Add Pages in PDF 
linktitle: Agregar Páginas
type: docs
weight: 10
url: /java/add-pages/
description: Este artículo enseña cómo insertar (agregar) una página en la ubicación deseada de un archivo PDF. Aprenda a mover, eliminar (borrar) páginas de un archivo PDF utilizando la biblioteca Java.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Añadir o Insertar Página en un Archivo PDF

Aspose.PDF para Java te permite insertar una página en un documento PDF en cualquier ubicación del archivo, así como agregar páginas al final de un archivo PDF. Necesitas pasar la ubicación donde deseas insertar la página en blanco al método de inserción. Esta sección muestra cómo agregar páginas a un PDF con Aspose.PDF para Java.

### Insertar Página Vacía en un Archivo PDF en la Ubicación Deseada

El siguiente fragmento de código muestra cómo insertar una página vacía en un archivo PDF:

1. Crea un objeto de la clase [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) con el archivo PDF de entrada.

1. Llama al método Insert de la colección [PageCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/PageCollection) con el índice especificado.
1. Guarda el PDF de salida usando el método Save.

El siguiente fragmento de código te muestra cómo insertar una página en un archivo PDF.

```java
package com.aspose.pdf.examples;

import com.aspose.pdf.*;

public class ExampleAddPages {

    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

    public static void InsertEmptyPageInPDFFileAtDesiredLocation() {
        Document document = new Document();

        // Añadir página
        document.getPages().add();

        // Insertar una página vacía en un PDF
        document.getPages().insert(2);

        // Guardar PDF actualizado
        document.save(_dataDir + "InsertEmptyPage_out.pdf");
    }
```

En el ejemplo anterior, añadimos una página vacía con parámetros predeterminados. Si necesitas que el tamaño de la página sea el mismo que otra página en el documento, deberías añadir
unas pocas líneas de código:

```java
    public static void InsertEmptyPageInPDFFileAtDesiredLocation01() {
        Document document = new Document();

        // Añadir página
        Page page1 = document.getPages().add();

        // Insertar una página vacía en un PDF
        Page page2 = document.getPages().insert(2);
        ;
        // copiar parámetros de la página desde la página 1
        page2.setArtBox(page1.getArtBox());
        page2.setBleedBox(page1.getBleedBox());
        page2.setCropBox(page1.getCropBox());
        page2.setMediaBox(page1.getMediaBox());
        page2.setTrimBox(page1.getTrimBox());

        // Guardar PDF actualizado
        document.save(_dataDir + "InsertEmptyPage_out.pdf");
    }
```


### Agregar una Página Vacía al Final de un Archivo PDF

A veces, deseas asegurarte de que un documento termine en una página vacía. Este tema explica cómo insertar una página vacía al final del documento PDF.

Para insertar una página vacía al final de un archivo PDF:

1. Crea un objeto de la clase [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) con el archivo PDF de entrada.
1. Llama al método Add de la colección [PageCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/PageCollection), sin ningún parámetro.
1. Guarda el PDF de salida utilizando el método Save.

El siguiente fragmento de código te muestra cómo insertar una página vacía al final de un archivo PDF.

```java
public static void AddAnEmptyPageAtTheEndOfAPDFFile() {

        Document document = new Document();
        // Agregar página
        document.getPages().add();

        // Insertar una página vacía al final de un archivo PDF
        document.getPages().add();

        // Guardar PDF actualizado
        document.save(_dataDir + "InsertEmptyPageAtEnd_out.pdf");
    }

}
```