---
title: Crear documento PDF de varias páginas en una
linktitle: Crear documento PDF de varias páginas en una
type: docs
weight: 10
url: /java/create-n-up-pdf-document/
description: Cree un diseño PDF de 2x2 N-Up en Java con la fachada PdfFileEditor.
lastmod: "2026-06-09"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Genere un diseño PDF N-Up a partir de un documento existente en Java
Abstract: Aprenda a crear un documento PDF N-Up con Aspose.PDF para Java. El ejemplo de Java utiliza PdfFileEditor para colocar cuatro páginas de origen en cada hoja de salida y también muestra una variante de retorno booleano para la verificación de fallas.
---
## Crear un documento PDF de varias páginas en una



El ejemplo de Java utiliza `PdfFileEditor.makeNUp` para crear un diseño de 2x2 a partir de un PDF existente.


### 
Pasos


1. 
Cree una instancia `PdfFileEditor`.

2. 
Llame a `makeNUp` con el archivo de entrada, el archivo de salida y el número de columnas y filas.
3. Guarde el documento generado.

4. 
Si desea una verificación de éxito explícita, llame a la variante de retorno booleano y maneje un resultado `false`.


### 
Ejemplo de Java

```java
public static void createNupPdfDocument(Path inputFile, Path outputFile) {
    PdfFileEditor nupMaker = new PdfFileEditor();
    nupMaker.makeNUp(inputFile.toString(), outputFile.toString(), 2, 2);
}

public static void tryCreateNupPdfDocument(Path inputFile, Path outputFile) {
    PdfFileEditor nupMaker = new PdfFileEditor();
    if (!nupMaker.makeNUp(inputFile.toString(), outputFile.toString(), 2, 2)) {
        System.out.println("Failed to create N-Up PDF document.");
    }
}
```
