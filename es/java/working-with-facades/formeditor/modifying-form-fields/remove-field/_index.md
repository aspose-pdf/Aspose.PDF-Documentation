---
title: Eliminar campo
linktitle: Eliminar campo
type: docs
weight: 40
url: /es/java/remove-field/
description: Aprenda cómo eliminar un campo de formulario existente de un documento PDF en Java utilizando la fachada FormEditor en Aspose.PDF.
lastmod: "2026-09-28"
TechArticle: true
AlternativeHeadline: Eliminar un campo de formulario PDF en Java
Abstract: Este artículo muestra cómo vincular un PDF existente, eliminar un campo especificado y guardar el documento actualizado utilizando la fachada FormEditor en Aspose.PDF for Java.
---
## Eliminar un campo

1. Vincule el PDF de origen a la fachada `FormEditor`.
2. Llame `removeField(...)` para el nombre del campo de destino.
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
