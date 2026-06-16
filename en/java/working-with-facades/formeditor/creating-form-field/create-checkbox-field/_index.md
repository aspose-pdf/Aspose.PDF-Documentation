---
title: Create CheckBox Field
linktitle: Create CheckBox Field
type: docs
weight: 20
url: /java/create-checkbox-field/
description: Learn how to add a check box form field to a PDF document in Java using the FormEditor facade in Aspose.PDF.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: Create a checkbox field in a PDF with Java
Abstract: This article shows how to bind an existing PDF, add a check box field at a specified position, and save the modified document using the FormEditor facade in Aspose.PDF for Java.
---
Use `FormEditorExamples.createCheckBoxField(...)` to add a check box field to a PDF form.

## Create a check box field

1. Bind the source PDF to the `FormEditor` facade.
2. Add the check box field with `FieldType.CheckBox`, the field name, caption, page, and rectangle.
3. Save the updated document.

```java
public static void createCheckBoxField(Path inputFile, Path outputFile) {
    FormEditor editor = new FormEditor();
    try {
        editor.bindPdf(inputFile.toString());
        editor.addField(FieldType.CheckBox, "checkbox1", "Check Box 1", 1, 240, 498, 256, 514);
        editor.save(outputFile.toString());
    } finally {
        editor.close();
    }
}
```
