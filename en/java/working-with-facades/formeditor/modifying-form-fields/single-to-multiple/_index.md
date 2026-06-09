---
title: Single To Multiple
type: docs
weight: 60
url: /java/single-to-multiple/
description: Learn how to convert a single-line text field into a multi-line field in a PDF document in Java using the FormEditor facade in Aspose.PDF.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: Convert a single-line PDF field to multi-line in Java
Abstract: This article shows how to bind an existing PDF, convert a single-line field to a multi-line field, and save the updated document using the FormEditor facade in Aspose.PDF for Java.
---
## Convert a single-line field to multiple lines

1. Bind the source PDF to the `FormEditor` facade.
2. Call `single2Multiple(...)` for the target field name.
3. Save the updated document.

```java
public static void singleToMultiple(Path inputFile, Path outputFile) {
    FormEditor editor = new FormEditor();
    try {
        editor.bindPdf(inputFile.toString());
        editor.single2Multiple("City");
        editor.save(outputFile.toString());
    } finally {
        editor.close();
    }
}
```
