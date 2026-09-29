---
title: Obtener información de la página
linktitle: Obtener información de la página
type: docs
weight: 10
url: /es/java/get-page-info/
description: Aprenda cómo inspeccionar el ancho, la altura y la rotación de la página en Java con la fachada PdfFileInfo.
lastmod: "2026-09-29"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Obtener información de la página PDF usando Aspose.PDF for Java
Abstract: Aprenda cómo recuperar la información de la página con Aspose.PDF for Java. El ejemplo en Java usa PdfFileInfo para leer el ancho, la altura y la rotación de la página 1, de modo que pueda inspeccionar su diseño antes de un procesamiento adicional.
---
## Obtener información de la página

Este ejemplo lee las principales propiedades geométricas de la página 1.

### Pasos

1. Cree un objeto `PdfFileInfo` para el PDF de origen.
2. Llame `getPageWidth`, `getPageHeight`, y `getPageRotation` para la página que desea inspeccionar.
3. Utilice o imprime los valores devueltos.
4. Cierre la instancia de `PdfFileInfo`.

### Ejemplo en Java

```java
public static void getPageInformation(Path inputFile) {
    PdfFileInfo pdfInfo = new PdfFileInfo(inputFile.toString());
    System.out.println("Page Width: " + pdfInfo.getPageWidth(1));
    System.out.println("Page Height: " + pdfInfo.getPageHeight(1));
    System.out.println("Page Rotation: " + pdfInfo.getPageRotation(1));
    pdfInfo.close();
}
```
