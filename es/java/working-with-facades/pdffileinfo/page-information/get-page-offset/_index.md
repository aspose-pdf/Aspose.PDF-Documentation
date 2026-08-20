---
title: Obtener desplazamiento de página
linktitle: Obtener desplazamiento de página
type: docs
weight: 20
url: /java/get-page-offset/
description: Aprenda a inspeccionar los desplazamientos de las páginas X e Y en Java con la fachada PdfFileInfo.
lastmod: "2026-06-09"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Obtenga desplazamientos de páginas PDF usando Java
Abstract: Aprenda cómo recuperar desplazamientos de página con Aspose.PDF para Java. El ejemplo de Java utiliza PdfFileInfo para leer los desplazamientos X e Y de la página 1 y convierte los valores de puntos a pulgadas para facilitar el análisis del diseño.
---
## Obtener desplazamiento de página



Utilice este flujo de trabajo cuando necesite comprender cómo se coloca el contenido de la página en relación con el origen del PDF.


### 
Pasos


1. 
Cree un objeto `PdfFileInfo` para el PDF de entrada.

2. 
Llame a `getPageXOffset` y `getPageYOffset` para obtener la página de destino.
3. Convierta los valores de puntos a pulgadas dividiendo por `72.0`.

4. 
Utilice o imprima los valores convertidos.

5. 
Cierre la instancia `PdfFileInfo`.


### 
Ejemplo de Java

```java
public static void getPageOffsets(Path inputFile) {
    PdfFileInfo pdfInfo = new PdfFileInfo(inputFile.toString());
    System.out.println("Page X Offset: " + (pdfInfo.getPageXOffset(1) / 72.0) + " inches");
    System.out.println("Page Y Offset: " + (pdfInfo.getPageYOffset(1) / 72.0) + " inches");
    pdfInfo.close();
}
```
