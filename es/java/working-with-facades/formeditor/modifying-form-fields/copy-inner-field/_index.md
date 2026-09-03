---
title: Copiar campo interior
linktitle: Copiar campo interior
type: docs
weight: 70
url: /java/copy-inner-field/
description: Aprenda a copiar un campo de formulario a una nueva posición dentro del mismo documento PDF en Java usando la fachada FormEditor en Aspose.PDF.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: Copie un campo de formulario PDF dentro del mismo documento en Java
Abstract: Este artículo muestra cómo vincular un PDF existente, duplicar un campo en otra página y posición y guardar el documento actualizado usando la fachada FormEditor en Aspose.PDF para Java.
---
## Copiar un campo dentro del mismo PDF


1. Vincule el PDF de origen a la fachada `FormEditor`.

2. Llame a `copyInnerField(...)` con el nombre del campo de origen, el nuevo nombre del campo, la página y las coordenadas.

3. Guarde el documento actualizado.

```java
public static void copyInnerField(Path inputFile, Path outputFile) {
    FormEditor editor = new FormEditor();
    try {
        editor.bindPdf(inputFile.toString());
        editor.copyInnerField("First Name", "First Name Copy", 2, 200, 600);
        editor.save(outputFile.toString());
    } finally {
        editor.close();
    }
}
```
