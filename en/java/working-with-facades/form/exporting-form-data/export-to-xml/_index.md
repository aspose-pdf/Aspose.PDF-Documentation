---
title: Export to XML
linktitle: Export to XML
type: docs
weight: 40
url: /java/export-to-xml/
description: Learn how to export PDF form data to XML in Java using the Form facade in Aspose.PDF.
lastmod: "2026-05-28"
TechArticle: true
AlternativeHeadline: Export AcroForm data to XML in Java
Abstract: This article shows how to bind a PDF form and export its field values to an XML stream with the Form facade in Aspose.PDF for Java.
---
Use `FormExamples.exportXml(...)` to save form field data as XML.

```java
public static void exportXml(Path inputFile, Path outputFile) throws Exception {
    Form form = new Form();
    try (OutputStream outputStream = Files.newOutputStream(outputFile)) {
        form.bindPdf(inputFile.toString());
        form.exportXml(outputStream);
    } finally {
        form.close();
    }
}
```
