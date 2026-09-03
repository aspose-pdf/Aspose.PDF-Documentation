---
title: Establecer límite de campo
linktitle: Establecer límite de campo
type: docs
weight: 50
url: /es/java/set-field-limit/
description: Aprenda cómo establecer un límite máximo de caracteres para un campo de formulario PDF en Java utilizando la fachada FormEditor en Aspose.PDF.
lastmod: "2026-09-03"
TechArticle: true
AlternativeHeadline: Establecer un límite de caracteres para un campo de formulario PDF en Java
Abstract: Este artículo muestra cómo vincular un PDF existente, establecer el límite máximo de caracteres de un campo y guardar el documento actualizado utilizando la fachada FormEditor en Aspose.PDF for Java.
---
## Establecer un límite de caracteres del campo

1. Vincular el PDF de origen al `FormEditor` fachada.
2. Llamar `setFieldLimit(...)` para el campo de destino y el número máximo de caracteres.
3. Guarde el documento actualizado.

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
