---
title: Eliminar Imágenes de un Archivo PDF
linktitle: Eliminar Imágenes
type: docs
weight: 20
url: es/java/delete-images-from-pdf-file/
description: Esta sección explica cómo eliminar imágenes de un archivo PDF usando Aspose.PDF para Java.
lastmod: "2021-06-05"
---

Para eliminar una imagen de un archivo PDF, simplemente use el método delete(..) de la colección Images.

1. Cree un objeto Document y abra el archivo PDF de entrada.
1. Obtenga la página que contiene la imagen de la colección [Pages](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page) del objeto [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document).
1. Las imágenes se encuentran en la colección Images, que se encuentra en la colección [Resources](https://reference.aspose.com/pdf/java/com.aspose.pdf/Resources) de la página.
1. Elimine una imagen con el método Delete de la colección Images.
1. Guarde el resultado utilizando el método Save del objeto Document.

El siguiente fragmento de código muestra cómo eliminar una imagen de un archivo PDF.

```java
package com.aspose.pdf.examples;

import com.aspose.pdf.Color;
import com.aspose.pdf.Document;
import com.aspose.pdf.FontRepository;
import com.aspose.pdf.FontStyles;
import com.aspose.pdf.HorizontalAlignment;
import com.aspose.pdf.PageNumberStamp;

public class ExampleDeleteImages {

    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

    public static void ExampleAddPageNumber() {

        // Abrir documento
        Document pdfDocument = new Document(_dataDir + "PageNumberStamp.pdf");

        // Crear sello de número de página
        PageNumberStamp pageNumberStamp = new PageNumberStamp();

        // Si el sello es de fondo
        pageNumberStamp.setBackground(false);
        pageNumberStamp.setFormat("Page # of " + pdfDocument.getPages().size());
        pageNumberStamp.setBottomMargin (10);
        pageNumberStamp.setHorizontalAlignment ( HorizontalAlignment.Center);
        pageNumberStamp.setStartingNumber(1);
        // Establecer propiedades de texto
        pageNumberStamp.getTextState().setFont (FontRepository.findFont("Arial"));
        pageNumberStamp.getTextState().setFontSize (14.0F);
        pageNumberStamp.getTextState().setFontStyle (FontStyles.Bold);        
        pageNumberStamp.getTextState().setForegroundColor (Color.getAqua());

        // Añadir sello a una página en particular
        pdfDocument.getPages().get_Item(1).addStamp(pageNumberStamp);

        _dataDir = _dataDir + "PageNumberStamp_out.pdf";
        // Guardar documento de salida
        pdfDocument.save(_dataDir);

    }
}
```