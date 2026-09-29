---
title: Obtener preferencias del visor
linktitle: Obtener preferencias del visor
type: docs
weight: 10
url: /es/java/get-viewer-preferences/
description: Aprenda cómo leer las preferencias del visor de un documento PDF en Java usando la fachada PdfContentEditor en Aspose.PDF.
lastmod: "2026-09-28"
TechArticle: true
AlternativeHeadline: Leer preferencias del visor PDF en Java
Abstract: Este artículo muestra cómo vincular un PDF y mostrar el valor actual de la preferencia del visor usando la fachada PdfContentEditor en Aspose.PDF for Java.
---
## Obtener la preferencia actual del visor

1. Vincule el PDF fuente a la fachada `PdfContentEditor`.
2. Llame a `getViewerPreference()` para leer el valor actual.
3. Inspeccione o imprima la bandera de preferencia devuelta.

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
