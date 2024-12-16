---
title: Combinar PDF programáticamente
linktitle: Combinar archivos PDF
type: docs
weight: 50
url: /es/java/merge-pdf-documents/
description: Esta página explica cómo combinar documentos PDF en un solo archivo PDF con Java.
lastmod: "2021-06-05"
---

Ahora, combinar archivos pdf es una de las tareas más demandadas.
Este artículo muestra cómo combinar múltiples archivos PDF en un solo documento PDF usando Aspose.PDF para Java. El ejemplo está escrito en Java, pero la API se puede usar en otros lenguajes de programación. Los archivos PDF se combinan de tal manera que el primero se une al final del otro documento.

## Combinar archivos PDF usando Java

{{% alert color="primary" %}}

Puede combinar archivos PDF usando Aspose.PDF y obtener los resultados en línea en este enlace: [products.aspose.app/pdf/merger](https://products.aspose.app/pdf/merger)

{{% /alert %}}

Para concatenar dos archivos PDF:

1. Cree dos objetos [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/class-use/Document), cada uno conteniendo uno de los archivos PDF de entrada.

1. Luego, llame al método Add de la colección [PageCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/class-use/PageCollection) para el objeto Document al que desea agregar el otro archivo PDF.
1. Pase la colección PageCollection del segundo objeto Document al método Add de la primera colección PageCollection.
1. Finalmente, guarde el archivo PDF de salida utilizando el método Save.

El siguiente fragmento de código muestra cómo concatenar archivos PDF con Java.

```java
package com.aspose.pdf.examples;

import com.aspose.pdf.*;

public class ExampleMerge {
    // La ruta al directorio de documentos.
    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

    public static void Merge() {
        
        // Abrir el primer documento
        Document pdfDocument1 = new Document(_dataDir + "Concat1.pdf");
        // Abrir el segundo documento
        Document pdfDocument2 = new Document(_dataDir + "Concat2.pdf");

        // Agregar páginas del segundo documento al primero
        pdfDocument1.getPages().add(pdfDocument2.getPages());

        // Guardar el archivo de salida concatenado
        pdfDocument1.save(_dataDir+"ConcatenatePdfFiles_out.pdf");

    }

}
```