---
title: Crear botón Enviar
linktitle: Crear botón Enviar
type: docs
weight: 60
url: /java/create-submit-button/
description: Aprenda cómo agregar un botón de envío a un documento PDF en Java usando la fachada FormEditor en Aspose.PDF.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: Cree un botón de envío de PDF en Java
Abstract: Este artículo muestra cómo vincular un PDF existente, agregar un campo de botón de envío con una URL de destino y guardar el documento modificado usando la fachada FormEditor en Aspose.PDF para Java.
---
Utilice `FormEditorExamples.createSubmitButton(...)` para crear un botón que envíe datos del formulario.


## 
Crear un botón de enviar


1. 
Vincule el PDF de origen a la fachada `FormEditor`.

2. 
Llame a `addSubmitBtn(...)` con el nombre del botón, la página, la etiqueta, la URL de destino y el rectángulo.

3. 
Guarde el documento actualizado.

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
