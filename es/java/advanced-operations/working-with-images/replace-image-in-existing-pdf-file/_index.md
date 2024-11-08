---
title: Reemplazar Imagen en un Archivo PDF Existente
linktitle: Reemplazar Imagen
type: docs
weight: 70
url: /es/java/replace-image-in-existing-pdf-file/
description: Esta sección describe cómo reemplazar una imagen en un archivo PDF existente utilizando una biblioteca Java.
lastmod: "2021-06-05"
---

El método [Replace](https://reference.aspose.com/pdf/java/com.aspose.pdf/XImageCollection#replace-int-java.io.InputStream-) de la colección [XImages](https://reference.aspose.com/pdf/java/com.aspose.pdf/XImageCollection) te permite reemplazar una imagen en un archivo PDF existente.

La colección de Imágenes se puede encontrar en la colección de Recursos de una página. Para reemplazar una imagen:

1. Abre el archivo PDF usando el objeto Document.
2. Reemplaza una imagen en particular, guarda el archivo PDF actualizado usando el método Save del objeto Document.

El siguiente fragmento de código te muestra cómo reemplazar una imagen en un archivo PDF.

```java
package com.aspose.pdf.examples;

import java.io.FileInputStream;
import java.io.FileNotFoundException;

import com.aspose.pdf.Document;

public class ExampleReplaceImage {
    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";
    public static void Replace() {
        // Abrir documento
        Document pdfDocument = new Document("input.pdf");
        // Reemplazar una imagen en particular
        try {
            pdfDocument.getPages().get_Item(1).getResources().getImages().replace(1, new FileInputStream("lovely.jpg"));
        } catch (FileNotFoundException e) {
            // TODO Auto-generated catch block
            e.printStackTrace();
        }
        // Guardar el archivo PDF actualizado
        pdfDocument.save(_dataDir + "output.pdf");
    }
}
```