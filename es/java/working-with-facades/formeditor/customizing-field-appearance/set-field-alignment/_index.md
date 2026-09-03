---
title: Establecer alineación de campo
linktitle: Establecer alineación de campo
type: docs
weight: 20
url: /java/set-field-alignment/
description: Aprenda a configurar la alineación horizontal del texto para un campo de formulario PDF en Java usando la fachada FormEditor en Aspose.PDF.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: Establecer la alineación de los campos del formulario PDF en Java
Abstract: Este artículo muestra cómo vincular un PDF existente, establecer la alineación horizontal del campo y guardar el documento actualizado usando la fachada FormEditor en Aspose.PDF para Java.
---
## Establecer alineación de campo horizontal


1. Vincule el PDF de origen a la fachada `FormEditor`.

2. Llame a `setFieldAlignment(...)` para obtener el campo objetivo y la constante de alineación deseada.

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
