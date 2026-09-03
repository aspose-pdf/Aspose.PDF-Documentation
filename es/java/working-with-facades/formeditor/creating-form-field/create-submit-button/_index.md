---
title: Crear botón de envío
linktitle: Crear botón de envío
type: docs
weight: 60
url: /es/java/create-submit-button/
description: Aprenda cómo agregar un botón de envío a un documento PDF en Java usando la fachada FormEditor en Aspose.PDF.
lastmod: "2026-09-03"
TechArticle: true
AlternativeHeadline: Crear un botón de envío PDF en Java
Abstract: Este artículo muestra cómo enlazar un PDF existente, agregar un campo de botón de envío con una URL de destino y guardar el documento modificado usando la fachada FormEditor en Aspose.PDF for Java.
---
Usar `FormEditorExamples.createSubmitButton(...)` para crear un botón que envíe los datos del formulario.

## Crear un botón de envío

1. Vincular el PDF de origen al `FormEditor` fachada.
2. Llamar `addSubmitBtn(...)` con el nombre del botón, la página, la etiqueta, la URL de destino y el rectángulo.
3. Guarda el documento actualizado.

```java
public static void createSubmitButton(Path inputFile, Path outputFile) {
    FormEditor editor = new FormEditor();
    try {
        editor.bindPdf(inputFile.toString());
        editor.addSubmitBtn("submitbutton", 1, "Submit", "http://localhost/testing/show", 100, 450, 150, 475);
        editor.save(outputFile.toString());
    } finally {
        editor.close();
    }
}
```
