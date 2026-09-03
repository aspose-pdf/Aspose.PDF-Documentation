---
title: Eliminar páginas de PDF
linktitle: Eliminar páginas de PDF
type: docs
weight: 20
url: /es/java/delete-pages-from-pdf/
description: Eliminar páginas seleccionadas de un PDF en Java con la fachada PdfFileEditor.
lastmod: "2026-09-03"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Eliminar páginas específicas de un documento PDF con Java
Abstract: Aprende cómo eliminar páginas de un PDF con Aspose.PDF for Java. El ejemplo en Java utiliza PdfFileEditor para eliminar un conjunto definido de números de página y guardar las páginas restantes como un nuevo documento.
---
## Eliminar páginas de un PDF

El ejemplo en Java elimina las páginas 2 y 4 del documento fuente.

### Pasos

1. Crear un `PdfFileEditor` instancia.
2. Construye una matriz con los números de página a eliminar.
3. Llamar `delete` con el archivo de entrada, la matriz de páginas y el archivo de salida.
4. Guarda el PDF resultante.

### Ejemplo en Java

```java
public static void deletePagesFromPdf(Path inputFile, Path outputFile) {
    PdfFileEditor pdfEditor = new PdfFileEditor();
    pdfEditor.delete(inputFile.toString(), new int[] {2, 4}, outputFile.toString());
}
```
