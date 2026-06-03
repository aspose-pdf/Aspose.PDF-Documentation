---
title: Rename Field
type: docs
weight: 50
url: /java/rename-field/
description: Learn how to rename an existing form field in a PDF document in Java using the FormEditor facade in Aspose.PDF.
lastmod: "2026-06-03"
TechArticle: true
AlternativeHeadline: Rename a PDF form field in Java
Abstract: This article shows how to bind an existing PDF, rename a specified field, and save the updated document using the FormEditor facade in Aspose.PDF for Java.
---
## Rename a field

1. Bind the source PDF to the `FormEditor` facade.
2. Call `renameField(...)` with the current field name and the new field name.
3. Save the updated document.

```java
public static void renameField(Path inputFile, Path outputFile) {
    FormEditor editor = new FormEditor();
    try {
        editor.bindPdf(inputFile.toString());
        editor.renameField("City", "Town");
        editor.save(outputFile.toString());
    } finally {
        editor.close();
    }
}
```
