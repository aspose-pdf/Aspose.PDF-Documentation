---
title: Export to FDF
type: docs
weight: 10
url: /java/export-to-fdf/
description: Learn how to export PDF form field values to FDF in Java using the Form facade in Aspose.PDF.
lastmod: "2026-06-03"
TechArticle: true
AlternativeHeadline: Export AcroForm data to FDF in Java
Abstract: This article shows how to bind a PDF form and export its field data to an FDF stream with the Form facade in Aspose.PDF for Java.
---
Use `FormExamples.exportFdf(...)` when you need to serialize AcroForm field data as FDF.

```java
public static void exportFdf(Path inputFile, Path outputFile) throws Exception {
    Form form = new Form();
    try (OutputStream outputStream = Files.newOutputStream(outputFile)) {
        form.bindPdf(inputFile.toString());
        form.exportFdf(outputStream);
    } finally {
        form.close();
    }
}
```
