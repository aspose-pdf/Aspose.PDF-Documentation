---
title: Eliminar Tablas de un PDF existente
linktitle: Eliminar Tablas
type: docs
weight: 40
url: es/java/remove-tables-from-existing-pdf/
description: Aspose.PDF para Java le permite eliminar una o varias tablas de su documento PDF.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

{{% alert color="primary" %}}

Aspose.PDF para Java ofrece las capacidades para insertar/crear una tabla dentro de un documento PDF mientras se genera desde cero o también puede agregar el objeto de la tabla en cualquier documento PDF existente. Sin embargo, puede que tenga un requisito para [Manipular Tablas en un PDF existente](https://docs.aspose.com/pdf/java/manipulate-tables-in-existing-pdf/) donde puede actualizar los contenidos en las celdas existentes de la tabla. Sin embargo, puede que se encuentre con un requisito para eliminar objetos de tabla de un documento PDF existente.

{{% /alert %}}

Para eliminar las tablas, necesitamos usar la clase [TableAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/TableAbsorber) para obtener las tablas en el PDF existente y luego llamar al método [Remove](https://reference.aspose.com/pdf/java/com.aspose.pdf/TableAbsorber#remove-com.aspose.pdf.AbsorbedTable-).

## Eliminar Tabla del documento PDF

Hemos añadido una nueva función, es decir, Remove(), a la clase existente [TableAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/TableAbsorber) para eliminar una tabla del documento PDF. Una vez que el absorbedor encuentra con éxito las tablas en la página, se vuelve capaz de eliminarlas. Por favor, consulte el siguiente fragmento de código que muestra cómo eliminar una tabla de un documento PDF:

```java
package com.aspose.pdf.examples;

import com.aspose.pdf.*;

public class ExampleRemoveTable {
    
    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

    public static void RemoveTable() {
        // Cargar documento PDF existente
        Document pdfDocument = new Document(_dataDir + "Table_input.pdf");

        // Crear objeto TableAbsorber para encontrar tablas
        TableAbsorber absorber = new TableAbsorber();

        // Visitar la primera página con el absorbedor
        absorber.visit(pdfDocument.getPages().get_Item(1));

        // Obtener la primera tabla en la página
        AbsorbedTable table = absorber.getTableList().get(0);

        // Eliminar la tabla
        absorber.remove(table);

        // Guardar PDF
        pdfDocument.save(_dataDir + "Table_out.pdf");
    }  
```


## Eliminar Múltiples Tablas de un Documento PDF

A veces, un documento PDF puede contener más de una tabla y puede que tengas el requerimiento de eliminar múltiples tablas de él. Para eliminar múltiples tablas de un documento PDF, utiliza el siguiente fragmento de código:

```java
    public static void RemoveMultipleTable() {
        // Cargar documento PDF existente
        Document pdfDocument = new Document(_dataDir + "Table_input2.pdf");

        // Crear objeto TableAbsorber para encontrar tablas
        TableAbsorber absorber = new TableAbsorber();

        // Visitar la segunda página con el absorber
        absorber.visit(pdfDocument.getPages().get_Item(2));

        // Recorrer la copia de la colección y eliminar tablas
        for (AbsorbedTable table : absorber.getTableList())
            absorber.remove(table);

        // Guardar documento
        pdfDocument.save(_dataDir + "Table2_out.pdf");
    }
}
```