---
title: Anotaciones de marca de agua usando Java
linktitle: Anotaciones de marca de agua
type: docs
weight: 70
url: /es/java/pdfannotationeditor-class/watermark-annotations/
description: Aprenda cómo agregar, inspeccionar y eliminar anotaciones de marca de agua en documentos PDF usando Java.
lastmod: "2026-09-03"
TechArticle: true
AlternativeHeadline: Trabaje con anotaciones de marca de agua en archivos PDF usando Java
Abstract: Este artículo explica cómo crear, inspeccionar y eliminar anotaciones de marca de agua en documentos PDF usando Java. Cubre la adición de una anotación de marca de agua de texto con estado de texto personalizado y opacidad, la lectura de áreas de anotaciones de marca de agua existentes y la eliminación de anotaciones de marca de agua.
---
## Agregar una anotación de marca de agua

1. Abra el PDF de entrada y defina el rectángulo donde se colocará la anotación de marca de agua.
2. Crear el `WatermarkAnnotation`, añádelo a la página y configura el estado del texto de la marca de agua y la opacidad.
3. Aplique las líneas de texto de la marca de agua y guarde el PDF modificado.

```java
public static void watermarkAdd(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        WatermarkAnnotation watermarkAnnotation = new WatermarkAnnotation(
                document.getPages().get_Item(1), new Rectangle(100, 0, 400, 100, true));

        document.getPages().get_Item(1).getAnnotations().add(watermarkAnnotation);

        TextState textState = new TextState();
        textState.setForegroundColor(Color.getBlue());
        textState.setFontSize(25);
        textState.setFont(FontRepository.findFont("Arial"));

        watermarkAnnotation.setOpacity(0.5);
        watermarkAnnotation.setTextAndState(new String[]{"HELLO", "Line 1", "Line 2"}, textState);

        document.save(outputFile.toString());
    }
}
```
