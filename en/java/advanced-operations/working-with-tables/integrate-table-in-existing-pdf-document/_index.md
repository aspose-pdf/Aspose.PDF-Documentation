---
title: Integrate PDF Tables with Data Sources in Java
linktitle: Integrate Table
type: docs
weight: 30
url: /java/integrate-table/
description: Learn how to integrate PDF tables with structured data sources such as CSV files in Java.
lastmod: "2026-06-09"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Build PDF tables from structured data with Java
Abstract: This article explains how to integrate PDF tables with external data using Aspose.PDF for Java. It covers reading CSV data, selecting specific columns, building a styled Table object from the parsed rows, and rendering the result into a PDF document.
---
The Java example builds PDF tables from CSV data without relying on external dataframe libraries.

## Build a table from CSV rows

Use this example when selected CSV columns should be transformed into a styled PDF table.

1. Create a [Table](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/table/) and configure its borders.
1. Detect the required column indexes from the CSV header row.
1. Add the header row and the requested number of data rows, then return the table.

```java
public static Table createTableFromCsv(List<String[]> rows, int maxRows) {
    Table table = new Table();
    table.setBorder(new BorderInfo(BorderSide.All, 1, Color.getLightGray()));
    table.setDefaultCellBorder(new BorderInfo(BorderSide.Bottom, 1, Color.getLightGray()));

    String[] header = rows.get(0);
    int[] selectedColumns = findColumns(header, "city", "country", "population", "iso3");

    Row headerRow = table.getRows().add();
    headerRow.setRowBroken(false);
    for (int columnIndex : selectedColumns) {
        Cell cell = headerRow.getCells().add(header[columnIndex]);
        cell.setBackgroundColor(Color.getLightGray());
    }

    int limit = Math.min(maxRows, rows.size() - 1);
    for (int rowIndex = 1; rowIndex <= limit; rowIndex++) {
        Row row = table.getRows().add();
        String[] rowData = rows.get(rowIndex);
        for (int columnIndex : selectedColumns) {
            row.getCells().add(columnIndex < rowData.length ? rowData[columnIndex] : "");
        }
    }

    return table;
}
```

## Create a PDF from CSV data

Use this example when CSV input should be rendered as a PDF table document.

1. Read the CSV rows from the input file.
1. Preview a subset of the parsed rows in the console.
1. Create a PDF [Document](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/document/), add the generated table, and save the output file.

```java
public static void createPdfFromCsv(Path inputFile, Path outputFile, int maxRows) throws Exception {
    List<String[]> rows = readCsv(inputFile);
    for (int i = 0; i < Math.min(20, rows.size()); i++) {
        System.out.println(String.join(" | ", rows.get(i)));
    }

    try (Document document = new Document()) {
        Page page = document.getPages().add();
        page.getParagraphs().add(createTableFromCsv(rows, maxRows));
        document.save(outputFile.toString());
    }
}
```

## Find CSV column indexes by name

Use this helper when specific named columns must be located in the CSV header row.

1. Iterate through the requested column names.
1. Search the header row for matching indexes.
1. Return the collected column positions.

```java
private static int[] findColumns(String[] header, String... names) {
    int[] indexes = new int[names.length];
    for (int i = 0; i < names.length; i++) {
        indexes[i] = 0;
        for (int j = 0; j < header.length; j++) {
            if (names[i].equals(header[j])) {
                indexes[i] = j;
                break;
            }
        }
    }
    return indexes;
}
```

## Read CSV rows from a file

Use this helper when the CSV source should be loaded into memory before table generation.

1. Read all lines from the input file.
1. Split each line with the CSV parser helper.
1. Return the collected row values.

```java
private static List<String[]> readCsv(Path inputFile) throws Exception {
    List<String[]> rows = new ArrayList<>();
    for (String line : Files.readAllLines(inputFile)) {
        rows.add(splitCsvLine(line));
    }
    return rows;
}
```

## Split one CSV line into values

Use this helper when a CSV row may contain quoted values and escaped quote characters.

1. Iterate through the characters in the line.
1. Track whether the parser is currently inside quoted text.
1. Build the final value list and return it as an array.

```java
private static String[] splitCsvLine(String line) {
    List<String> values = new ArrayList<>();
    StringBuilder current = new StringBuilder();
    boolean inQuotes = false;
    for (int i = 0; i < line.length(); i++) {
        char ch = line.charAt(i);
        if (ch == '"') {
            if (inQuotes && i + 1 < line.length() && line.charAt(i + 1) == '"') {
                current.append('"');
                i++;
            } else {
                inQuotes = !inQuotes;
            }
        } else if (ch == ',' && !inQuotes) {
            values.add(current.toString());
            current.setLength(0);
        } else {
            current.append(ch);
        }
    }
    values.add(current.toString());
    return values.toArray(String[]::new);
}
```
