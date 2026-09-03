---
title: Crear campo RadioButton
linktitle: Crear campo RadioButton
type: docs
weight: 50
url: /es/java/create-radiobutton-field/
description: Aprenda cómo agregar un campo de botón de opción a un documento PDF en Java usando la fachada FormEditor en Aspose.PDF.
lastmod: "2026-09-03"
TechArticle: true
AlternativeHeadline: Crear un campo de botón de opción en un PDF con Java
Abstract: Este artículo muestra cómo vincular un PDF existente, configurar la configuración de diseño del botón de opción, crear un campo de botón de opción y guardar el documento modificado usando la fachada FormEditor en Aspose.PDF for Java.
---
Usar `FormEditorExamples.createRadioButtonField(...)` para crear un campo de botón de opción con opciones predefinidas.

## Crear un campo de botón de opción

1. Vincular el PDF de origen al `FormEditor` fachada.
2. Configura la separación, la orientación y el tamaño de los botones de opción.
3. Define los elementos de los botones de opción.
4. Agrega el campo de botón de opción con su selección predeterminada y rectángulo.
5. Guarda el documento actualizado.

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
