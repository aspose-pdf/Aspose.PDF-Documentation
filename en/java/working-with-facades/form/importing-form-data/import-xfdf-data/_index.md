---
title: Import XFDF Data
linktitle: Import XFDF Data
type: docs
weight: 20
url: /java/import-xfdf-data/
description: Learn how to import XFDF form data into a PDF form with Java using the Form facade in Aspose.PDF.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: Import AcroForm data from XFDF in Java
Abstract: This article shows how to bind a PDF form, import field values from an XFDF stream, and save the updated document with the Form facade in Aspose.PDF for Java.
---
Use `FormExamples.importXfdf(...)` to populate a form from XFDF data.

```java
public static void importXfdf(Path inputFile, Path dataFile, Path outputFile) throws Exception {
    Form form = new Form();
    try (InputStream inputStream = Files.newInputStream(dataFile)) {
        form.bindPdf(inputFile.toString());
        form.importXfdf(inputStream);
        form.save(outputFile.toString());
    } finally {
        form.close();
    }
}
```
