---
title: Crear documento PDF N-Up
linktitle: Crear documento PDF N-Up
type: docs
weight: 10
url: /es/java/create-n-up-pdf-document/
description: Crear un diseño PDF N-Up 2x2 en Java con la fachada PdfFileEditor.
lastmod: "2026-09-29"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Generar un diseño PDF N-Up a partir de un documento existente en Java
Abstract: Aprenda cómo crear un documento PDF N-Up con Aspose.PDF for Java. El ejemplo en Java utiliza PdfFileEditor para colocar cuatro páginas de origen en cada hoja de salida y también muestra una variante que devuelve un booleano para la verificación de errores.
---
## Crear un documento PDF N-Up

El ejemplo de Java usa `PdfFileEditor.makeNUp` para crear un diseño 2x2 a partir de un PDF existente.

### Pasos

1. Cree una instancia de `PdfFileEditor`.
2. Llame `makeNUp` con el archivo de entrada, el archivo de salida y el número de columnas y filas.
3. Guarde el documento generado.
4. Si desea una verificación explícita del éxito, llama a la variante que devuelve un booleano y maneje un `false` resultado.

### Ejemplo en Java

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
