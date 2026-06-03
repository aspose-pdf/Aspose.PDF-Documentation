---
title: Set Field Alignment
type: docs
weight: 20
url: /java/set-field-alignment/
description: Learn how to set horizontal text alignment for a PDF form field in Java using the FormEditor facade in Aspose.PDF.
lastmod: "2026-06-03"
TechArticle: true
AlternativeHeadline: Set PDF form field alignment in Java
Abstract: This article shows how to bind an existing PDF, set horizontal field alignment, and save the updated document using the FormEditor facade in Aspose.PDF for Java.
---
## Set horizontal field alignment

1. Bind the source PDF to the `FormEditor` facade.
2. Call `setFieldAlignment(...)` for the target field and desired alignment constant.
3. Save the updated document.

```java
public static void setFieldAlignment(Path inputFile, Path outputFile) {
    FormEditor editor = new FormEditor();
    try {
        editor.bindPdf(inputFile.toString());
        editor.setFieldAlignment("First Name", FormFieldFacade.ALIGN_CENTER);
        editor.save(outputFile.toString());
    } finally {
        editor.close();
    }
}
```
