---
title: Establecer URL de envío
linktitle: Establecer URL de envío
type: docs
weight: 30
url: /es/java/set-submit-url/
description: Aprenda cómo establecer una URL de envío para un botón de formulario PDF en Java usando la fachada FormEditor en Aspose.PDF.
lastmod: "2026-09-03"
TechArticle: true
AlternativeHeadline: Configure una URL de envío de formulario PDF en Java
Abstract: Este artículo muestra cómo vincular un PDF existente, establecer una URL de envío y una bandera de envío para un campo de botón, y guardar el documento actualizado usando la fachada FormEditor en Aspose.PDF for Java.
---
## Establecer una URL de envío

1. Vincular el PDF de origen a `FormEditor` fachada.
2. Llamar `setSubmitUrl(...)` para el campo de botón.
3. Aplique la bandera de envío para el formato de envío.
4. Guarde el documento actualizado.

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
