---
title: Concatenar dos archivos PDF
linktitle: Concatenar dos archivos PDF
type: docs
weight: 60
url: /java/concatenate-two-files/
description: Combine dos archivos PDF en un solo documento en Java con la fachada PdfFileEditor.
lastmod: "2026-06-09"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Concatene dos archivos PDF en un único documento de salida con Java
Abstract: Aprenda a concatenar dos archivos PDF con Aspose.PDF para Java. El ejemplo de Java utiliza PdfFileEditor y la sobrecarga `concatenate` basada en matrices para combinar dos documentos de origen en un PDF de salida.
---
## Concatenar dos archivos PDF



Este artículo se asigna directamente al ejemplo `mergePdfDocuments` en `PdfFileEditorExamples.java`.


### 
Pasos


1. 
Cree una instancia `PdfFileEditor`.

2. 
Pase las dos rutas del archivo de entrada como una matriz de cadenas.
3. Llame a `concatenate` con la matriz y la ruta del archivo de salida.

4. 
Guarde el PDF combinado.

```java
public static void mergePdfDocuments(Path firstInputFile, Path secondInputFile, Path outputFile) {
    PdfFileEditor pdfEditor = new PdfFileEditor();
    pdfEditor.concatenate(new String[] {firstInputFile.toString(), secondInputFile.toString()}, outputFile.toString());
}
```
