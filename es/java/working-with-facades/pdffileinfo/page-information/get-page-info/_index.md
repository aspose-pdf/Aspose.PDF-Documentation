---
title: Get Page Information
linktitle: Get Page Information
type: docs
weight: 10
url: /java/get-page-info/
description: Aprenda a inspeccionar el ancho, el alto y la rotación de la página en Java con la fachada PdfFileInfo.
lastmod: "2026-06-09"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Obtenga información de la página PDF utilizando Aspose.PDF para Java
Abstract: Aprenda cómo recuperar información de la página con Aspose.PDF para Java. El ejemplo de Java utiliza PdfFileInfo para leer el ancho, alto y rotación de la página 1 para que pueda inspeccionar su diseño antes de seguir procesando.
---
## Obtener información de la página

Este ejemplo lee las principales propiedades geométricas de la página 1.

### Pasos

1. Create a `PdfFileInfo` object for the source PDF.
2. Call `getPageWidth`, `getPageHeight`, and `getPageRotation` for the page you want to inspect.
3. Use or print the returned values.
4. Close the `PdfFileInfo` instance.

### Java example

```java
public static void getPageInformation(Path inputFile) {
    PdfFileInfo pdfInfo = new PdfFileInfo(inputFile.toString());
    System.out.println("Page Width: " + pdfInfo.getPageWidth(1));
    System.out.println("Page Height: " + pdfInfo.getPageHeight(1));
    System.out.println("Page Rotation: " + pdfInfo.getPageRotation(1));
    pdfInfo.close();
}
```
