---
title: Fill Radio Button Fields
linktitle: Llenar los campos del botón de opción
type: docs
weight: 30
url: /java/fill-radio-button-fields/
description: Aprenda a seleccionar el valor de un botón de opción en un formulario PDF con Java usando la fachada del formulario en Aspose.PDF.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: Select a radio button field option in Java
Abstract: Este artículo muestra cómo vincular un formulario PDF, seleccionar una opción de botón de opción por índice y guardar el documento actualizado con la fachada del formulario en Aspose.PDF para Java.
---
Use `FormExamples.fillRadioButtonFields(...)` to select a radio button option.

```java
public static void fillRadioButtonFields(Path inputFile, Path outputFile) {
    Form form = new Form();
    try {
        form.bindPdf(inputFile.toString());
        form.fillField("gender", 0);
        form.save(outputFile.toString());
    } finally {
        form.close();
    }
}
```
