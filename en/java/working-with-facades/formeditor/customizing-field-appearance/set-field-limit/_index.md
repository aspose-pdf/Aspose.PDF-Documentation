---
title: Set Field Limit
type: docs
weight: 50
url: /java/set-field-limit/
description: Learn how to set a maximum character limit for a PDF form field in Java using the FormEditor facade in Aspose.PDF.
lastmod: "2026-06-03"
TechArticle: true
AlternativeHeadline: Set a character limit for a PDF form field in Java
Abstract: This article shows how to bind an existing PDF, set the maximum character limit of a field, and save the updated document using the FormEditor facade in Aspose.PDF for Java.
---
## Set a field character limit

1. Bind the source PDF to the `FormEditor` facade.
2. Call `setFieldLimit(...)` for the target field and maximum character count.
3. Save the updated document.

```java
public static void setFieldLimit(Path inputFile, Path outputFile) {
    FormEditor editor = new FormEditor();
    try {
        editor.bindPdf(inputFile.toString());
        editor.setFieldLimit("First Name", 15);
        editor.save(outputFile.toString());
    } finally {
        editor.close();
    }
}
```
