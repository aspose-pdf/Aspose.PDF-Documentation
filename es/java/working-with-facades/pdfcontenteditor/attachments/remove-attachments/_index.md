---
title: Eliminar archivos adjuntos
linktitle: Eliminar archivos adjuntos
type: docs
weight: 50
url: /es/java/remove-attachments/
description: Aprenda cómo eliminar todos los archivos adjuntos de un documento PDF en Java utilizando la fachada PdfContentEditor en Aspose.PDF.
lastmod: "2026-09-28"
TechArticle: true
AlternativeHeadline: Eliminar todos los archivos adjuntos PDF en Java
Abstract: Este artículo muestra cómo vincular un PDF, eliminar todos los archivos adjuntos del documento y guardar el archivo actualizado utilizando la fachada PdfContentEditor en Aspose.PDF for Java.
---
## Eliminar todos los archivos adjuntos

1. Vincule el PDF de origen a la fachada `PdfContentEditor`.
2. Llame `deleteAttachments()` para eliminar cada archivo adjunto incrustado.
3. Guarde el documento PDF actualizado.

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
