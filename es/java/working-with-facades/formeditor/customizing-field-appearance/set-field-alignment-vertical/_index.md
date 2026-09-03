---
title: Establecer alineación de campo vertical
linktitle: Establecer alineación de campo vertical
type: docs
weight: 30
url: /java/set-field-alignment-vertical/
description: Aprenda cómo configurar la alineación vertical para un campo de formulario PDF en Java usando la fachada FormEditor en Aspose.PDF.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: Establecer alineación vertical para un campo de formulario PDF en Java
Abstract: Este artículo muestra cómo vincular un PDF existente, establecer la alineación vertical del campo y guardar el documento actualizado usando la fachada FormEditor en Aspose.PDF para Java.
---
## Establecer alineación de campo vertical


1. Vincule el PDF de origen a la fachada `FormEditor`.

2. Llame a `setFieldAlignmentV(...)` para obtener el campo objetivo y la constante de alineación vertical deseada.

3. Guarde el documento actualizado.

```java
public static void setFieldAlignmentVertical(Path inputFile, Path outputFile) {
    FormEditor editor = new FormEditor();
    try {
        editor.bindPdf(inputFile.toString());
        editor.setFieldAlignmentV("First Name", FormFieldFacade.ALIGN_BOTTOM);
        editor.save(outputFile.toString());
    } finally {
        editor.close();
    }
}
```
