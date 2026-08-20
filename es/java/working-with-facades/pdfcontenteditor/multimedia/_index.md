---
title: Multimedios
linktitle: Multimedios
type: docs
weight: 70
url: /java/pdfcontenteditor-multimedia/
description: Conozca la cobertura multimedia actual disponible en la fachada de Java PdfContentEditor en Aspose.PDF.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: Flujos de trabajo de anotaciones multimedia en Java con PdfContentEditor
Abstract: Esta sección cubre los flujos de trabajo relacionados con multimedia actualmente admitidos por el conjunto de ejemplos de Java PdfContentEditor. El repositorio incluye un ejemplo de anotación directa de película, mientras que los temas de sonido no compatibles se conservan como notas de alcance explícitas.
---
La clase Java actual `PdfContentEditorExamples` admite directamente `addMovieAnnotation(...)`.


## 
Agregar una anotación de película


1. 
Vincule el PDF de origen a la fachada `PdfContentEditor`.

2. 
Llame a `createMovie(...)` con el rectángulo de anotación, la ruta del archivo de película y el número de página.

3. 
Guarde el documento PDF actualizado.

```java
public static void addMovieAnnotation(Path inputFile, Path movieFile, Path outputFile) {
    PdfContentEditor editor = new PdfContentEditor();
    try {
        editor.bindPdf(inputFile.toString());
        editor.createMovie(new Rectangle(80, 500, 220, 120), movieFile.toString(), 1);
        editor.save(outputFile.toString());
    } finally {
        editor.close();
    }
}
```
