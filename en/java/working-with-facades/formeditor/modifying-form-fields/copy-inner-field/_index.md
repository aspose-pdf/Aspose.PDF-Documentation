---
title: Copy Inner Field
type: docs
weight: 70
url: /java/copy-inner-field/
description: Learn how to copy a form field to a new position within the same PDF document in Java using the FormEditor facade in Aspose.PDF.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: Copy a PDF form field within the same document in Java
Abstract: This article shows how to bind an existing PDF, duplicate a field to another page and position, and save the updated document using the FormEditor facade in Aspose.PDF for Java.
---
## Copy a field inside the same PDF

1. Bind the source PDF to the `FormEditor` facade.
2. Call `copyInnerField(...)` with the source field name, new field name, page, and coordinates.
3. Save the updated document.

```java
public static void copyInnerField(Path inputFile, Path outputFile) {
    FormEditor editor = new FormEditor();
    try {
        editor.bindPdf(inputFile.toString());
        editor.copyInnerField("First Name", "First Name Copy", 2, 200, 600);
        editor.save(outputFile.toString());
    } finally {
        editor.close();
    }
}
```
