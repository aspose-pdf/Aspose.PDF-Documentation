---
title: Copy Outer Field
type: docs
weight: 80
url: /java/copy-outer-field/
description: Learn how to copy a form field from one PDF document into another in Java using the FormEditor facade in Aspose.PDF.
lastmod: "2026-06-03"
TechArticle: true
AlternativeHeadline: Copy a PDF form field between documents in Java
Abstract: This article shows how to create a destination PDF, bind it to the FormEditor facade, copy a field from another document, and save the result using Aspose.PDF for Java.
---
## Copy a field from another PDF

1. Create a destination PDF with at least one page.
2. Bind the destination PDF to the `FormEditor` facade.
3. Call `copyOuterField(...)` with the source document path, field name, target page, and coordinates.
4. Save the updated destination document.

```java
public static void copyOuterField(Path inputFile, Path outputFile) {
    try (Document document = new Document()) {
        document.getPages().add();
        document.save(outputFile.toString());
    }

    FormEditor editor = new FormEditor();
    try {
        editor.bindPdf(outputFile.toString());
        editor.copyOuterField(inputFile.toString(), "First Name", 1, 200, 600);
        editor.save(outputFile.toString());
    } finally {
        editor.close();
    }
}
```
