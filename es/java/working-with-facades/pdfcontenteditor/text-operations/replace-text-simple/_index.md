---
title: Reemplazar texto simple
linktitle: Reemplazar texto simple
type: docs
weight: 10
url: /java/replace-text-simple/
description: Aprenda a reemplazar texto en un documento PDF en Java usando la fachada PdfContentEditor en Aspose.PDF.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: Reemplazar texto en un PDF en Java
Abstract: Este artículo muestra cómo vincular un PDF, configurar el alcance de reemplazo de texto, reemplazar todas las apariciones de texto coincidentes y guardar el documento actualizado usando la fachada PdfContentEditor en Aspose.PDF para Java.
---
## Reemplazar texto en todo el documento


1. 
Vincule el PDF de origen a la fachada `PdfContentEditor`.

2. 
Establezca el alcance del texto de reemplazo en `ReplaceAll`.

3. 
Llame a `replaceText(...)` con el texto de búsqueda y el texto de reemplazo.

4. 
Guarde el documento PDF actualizado.

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
