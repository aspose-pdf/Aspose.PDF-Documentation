---
title: Establecer número de comb del campo
linktitle: Establecer número de comb del campo
type: docs
weight: 60
url: /es/java/set-field-comb-number/
description: Aprenda cómo establecer un número de comb para un campo de formulario PDF en Java usando la fachada FormEditor en Aspose.PDF.
lastmod: "2026-09-03"
TechArticle: true
AlternativeHeadline: Establezca un número de comb para un campo de formulario PDF en Java.
Abstract: Este artículo muestra cómo vincular un PDF existente, establecer un número de comb para un campo y guardar el documento actualizado usando la fachada FormEditor en Aspose.PDF for Java.
---
## Establecer un número de comb de campo

1. Vincular el PDF de origen al `FormEditor` fachada.
2. Llamar `setFieldCombNumber(...)` para el campo de destino y el valor comb.
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
