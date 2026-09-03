---
title: Reemplazar texto con estado
linktitle: Reemplazar texto con estado
type: docs
weight: 20
url: /java/replace-text-with-state/
description: Aprenda a reemplazar texto con formato personalizado en Java usando la fachada PdfContentEditor en Aspose.PDF.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: Reemplace el texto PDF con formato personalizado en Java
Abstract: Este artículo muestra cómo vincular un PDF, configurar un TextState personalizado, reemplazar todas las apariciones de texto coincidentes y guardar el documento actualizado usando la fachada PdfContentEditor en Aspose.PDF para Java.
---
## Reemplazar texto con un estado de texto personalizado


1. Vincule el PDF de origen a la fachada `PdfContentEditor`.

2. Cree y configure un `TextState` con el color y tamaño de fuente requeridos.

3. Establezca el alcance del texto de reemplazo en `ReplaceAll`.

4. Llame a `replaceText(...)` con el texto de búsqueda, el texto de reemplazo y `TextState` configurado.
5. Guarde el documento PDF actualizado.

```java
public static void replaceTextWithState(Path inputFile, Path outputFile) {
    PdfContentEditor editor = new PdfContentEditor();
    try {
        editor.bindPdf(inputFile.toString());
        TextState textState = new TextState();
        textState.setForegroundColor(com.aspose.pdf.Color.getBlue());
        textState.setFontSize(14);
        editor.getReplaceTextStrategy().setReplaceScope(ReplaceTextStrategy.Scope.ReplaceAll);
        editor.replaceText("software", "SOFTWARE", textState);
        editor.save(outputFile.toString());
    } finally {
        editor.close();
    }
}
```
