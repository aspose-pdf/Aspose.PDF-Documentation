---
title: decorar campo
linktitle: decorar campo
type: docs
weight: 10
url: /java/decorate-field/
description: Aprenda a decorar un campo de formulario PDF con colores y alineación en Java usando la fachada FormEditor en Aspose.PDF.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: Decorar un campo de formulario PDF en Java
Abstract: Este artículo muestra cómo vincular un PDF existente, configurar un FormFieldFacade con colores y alineación, decorar un campo y guardar el documento actualizado usando la fachada FormEditor en Aspose.PDF para Java.
---
## decorar un campo


1. 
Vincule el PDF de origen a la fachada `FormEditor`.

2. 
Configure un `FormFieldFacade` con los colores y la alineación requeridos.

3. 
Pase la fachada al editor y llame a `decorateField(...)`.

4. 
Guarde el documento actualizado.

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
