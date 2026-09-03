---
title: Agregar sello de goma
linktitle: Agregar sello de goma
type: docs
weight: 10
url: /java/add-rubber-stamp/
description: Aprenda a agregar una anotación de sello de goma a un documento PDF en Java usando la fachada PdfContentEditor en Aspose.PDF.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: Agregar un sello de goma a un PDF en Java
Abstract: Este artículo muestra cómo vincular un PDF, crear una anotación de sello con texto y color de etiqueta y guardar el documento actualizado usando la fachada PdfContentEditor en Aspose.PDF para Java.
---
## Añadir un sello de goma


1. Vincule el PDF de origen a la fachada `PdfContentEditor`.

2. Llame a `createRubberStamp(...)` con el número de página, el rectángulo, el título, el contenido y el color.

3. Guarde el documento PDF actualizado.

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
