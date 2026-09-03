---
title: Concatenar varios archivos PDF
linktitle: Concatenar varios archivos PDF
type: docs
weight: 20
url: /es/java/concatenate-pdf-files/
description: Combinar archivos PDF en Java con el flujo de trabajo de concatenación basado en matrices de PdfFileEditor.
lastmod: "2026-09-03"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Combinar varios archivos PDF en un solo documento con Java
Abstract: Aprenda cómo concatenar archivos PDF con Aspose.PDF for Java. El ejemplo del repositorio utiliza la sobrecarga `concatenate` basada en matrices con dos entradas, y el mismo flujo de trabajo se puede ampliar a listas de archivos más largas porque el método acepta una matriz de cadenas con rutas de origen.
---
## Concatenar archivos PDF

El ejemplo de Java combina dos archivos al pasarlos al basado en matrices `concatenate` sobrecargar.

### Pasos

1. Crear un `PdfFileEditor` instancia.
2. Construye una matriz de cadenas con las rutas de los PDF de entrada.
3. Llamar `concatenate` con la matriz de entrada y la ruta del archivo de salida.
4. Guarda el documento fusionado.

```java
public static void mergePdfDocuments(Path firstInputFile, Path secondInputFile, Path outputFile) {
    PdfFileEditor pdfEditor = new PdfFileEditor();
    pdfEditor.concatenate(new String[] {firstInputFile.toString(), secondInputFile.toString()}, outputFile.toString());
}
```

Para combinar más de dos archivos, amplíe la matriz de cadenas pasada a `concatenate`.
