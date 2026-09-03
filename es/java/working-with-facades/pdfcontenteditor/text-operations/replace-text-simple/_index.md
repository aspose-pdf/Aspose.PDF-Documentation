---
title: Reemplazar texto simple
linktitle: Reemplazar texto simple
type: docs
weight: 10
url: /es/java/replace-text-simple/
description: Aprenda a reemplazar texto a lo largo de un documento PDF en Java usando la fachada PdfContentEditor en Aspose.PDF.
lastmod: "2026-09-03"
TechArticle: true
AlternativeHeadline: Reemplazar texto en un PDF en Java
Abstract: Este artículo muestra cómo enlazar un PDF, configurar el alcance de reemplazo de texto, reemplazar todas las ocurrencias de texto coincidentes y guardar el documento actualizado usando la fachada PdfContentEditor en Aspose.PDF for Java.
---
## Reemplazar texto a lo largo del documento

1. Vincule el PDF de origen a `PdfContentEditor` fachada.
2. Establezca el alcance de replace-text a `ReplaceAll`.
3. Llamar `replaceText(...)` con el texto de búsqueda y el texto de reemplazo.
4. Guarde el documento PDF actualizado.

```java
public static void replaceTextSimple(Path inputFile, Path outputFile) {
    PdfContentEditor editor = new PdfContentEditor();
    try {
        editor.bindPdf(inputFile.toString());
        editor.getReplaceTextStrategy().setReplaceScope(ReplaceTextStrategy.Scope.ReplaceAll);
        editor.replaceText("33", "XXXIII ");
        editor.save(outputFile.toString());
    } finally {
        editor.close();
    }
}
```
