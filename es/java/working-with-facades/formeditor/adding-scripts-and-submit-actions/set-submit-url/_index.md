---
title: Establecer URL de envío
linktitle: Establecer URL de envío
type: docs
weight: 30
url: /java/set-submit-url/
description: Aprenda a configurar una URL de envío para un botón de formulario PDF en Java usando la fachada FormEditor en Aspose.PDF.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: Configurar una URL de envío de formulario PDF en Java
Abstract: Este artículo muestra cómo vincular un PDF existente, establecer una URL de envío y un indicador de envío para un campo de botón, y guardar el documento actualizado usando la fachada FormEditor en Aspose.PDF para Java.
---
## Establecer una URL de envío

1. Vincule el PDF de origen a la fachada `FormEditor`.
2. Llame a `setSubmitUrl(...)` para el campo del botón.
3. Apply the submit flag for the submission format.
4. Save the updated document.

```java
public static void setSubmitUrl(Path inputFile, Path outputFile) {
    FormEditor editor = new FormEditor();
    try {
        editor.bindPdf(inputFile.toString());
        editor.setSubmitUrl("Script_Demo_Button", "http://www.example.com/submit");
        editor.setSubmitFlag("Script_Demo_Button", SubmitFormFlag.Xfdf);
        editor.save(outputFile.toString());
    } finally {
        editor.close();
    }
}
```
