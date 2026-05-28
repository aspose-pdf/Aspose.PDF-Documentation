---
title: Import FDF Data
type: docs
weight: 10
url: /java/import-fdf-data/
description: Learn how to import FDF form data into a PDF form with Java using the Form facade in Aspose.PDF.
lastmod: "2026-05-28"
TechArticle: true
AlternativeHeadline: Import AcroForm data from FDF in Java
Abstract: This article shows how to bind a PDF form, import field values from an FDF stream, and save the updated document with the Form facade in Aspose.PDF for Java.
---
Use `FormExamples.importFdf(...)` to apply field values from an FDF file.

```java
public static void importFdf(Path inputFile, Path dataFile, Path outputFile) throws Exception {
    Form form = new Form();
    try (InputStream inputStream = Files.newInputStream(dataFile)) {
        form.bindPdf(inputFile.toString());
        form.importFdf(inputStream);
        form.save(outputFile.toString());
    } finally {
        form.close();
    }
}
```
