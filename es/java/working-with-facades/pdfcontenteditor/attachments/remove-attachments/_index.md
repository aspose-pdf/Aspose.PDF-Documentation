---
title: Eliminar archivos adjuntos
linktitle: Eliminar archivos adjuntos
type: docs
weight: 50
url: /java/remove-attachments/
description: Aprenda cómo eliminar todos los documentos adjuntos de un PDF en Java usando la fachada PdfContentEditor en Aspose.PDF.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: Eliminar todos los archivos adjuntos PDF en Java
Abstract: Este artículo muestra cómo vincular un PDF, eliminar todos los documentos adjuntos y guardar el archivo actualizado usando la fachada PdfContentEditor en Aspose.PDF para Java.
---
## Eliminar todos los archivos adjuntos


1. 
Vincule el PDF de origen a la fachada `PdfContentEditor`.

2. 
Llame a `deleteAttachments()` para eliminar todos los archivos adjuntos incrustados.

3. 
Guarde el documento PDF actualizado.

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
