---
title: Establecer alineación de campo
linktitle: Establecer alineación de campo
type: docs
weight: 20
url: /es/java/set-field-alignment/
description: Aprenda cómo establecer la alineación horizontal del texto para un campo de formulario PDF en Java usando la fachada FormEditor en Aspose.PDF.
lastmod: "2026-09-29"
TechArticle: true
AlternativeHeadline: Establecer la alineación del campo de formulario PDF en Java
Abstract: Este artículo muestra cómo vincular un PDF existente, establecer la alineación horizontal del campo y guardar el documento actualizado usando la fachada FormEditor en Aspose.PDF for Java.
---
## Establecer alineación horizontal del campo

1. Vincule el PDF de origen a la fachada `FormEditor`.
2. Llame `setFieldAlignment(...)` para el campo objetivo y la constante de alineación deseada.
3. Guarde el documento actualizado.

```java
public static void setFieldAlignment(Path inputFile, Path outputFile) {
    FormEditor editor = new FormEditor();
    try {
        editor.bindPdf(inputFile.toString());
        editor.setFieldAlignment("First Name", FormFieldFacade.ALIGN_CENTER);
        editor.save(outputFile.toString());
    } finally {
        editor.close();
    }
}
```
