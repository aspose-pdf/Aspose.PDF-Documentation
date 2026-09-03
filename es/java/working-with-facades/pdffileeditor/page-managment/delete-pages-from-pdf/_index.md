---
title: Eliminar páginas de PDF
linktitle: Eliminar páginas de PDF
type: docs
weight: 20
url: /java/delete-pages-from-pdf/
description: Elimine páginas seleccionadas de un PDF en Java con la fachada PdfFileEditor.
lastmod: "2026-06-09"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Eliminar páginas específicas de un documento PDF con Java
Abstract: Aprenda a eliminar páginas de un PDF con Aspose.PDF para Java. El ejemplo de Java utiliza PdfFileEditor para eliminar un conjunto definido de números de página y guardar las páginas restantes como un documento nuevo.
---
## Eliminar páginas de un PDF



El ejemplo de Java elimina las páginas 2 y 4 del documento fuente.


### 
Pasos


1. Cree una instancia `PdfFileEditor`.

2. Cree una matriz con los números de página que desea eliminar.
3. Llame a `delete` con el archivo de entrada, la matriz de páginas y el archivo de salida.

4. Guarde el PDF resultante.


### 
Ejemplo de Java

```java
public static void deletePagesFromPdf(Path inputFile, Path outputFile) {
    PdfFileEditor pdfEditor = new PdfFileEditor();
    pdfEditor.delete(inputFile.toString(), new int[] {2, 4}, outputFile.toString());
}
```
