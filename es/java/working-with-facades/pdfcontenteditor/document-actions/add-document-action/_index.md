---
title: Agregar acción de documento
linktitle: Agregar acción de documento
type: docs
weight: 10
url: /java/add-document-action/
description: Aprenda cómo agregar una acción de apertura de documento a un PDF en Java usando la fachada PdfContentEditor en Aspose.PDF.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: Agregar una acción de apertura de documento a un PDF en Java
Abstract: Este artículo muestra cómo vincular un PDF, adjuntar una acción de JavaScript al evento de apertura del documento y guardar el documento actualizado usando la fachada PdfContentEditor en Aspose.PDF para Java.
---
## Agregar una acción de apertura de documento


1. Vincule el PDF de origen a la fachada `PdfContentEditor`.

2. Llame a `addDocumentAdditionalAction(...)` con el evento `DOCUMENT_OPEN` y el texto de acción de JavaScript.

3. Guarde el documento PDF actualizado.

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
