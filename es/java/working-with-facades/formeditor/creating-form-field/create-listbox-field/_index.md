---
title: Crear campo ListBox
linktitle: Crear campo ListBox
type: docs
weight: 40
url: /es/java/create-listbox-field/
description: Aprenda cómo agregar un campo de lista desplegable a un documento PDF en Java utilizando la fachada FormEditor en Aspose.PDF.
lastmod: "2026-09-03"
TechArticle: true
AlternativeHeadline: Crear un campo de lista desplegable en un PDF con Java
Abstract: Este artículo muestra cómo vincular un PDF existente, definir los elementos de la lista, agregar un campo de lista desplegable y guardar el documento modificado utilizando la fachada FormEditor en Aspose.PDF for Java.
---
Usar `FormEditorExamples.createListBoxField(...)` para crear un cuadro de lista con elementos predefinidos.

## Crear un campo de lista desplegable

1. Vincular el PDF fuente al `FormEditor` fachada.
2. Definir los elementos de lista disponibles con `setItems(...)`.
3. Agregue el campo de cuadro de lista con su valor predeterminado y rectángulo.
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
