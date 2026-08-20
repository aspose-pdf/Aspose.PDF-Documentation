---
title: Insertar páginas en PDF
linktitle: Insertar páginas en PDF
type: docs
weight: 40
url: /java/insert-pages-into-pdf/
description: Inserte páginas seleccionadas de un PDF en otro en Java con la fachada PdfFileEditor.
lastmod: "2026-06-09"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Insertar páginas de otro PDF en una posición elegida con Java
Abstract: Aprenda a insertar páginas en un PDF con Aspose.PDF para Java. El ejemplo de Java utiliza PdfFileEditor para insertar páginas seleccionadas de un segundo documento después de un número de página determinado en el PDF de destino.
---
## Insertar páginas en un PDF



El ejemplo de Java inserta las páginas 1 y 2 del documento secundario después de la página 2 del PDF de destino.


### 
Pasos


1. 
Cree una instancia `PdfFileEditor`.

2. 
Elija el punto de inserción en el documento de destino.
3. Seleccione los números de página para copiar del documento fuente.

4. 
Llame a `insert` con el archivo de destino, el punto de inserción, el archivo de origen, la matriz de páginas y el archivo de salida.

5. 
Guarde el PDF actualizado.


### 
Ejemplo de Java

```java
public static void insertPagesIntoPdf(Path inputFile, Path sampleFile, Path outputFile) {
    PdfFileEditor pdfEditor = new PdfFileEditor();
    pdfEditor.insert(inputFile.toString(), 2, sampleFile.toString(), new int[] {1, 2}, outputFile.toString());
}
```
