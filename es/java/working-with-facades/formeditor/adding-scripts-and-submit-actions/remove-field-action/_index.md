---
title: Remove Field Action
linktitle: Eliminar acción de campo
type: docs
weight: 50
url: /java/remove-field-action/
description: Aprenda cómo eliminar una acción de campo de un campo de formulario PDF en Java usando la fachada FormEditor en Aspose.PDF.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: Eliminar una acción de campo de formulario PDF en Java
Abstract: This article shows how to bind an existing PDF, remove the action associated with a specific field, and save the updated document using the FormEditor facade in Aspose.PDF for Java.
---
## Remove a field action

1. Vincule el PDF de origen a la fachada `FormEditor`.
2. Llame a `removeFieldAction(...)` para el campo de destino.
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
