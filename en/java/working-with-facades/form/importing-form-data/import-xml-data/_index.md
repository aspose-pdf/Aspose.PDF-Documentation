---
title: Import XML Data
type: docs
weight: 40
url: /java/import-xml-data/
description: Learn how to import XML form data into a PDF form with Java using the Form facade in Aspose.PDF.
lastmod: "2026-06-03"
TechArticle: true
AlternativeHeadline: Import AcroForm data from XML in Java
Abstract: This article shows how to bind a PDF form, import field values from an XML stream, and save the updated document with the Form facade in Aspose.PDF for Java.
---
Use `FormExamples.importXml(...)` to populate a form from XML data.

```java
public static void importXml(Path inputFile, Path dataFile, Path outputFile) throws Exception {
    Form form = new Form();
    try (InputStream inputStream = Files.newInputStream(dataFile)) {
        form.bindPdf(inputFile.toString());
        form.importXml(inputStream);
        form.save(outputFile.toString());
    } finally {
        form.close();
    }
}
```
