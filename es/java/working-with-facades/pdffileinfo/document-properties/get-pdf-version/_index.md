---
title: Get PDF Version
linktitle: Get PDF Version
type: docs
weight: 20
url: /java/get-pdf-version/
description: Learn how to retrieve the version of a PDF document in Java with the PdfFileInfo facade.
lastmod: "2026-06-09"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Retrieve PDF Version Using Aspose.PDF for Java
Abstract: Aprenda cómo recuperar la versión PDF con Aspose.PDF para Java. El ejemplo de Java crea un objeto PdfFileInfo, lee la cadena de versión con `getPdfVersion()`, imprime el resultado y cierra el objeto de información del archivo.
---
## Obtener la versión PDF

Utilice este flujo de trabajo cuando necesite comprobar la compatibilidad de archivos o dirigir un documento a través de una lógica de procesamiento específica de la versión.

### Pasos

1. Cree un objeto `PdfFileInfo` para el archivo PDF.
2. Call `getPdfVersion()` to retrieve the reported version.
3. Utilice o imprima el valor de la versión.
4. Close the `PdfFileInfo` instance.

### Java example

```java
public static void getPdfVersion(Path inputFile) {
    PdfFileInfo pdfInfo = new PdfFileInfo(inputFile.toString());
    System.out.println();
    System.out.println("PDF Version: " + pdfInfo.getPdfVersion());
    pdfInfo.close();
}
```
