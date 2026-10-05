---
title: Obtener versión de PDF
linktitle: Obtener versión de PDF
type: docs
weight: 20
url: /es/java/get-pdf-version/
description: Aprende cómo recuperar la versión de un documento PDF en Java con la fachada PdfFileInfo.
lastmod: "2026-09-29"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Recuperar versión de PDF usando Aspose.PDF for Java
Abstract: Aprende cómo obtener la versión del PDF con Aspose.PDF for Java. El ejemplo en Java crea un objeto PdfFileInfo, lee la cadena de versión con `getPdfVersion()`, imprime el resultado y cierra el objeto de información del archivo.
---
## Obtener versión de PDF

Utiliza este flujo de trabajo cuando necesites comprobar la compatibilidad de archivos o encaminar un documento a través de una lógica de procesamiento específica por versión.

### Pasos

1. Cree un objeto `PdfFileInfo` para el archivo PDF.
2. Llame a `getPdfVersion()` para recuperar la versión reportada.
3. Utilice o imprima el valor de la versión.
4. Cierre la instancia de `PdfFileInfo`.

### Ejemplo en Java

```java
public static void getPdfVersion(Path inputFile) {
    PdfFileInfo pdfInfo = new PdfFileInfo(inputFile.toString());
    System.out.println();
    System.out.println("PDF Version: " + pdfInfo.getPdfVersion());
    pdfInfo.close();
}
```
