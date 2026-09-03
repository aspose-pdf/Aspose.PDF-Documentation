---
title: Agregar sello de goma
linktitle: Agregar sello de goma
type: docs
weight: 10
url: /es/java/add-rubber-stamp/
description: Aprenda cómo agregar una anotación de sello de goma a un documento PDF en Java usando la fachada PdfContentEditor en Aspose.PDF.
lastmod: "2026-09-03"
TechArticle: true
AlternativeHeadline: Agregar un sello de goma a un PDF en Java
Abstract: Este artículo muestra cómo enlazar un PDF, crear una anotación de sello de goma con texto de etiqueta y color, y guardar el documento actualizado usando la fachada PdfContentEditor en Aspose.PDF for Java.
---
## Agregar un sello de goma

1. Vincular el PDF de origen a la `PdfContentEditor` fachada.
2. Llamada `createRubberStamp(...)` con el número de página, rectángulo, título, contenidos y color.
3. Guardar el documento PDF actualizado.

```java
public static void addRubberStamp(Path inputFile, Path outputFile) {
    PdfContentEditor editor = new PdfContentEditor();
    try {
        editor.bindPdf(inputFile.toString());
        editor.createRubberStamp(1, new Rectangle(120, 450, 180, 60), "Approved", "Approved by reviewer", Color.GREEN);
        editor.save(outputFile.toString());
    } finally {
        editor.close();
    }
}
```
