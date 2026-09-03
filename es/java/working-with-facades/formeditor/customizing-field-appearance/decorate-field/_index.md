---
title: Decorar Campo
linktitle: Decorar Campo
type: docs
weight: 10
url: /es/java/decorate-field/
description: Aprenda cómo decorar un campo de formulario PDF con colores y alineación en Java usando la fachada FormEditor en Aspose.PDF.
lastmod: "2026-09-03"
TechArticle: true
AlternativeHeadline: Decorar un campo de formulario PDF en Java
Abstract: Este artículo muestra cómo vincular un PDF existente, configurar un FormFieldFacade con colores y alineación, decorar un campo y guardar el documento actualizado usando la fachada FormEditor en Aspose.PDF for Java.
---
## Decorar un campo

1. Vincula el PDF de origen al `FormEditor` fachada.
2. Configura un `FormFieldFacade` con los colores y la alineación requeridos.
3. Pase la fachada al editor y llame `decorateField(...)`.
4. Guarde el documento actualizado.

```java
public static void decorateField(Path inputFile, Path outputFile) {
    FormEditor editor = new FormEditor();
    try {
        editor.bindPdf(inputFile.toString());
        FormFieldFacade facade = new FormFieldFacade();
        facade.setBackgroundColor(Color.RED);
        facade.setTextColor(Color.BLUE);
        facade.setBorderColor(Color.GREEN);
        facade.setAlignment(FormFieldFacade.ALIGN_CENTER);
        editor.setFacade(facade);
        editor.decorateField("First Name");
        editor.save(outputFile.toString());
    } finally {
        editor.close();
    }
}
```
