---
title: Concatenar varios archivos PDF
linktitle: Concatenar varios archivos PDF
type: docs
weight: 20
url: /java/concatenate-pdf-files/
description: Combine archivos PDF en Java con el flujo de trabajo de concatenación de PdfFileEditor basado en matrices.
lastmod: "2026-06-09"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Fusione varios archivos PDF en un solo documento con Java
Abstract: Aprenda a concatenar archivos PDF con Aspose.PDF para Java. El ejemplo del repositorio utiliza la sobrecarga `concatenate` basada en matrices con dos entradas, y el mismo flujo de trabajo se puede extender a listas de archivos más largas porque el método acepta una matriz de cadenas de rutas de origen.
---
## Concatenar archivos PDF



El ejemplo de Java fusiona dos archivos pasándolos a la sobrecarga `concatenate` basada en matrices.


### 
Pasos


1. Cree una instancia `PdfFileEditor`.

2. Cree una matriz de cadenas con las rutas del PDF de entrada.
3. Llame a `concatenate` con la matriz de entrada y la ruta del archivo de salida.

4. Guarde el documento combinado.


```java
public static void mergePdfDocuments(Path firstInputFile, Path secondInputFile, Path outputFile) {
    PdfFileEditor pdfEditor = new PdfFileEditor();
    pdfEditor.concatenate(new String[] {firstInputFile.toString(), secondInputFile.toString()}, outputFile.toString());
}
```


Para fusionar más de dos archivos, extienda la matriz de cadenas pasada a `concatenate`.
