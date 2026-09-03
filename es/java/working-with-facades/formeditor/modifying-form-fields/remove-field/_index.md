---
title: Eliminar campo
linktitle: Eliminar campo
type: docs
weight: 40
url: /java/remove-field/
description: Aprenda cómo eliminar un campo de formulario existente de un documento PDF en Java usando la fachada FormEditor en Aspose.PDF.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: Eliminar un campo de formulario PDF en Java
Abstract: Este artículo muestra cómo vincular un PDF existente, eliminar un campo específico y guardar el documento actualizado usando la fachada FormEditor en Aspose.PDF para Java.
---
## Eliminar un campo


1. Vincule el PDF de origen a la fachada `FormEditor`.

2. Llame a `removeField(...)` para obtener el nombre del campo de destino.

3. Guarde el documento actualizado.

```java
public static void removeField(Path inputFile, Path outputFile) {
    FormEditor editor = new FormEditor();
    try {
        editor.bindPdf(inputFile.toString());
        editor.removeField("Country");
        editor.save(outputFile.toString());
    } finally {
        editor.close();
    }
}
```
