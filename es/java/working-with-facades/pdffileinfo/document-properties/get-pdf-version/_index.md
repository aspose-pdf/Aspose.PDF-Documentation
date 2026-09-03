---
title: Obtener la versión PDF
linktitle: Obtener la versión PDF
type: docs
weight: 20
url: /java/get-pdf-version/
description: Aprenda cómo recuperar la versión de un documento PDF en Java con la fachada PdfFileInfo.
lastmod: "2026-06-09"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Recuperar la versión PDF usando Aspose.PDF para Java
Abstract: Aprenda cómo recuperar la versión PDF con Aspose.PDF para Java. El ejemplo de Java crea un objeto PdfFileInfo, lee la cadena de versión con `getPdfVersion()`, imprime el resultado y cierra el objeto de información del archivo.
---
## Obtener la versión PDF



Utilice este flujo de trabajo cuando necesite comprobar la compatibilidad de archivos o dirigir un documento a través de una lógica de procesamiento específica de la versión.


### 
Pasos


1. Cree un objeto `PdfFileInfo` para el archivo PDF.

2. Llame a `getPdfVersion()` para recuperar la versión reportada.
3. Utilice o imprima el valor de la versión.

4. Cierre la instancia `PdfFileInfo`.


### 
Ejemplo de Java

```java
public static void getPdfVersion(Path inputFile) {
    PdfFileInfo pdfInfo = new PdfFileInfo(inputFile.toString());
    System.out.println();
    System.out.println("PDF Version: " + pdfInfo.getPdfVersion());
    pdfInfo.close();
}
```
