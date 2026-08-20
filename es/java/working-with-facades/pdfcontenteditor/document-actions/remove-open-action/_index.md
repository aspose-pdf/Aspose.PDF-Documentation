---
title: Eliminar acción abierta
linktitle: Eliminar acción abierta
type: docs
weight: 20
url: /java/remove-open-action/
description: Aprenda cómo eliminar la acción de apertura de documento de un PDF en Java usando la fachada PdfContentEditor en Aspose.PDF.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: Eliminar una acción de apertura de documento PDF en Java
Abstract: Este artículo muestra cómo vincular un PDF, eliminar la acción de apertura de documento y guardar el documento actualizado usando la fachada PdfContentEditor en Aspose.PDF para Java.
---
## Eliminar la acción de abrir documento


1. 
Vincule el PDF de origen a la fachada `PdfContentEditor`.

2. 
Llame a `removeDocumentOpenAction()`.

3. 
Guarde el documento PDF actualizado.

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
