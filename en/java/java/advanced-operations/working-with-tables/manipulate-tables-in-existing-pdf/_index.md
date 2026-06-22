---
title: Manipulate Tables in Existing PDF Documents
linktitle: Manipulate Tables
type: docs
weight: 40
url: /java/manipulating-tables/
description: Learn how to inspect and modify tables in existing PDF documents using Java.
lastmod: "2026-06-09"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Inspect and modify existing PDF tables with Java
Abstract: This article explains how to manipulate tables already present in PDF documents using Aspose.PDF for Java. It covers locating tables with TableAbsorber, updating text inside a cell, and replacing a detected table with a new Table object.
---
Use `TableAbsorber` when you need to locate existing tables and update their content.

## Replace text inside a table cell

Use this example when the text in a detected cell should be updated without rebuilding the whole table.

1. Open the source PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) and visit the page with [TableAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/tableabsorber/).
1. Validate that the target table and cell text fragments exist.
1. Replace the cell text and save the updated document.

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

## Replace a detected table with a new table

Use this example when the original table should be fully replaced by a newly constructed one.

1. Open the source PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) and detect tables on the page.
1. Create a new [Table](https://reference.aspose.com/pdf/java/com.aspose.pdf/table/) with the desired structure.
1. Replace the absorbed table and save the output PDF.

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
