---
title: Mover campo
linktitle: Mover campo
type: docs
weight: 30
url: /java/move-field/
description: Aprenda cómo mover un campo de formulario existente en un documento PDF en Java usando la fachada FormEditor en Aspose.PDF.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: Mover un campo de formulario PDF a una nueva posición en Java
Abstract: Este artículo muestra cómo vincular un PDF existente, mover un campo a nuevas coordenadas y guardar el documento actualizado usando la fachada FormEditor en Aspose.PDF para Java.
---
## Mover un campo


1. 
Vincule el PDF de origen a la fachada `FormEditor`.

2. 
Llame a `moveField(...)` con el nombre del campo de destino y las nuevas coordenadas del rectángulo.

3. 
Guarde el documento actualizado.

```java
public static void moveField(Path inputFile, Path outputFile) {
    FormEditor editor = new FormEditor();
    try {
        editor.bindPdf(inputFile.toString());
        editor.moveField("Country", 200, 600, 280, 620);
        editor.save(outputFile.toString());
    } finally {
        editor.close();
    }
}
```
