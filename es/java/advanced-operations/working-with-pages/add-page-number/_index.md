---
title: Añadir Número de Página al PDF
linktitle: Añadir Número de Página
type: docs
weight: 100
url: es/java/add-page-number/
description: Aspose.PDF para Java te permite añadir una Estampa de Número de Página a tu archivo PDF usando la clase PageNumber Stamp.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Todos los documentos deben tener números de página. El número de página facilita al lector localizar diferentes partes del documento.
**Aspose.PDF para Java** te permite añadir números de página con PageNumberStamp.

{{% alert color="primary" %}}

Prueba en línea. Puedes comprobar la calidad de la conversión de Aspose.PDF y ver los resultados en línea en este enlace [products.aspose.app/pdf/page-number](https://products.aspose.app/pdf/page-number)

{{% /alert %}}

Puedes usar la clase [PageNumberStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/PageNumberStamp) para añadir una estampa de número de página en un documento PDF.
 El documento de la clase [PageNumberStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/PageNumberStamp) proporciona métodos para crear un sello basado en números de página como formato, márgenes, alineaciones, número de inicio, etc. Para agregar un sello de número de página, necesitas crear un objeto [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) y un objeto [PageNumberStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/PageNumberStamp) con las propiedades requeridas. Después, puedes llamar al método [addStamp(..)](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page#addStamp-com.aspose.pdf.Stamp-) de la clase [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page) para agregar el sello en el archivo PDF. También puedes establecer los atributos de fuente del sello del número de página.

El siguiente fragmento de código te muestra cómo agregar números de página en un archivo PDF.

```java
package com.aspose.pdf.examples;

import com.aspose.pdf.Color;
import com.aspose.pdf.Document;
import com.aspose.pdf.FontRepository;
import com.aspose.pdf.FontStyles;
import com.aspose.pdf.HorizontalAlignment;
import com.aspose.pdf.PageNumberStamp;

public class ExampleAddPageNumberToPDF {

    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

    public static void ExampleAddPageNumber() {

        // Abrir documento
        Document pdfDocument = new Document(_dataDir + "PageNumberStamp.pdf");

        // Crear sello de número de página
        PageNumberStamp pageNumberStamp = new PageNumberStamp();

        // Si el sello es de fondo
        pageNumberStamp.setBackground(false);
        pageNumberStamp.setFormat("Página # de " + pdfDocument.getPages().size());
        pageNumberStamp.setBottomMargin(10);
        pageNumberStamp.setHorizontalAlignment(HorizontalAlignment.Center);
        pageNumberStamp.setStartingNumber(1);
        // Establecer propiedades del texto
        pageNumberStamp.getTextState().setFont(FontRepository.findFont("Arial"));
        pageNumberStamp.getTextState().setFontSize(14.0F);
        pageNumberStamp.getTextState().setFontStyle(FontStyles.Bold);        
        pageNumberStamp.getTextState().setForegroundColor(Color.getAqua());

        // Agregar sello a una página en particular
        pdfDocument.getPages().get_Item(1).addStamp(pageNumberStamp);

        _dataDir = _dataDir + "PageNumberStamp_out.pdf";
        // Guardar documento de salida
        pdfDocument.save(_dataDir);

    }
}
```