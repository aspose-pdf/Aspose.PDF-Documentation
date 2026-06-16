---
title: Set Field Appearance
linktitle: Set Field Appearance
type: docs
weight: 40
url: /java/set-field-appearance/
description: Learn how to change the visual appearance flags of a PDF form field in Java using the FormEditor facade in Aspose.PDF.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: Change PDF form field appearance flags in Java
Abstract: This article shows how to bind an existing PDF, apply an appearance flag to a field, and save the updated document using the FormEditor facade in Aspose.PDF for Java.
---
## Set field appearance flags

1. Bind the source PDF to the `FormEditor` facade.
2. Call `setFieldAppearance(...)` for the target field and chosen annotation flag.
3. Save the updated document.

```java
public static void setFieldAppearance(Path inputFile, Path outputFile) {
    FormEditor editor = new FormEditor();
    try {
        editor.bindPdf(inputFile.toString());
        editor.setFieldAppearance("First Name", AnnotationFlags.Hidden);
        editor.save(outputFile.toString());
    } finally {
        editor.close();
    }
}
```
