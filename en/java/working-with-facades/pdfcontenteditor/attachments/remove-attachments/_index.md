---
title: Remove Attachments
type: docs
weight: 50
url: /java/remove-attachments/
description: Learn how to remove all document attachments from a PDF in Java using the PdfContentEditor facade in Aspose.PDF.
lastmod: "2026-06-03"
TechArticle: true
AlternativeHeadline: Remove all PDF attachments in Java
Abstract: This article shows how to bind a PDF, delete all document attachments, and save the updated file using the PdfContentEditor facade in Aspose.PDF for Java.
---
## Remove all attachments

1. Bind the source PDF to the `PdfContentEditor` facade.
2. Call `deleteAttachments()` to remove every embedded attachment.
3. Save the updated PDF document.

```java
public static void removeAttachments(Path inputFile, Path outputFile) {
    PdfContentEditor editor = new PdfContentEditor();
    try {
        editor.bindPdf(inputFile.toString());
        editor.deleteAttachments();
        editor.save(outputFile.toString());
    } finally {
        editor.close();
    }
}
```
