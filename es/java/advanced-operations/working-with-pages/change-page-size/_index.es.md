---
title: Cambiar el Tamaño de Página de PDF Programáticamente
linktitle: Cambiar Tamaño de Página
type: docs
weight: 50
url: /java/change-page-size/
description: Cambia el tamaño de página de tu archivo PDF usando la biblioteca Java.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Cambiar el Tamaño de Página de PDF

Aspose.PDF para Java te permite cambiar el tamaño de página de un PDF con simples líneas de código en tus aplicaciones Java. Este tema explica cómo actualizar/cambiar las dimensiones de página (tamaño) de un archivo PDF existente.

La clase [Page](https://reference.aspose.com/pdf//java/com.aspose.pdf/page) contiene el método SetPageSize(...) que te permite establecer el tamaño de la página. El fragmento de código a continuación actualiza las dimensiones de la página en unos pocos pasos sencillos:

1. Cargar el archivo PDF de origen.
1. Obtener las páginas en el objeto [PageCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/pagecollection).
1. Obtener una página dada.
1. Llamar al método SetPageSize(..) para actualizar sus dimensiones.

1. Llama al método Save(..) de la clase [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) para generar el archivo PDF con dimensiones de página actualizadas.

{{% alert color="primary" %}}

Tenga en cuenta que las propiedades de altura y anchura usan puntos como unidad básica, donde 1 pulgada = 72 puntos y 1 cm = 1/2.54 pulgada = 0.3937 pulgada = 28.3 puntos.

{{% /alert %}}

El siguiente fragmento de código muestra cómo cambiar las dimensiones de la página PDF al tamaño A4.

```java
package com.aspose.pdf.examples;

import com.aspose.pdf.*;

public class ExampleChangePDFPageSize {
    // La ruta al directorio de documentos.
    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

    public static void ChangePDFPageSize() {
        
        // Abrir el primer documento
        Document pdfDocument = new Document(_dataDir + "sample.pdf");
                
        // Obtener la colección de páginas
        PageCollection pageCollection = pdfDocument.getPages();

        // Obtener una página en particular
        Page pdfPage = pageCollection.get_Item(1);

        // Establecer el tamaño de la página como A4 (11.7 x 8.3 in) y en Aspose.Pdf, 1 pulgada = 72 puntos
        // Entonces las dimensiones A4 en puntos serán (842.4, 597.6)
        pdfPage.setPageSize(597.6, 842.4);

        _dataDir = _dataDir + "UpdateDimensions_out.pdf";
        
        // Guardar el documento actualizado
        pdfDocument.save(_dataDir);
    }
```


## Obtener Tamaño de Página de PDF

Puede leer el tamaño de página de un archivo PDF existente usando Aspose.PDF para Java. El siguiente ejemplo de código muestra cómo leer las dimensiones de una página PDF usando Java.

```java
    public static void GetPDFPageSize() {
        
        // Abrir el primer documento
        Document pdfDocument = new Document(_dataDir + "sample.pdf");
                
        // Agrega una página en blanco al documento PDF
        Page page = pdfDocument.getPages().size() > 0 ? pdfDocument.getPages().get_Item(1) : pdfDocument.getPages().add();
        
        // Obtener información de altura y ancho de la página
        System.out.println(page.getPageRect(true).getWidth() + ":" + page.getPageRect(true).getHeight());
        
        // Rotar página en un ángulo de 90 grados
        page.setRotate (Rotation.on90);

        // Obtener información de altura y ancho de la página
        System.out.println(page.getPageRect(true).getWidth() + ":" + page.getPageRect(true).getHeight());
        
        // Guardar el documento actualizado
        _dataDir = _dataDir + "UpdateDimensions_out.pdf";
        pdfDocument.save(_dataDir);
    }

}
```