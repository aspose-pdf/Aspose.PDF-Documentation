---
title: Move Field
linktitle: Move Field
type: docs
weight: 30
url: /java/move-field/
description: Learn how to move an existing form field in a PDF document in Java using the FormEditor facade in Aspose.PDF.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: Move a PDF form field to a new position in Java
Abstract: This article shows how to bind an existing PDF, move a field to new coordinates, and save the updated document using the FormEditor facade in Aspose.PDF for Java.
---
## Move a field

1. Bind the source PDF to the `FormEditor` facade.
2. Call `moveField(...)` with the target field name and new rectangle coordinates.
3. Save the updated document.

```java
public static void moveField(Path inputFile, Path outputFile) {
    FormEditor editor = new FormEditor();
    try {
        editor.bindPdf(inputFile.toString());
        editor.moveField("Country", 200, 600, 280, 620);
        editor.save(outputFile.toString());
    } finally {
        editor.close();
    }
}
```
