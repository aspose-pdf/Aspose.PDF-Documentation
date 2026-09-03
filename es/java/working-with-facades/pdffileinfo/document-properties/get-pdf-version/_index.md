---
title: Obtener versión PDF
linktitle: Obtener versión PDF
type: docs
weight: 20
url: /es/java/get-pdf-version/
description: Aprenda cómo obtener la versión de un documento PDF en Java con la fachada PdfFileInfo.
lastmod: "2026-09-03"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Obtener versión PDF usando Aspose.PDF for Java
Abstract: Aprenda cómo obtener la versión PDF con Aspose.PDF for Java. El ejemplo en Java crea un objeto PdfFileInfo, lee la cadena de versión con `getPdfVersion()`, imprime el resultado y cierra el objeto de información del archivo.
---
## Obtener versión PDF

Utilice este flujo de trabajo cuando necesite verificar la compatibilidad de archivos o dirigir un documento a través de una lógica de procesamiento específica por versión.

### Pasos

1. Crear un `PdfFileInfo` objeto para el archivo PDF.
2. Llamar `getPdfVersion()` para recuperar la versión reportada.
3. Usa o imprime el valor de la versión.
4. Cerrar el `PdfFileInfo` instancia.

### Ejemplo en Java

```java
public static void getPdfVersion(Path inputFile) {
    PdfFileInfo pdfInfo = new PdfFileInfo(inputFile.toString());
    System.out.println();
    System.out.println("PDF Version: " + pdfInfo.getPdfVersion());
    pdfInfo.close();
}
```
