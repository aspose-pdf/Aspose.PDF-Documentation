---
title: Import and Export Annotations using Java
linktitle: Import and Export Annotations
type: docs
weight: 80
url: /java/import-export-annotations/
description: Learn how to copy annotations from one PDF document into another PDF document using Aspose.PDF for Java.
lastmod: "2026-05-27"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Transfer PDF annotations between documents in Java.
Abstract: This article explains how to copy annotations from a source PDF and export them into a new PDF document using Aspose.PDF for Java. The workflow loads the source file, creates the destination document, adds a page, copies annotations from the first source page, and saves the result.
---
```java
public static void importExport(Path inputFile, Path outputFile) {
    try (Document sourceDocument = new Document(inputFile.toString());
         Document destinationDocument = new Document()) {
        Page page = destinationDocument.getPages().add();

        for (Annotation annotation : sourceDocument.getPages().get_Item(1).getAnnotations()) {
            page.getAnnotations().add(annotation, true);
        }

        destinationDocument.save(outputFile.toString());
    }
}
```
