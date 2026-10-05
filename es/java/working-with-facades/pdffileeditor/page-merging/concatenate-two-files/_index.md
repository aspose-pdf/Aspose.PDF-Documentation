---
title: Concatenar dos archivos PDF
linktitle: Concatenar dos archivos PDF
type: docs
weight: 60
url: /es/java/concatenate-two-files/
description: Combine dos archivos PDF en un solo documento en Java con la fachada PdfFileEditor.
lastmod: "2026-09-29"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Concatenar dos archivos PDF en un único documento de salida con Java
Abstract: Aprenda cómo concatenar dos archivos PDF con Aspose.PDF for Java. El ejemplo Java usa PdfFileEditor y la sobrecarga basada en matriz `concatenate` para combinar dos documentos de origen en un PDF de salida.
---
## Concatenar dos archivos PDF

Este artículo se asigna directamente a `mergePdfDocuments` ejemplo en `PdfFileEditorExamples.java`.

### Pasos

1. Cree una instancia de `PdfFileEditor`.
2. Pase las dos rutas de archivo de entrada como una matriz de cadenas.
3. Llame `concatenate` con la matriz y la ruta del archivo de salida.
4. Guarde el PDF combinado.

```java
public static void mergePdfDocuments(Path firstInputFile, Path secondInputFile, Path outputFile) {
    PdfFileEditor pdfEditor = new PdfFileEditor();
    pdfEditor.concatenate(new String[] {firstInputFile.toString(), secondInputFile.toString()}, outputFile.toString());
}
```
