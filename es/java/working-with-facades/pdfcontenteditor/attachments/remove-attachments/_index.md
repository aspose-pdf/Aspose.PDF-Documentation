---
title: Eliminar archivos adjuntos
linktitle: Eliminar archivos adjuntos
type: docs
weight: 50
url: /es/java/remove-attachments/
description: Aprenda cómo eliminar todos los archivos adjuntos de documentos de un PDF en Java utilizando la fachada PdfContentEditor en Aspose.PDF.
lastmod: "2026-09-03"
TechArticle: true
AlternativeHeadline: Eliminar todos los archivos adjuntos de PDF en Java
Abstract: Este artículo muestra cómo vincular un PDF, eliminar todos los archivos adjuntos de documentos y guardar el archivo actualizado utilizando la fachada PdfContentEditor en Aspose.PDF para Java.
---
## Eliminar todos los archivos adjuntos

1. Vincular el PDF de origen al `PdfContentEditor` fachada.
2. Llamar `deleteAttachments()` para eliminar cada adjunto incrustado.
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
