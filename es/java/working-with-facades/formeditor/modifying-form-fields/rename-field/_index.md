---
title: Renombrar campo
linktitle: Renombrar campo
type: docs
weight: 50
url: /es/java/rename-field/
description: Aprenda cómo renombrar un campo de formulario existente en un documento PDF en Java usando la fachada FormEditor en Aspose.PDF.
lastmod: "2026-09-29"
TechArticle: true
AlternativeHeadline: Renombrar un campo de formulario PDF en Java
Abstract: Este artículo muestra cómo enlazar un PDF existente, renombrar un campo especificado y guardar el documento actualizado usando la fachada FormEditor en Aspose.PDF for Java.
---
## Renombrar un campo

1. Vincule el PDF de origen a la fachada `FormEditor`.
2. Llame `renameField(...)` con el nombre de campo actual y el nuevo nombre de campo.
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
