---
title: Set Field Alignment Vertical
type: docs
weight: 30
url: /java/set-field-alignment-vertical/
description: Learn how to set vertical alignment for a PDF form field in Java using the FormEditor facade in Aspose.PDF.
lastmod: "2026-06-03"
TechArticle: true
AlternativeHeadline: Set vertical alignment for a PDF form field in Java
Abstract: This article shows how to bind an existing PDF, set vertical field alignment, and save the updated document using the FormEditor facade in Aspose.PDF for Java.
---
## Set vertical field alignment

1. Bind the source PDF to the `FormEditor` facade.
2. Call `setFieldAlignmentV(...)` for the target field and desired vertical alignment constant.
3. Save the updated document.

```java
public static void setFieldAlignmentVertical(Path inputFile, Path outputFile) {
    FormEditor editor = new FormEditor();
    try {
        editor.bindPdf(inputFile.toString());
        editor.setFieldAlignmentV("First Name", FormFieldFacade.ALIGN_BOTTOM);
        editor.save(outputFile.toString());
    } finally {
        editor.close();
    }
}
```
