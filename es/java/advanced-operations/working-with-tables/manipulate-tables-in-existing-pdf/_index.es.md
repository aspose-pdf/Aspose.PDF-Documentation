---
title: Manipulate Tables in existing PDF
linktitle: Manipulate Tables
type: docs
weight: 30
url: /java/manipulate-tables-in-existing-pdf/
description: Manipule las tablas en un archivo PDF existente y reemplace la tabla antigua con una nueva en el documento PDF con Aspose.PDF para Java.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Manipular tablas en un PDF existente

Una de las primeras características admitidas por Aspose.PDF para Java es su capacidad para trabajar con tablas y ofrece un gran soporte para agregar tablas en archivos PDF que se generan desde cero o en cualquier archivo PDF existente.
 Tienes también la capacidad de integrar la tabla con la base de datos (DOM) para crear tablas dinámicas basadas en el contenido de la base de datos. En esta nueva versión, hemos implementado una nueva característica de búsqueda y análisis de tablas simples que ya existen en la página de un documento PDF. Una nueva clase llamada **Aspose.PDF.Text.TableAbsorber** proporciona estas capacidades. El uso de TableAbsorber es muy similar a la clase existente TextFragmentAbsorber.

El siguiente fragmento de código muestra los pasos para actualizar el contenido en una celda de tabla en particular.

```java
package com.aspose.pdf.examples;

import com.aspose.pdf.*;

public class ExampleManipulate {

    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

    public static void ManipulateTables() {

        // Cargar archivo PDF existente
        Document pdfDocument = new Document(_dataDir + "input.pdf");
        // Crear objeto TableAbsorber para encontrar tablas
        TableAbsorber absorber = new TableAbsorber();

        // Visitar la primera página con el absorber
        absorber.visit(pdfDocument.getPages().get_Item(1));

        // Obtener acceso a la primera tabla en la página, su primera celda y fragmentos de texto en ella
        TextFragment fragment = absorber.getTableList().get(0).getRowList().get(0).getCellList().get(0)
                .getTextFragments().get_Item(1);

        // Cambiar el texto del primer fragmento de texto en la celda
        fragment.setText("hola mundo");

        pdfDocument.save(_dataDir + "ManipulateTable_out.pdf");
    }
```

## Reemplazar la tabla antigua con una nueva en un documento PDF

En caso de que necesites encontrar una tabla en particular y reemplazarla con la deseada, puedes usar el método Replace() de la clase [TableAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/TableAbsorber) para hacerlo.

El siguiente ejemplo demuestra la funcionalidad para reemplazar la tabla dentro de un documento PDF:

```java
public static void ReplaceOldTableWithNew() {

        // Cargar documento PDF existente
        Document pdfDocument = new Document(_dataDir + "Table_input2.pdf");

        // Crear objeto TableAbsorber para encontrar tablas
        TableAbsorber absorber = new TableAbsorber();

        Page page = pdfDocument.getPages().get_Item(1);

        // Visitar la primera página con el absorbedor
        absorber.visit(page);

        // Obtener la primera tabla en la página
        AbsorbedTable table = absorber.getTableList().get(0);

        // Crear nueva tabla
        Table newTable = new Table();
        newTable.setColumnWidths("100 100 100");
        newTable.setDefaultCellBorder (new BorderInfo(BorderSide.All, 1F));

        Row row = newTable.getRows().add();
        row.getCells().add("Col 1");
        row.getCells().add("Col 2");
        row.getCells().add("Col 3");

        // Reemplazar la tabla con la nueva
        absorber.replace(page, table, newTable);

        // Guardar documento
        pdfDocument.save(_dataDir + "TableReplaced_out.pdf");
        
    }

}
```