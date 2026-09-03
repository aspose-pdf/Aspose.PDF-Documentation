---
title: Eliminar acción de campo
linktitle: Eliminar acción de campo
type: docs
weight: 50
url: /es/java/remove-field-action/
description: Aprenda cómo eliminar una acción de campo de un campo de formulario PDF en Java usando la fachada FormEditor en Aspose.PDF.
lastmod: "2026-09-03"
TechArticle: true
AlternativeHeadline: Eliminar una acción de campo de formulario PDF en Java
Abstract: Este artículo muestra cómo vincular un PDF existente, eliminar la acción asociada a un campo específico y guardar el documento actualizado usando la fachada FormEditor en Aspose.PDF for Java.
---
## Eliminar una acción de campo

1. Vincula el PDF fuente a la `FormEditor` fachada.
2. Llamar `removeFieldAction(...)` para el campo de destino.
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
