---
title: Crear campo de casilla de verificación
linktitle: Crear campo de casilla de verificación
type: docs
weight: 20
url: /java/create-checkbox-field/
description: Aprenda cómo agregar un campo de formulario de casilla de verificación a un documento PDF en Java usando la fachada FormEditor en Aspose.PDF.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: Crear un campo de casilla de verificación en un PDF con Java
Abstract: Este artículo muestra cómo vincular un PDF existente, agregar un campo de casilla de verificación en una posición específica y guardar el documento modificado usando la fachada FormEditor en Aspose.PDF para Java.
---
Utilice `FormEditorExamples.createCheckBoxField(...)` para agregar un campo de casilla de verificación a un formulario PDF.


## 
Crear un campo de casilla de verificación


1. Vincule el PDF de origen a la fachada `FormEditor`.

2. Agregue el campo de casilla de verificación con `FieldType.CheckBox`, el nombre del campo, el título, la página y el rectángulo.

3. Guarde el documento actualizado.

```java
public static void createCheckBoxField(Path inputFile, Path outputFile) {
    FormEditor editor = new FormEditor();
    try {
        editor.bindPdf(inputFile.toString());
        editor.addField(FieldType.CheckBox, "checkbox1", "Check Box 1", 1, 240, 498, 256, 514);
        editor.save(outputFile.toString());
    } finally {
        editor.close();
    }
}
```
