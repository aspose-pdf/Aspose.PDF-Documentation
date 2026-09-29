---
title: Establecer apariencia del campo
linktitle: Establecer apariencia del campo
type: docs
weight: 40
url: /es/java/set-field-appearance/
description: Aprenda cómo cambiar los indicadores de apariencia visual de un campo de formulario PDF en Java usando la fachada FormEditor en Aspose.PDF.
lastmod: "2026-09-28"
TechArticle: true
AlternativeHeadline: Cambiar los indicadores de apariencia de campos de formulario PDF en Java
Abstract: Este artículo muestra cómo vincular un PDF existente, aplicar un indicador de apariencia a un campo y guardar el documento actualizado usando la fachada FormEditor en Aspose.PDF for Java.
---
## Establecer indicadores de apariencia del campo

1. Vincule el PDF de origen a la fachada `FormEditor`.
2. Llame `setFieldAppearance(...)` para el campo de destino y la bandera de anotación elegida.
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
