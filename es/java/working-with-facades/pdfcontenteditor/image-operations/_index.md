---
title: Operaciones de imagen
linktitle: Operaciones de imagen
type: docs
weight: 50
url: /java/pdfcontenteditor-image-operations/
description: Conozca la cobertura actual de operaciones de imágenes de Java disponible en la fachada de PdfContentEditor en Aspose.PDF.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: Flujos de trabajo de edición de imágenes en Java con PdfContentEditor
Abstract: Esta sección cubre los flujos de trabajo relacionados con imágenes actualmente admitidos por el conjunto de ejemplos de Java PdfContentEditor. El repositorio incluye un ejemplo directo para reemplazar una imagen, mientras que los temas sobre eliminación de imágenes no admitidas se conservan como notas de alcance explícitas.
---
La clase Java actual `PdfContentEditorExamples` admite directamente `replaceImage(...)`.


## 
Reemplazar una imagen


1. Vincule el PDF de origen a la fachada `PdfContentEditor`.

2. Llame a `replaceImage(...)` con el número de página, el índice de la imagen y la ruta de la imagen de reemplazo.

3. Guarde el documento PDF actualizado.

```java
public static void replaceImage(Path inputFile, Path imageFile, Path outputFile) {
    PdfContentEditor editor = new PdfContentEditor();
    try {
        editor.bindPdf(inputFile.toString());
        editor.replaceImage(1, 1, imageFile.toString());
        editor.save(outputFile.toString());
    } finally {
        editor.close();
    }
}
```
