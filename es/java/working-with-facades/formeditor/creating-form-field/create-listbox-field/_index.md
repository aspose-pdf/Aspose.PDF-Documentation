---
title: Create ListBox Field
linktitle: Create ListBox Field
type: docs
weight: 40
url: /java/create-listbox-field/
description: Learn how to add a list box field to a PDF document in Java using the FormEditor facade in Aspose.PDF.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: Create a list box field in a PDF with Java
Abstract: This article shows how to bind an existing PDF, define list items, add a list box field, and save the modified document using the FormEditor facade in Aspose.PDF for Java.
---
Use `FormEditorExamples.createListBoxField(...)` to create a list box with predefined items.

## Create a list box field

1. Bind the source PDF to the `FormEditor` facade.
2. Define the available list items with `setItems(...)`.
3. Add the list box field with its default value and rectangle.
4. Save the updated document.

```java
public static void createListBoxField(Path inputFile, Path outputFile) {
    FormEditor editor = new FormEditor();
    try {
        editor.bindPdf(inputFile.toString());
        editor.setItems(new String[] {"Australia", "New Zealand", "Malaysia"});
        editor.addField(FieldType.ListBox, "listbox1", "Australia", 1, 230, 398, 350, 514);
        editor.save(outputFile.toString());
    } finally {
        editor.close();
    }
}
```
