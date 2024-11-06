---
title: Extraer Imágenes de un Archivo PDF
linktitle: Extraer Imágenes
type: docs
weight: 30
url: es/java/extract-images-from-pdf-file/
description: Esta sección muestra cómo extraer imágenes de un archivo PDF usando una biblioteca Java.
lastmod: "2021-06-05"
---

Cada página contiene una colección de [Resources](https://reference.aspose.com/pdf/java/com.aspose.pdf/Resources), y esta, a su vez, contiene la colección de Imágenes, donde se guardan todas las imágenes de una página. El objeto [XImage](https://reference.aspose.com/pdf/java/com.aspose.pdf/XImage) obtiene una imagen dada en la colección de Imágenes.

Para extraer una imagen de una página:

Obtén la imagen de la colección de Imágenes usando el índice de imagen.
Usa el método save(..) del objeto [XImage](https://reference.aspose.com/pdf/java/com.aspose.pdf/XImage) para guardar la imagen extraída.

El siguiente fragmento de código muestra cómo extraer imágenes del archivo PDF.

```java
package com.aspose.pdf.examples;

import java.io.FileOutputStream;
import java.io.IOException;

import com.aspose.pdf.*;
import com.aspose.pdf.internal.html.rendering.image.ImageFormat;

public class ExampleExtractImages {

    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

    public static void ExtractImages() throws IOException {

        // Abrir documento
        Document pdfDocument = new Document(_dataDir + "ExtractImages.pdf");

        // Extraer una imagen particular
        XImage xImage = pdfDocument.getPages().get_Item(1).getResources().getImages().get_Item(1);

        FileOutputStream outputImage = new FileOutputStream(_dataDir + "output.jpg");

        // Guardar imagen de salida
        xImage.save(outputImage, ImageFormat.Jpeg);
        outputImage.close();

        // Guardar archivo PDF actualizado
        pdfDocument.save(_dataDir + "ExtractImages_out.pdf");
    }
}
```