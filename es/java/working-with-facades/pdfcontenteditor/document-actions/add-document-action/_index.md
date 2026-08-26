---
title: Agregar acción de documento
linktitle: Add Document Action
type: docs
weight: 10
url: /java/add-document-action/
description: Aprenda cómo agregar una acción de apertura de documento a un PDF en Java usando la fachada PdfContentEditor en Aspose.PDF.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: Agregar una acción de apertura de documento a un PDF en Java
Abstract: This article shows how to bind a PDF, attach a JavaScript action to the document-open event, and save the updated document using the PdfContentEditor facade in Aspose.PDF for Java.
---
## Add a document-open action

1. Bind the source PDF to the `PdfContentEditor` facade.
2. Call `addDocumentAdditionalAction(...)` with the `DOCUMENT_OPEN` event and the JavaScript action text.
3. Save the updated PDF document.

```java
public static void addDocumentAction(Path inputFile, Path outputFile) {
    PdfContentEditor editor = new PdfContentEditor();
    try {
        editor.bindPdf(inputFile.toString());
        editor.addDocumentAdditionalAction(PdfContentEditor.DOCUMENT_OPEN, "app.alert('Document opened with PdfContentEditor action');");
        editor.save(outputFile.toString());
    } finally {
        editor.close();
    }
}
```
