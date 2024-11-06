---
title: Rotar Páginas de PDF programáticamente
linktitle: Rotar Páginas de PDF
type: docs
weight: 60
url: es/java/rotate-pages/
description: Cambiar la orientación de la página y ajustar el contenido de la página a la nueva orientación de página utilizando Java.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Cambiar la Orientación de la Página

Este artículo describe cómo actualizar o cambiar la orientación de las páginas en un archivo PDF existente.

Aspose.PDF para Java tiene la función de cambiar la orientación de la página de horizontal a vertical y viceversa. Para cambiar la orientación de la página, configure el [MediaBox](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page#setMediaBox-com.aspose.pdf.Rectangle-) de la página usando el siguiente fragmento de código.

También puede cambiar la orientación de la página configurando el ángulo de rotación utilizando el método Rotate().

```java
package com.aspose.pdf.examples;

import com.aspose.pdf.*;

public class ExampleRotatePDFPages  {

    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

    public static void RotatePages() {
        // Abrir documento
        Document pdfDocument = new Document(_dataDir + "sample2.pdf");

        for (Page page : pdfDocument.getPages())
        {            
            // Rectángulo r = page.getMediaBox();
            // double newHeight = r.getWidth();
            // double newWidth = r.getHeight();
            // double newLLX = r.getLLX();
            // // Debemos mover la página hacia arriba para compensar el cambio de tamaño de página
            // // (el borde inferior de la página es 0,0 y la información generalmente se coloca desde la
            // // parte superior de la página. Por eso movemos el borde inferior hacia arriba en la diferencia entre
            // // la altura antigua y la nueva.
            // double newLLY = r.getLLY() + (r.getHeight() - newHeight);
            // page.setMediaBox (new Rectangle(newLLX, newLLY, newLLX + newWidth, newLLY + newHeight));
            // // A veces también necesitamos configurar CropBox (si se configuró en el archivo original)
            // page.setCropBox(new Rectangle(newLLX, newLLY, newLLX + newWidth, newLLY + newHeight));

            // Configurando el ángulo de rotación de la página
            page.setRotate(Rotation.on90);
        }

        _dataDir = _dataDir + "ChangeOrientation_out.pdf";
        // Guardar el archivo de salida
        pdfDocument.save(_dataDir);
    }    
}
```