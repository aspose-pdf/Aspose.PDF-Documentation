---
title: Add Rubber Stamp
type: docs
weight: 10
url: /java/add-rubber-stamp/
description: Learn how to add a rubber stamp annotation to a PDF document in Java using the PdfContentEditor facade in Aspose.PDF.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: Add a rubber stamp to a PDF in Java
Abstract: This article shows how to bind a PDF, create a rubber stamp annotation with label text and color, and save the updated document using the PdfContentEditor facade in Aspose.PDF for Java.
---
## Add a rubber stamp

1. Bind the source PDF to the `PdfContentEditor` facade.
2. Call `createRubberStamp(...)` with the page number, rectangle, title, contents, and color.
3. Save the updated PDF document.

```java
public static void addRubberStamp(Path inputFile, Path outputFile) {
    PdfContentEditor editor = new PdfContentEditor();
    try {
        editor.bindPdf(inputFile.toString());
        editor.createRubberStamp(1, new Rectangle(120, 450, 180, 60), "Approved", "Approved by reviewer", Color.GREEN);
        editor.save(outputFile.toString());
    } finally {
        editor.close();
    }
}
```
