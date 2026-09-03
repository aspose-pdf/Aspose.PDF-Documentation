---
title: Eliminar acción de apertura
linktitle: Eliminar acción de apertura
type: docs
weight: 20
url: /es/java/remove-open-action/
description: Aprenda cómo eliminar la acción de apertura del documento de un PDF en Java usando la fachada PdfContentEditor en Aspose.PDF.
lastmod: "2026-09-03"
TechArticle: true
AlternativeHeadline: Eliminar una acción de apertura de documento PDF en Java
Abstract: Este artículo muestra cómo vincular un PDF, eliminar la acción de apertura del documento y guardar el documento actualizado usando la fachada PdfContentEditor en Aspose.PDF para Java.
---
## Eliminar la acción de apertura del documento

1. Vincular el PDF de origen al `PdfContentEditor` fachada.
2. Llamar `removeDocumentOpenAction()`.
3. Guarde el documento PDF actualizado.

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
