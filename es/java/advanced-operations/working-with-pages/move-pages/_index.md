---
title: Mover Páginas de PDF
linktitle: Mover Páginas
type: docs
weight: 20
url: es/java/move-pages/
description: Intenta mover páginas a la ubicación deseada o al final de un archivo PDF utilizando Aspose.PDF para Java.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Mover una Página de un Documento PDF a Otro

Este tema explica cómo mover una página de un documento PDF al final de otro documento usando Java.
Para mover una página debemos:

1. Crear un objeto de la clase [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) con el archivo PDF de origen.
1. Crear un objeto de la clase [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) con el archivo PDF de destino.
1. Obtener la página de la colección [PageCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/class-use/PageCollection).
1. Agregar la página al documento de destino.
1. Guardar el PDF de salida utilizando el método Save.
1. Eliminar la página en el documento de origen.
1. Guardar el PDF de origen utilizando el método Save.

El siguiente fragmento de código te muestra cómo mover una página.

```java
package com.aspose.pdf.examples;

import com.aspose.pdf.*;

public class ExampleMovePDFPages {

  private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

  public static void MovePage() {
    String srcFileName = _dataDir + "<enter file name>";
    String dstFileName = _dataDir + "<enter file name>";
    Document srcDocument = new Document();
    Document dstDocument = new Document();
    Page page = srcDocument.getPages().get_Item(2);
    dstDocument.getPages().add(page);
    // Guardar archivo de salida
    dstDocument.save(srcFileName);
    srcDocument.getPages().delete(2);
    srcDocument.save(dstFileName);
  }
```

## Mover varias páginas de un documento PDF a otro

1. Crear un objeto de clase [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) con el archivo PDF de origen.
1. Crear un objeto de clase [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) con el archivo PDF de destino.
1. Definir un array con los números de página a mover.

1. Ejecutar un bucle a través del array:
    1. Obtener la página de la [PageCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/class-use/PageCollection) de la colección.
    1. Añadir la página al documento de destino.
1. Guardar el PDF de salida usando el método Save.
1. Eliminar la página en el documento de origen usando el array.
1. Guardar el PDF de origen usando el método Save.

El siguiente fragmento de código muestra cómo insertar una página vacía al final de un archivo PDF.

```java
  public static void MoveBunchPages() {
    String srcFileName = _dataDir + "<enter file name>";
    String dstFileName = _dataDir + "<enter file name>";
    Document srcDocument = new Document(srcFileName);
    Document dstDocument = new Document();

    Integer[] pages = { 1, 3 };
    for (int pageIndex : pages) {
      Page page = srcDocument.getPages().get_Item(pageIndex);
      dstDocument.getPages().add(page);
    }
    // Guardar archivos de salida
    dstDocument.save(srcFileName);
    srcDocument.getPages().delete(pages);

    srcDocument.save(dstFileName);
  }
```

## Mover una página a una nueva ubicación en el documento PDF actual

1. Cree un objeto de la clase [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) con el archivo PDF de origen.
1. Obtenga la página de la colección de [PageCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/class-use/PageCollection).
1. Agregue la página a la nueva ubicación (por ejemplo, al final).
1. Elimine la página en la ubicación anterior.
1. Guarde el PDF de salida usando el método Save.

```java
  public static void MovePagesInOnePDF() {
    String srcFileName = _dataDir + "<enter file name>";
    String dstFileName = _dataDir + "<enter file name>";

    Document srcDocument = new Document(srcFileName);
    Page page = srcDocument.getPages().get_Item(2);
    srcDocument.getPages().add(page);
    srcDocument.getPages().delete(2);

    // Guardar archivo de salida
    srcDocument.save(dstFileName);
  }
}
```