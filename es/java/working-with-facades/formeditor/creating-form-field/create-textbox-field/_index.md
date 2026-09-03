---
title: Crear campo TextBox
linktitle: Crear campo TextBox
type: docs
weight: 10
url: /es/java/create-textbox-field/
description: Aprenda cómo agregar campos de cuadro de texto a un documento PDF en Java usando la fachada FormEditor en Aspose.PDF.
lastmod: "2026-09-03"
TechArticle: true
AlternativeHeadline: Crear campos de formulario de texto en un PDF con Java
Abstract: Este artículo muestra cómo enlazar un PDF existente, agregar campos de texto con valores predeterminados y guardar el documento modificado usando la fachada FormEditor en Aspose.PDF for Java.
---
Usar `FormEditorExamples.createTextBoxField(...)` para agregar campos de texto a un formulario PDF.

## Crear campos de cuadro de texto

1. Vincular el PDF de origen a `FormEditor` fachada.
2. Agregar cada campo de texto con `FieldType.Text`, el nombre del campo, valor predeterminado, número de página y rectángulo.
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
