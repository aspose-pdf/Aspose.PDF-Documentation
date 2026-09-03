---
title: Agregar acción de documento
linktitle: Agregar acción de documento
type: docs
weight: 10
url: /es/java/add-document-action/
description: Aprenda cómo agregar una acción de apertura de documento a un PDF en Java usando la fachada PdfContentEditor en Aspose.PDF.
lastmod: "2026-09-03"
TechArticle: true
AlternativeHeadline: Agregar una acción de apertura de documento a un PDF en Java
Abstract: Este artículo muestra cómo vincular un PDF, adjuntar una acción JavaScript al evento de apertura de documento y guardar el documento actualizado usando la fachada PdfContentEditor en Aspose.PDF for Java.
---
## Agregar una acción de apertura de documento

1. Vincula el PDF de origen a la `PdfContentEditor` fachada.
2. Llamar `addDocumentAdditionalAction(...)` con el `DOCUMENT_OPEN` evento y el texto de la acción JavaScript.
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
