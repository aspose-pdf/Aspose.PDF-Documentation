---
title: Establecer script de campo
linktitle: Establecer script de campo
type: docs
weight: 20
url: /es/java/set-field-script/
description: Aprenda cómo asignar o actualizar una acción JavaScript en un campo de formulario PDF en Java usando la fachada FormEditor en Aspose.PDF.
lastmod: "2026-09-29"
TechArticle: true
AlternativeHeadline: Establecer una acción JavaScript en un campo de formulario PDF en Java
Abstract: Este artículo muestra cómo enlazar un PDF existente, agregar un script inicial, reemplazarlo con un script actualizado y guardar el documento modificado usando la fachada FormEditor en Aspose.PDF for Java.
---
## Establecer un script de campo

1. Vincule el PDF de origen a la fachada `FormEditor`.
2. Añada una acción JavaScript inicial al campo.
3. Reemplácela con el texto del script actualizado.
4. Guarde el documento actualizado.

```java
public static void setFieldScript(Path inputFile, Path outputFile) {
    FormEditor editor = new FormEditor();
    try {
        editor.bindPdf(inputFile.toString());
        editor.addFieldScript("Script_Demo_Button", "app.alert('Script 1 has been executed');");
        editor.setFieldScript("Script_Demo_Button", "app.alert('Script 2 has been executed');");
        editor.save(outputFile.toString());
    } finally {
        editor.close();
    }
}
```
