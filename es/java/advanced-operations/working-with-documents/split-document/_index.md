---
title: Dividir PDF programáticamente
linktitle: Dividir archivos PDF
type: docs
weight: 60
url: es/java/split-document/
description: Este tema muestra cómo dividir páginas PDF en archivos PDF individuales en sus aplicaciones Java.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

{{% alert color="primary" %}}

Puede dividir archivos PDF usando Aspose.PDF y obtener los resultados en línea en este enlace: [products.aspose.app/pdf/splitter](https://products.aspose.app/pdf/splitter)

{{% /alert %}}

Este tema muestra cómo dividir páginas PDF con Aspose.PDF para Java en archivos PDF individuales en sus aplicaciones Java. Para dividir páginas PDF en archivos PDF de una sola página usando Java, se pueden seguir los siguientes pasos:

1. Recorrer las páginas del documento PDF a través de la colección [PageCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/pagecollection) del objeto [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document).

1. Para cada iteración, crea un nuevo objeto Document y añade el objeto individual [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page) al documento vacío.
1. Guarda el nuevo PDF usando el método Save.

El siguiente fragmento de código Java te muestra cómo dividir las páginas de un PDF en archivos PDF individuales.

```java
package com.aspose.pdf.examples;

import com.aspose.pdf.*;

public class ExampleSplit {
    // La ruta al directorio de documentos.
    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

    public static void Split() {
        
        // Abrir documento
        Document pdfDocument = new Document(_dataDir + "SplitToPages.pdf");

        int pageCount = 1;

        // Recorrer todas las páginas
        for(Page pdfPage : pdfDocument.getPages())
        {
            Document newDocument = new Document();
            newDocument.getPages().add(pdfPage);
            newDocument.save(_dataDir + "page_" + pageCount + "_out" + ".pdf");
            pageCount++;
        }
    }

}
```