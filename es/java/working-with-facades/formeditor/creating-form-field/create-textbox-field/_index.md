---
title: Crear campo de cuadro de texto
linktitle: Crear campo de cuadro de texto
type: docs
weight: 10
url: /java/create-textbox-field/
description: Aprenda a agregar campos de cuadro de texto a un documento PDF en Java usando la fachada FormEditor en Aspose.PDF.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: Cree campos de formulario de texto en un PDF con Java
Abstract: Este artículo muestra cómo vincular un PDF existente, agregar campos de texto con valores predeterminados y guardar el documento modificado usando la fachada FormEditor en Aspose.PDF para Java.
---
Utilice `FormEditorExamples.createTextBoxField(...)` para agregar campos de texto a un formulario PDF.


## 
Crear campos de cuadro de texto


1. Vincule el PDF de origen a la fachada `FormEditor`.

2. Agregue cada campo de texto con `FieldType.Text`, el nombre del campo, el valor predeterminado, el número de página y el rectángulo.

3. Guarde el documento actualizado.

```java
public static void createTextBoxField(Path inputFile, Path outputFile) {
    FormEditor editor = new FormEditor();
    try {
        editor.bindPdf(inputFile.toString());
        editor.addField(FieldType.Text, "first_name", "Alexander", 1, 50, 570, 150, 590);
        editor.addField(FieldType.Text, "last_name", "Smith", 1, 235, 570, 330, 590);
        editor.save(outputFile.toString());
    } finally {
        editor.close();
    }
}
```
