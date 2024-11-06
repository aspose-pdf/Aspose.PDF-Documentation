---
title: Establecer Tamaño de Imagen
linktitle: Establecer Tamaño de Imagen
type: docs
weight: 80
url: es/java/set-image-size/
description: Esta sección describe cómo establecer el tamaño de la imagen en un archivo PDF usando la biblioteca Java.
lastmod: "2021-06-05"
---

Es posible establecer el tamaño de una imagen que se está añadiendo a un archivo PDF. Para establecer el tamaño, puedes usar los métodos [setFixWidth](https://reference.aspose.com/pdf/java/com.aspose.pdf/Image#setFixWidth-double-) y [setFixHeight](https://reference.aspose.com/pdf/java/com.aspose.pdf/Image#setFixHeight-double-) de la clase com.aspose.pdf.Image.

El siguiente fragmento de código demuestra cómo establecer el tamaño de una imagen:

```java
package com.aspose.pdf.examples;

import com.aspose.pdf.*;

public class ExampleSetImageSize {
    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

    public static void Replace() {
        // Instanciar objeto Document
        Document doc = new Document();
        // añadir página a la colección de páginas del archivo PDF
        Page page = doc.getPages().add();
        // Crear una instancia de imagen
        Image img = new Image();
        // Establecer ancho y alto de la imagen en puntos
        img.setFixWidth (100);
        img.setFixHeight (100);
        // Establecer tipo de imagen como SVG
        img.setFileType (ImageFileType.Svg);
        // Ruta para el archivo fuente
        img.setFile (_dataDir + "aspose-logo.jpg");
        page.getParagraphs().add(img);
        // Establecer propiedades de la página
        page.getPageInfo().setWidth(800);
        page.getPageInfo().setHeight(800);        
        // guardar el archivo PDF resultante
        doc.save(_dataDir + "SetImageSize_out.pdf");
    }
}
```