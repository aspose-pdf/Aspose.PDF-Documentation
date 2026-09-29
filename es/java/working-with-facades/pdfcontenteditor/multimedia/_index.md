---
title: Multimedia
linktitle: Multimedia
type: docs
weight: 70
url: /es/java/pdfcontenteditor-multimedia/
description: Aprenda la cobertura multimedia actual disponible en la fachada Java PdfContentEditor de Aspose.PDF.
lastmod: "2026-09-28"
TechArticle: true
AlternativeHeadline: Flujos de trabajo de anotación multimedia en Java con PdfContentEditor
Abstract: Esta sección cubre los flujos de trabajo relacionados con multimedia que actualmente son compatibles con el conjunto de ejemplos Java PdfContentEditor. El repositorio incluye un ejemplo directo de anotación de película, mientras que los temas de sonido no compatibles se conservan como notas de alcance explícitas.
---
El Java actual `PdfContentEditorExamples` clase admite directamente `addMovieAnnotation(...)`.

## Agregar una anotación de película

1. Vincule el PDF de origen a la fachada `PdfContentEditor`.
2. Llame `createMovie(...)` con el rectángulo de anotación, la ruta del archivo de película y el número de página.
3. Guarde el documento PDF actualizado.

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
