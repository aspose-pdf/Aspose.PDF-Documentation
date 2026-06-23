---
title: Extract Data from Table in PDF with Java
linktitle: Extract Data from Table
type: docs
weight: 40
url: /java/extract-data-from-table-in-pdf/
description: Learn how to extract table data from PDF files with Aspose.PDF for Java and export detected tables for further processing.
lastmod: "2026-06-16"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: How to Extract Data from Table in PDF via Java
Abstract: This article explains how to extract and process table data from PDF documents with Aspose.PDF for Java. It shows how to scan pages with `TableAbsorber`, read rows and cells from detected tables, limit extraction to a specific annotated region, and export the result to Excel.
---
## Extract tables from PDF

Use `TableAbsorber` to find tables on each page and iterate through rows, cells, text fragments, and text segments.

1. Open the source PDF in a [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) instance.
1. Iterate through the document [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) objects because tables are detected page by page.
1. Create a [TableAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/tableabsorber/) for each page and call `visit(page)` to populate the detected table list.
1. Iterate through the detected [AbsorbedTable](https://reference.aspose.com/pdf/java/com.aspose.pdf/absorbedtable/), [AbsorbedRow](https://reference.aspose.com/pdf/java/com.aspose.pdf/absorbedrow/), [AbsorbedCell](https://reference.aspose.com/pdf/java/com.aspose.pdf/absorbedcell/), [TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf/textfragment/), and `TextSegment` objects.
1. Build the extracted row text from the fragment content and print the table data.

```java
public static void extractTablesFromPdf(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (Page page : document.getPages()) {
            TableAbsorber absorber = new TableAbsorber();
            absorber.visit(page);

            for (AbsorbedTable table : absorber.getTableList()) {
                System.out.println("Table");
                for (AbsorbedRow row : table.getRowList()) {
                    StringBuilder rowText = new StringBuilder();
                    for (AbsorbedCell cell : row.getCellList()) {
                        if (rowText.length() > 0) {
                            rowText.append("|");
                        }
                        StringBuilder cellText = new StringBuilder();
                        for (TextFragment fragment : cell.getTextFragments()) {
                            StringBuilder fragmentText = new StringBuilder();
                            for (TextSegment segment : fragment.getSegments()) {
                                fragmentText.append(segment.getText());
                            }
                            if (cellText.length() > 0) {
                                cellText.append("|");
                            }
                            cellText.append(fragmentText);
                        }
                        rowText.append(cellText);
                    }
                    System.out.println(rowText);
                }
            }
        }
    }
}
```

## Extract a table from a specific marked area

This example finds a square annotation, compares its rectangle to each detected table, and outputs only tables inside the marked region.

1. Open the source PDF in a [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) instance.
1. Get the target [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) and locate the square [Annotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/annotation/) that marks the extraction region.
1. Create a [TableAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/tableabsorber/) and call `visit(page)` to detect tables on that page.
1. Compare each detected [AbsorbedTable](https://reference.aspose.com/pdf/java/com.aspose.pdf/absorbedtable/) [Rectangle](https://reference.aspose.com/pdf/java/com.aspose.pdf/rectangle/) with the annotation rectangle bounds.
1. Iterate through the matching [AbsorbedRow](https://reference.aspose.com/pdf/java/com.aspose.pdf/absorbedrow/) and [AbsorbedCell](https://reference.aspose.com/pdf/java/com.aspose.pdf/absorbedcell/) objects and reconstruct the row text.
1. Print the table data for the marked region only.

```java
public static void extractTableFromSpecificArea(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        Page page = document.getPages().get_Item(1);

        Annotation squareAnnotation = null;
        for (Annotation annotation : page.getAnnotations()) {
            if (annotation.getAnnotationType() == AnnotationType.Square) {
                squareAnnotation = annotation;
                break;
            }
        }

        if (squareAnnotation == null) {
            System.out.println("No square annotation found.");
            return;
        }

        TableAbsorber absorber = new TableAbsorber();
        absorber.visit(page);

        for (AbsorbedTable table : absorber.getTableList()) {
            Rectangle tableRect = table.getRectangle();
            Rectangle annotationRect = squareAnnotation.getRect();

            boolean isInRegion = annotationRect.getLLX() < tableRect.getLLX()
                    && annotationRect.getLLY() < tableRect.getLLY()
                    && annotationRect.getURX() > tableRect.getURX()
                    && annotationRect.getURY() > tableRect.getURY();

            if (isInRegion) {
                for (AbsorbedRow row : table.getRowList()) {
                    StringBuilder rowText = new StringBuilder();
                    for (AbsorbedCell cell : row.getCellList()) {
                        if (rowText.length() > 0) {
                            rowText.append("|");
                        }
                        StringBuilder cellText = new StringBuilder();
                        for (TextFragment fragment : cell.getTextFragments()) {
                            StringBuilder fragmentText = new StringBuilder();
                            for (TextSegment segment : fragment.getSegments()) {
                                fragmentText.append(segment.getText());
                            }
                            if (cellText.length() > 0) {
                                cellText.append("|");
                            }
                            cellText.append(fragmentText);
                        }
                        rowText.append(cellText);
                    }
                    System.out.println(rowText);
                }
            }
        }
    }
}
```

## Export tables to Excel

1. Open the source PDF in a [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) instance.
1. Create [ExcelSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/excelsaveoptions/) for the export.
1. Set the Excel output format to `XLSX` so detected table layout is written as an Excel workbook.
1. Call `document.save(outputFile.toString(), excelSave)` to export the document in Excel format.

```java
public static void exportTablesToExcel(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        ExcelSaveOptions excelSave = new ExcelSaveOptions();
        excelSave.setFormat(ExcelSaveOptions.ExcelFormat.XLSX);
        document.save(outputFile.toString(), excelSave);
    }
}
```
