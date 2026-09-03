---
title: Obtener preferencias del visor
linktitle: Obtener preferencias del visor
type: docs
weight: 10
url: /es/java/get-viewer-preferences/
description: Aprenda cómo leer las preferencias del visor de un documento PDF en Java usando la fachada PdfContentEditor en Aspose.PDF.
lastmod: "2026-09-03"
TechArticle: true
AlternativeHeadline: Leer las preferencias del visor PDF en Java
Abstract: Este artículo muestra cómo enlazar un PDF e imprimir el valor actual de la preferencia del visor usando la fachada PdfContentEditor en Aspose.PDF para Java.
---
## Obtener la preferencia actual del visor

1. Vincular el PDF de origen al `PdfContentEditor` fachada.
2. Llamar `getViewerPreference()` para leer el valor actual.
3. Inspecciona o imprime la bandera de preferencia devuelta.

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
