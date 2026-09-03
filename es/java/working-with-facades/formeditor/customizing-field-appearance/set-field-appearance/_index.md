---
title: Establecer apariencia de campo
linktitle: Establecer apariencia de campo
type: docs
weight: 40
url: /java/set-field-appearance/
description: Aprenda a cambiar los indicadores de apariencia visual de un campo de formulario PDF en Java usando la fachada FormEditor en Aspose.PDF.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: Cambiar los indicadores de apariencia del campo del formulario PDF en Java
Abstract: Este artículo muestra cómo vincular un PDF existente, aplicar un indicador de apariencia a un campo y guardar el documento actualizado usando la fachada FormEditor en Aspose.PDF para Java.
---
## Establecer indicadores de apariencia de campo


1. Vincule el PDF de origen a la fachada `FormEditor`.

2. Llame a `setFieldAppearance(...)` para obtener el campo de destino y el indicador de anotación elegido.

3. Guarde el documento actualizado.

```java
public static void setFieldAppearance(Path inputFile, Path outputFile) {
    FormEditor editor = new FormEditor();
    try {
        editor.bindPdf(inputFile.toString());
        editor.setFieldAppearance("First Name", AnnotationFlags.Hidden);
        editor.save(outputFile.toString());
    } finally {
        editor.close();
    }
}
```
