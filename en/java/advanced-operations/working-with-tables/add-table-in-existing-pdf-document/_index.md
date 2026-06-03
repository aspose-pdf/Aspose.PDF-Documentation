---
title: Add Tables to PDF in Java
linktitle: Adding Tables
type: docs
weight: 10
url: /java/adding-tables/
description: Learn how to add and configure tables in existing PDF documents in Java.
lastmod: "2026-05-27"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Add and format tables in PDF documents with Java
Abstract: This article explains how to add and configure tables in PDF documents using Aspose.PDF for Java. It covers table creation, borders, margins, padding, row and column spans, AutoFit behavior, image insertion in cells, repeating rows and columns, HTML and LaTeX fragments, and multi-page rendering control.
---
Aspose.PDF for Java provides a rich `Table` API for building tables with layout and content customization.

## Create a simple table

1. Initialize the PDF document and any resources required by this example.
2. Build and configure the Aspose.PDF objects needed to create a simple table.
3. Save the output document or generated file.

```java
public static void createTable(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();
        Table table = new Table();
        table.setBorder(new BorderInfo(BorderSide.All, 5, Color.getLightGray()));
        table.setDefaultCellBorder(new BorderInfo(BorderSide.All, 5, Color.getLightGray()));
        for (int rowCount = 0; rowCount < 10; rowCount++) {
            Row row = table.getRows().add();
            row.getCells().add("Column (" + rowCount + ", 1)");
            row.getCells().add("Column (" + rowCount + ", 2)");
            row.getCells().add("Column (" + rowCount + ", 3)");
        }
        page.getParagraphs().add(table);
        document.save(outputFile.toString());
    }
}
```
