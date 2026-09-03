---
title: Cambiar preferencias de visualización
linktitle: Cambiar preferencias de visualización
type: docs
weight: 20
url: /es/java/change-viewer-preferences/
description: Aprenda cómo cambiar las preferencias de visualización de un documento PDF en Java usando la fachada PdfContentEditor en Aspose.PDF.
lastmod: "2026-09-03"
TechArticle: true
AlternativeHeadline: Cambiar preferencias de visualización de PDF en Java
Abstract: Este artículo muestra cómo vincular un PDF, modificar el valor actual de la preferencia de visualización y guardar el documento actualizado usando la fachada PdfContentEditor en Aspose.PDF for Java.
---
## Cambiar la preferencia de visualización

1. Vincular el PDF de origen al `PdfContentEditor` fachada.
2. Lee el valor actual de la preferencia del visor.
3. Combínalo con la bandera adicional deseada y pasa el resultado a `changeViewerPreference(...)`.
4. Guarda el documento PDF actualizado.

```java
public static void changeViewerPreferences(Path inputFile, Path outputFile) {
    PdfContentEditor editor = new PdfContentEditor();
    try {
        editor.bindPdf(inputFile.toString());
        editor.changeViewerPreference(editor.getViewerPreference() | 1);
        editor.save(outputFile.toString());
    } finally {
        editor.close();
    }
}
```
