---
title: Create TextBox Field
linktitle: Create TextBox Field
type: docs
weight: 10
url: /java/create-textbox-field/
description: Learn how to add text box fields to a PDF document in Java using the FormEditor facade in Aspose.PDF.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: Create text form fields in a PDF with Java
Abstract: This article shows how to bind an existing PDF, add text fields with default values, and save the modified document using the FormEditor facade in Aspose.PDF for Java.
---
Use `FormEditorExamples.createTextBoxField(...)` to add text fields to a PDF form.

## Create text box fields

1. Bind the source PDF to the `FormEditor` facade.
2. Add each text field with `FieldType.Text`, the field name, default value, page number, and rectangle.
3. Save the updated document.

```java
public static void createTextBoxField(Path inputFile, Path outputFile) {
    FormEditor editor = new FormEditor();
    try {
        editor.bindPdf(inputFile.toString());
        editor.addField(FieldType.Text, "first_name", "Alexander", 1, 50, 570, 150, 590);
        editor.addField(FieldType.Text, "last_name", "Smith", 1, 235, 570, 330, 590);
        editor.save(outputFile.toString());
    } finally {
        editor.close();
    }
}
```
