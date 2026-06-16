---
title: Export to XFDF
linktitle: Export to XFDF
type: docs
weight: 20
url: /java/export-to-xfdf/
description: Learn how to export PDF form field data to XFDF in Java using the Form facade in Aspose.PDF.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: Export AcroForm data to XFDF in Java
Abstract: This article shows how to bind a PDF form and export its field values to an XFDF stream with the Form facade in Aspose.PDF for Java.
---
Use `FormExamples.exportXfdf(...)` to write form field data as XFDF.

```java
public static void exportXfdf(Path inputFile, Path outputFile) throws Exception {
    Form form = new Form();
    try (OutputStream outputStream = Files.newOutputStream(outputFile)) {
        form.bindPdf(inputFile.toString());
        form.exportXfdf(outputStream);
    } finally {
        form.close();
    }
}
```
