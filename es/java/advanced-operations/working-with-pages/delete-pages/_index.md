---
title: Eliminar páginas de PDF programáticamente 
linktitle: Eliminar páginas de PDF
type: docs
weight: 40
url: /es/java/delete-pages/
description: Puedes eliminar páginas de tu archivo PDF usando la biblioteca de Java.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Puedes eliminar páginas de un archivo PDF usando Aspose.PDF para Java. Para eliminar una página en particular de la [PageCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/pagecollection) simplemente llama al método delete() y especifica el índice de la página particular que deseas eliminar. Luego llama al método save para guardar el archivo PDF actualizado.

## Eliminar página de un archivo PDF

1. Llama al método Delete y especifica el índice de la página
1. Llama al método Save para guardar el archivo PDF actualizado
El siguiente fragmento de código muestra cómo eliminar una página en particular del archivo PDF usando Java.

```java
package com.aspose.pdf.examples;

import com.aspose.pdf.*;

public class ExampleDeletePage {

  private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

  public static void DeletePageFromPDFFile() {

    // Abrir documento
    Document pdfDocument = new Document(_dataDir + "sample.pdf");

    // Eliminar una página en particular
    pdfDocument.getPages().delete(2);

    _dataDir = _dataDir + "DeleteParticularPage_out.pdf";
    // Guardar PDF actualizado
    pdfDocument.save(_dataDir);    

  }
```