---
title: Crear campo ComboBox
linktitle: Crear campo ComboBox
type: docs
weight: 30
url: /es/java/create-combobox-field/
description: Aprenda cómo agregar un campo combo box a un documento PDF en Java usando la fachada FormEditor en Aspose.PDF.
lastmod: "2026-09-03"
TechArticle: true
AlternativeHeadline: Crear un campo combo box en un PDF con Java
Abstract: Este artículo muestra cómo vincular un PDF existente, agregar un campo combo box, completarlo con elementos y guardar el documento modificado usando la fachada FormEditor en Aspose.PDF for Java.
---
Usar `FormEditorExamples.createComboBoxField(...)` para crear un cuadro combinado y añadir elementos seleccionables.

## Crear un campo ComboBox

1. Vincular el PDF de origen a `FormEditor` fachada.
2. Agrega el campo de cuadro combinado con su valor predeterminado y el rectángulo objetivo.
3. Agrega los elementos seleccionables del cuadro combinado.
4. Guarda el documento actualizado.

```java
public static void createComboBoxField(Path inputFile, Path outputFile) {
    FormEditor editor = new FormEditor();
    try {
        editor.bindPdf(inputFile.toString());
        editor.addField(FieldType.ComboBox, "combobox1", "Australia", 1, 230, 498, 350, 514);
        editor.addListItem("combobox1", new String[] {"Australia", "Australia"});
        editor.addListItem("combobox1", new String[] {"New Zealand", "New Zealand"});
        editor.save(outputFile.toString());
    } finally {
        editor.close();
    }
}
```
