---
title: Integrate PDF Tables with Data Sources in Java
linktitle: Integrate Table
type: docs
weight: 30
url: /java/integrate-table/
description: Learn how to integrate PDF tables with structured data sources such as CSV files in Java.
lastmod: "2026-05-27"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Build PDF tables from structured data with Java
Abstract: This article explains how to integrate PDF tables with external data using Aspose.PDF for Java. It covers reading CSV data, selecting specific columns, building a styled Table object from the parsed rows, and rendering the result into a PDF document.
---
The Java example builds PDF tables from CSV data without relying on external dataframe libraries.

## Create a table from CSV rows

1. Initialize the PDF document and any resources required by this example.
2. Build and configure the Aspose.PDF objects needed to create a table from CSV rows.
3. Save the output document or generated file.

```java
public static Table createTableFromCsv(List<String[]> rows, int maxRows) {
    Table table = new Table();
    table.setBorder(new BorderInfo(BorderSide.All, 1, Color.getLightGray()));
    table.setDefaultCellBorder(new BorderInfo(BorderSide.Bottom, 1, Color.getLightGray()));

    String[] header = rows.get(0);
    int[] selectedColumns = findColumns(header, "city", "country", "population", "iso3");

    Row headerRow = table.getRows().add();
    for (int columnIndex : selectedColumns) {
        Cell cell = headerRow.getCells().add(header[columnIndex]);
        cell.setBackgroundColor(Color.getLightGray());
    }

    return table;
}
```

## Create a PDF from CSV data

1. Initialize the PDF document and any resources required by this example.
2. Build and configure the Aspose.PDF objects needed to create a PDF from CSV data.
3. Save the output document or generated file.

```java
public static void createPdfFromCsv(Path inputFile, Path outputFile, int maxRows) throws Exception {
    List<String[]> rows = readCsv(inputFile);

    try (Document document = new Document()) {
        Page page = document.getPages().add();
        page.getParagraphs().add(createTableFromCsv(rows, maxRows));
        document.save(outputFile.toString());
    }
}
```


