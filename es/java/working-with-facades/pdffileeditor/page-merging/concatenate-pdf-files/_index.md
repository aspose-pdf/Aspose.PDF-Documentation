---
title: Concatenar varios archivos PDF
linktitle: Concatenar varios archivos PDF
type: docs
weight: 20
url: /es/java/concatenate-pdf-files/
description: Combinar archivos PDF en Java con el flujo de trabajo de concatenación basado en matriz de PdfFileEditor.
lastmod: "2026-09-29"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Combinar varios archivos PDF en un solo documento con Java
Abstract: Aprenda cómo concatenar archivos PDF con Aspose.PDF for Java. El ejemplo del repositorio utiliza la sobrecarga basada en matriz `concatenate` con dos entradas, y el mismo flujo de trabajo se puede ampliar a listas de archivos más largas porque el método acepta una matriz de cadenas de rutas de origen.
---
## Concatenar archivos PDF

El ejemplo de Java combina dos archivos pasándolos al basado en matriz `concatenate` sobrecarga.

### Pasos

1. Cree una instancia de `PdfFileEditor`.
2. Construya una matriz de cadenas con las rutas de los PDF de entrada.
3. Llame `concatenate` con la matriz de entrada y la ruta del archivo de salida.
4. Guarde el documento combinado.

```java
public static void mergePdfDocuments(Path firstInputFile, Path secondInputFile, Path outputFile) {
    PdfFileEditor pdfEditor = new PdfFileEditor();
    pdfEditor.concatenate(new String[] {firstInputFile.toString(), secondInputFile.toString()}, outputFile.toString());
}
```

Para combinar más de dos archivos, amplíe la matriz de cadenas pasada a `concatenate`.
