---
title: Establecer alineación vertical del campo
linktitle: Establecer alineación vertical del campo
type: docs
weight: 30
url: /es/java/set-field-alignment-vertical/
description: Aprenda cómo establecer la alineación vertical para un campo de formulario PDF en Java usando la fachada FormEditor en Aspose.PDF.
lastmod: "2026-09-03"
TechArticle: true
AlternativeHeadline: Establecer alineación vertical para un campo de formulario PDF en Java
Abstract: Este artículo muestra cómo vincular un PDF existente, establecer la alineación vertical del campo y guardar el documento actualizado usando la fachada FormEditor en Aspose.PDF for Java.
---
## Establecer alineación vertical del campo

1. Vincular el PDF de origen al `FormEditor` fachada.
2. Llamada `setFieldAlignmentV(...)` para el campo objetivo y la constante de alineación vertical deseada.
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
