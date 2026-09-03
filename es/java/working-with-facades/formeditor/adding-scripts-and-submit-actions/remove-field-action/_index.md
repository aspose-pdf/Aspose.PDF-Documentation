---
title: Eliminar acción de campo
linktitle: Eliminar acción de campo
type: docs
weight: 50
url: /java/remove-field-action/
description: Aprenda cómo eliminar una acción de campo de un campo de formulario PDF en Java usando la fachada FormEditor en Aspose.PDF.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: Eliminar una acción de campo de formulario PDF en Java
Abstract: Este artículo muestra cómo vincular un PDF existente, eliminar la acción asociada con un campo específico y guardar el documento actualizado usando la fachada FormEditor en Aspose.PDF para Java.
---
## Eliminar una acción de campo


1. Vincule el PDF de origen a la fachada `FormEditor`.

2. Llame a `removeFieldAction(...)` para obtener el campo de destino.

3. Guarde el documento actualizado.

```java
public static void removeFieldAction(Path inputFile, Path outputFile) {
    FormEditor editor = new FormEditor();
    try {
        editor.bindPdf(inputFile.toString());
        editor.removeFieldAction("Script_Demo_Button");
        editor.save(outputFile.toString());
    } finally {
        editor.close();
    }
}
```
