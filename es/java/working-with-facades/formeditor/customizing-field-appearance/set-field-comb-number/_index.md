---
title: Establecer número de peine de campo
linktitle: Establecer número de peine de campo
type: docs
weight: 60
url: /java/set-field-comb-number/
description: Aprenda a configurar un número de peine para un campo de formulario PDF en Java usando la fachada FormEditor en Aspose.PDF.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: Establecer un número de peine para un campo de formulario PDF en Java
Abstract: Este artículo muestra cómo vincular un PDF existente, establecer un número de peine para un campo y guardar el documento actualizado usando la fachada FormEditor en Aspose.PDF para Java.
---
## Establecer un número de peine de campo


1. Vincule el PDF de origen a la fachada `FormEditor`.

2. Llame a `setFieldCombNumber(...)` para obtener el campo objetivo y el valor del peine.

3. Guarde el documento actualizado.

```java
public static void setFieldCombNumber(Path inputFile, Path outputFile) {
    FormEditor editor = new FormEditor();
    try {
        editor.bindPdf(inputFile.toString());
        editor.setFieldCombNumber("textCombField", 5);
        editor.save(outputFile.toString());
    } finally {
        editor.close();
    }
}
```
