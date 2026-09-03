---
title: Obtener desplazamiento de página
linktitle: Obtener desplazamiento de página
type: docs
weight: 20
url: /es/java/get-page-offset/
description: Aprenda cómo inspeccionar los offsets X e Y de la página en Java con la fachada PdfFileInfo.
lastmod: "2026-09-03"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Obtener offsets de página PDF usando Java
Abstract: Aprenda cómo recuperar los offsets de página con Aspose.PDF for Java. El ejemplo en Java usa PdfFileInfo para leer los offsets X e Y de la página 1 y convierte los valores de puntos a pulgadas para un análisis de diseño más sencillo.
---
## Obtener desplazamiento de página

Utilice este flujo de trabajo cuando necesite entender cómo se posiciona el contenido de la página en relación con el origen del PDF.

### Pasos

1. Crear un `PdfFileInfo` objeto para el PDF de entrada.
2. Llamar `getPageXOffset` y `getPageYOffset` para la página de destino.
3. Convierta los valores de puntos a pulgadas dividiendo por `72.0`.
4. Usa o imprime los valores convertidos.
5. Cerrar el `PdfFileInfo` instancia.

### Ejemplo de Java

```java
public static void getPageOffsets(Path inputFile) {
    PdfFileInfo pdfInfo = new PdfFileInfo(inputFile.toString());
    System.out.println("Page X Offset: " + (pdfInfo.getPageXOffset(1) / 72.0) + " inches");
    System.out.println("Page Y Offset: " + (pdfInfo.getPageYOffset(1) / 72.0) + " inches");
    pdfInfo.close();
}
```
