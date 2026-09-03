---
title: Agregar márgenes a páginas PDF
linktitle: Agregar márgenes a páginas PDF
type: docs
weight: 10
url: /es/java/add-margins-to-pdf-pages/
description: Agregar márgenes a páginas PDF seleccionadas en Java con la fachada PdfFileEditor.
lastmod: "2026-09-03"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Agregar márgenes a páginas específicas en un documento PDF con Java
Abstract: Aprenda cómo agregar márgenes a páginas seleccionadas con Aspose.PDF for Java. El ejemplo en Java utiliza PdfFileEditor para dirigirse a números de página individuales y aplicar valores de margen iguales en la parte superior, inferior, izquierda y derecha.
---
## Agregar márgenes a páginas PDF

El ejemplo en Java agrega márgenes de 36 puntos a las páginas 1 y 3 del documento de origen.

### Pasos

1. Crear un `PdfFileEditor` instancia.
2. Seleccione los números de página que deben recibir nuevos márgenes.
3. Llamar `addMargins` con el archivo de entrada, archivo de salida, lista de páginas y valores de margen.
4. Guarde el PDF actualizado.

### Ejemplo de Java

```java
public static void addMarginsToPdfPages(Path inputFile, Path outputFile) {
    PdfFileEditor pdfEditor = new PdfFileEditor();
    pdfEditor.addMargins(inputFile.toString(), outputFile.toString(), new int[] {1, 3}, 36, 36, 36, 36);
}
```
