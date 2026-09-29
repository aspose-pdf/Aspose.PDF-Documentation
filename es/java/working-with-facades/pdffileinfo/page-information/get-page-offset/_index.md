---
title: Obtener desplazamiento de página
linktitle: Obtener desplazamiento de página
type: docs
weight: 20
url: /es/java/get-page-offset/
description: Aprenda cómo inspeccionar los desplazamientos X y Y de la página en Java con la fachada PdfFileInfo.
lastmod: "2026-09-29"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Obtener desplazamientos de página PDF usando Java
Abstract: Aprenda cómo recuperar los desplazamientos de página con Aspose.PDF for Java. El ejemplo en Java usa PdfFileInfo para leer los desplazamientos X y Y de la página 1 y convierte los valores de puntos a pulgadas para un análisis de diseño más fácil.
---
## Obtener desplazamiento de página

Utilice este workflow cuando necesite comprender cómo se posiciona el contenido de la página con respecto al origen del PDF.

### Pasos

1. Cree un objeto `PdfFileInfo` para el PDF de entrada.
2. Llame `getPageXOffset` y `getPageYOffset` para la página objetivo.
3. Convierta los valores de punto a pulgadas dividiendo por `72.0`.
4. Utilice o imprima los valores convertidos.
5. Cierre la instancia de `PdfFileInfo`.

### Ejemplo de Java

```java
public static void getPageOffsets(Path inputFile) {
    PdfFileInfo pdfInfo = new PdfFileInfo(inputFile.toString());
    System.out.println("Page X Offset: " + (pdfInfo.getPageXOffset(1) / 72.0) + " inches");
    System.out.println("Page Y Offset: " + (pdfInfo.getPageYOffset(1) / 72.0) + " inches");
    pdfInfo.close();
}
```
