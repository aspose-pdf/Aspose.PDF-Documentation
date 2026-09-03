---
title: Crear campo de cuadro de lista
linktitle: Crear campo de cuadro de lista
type: docs
weight: 40
url: /java/create-listbox-field/
description: Aprenda cómo agregar un campo de cuadro de lista a un documento PDF en Java usando la fachada FormEditor en Aspose.PDF.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: Cree un campo de cuadro de lista en un PDF con Java
Abstract: Este artículo muestra cómo vincular un PDF existente, definir elementos de lista, agregar un campo de cuadro de lista y guardar el documento modificado usando la fachada FormEditor en Aspose.PDF para Java.
---
Utilice `FormEditorExamples.createListBoxField(...)` para crear un cuadro de lista con elementos predefinidos.


## 
Crear un campo de cuadro de lista


1. Vincule el PDF de origen a la fachada `FormEditor`.

2. Defina los elementos de la lista disponibles con `setItems(...)`.

3. Agregue el campo del cuadro de lista con su valor predeterminado y su rectángulo.
4. Guarde el documento actualizado.

```java
public static void createListBoxField(Path inputFile, Path outputFile) {
    FormEditor editor = new FormEditor();
    try {
        editor.bindPdf(inputFile.toString());
        editor.setItems(new String[] {"Australia", "New Zealand", "Malaysia"});
        editor.addField(FieldType.ListBox, "listbox1", "Australia", 1, 230, 398, 350, 514);
        editor.save(outputFile.toString());
    } finally {
        editor.close();
    }
}
```
