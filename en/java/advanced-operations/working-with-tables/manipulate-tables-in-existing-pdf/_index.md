---
title: Manipulate Tables in Existing PDF Documents
linktitle: Manipulate Tables
type: docs
weight: 40
url: /java/manipulating-tables/
description: Learn how to inspect and modify tables in existing PDF documents using Java.
lastmod: "2026-05-27"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Inspect and modify existing PDF tables with Java
Abstract: This article explains how to manipulate tables already present in PDF documents using Aspose.PDF for Java. It covers locating tables with TableAbsorber, updating text inside a cell, and replacing a detected table with a new Table object.
---
## Replace text inside a detected table cell

```java
public static void replaceCells(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        TableAbsorber absorber = new TableAbsorber();
        absorber.visit(document.getPages().get_Item(1));

        absorber.getTableList().get(0).getRowList().get(0).getCellList().get(0)
                .getTextFragments().get_Item(1).setText("New Value");
        document.save(outputFile.toString());
    }
}
```

The full example also validates that a table exists and that the target cell contains text fragments before updating the value.

## Replace a whole table

```java
public static void replaceTable(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        TableAbsorber absorber = new TableAbsorber();
        absorber.visit(document.getPages().get_Item(1));

        AbsorbedTable oldTable = absorber.getTableList().get(0);
        Table newTable = new Table();
        newTable.setColumnWidths("100 100 100");
        newTable.setDefaultCellBorder(new BorderInfo(BorderSide.All, 1.0f));

        Row row = newTable.getRows().add();
        row.getCells().add("Col 1");
        row.getCells().add("Col 2");
        row.getCells().add("Col 3");

        absorber.replace(document.getPages().get_Item(1), oldTable, newTable);
        document.save(outputFile.toString());
    }
}
```
