---
title: Obtener preferencias del espectador
linktitle: Obtener preferencias del espectador
type: docs
weight: 10
url: /java/get-viewer-preferences/
description: Aprenda a leer las preferencias del visor de un documento PDF en Java utilizando la fachada PdfContentEditor en Aspose.PDF.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: Leer las preferencias del visor de PDF en Java
Abstract: Este artículo muestra cómo vincular un PDF e imprimir el valor de preferencia del visor actual usando la fachada PdfContentEditor en Aspose.PDF para Java.
---
## Obtener la preferencia del espectador actual


1. Vincule el PDF de origen a la fachada `PdfContentEditor`.

2. Llame a `getViewerPreference()` para leer el valor actual.

3. Inspeccione o imprima el indicador de preferencia devuelto.

```java
public static void getViewerPreferences(Path inputFile) {
    PdfContentEditor editor = new PdfContentEditor();
    try {
        editor.bindPdf(inputFile.toString());
        System.out.println("Current viewer preference: " + editor.getViewerPreference());
    } finally {
        editor.close();
    }
}
```
