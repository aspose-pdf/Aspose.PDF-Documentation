---
title: Concatenar dos archivos PDF
linktitle: Concatenar dos archivos PDF
type: docs
weight: 60
url: /es/java/concatenate-two-files/
description: Combinar dos archivos PDF en un solo documento en Java con la fachada PdfFileEditor.
lastmod: "2026-09-03"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Concatenar dos archivos PDF en un documento de salida único con Java
Abstract: Aprenda cómo concatenar dos archivos PDF con Aspose.PDF for Java. El ejemplo en Java usa PdfFileEditor y la sobrecarga basada en matrices `concatenate` para combinar dos documentos fuente en un PDF de salida único.
---
## Concatenar dos archivos PDF

Este artículo se asigna directamente a `mergePdfDocuments` ejemplo en `PdfFileEditorExamples.java`.

### Pasos

1. Crear un `PdfFileEditor` instancia.
2. Pasa las dos rutas de archivo de entrada como una matriz de cadenas.
3. Llamar `concatenate` con el array y la ruta del archivo de salida.
4. Guarda el PDF combinado.

```java
public static void mergePdfDocuments(Path firstInputFile, Path secondInputFile, Path outputFile) {
    PdfFileEditor pdfEditor = new PdfFileEditor();
    pdfEditor.concatenate(new String[] {firstInputFile.toString(), secondInputFile.toString()}, outputFile.toString());
}
```
