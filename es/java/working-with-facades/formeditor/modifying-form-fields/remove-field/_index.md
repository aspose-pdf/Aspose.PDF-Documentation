---
title: Remove Field
linktitle: Remove Field
type: docs
weight: 40
url: /java/remove-field/
description: Learn how to remove an existing form field from a PDF document in Java using the FormEditor facade in Aspose.PDF.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: Delete a PDF form field in Java
Abstract: This article shows how to bind an existing PDF, remove a specified field, and save the updated document using the FormEditor facade in Aspose.PDF for Java.
---
## Remove a field

1. Bind the source PDF to the `FormEditor` facade.
2. Call `removeField(...)` for the target field name.
3. Save the updated document.

```java
public static void removeField(Path inputFile, Path outputFile) {
    FormEditor editor = new FormEditor();
    try {
        editor.bindPdf(inputFile.toString());
        editor.removeField("Country");
        editor.save(outputFile.toString());
    } finally {
        editor.close();
    }
}
```
