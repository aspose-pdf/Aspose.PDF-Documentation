---
title: Manipular tablas en documentos PDF existentes
linktitle: Manipular tablas
type: docs
weight: 40
url: /java/manipulating-tables/
description: Aprenda a inspeccionar y modificar tablas en documentos PDF existentes utilizando Java.
lastmod: "2026-06-09"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Inspeccionar y modificar tablas PDF existentes con Java
Abstract: Este artículo explica cómo manipular tablas que ya están presentes en documentos PDF usando Aspose.PDF para Java. Cubre la localización de tablas con TableAbsorber, la actualización de texto dentro de una celda y el reemplazo de una tabla detectada con un nuevo objeto Tabla.
---
Utilice `TableAbsorber` cuando necesite localizar tablas existentes y actualizar su contenido.


## 
Reemplazar texto dentro de una celda de tabla



Utilice este ejemplo cuando el texto de una celda detectada deba actualizarse sin reconstruir toda la tabla.


1. 
Abra el [Documento] PDF de origen(https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) y visite la página con [TableAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/tableabsorber/).

1. 
Valide que existan la tabla de destino y los fragmentos de texto de la celda.
1. Reemplace el texto de la celda y guarde el documento actualizado.


```java
public static void replaceCells(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        TableAbsorber absorber = new TableAbsorber();
        absorber.visit(document.getPages().get_Item(1));

        if (absorber.getTableList().isEmpty()) {
            throw new IllegalStateException("No tables were found on page 1.");
        }
        if (absorber.getTableList().get(0).getRowList().get(0).getCellList().get(0).getTextFragments().size() == 0) {
            throw new IllegalStateException("The target cell has no text fragments.");
        }

        absorber.getTableList().get(0).getRowList().get(0).getCellList().get(0)
                .getTextFragments().get_Item(1).setText("New Value");
        document.save(outputFile.toString());
    }
}
```

## 
Reemplazar una tabla detectada con una nueva tabla



Utilice este ejemplo cuando la tabla original deba reemplazarse por completo por una recién construida.


1. 
Abra el [Documento] PDF de origen(https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) y detecte tablas en la página.

1. 
Cree una nueva [Tabla](https://reference.aspose.com/pdf/java/com.aspose.pdf/table/) con la estructura deseada.
1. Reemplace la tabla absorbida y guarde el PDF de salida.

```java
public static void replaceTable(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        TableAbsorber absorber = new TableAbsorber();
        absorber.visit(document.getPages().get_Item(1));

        if (absorber.getTableList().isEmpty()) {
            throw new IllegalStateException("No tables were found on page 1.");
        }

        AbsorbedTable oldTable = absorber.getTableList().get(0);
        Table newTable = new Table();
        newTable.setColumnWidths("100 100 100");
        newTable.setDefaultCellBorder(new BorderInfo(BorderSide.All, 1.0f));

        Row row = newTable.getRows().add();
        row.getCells().add("Col 1");
        row.getCells().add("Col 2");
        row.getCells().add("Col 3");
        row = newTable.getRows().add();
        row.getCells().add("Col 12");
        row.getCells().add("Col 22");
        row.getCells().add("Col 32");

        absorber.replace(document.getPages().get_Item(1), oldTable, newTable);
        document.save(outputFile.toString());
    }
}
```
