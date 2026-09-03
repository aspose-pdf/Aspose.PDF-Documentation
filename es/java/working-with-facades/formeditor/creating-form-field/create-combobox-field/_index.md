---
title: Crear campo de cuadro combinado
linktitle: Crear campo de cuadro combinado
type: docs
weight: 30
url: /java/create-combobox-field/
description: Aprenda a agregar un campo de cuadro combinado a un documento PDF en Java usando la fachada FormEditor en Aspose.PDF.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: Crear un campo de cuadro combinado en un PDF con Java
Abstract: Este artículo muestra cómo vincular un PDF existente, agregar un campo de cuadro combinado, completarlo con elementos y guardar el documento modificado usando la fachada FormEditor en Aspose.PDF para Java.
---
Utilice `FormEditorExamples.createComboBoxField(...)` para crear un cuadro combinado y agregar elementos seleccionables.


## 
Crear un campo de cuadro combinado


1. Vincule el PDF de origen a la fachada `FormEditor`.

2. Agregue el campo del cuadro combinado con su valor predeterminado y el rectángulo de destino.

3. Agregue los elementos del cuadro combinado seleccionables.
4. Guarde el documento actualizado.

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
