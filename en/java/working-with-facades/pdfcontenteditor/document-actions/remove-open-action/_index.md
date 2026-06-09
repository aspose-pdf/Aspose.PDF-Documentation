---
title: Remove Open Action
type: docs
weight: 20
url: /java/remove-open-action/
description: Learn how to remove the document open action from a PDF in Java using the PdfContentEditor facade in Aspose.PDF.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: Remove a PDF document-open action in Java
Abstract: This article shows how to bind a PDF, remove the document-open action, and save the updated document using the PdfContentEditor facade in Aspose.PDF for Java.
---
## Remove the document-open action

1. Bind the source PDF to the `PdfContentEditor` facade.
2. Call `removeDocumentOpenAction()`.
3. Save the updated PDF document.

```java
public static void removeOpenAction(Path inputFile, Path outputFile) {
    PdfContentEditor editor = new PdfContentEditor();
    try {
        editor.bindPdf(inputFile.toString());
        editor.removeDocumentOpenAction();
        editor.save(outputFile.toString());
    } finally {
        editor.close();
    }
}
```
