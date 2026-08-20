---
title: Crear campo de botón de radio
linktitle: Crear campo de botón de radio
type: docs
weight: 50
url: /java/create-radiobutton-field/
description: Aprenda cómo agregar un campo de botón de opción a un documento PDF en Java usando la fachada FormEditor en Aspose.PDF.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: Cree un campo de botón de opción en un PDF con Java
Abstract: Este artículo muestra cómo vincular un PDF existente, configurar los ajustes de diseño del botón de opción, crear un campo de botón de opción y guardar el documento modificado usando la fachada FormEditor en Aspose.PDF para Java.
---
Utilice `FormEditorExamples.createRadioButtonField(...)` para crear un campo de botón de opción con opciones predefinidas.


## 
Crear un campo de botón de opción


1. 
Vincule el PDF de origen a la fachada `FormEditor`.

2. 
Configure el espacio, la orientación y el tamaño del elemento del botón de opción.

3. 
Defina los elementos del botón de opción.
4. Agregue el campo del botón de opción con su selección y rectángulo predeterminados.

5. 
Guarde el documento actualizado.

```java
public static void createRadioButtonField(Path inputFile, Path outputFile) {
    FormEditor editor = new FormEditor();
    try {
        editor.bindPdf(inputFile.toString());
        editor.setRadioGap(4);
        editor.setRadioHoriz(false);
        editor.setRadioButtonItemSize(20);
        editor.setItems(new String[] {"Australia", "New Zealand", "Malaysia"});
        editor.addField(FieldType.Radio, "radiobutton1", "Malaysia", 1, 240, 498, 256, 514);
        editor.save(outputFile.toString());
    } finally {
        editor.close();
    }
}
```
