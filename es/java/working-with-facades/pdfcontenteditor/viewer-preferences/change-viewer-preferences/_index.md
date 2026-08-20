---
title: Cambiar las preferencias del visor
linktitle: Cambiar las preferencias del visor
type: docs
weight: 20
url: /java/change-viewer-preferences/
description: Aprenda a cambiar las preferencias del visor de un documento PDF en Java usando la fachada PdfContentEditor en Aspose.PDF.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: Cambiar las preferencias del visor de PDF en Java
Abstract: Este artículo muestra cómo vincular un PDF, modificar el valor de preferencia del visor actual y guardar el documento actualizado usando la fachada PdfContentEditor en Aspose.PDF para Java.
---
## Cambiar la preferencia del espectador


1. 
Vincule el PDF de origen a la fachada `PdfContentEditor`.

2. 
Lea el valor de preferencia del espectador actual.

3. 
Combínelo con la bandera adicional deseada y pase el resultado a `changeViewerPreference(...)`.

4. 
Guarde el documento PDF actualizado.

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
