---
title: Create ComboBox Field
type: docs
weight: 30
url: /java/create-combobox-field/
description: Learn how to add a combo box field to a PDF document in Java using the FormEditor facade in Aspose.PDF.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: Create a combo box field in a PDF with Java
Abstract: This article shows how to bind an existing PDF, add a combo box field, populate it with items, and save the modified document using the FormEditor facade in Aspose.PDF for Java.
---
Use `FormEditorExamples.createComboBoxField(...)` to create a combo box and add selectable items.

## Create a combo box field

1. Bind the source PDF to the `FormEditor` facade.
2. Add the combo box field with its default value and target rectangle.
3. Add the selectable combo box items.
4. Save the updated document.

```java
public static void createComboBoxField(Path inputFile, Path outputFile) {
    FormEditor editor = new FormEditor();
    try {
        editor.bindPdf(inputFile.toString());
        editor.addField(FieldType.ComboBox, "combobox1", "Australia", 1, 230, 498, 350, 514);
        editor.addListItem("combobox1", new String[] {"Australia", "Australia"});
        editor.addListItem("combobox1", new String[] {"New Zealand", "New Zealand"});
        editor.save(outputFile.toString());
    } finally {
        editor.close();
    }
}
```
