---
title: Cambiar nombre de campo
linktitle: Cambiar nombre de campo
type: docs
weight: 50
url: /java/rename-field/
description: Aprenda a cambiar el nombre de un campo de formulario existente en un documento PDF en Java usando la fachada FormEditor en Aspose.PDF.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: Cambiar el nombre de un campo de formulario PDF en Java
Abstract: Este artículo muestra cómo vincular un PDF existente, cambiar el nombre de un campo específico y guardar el documento actualizado usando la fachada FormEditor en Aspose.PDF para Java.
---
## Cambiar el nombre de un campo


1. Vincule el PDF de origen a la fachada `FormEditor`.

2. Llame a `renameField(...)` con el nombre del campo actual y el nuevo nombre del campo.

3. Guarde el documento actualizado.

```java
public static void renameField(Path inputFile, Path outputFile) {
    FormEditor editor = new FormEditor();
    try {
        editor.bindPdf(inputFile.toString());
        editor.renameField("City", "Town");
        editor.save(outputFile.toString());
    } finally {
        editor.close();
    }
}
```
