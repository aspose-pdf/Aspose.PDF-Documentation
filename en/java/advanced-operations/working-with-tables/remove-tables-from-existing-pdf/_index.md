---
title: Remove Tables from Existing PDF Documents
linktitle: Remove Tables
description: Learn how to remove one or more tables from existing PDF documents in Java.
lastmod: "2026-06-04"
type: docs
weight: 50
url: /java/removing-tables/
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Delete one or multiple tables from PDF files with Java
Abstract: This article explains how to remove tables from existing PDF documents using Aspose.PDF for Java. It introduces TableAbsorber for locating tables and demonstrates how to delete a single table or remove all detected tables from a page.
---
## Remove one table

1. Open the source PDF document.
1. Create a TableAbsorber and visit the target page or document.
1. Remove the extracted table from the page.
1. Save the updated PDF document.

```java
public static void removeOneTable(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        TableAbsorber absorber = new TableAbsorber();
        absorber.visit(document.getPages().get_Item(1));
        absorber.remove(absorber.getTableList().get(0));
        document.save(outputFile.toString());
    }
}
```

## Remove all tables

1. Open the source PDF document.
1. Create a TableAbsorber and visit the target page or document.
1. Remove the extracted table from the page.
1. Save the updated PDF document.

```java
public static void removeAllTables(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        TableAbsorber absorber = new TableAbsorber();
        absorber.visit(document.getPages().get_Item(1));
        List<AbsorbedTable> tables = new ArrayList<>(absorber.getTableList());
        for (AbsorbedTable table : tables) {
            absorber.remove(table);
        }
        document.save(outputFile.toString());
    }
}
```
