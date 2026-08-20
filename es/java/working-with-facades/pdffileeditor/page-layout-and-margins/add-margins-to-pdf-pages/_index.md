---
title: Agregar márgenes a páginas PDF
linktitle: Agregar márgenes a páginas PDF
type: docs
weight: 10
url: /java/add-margins-to-pdf-pages/
description: Agregue márgenes a páginas PDF seleccionadas en Java con la fachada PdfFileEditor.
lastmod: "2026-06-09"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Agregue márgenes a páginas específicas en un documento PDF con Java
Abstract: Aprenda cómo agregar márgenes a páginas seleccionadas con Aspose.PDF para Java. El ejemplo de Java utiliza PdfFileEditor para apuntar a números de página individuales y aplicar valores iguales de margen superior, inferior, izquierdo y derecho.
---
## Agregar márgenes a las páginas PDF



El ejemplo de Java agrega márgenes de 36 puntos a las páginas 1 y 3 del documento fuente.


### 
Pasos


1. 
Cree una instancia `PdfFileEditor`.

2. 
Seleccione los números de página que deberían recibir nuevos márgenes.
3. Llame a `addMargins` con el archivo de entrada, el archivo de salida, la lista de páginas y los valores de margen.

4. 
Guarde el PDF actualizado.


### 
Ejemplo de Java

```java
public static void addMarginsToPdfPages(Path inputFile, Path outputFile) {
    PdfFileEditor pdfEditor = new PdfFileEditor();
    pdfEditor.addMargins(inputFile.toString(), outputFile.toString(), new int[] {1, 3}, 36, 36, 36, 36);
}
```
