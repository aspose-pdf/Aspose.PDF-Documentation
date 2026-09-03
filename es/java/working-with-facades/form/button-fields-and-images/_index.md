---
title: Campos de botón e imágenes
linktitle: Campos de botón e imágenes
type: docs
weight: 40
url: /es/java/button-fields-and-images/
description: Aprenda cómo agregar una apariencia de imagen a un campo de botón en un formulario PDF usando la fachada Form en Aspose.PDF for Java.
lastmod: "2026-09-03"
TechArticle: true
AlternativeHeadline: Agregar una apariencia de imagen a un campo de botón PDF en Java
Abstract: Este artículo muestra cómo usar la fachada Form en Aspose.PDF for Java para vincular un formulario PDF, cargar una imagen como flujo, rellenar un campo de botón de imagen y guardar el documento actualizado.
---
El ejemplo Java en `FormExamples.addImageAppearanceToButtonField(...)` muestra cómo actualizar la apariencia de un campo de botón con un flujo de imagen.

El flujo de trabajo es sencillo:

- enlazar el PDF de entrada con `form.bindPdf(...)`
- abra el archivo de imagen con `Files.newInputStream(...)`
- llamar `form.fillImageField(...)` para el campo de botón
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
