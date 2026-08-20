---
title: Establecer límite de campo
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
## Establecer un límite de caracteres de campo


1. 
Vincule el PDF de origen a la fachada `FormEditor`.

2. 
Llame a `setFieldLimit(...)` para conocer el campo de destino y el número máximo de caracteres.

3. 
Guarde el documento actualizado.

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
