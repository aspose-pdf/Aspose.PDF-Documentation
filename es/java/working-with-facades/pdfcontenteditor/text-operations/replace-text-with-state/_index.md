---
title: Reemplazar texto con estado
linktitle: Reemplazar texto con estado
type: docs
weight: 20
url: /es/java/replace-text-with-state/
description: Aprenda cómo reemplazar texto con formato personalizado en Java usando la fachada PdfContentEditor en Aspose.PDF.
lastmod: "2026-09-03"
TechArticle: true
AlternativeHeadline: Reemplazar texto PDF con formato personalizado en Java
Abstract: Este artículo muestra cómo enlazar un PDF, configurar un TextState personalizado, reemplazar todas las coincidencias de texto y guardar el documento actualizado usando la fachada PdfContentEditor en Aspose.PDF para Java.
---
## Reemplazar texto con un TextState personalizado

1. Vincular el PDF de origen a `PdfContentEditor` fachada.
2. Crear y configurar un `TextState` con el color y tamaño de fuente requeridos.
3. Establezca el alcance del texto de reemplazo en `ReplaceAll`.
4. Llamar `replaceText(...)` con el texto de búsqueda, el texto de reemplazo y configurado `TextState`.
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
