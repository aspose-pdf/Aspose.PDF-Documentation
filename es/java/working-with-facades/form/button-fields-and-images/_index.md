---
title: Campos de botones e imágenes
linktitle: Campos de botones e imágenes
type: docs
weight: 40
url: /java/button-fields-and-images/
description: Aprenda a agregar una apariencia de imagen a un campo de botón en un formulario PDF usando la fachada del formulario en Aspose.PDF para Java.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: Agregue una apariencia de imagen a un campo de botón PDF en Java
Abstract: Este artículo muestra cómo usar la fachada de formulario en Aspose.PDF para Java para vincular un formulario PDF, cargar una imagen como una secuencia, completar un campo de botón de imagen y guardar el documento actualizado.
---
El ejemplo de Java en `FormExamples.addImageAppearanceToButtonField(...)` muestra cómo actualizar la apariencia de un campo de botón con una secuencia de imágenes.



El flujo de trabajo es sencillo:


- 
vincular el PDF de entrada con `form.bindPdf(...)`

- 
abra el archivo de imagen con `Files.newInputStream(...)`

- 
llame a `form.fillImageField(...)` para el campo del botón
- guardar el PDF actualizado

```java
public static void addImageAppearanceToButtonField(Path inputFile, Path imageFile, Path outputFile) throws Exception {
    Form form = new Form();
    try (InputStream imageStream = Files.newInputStream(imageFile)) {
        form.bindPdf(inputFile.toString());
        form.fillImageField("Image1_af_image", imageStream);
        form.save(outputFile.toString());
    } finally {
        form.close();
    }
}
```
