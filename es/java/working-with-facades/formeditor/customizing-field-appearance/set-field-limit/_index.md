---
title: Set Field Limit
linktitle: Establecer límite de campo
type: docs
weight: 50
url: /java/set-field-limit/
description: Aprenda a establecer un límite máximo de caracteres para un campo de formulario PDF en Java usando la fachada FormEditor en Aspose.PDF.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: Establecer un límite de caracteres para un campo de formulario PDF en Java
Abstract: Este artículo muestra cómo vincular un PDF existente, establecer el límite máximo de caracteres de un campo y guardar el documento actualizado usando la fachada FormEditor en Aspose.PDF para Java.
---
## Set a field character limit

1. Bind the source PDF to the `FormEditor` facade.
2. Call `setFieldLimit(...)` for the target field and maximum character count.
3. Save the updated document.

```java
public static void setFieldLimit(Path inputFile, Path outputFile) {
    FormEditor editor = new FormEditor();
    try {
        editor.bindPdf(inputFile.toString());
        editor.setFieldLimit("First Name", 15);
        editor.save(outputFile.toString());
    } finally {
        editor.close();
    }
}
```
