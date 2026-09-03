---
title: Anotaciones basadas en texto usando Java
linktitle: Anotaciones de texto
type: docs
weight: 10
url: /es/java/pdfannotationeditor-class/text-based-annotations/
description: Aprenda cómo agregar, inspeccionar y eliminar anotaciones de texto, texto libre y tachado en documentos PDF usando Java.
lastmod: "2026-09-03"
TechArticle: true
AlternativeHeadline: Trabaje con anotaciones de texto PDF en Java
Abstract: Este artículo explica cómo crear, leer y eliminar anotaciones basadas en texto en documentos PDF usando Java. Cubre anotaciones de texto, anotaciones de texto libre y anotaciones de tachado basadas en las implementaciones de ejemplo en Java.
---
## Agregar una anotación de texto

1. Abra el PDF de entrada y seleccione la página donde se debe colocar la anotación de texto.
2. Crear el `TextAnnotation`, define su rectángulo, y establezca su título, asunto, indicadores y color.
3. Agregue la anotación a la página y guarde el documento actualizado.

```java
public static void textAnnotationAdd(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        TextAnnotation textAnnotation = new TextAnnotation(
                document.getPages().get_Item(1), new Rectangle(299.988, 613.664, 428.708, 680.769, true));
        textAnnotation.setTitle("Aspose User");
        textAnnotation.setSubject("Inserted text 1");
        textAnnotation.setFlags(AnnotationFlags.Print);
        textAnnotation.setColor(Color.getBlue());

        document.getPages().get_Item(1).getAnnotations().add(textAnnotation, false);
        document.save(outputFile.toString());
    }
}
```

## Agregar una anotación de texto libre

1. Cargue el PDF de origen y seleccione la página de destino y el rectángulo para la nota de texto libre.
2. Crear el `FreeTextAnnotation`, inicializar su apariencia predeterminada y establecer el título y el color.
3. Agregue la anotación a la página y guarde el resultado.

```java
public static void freeTextAnnotationAdd(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        FreeTextAnnotation freeTextAnnotation = new FreeTextAnnotation(
                document.getPages().get_Item(1),
                new Rectangle(299, 713, 308, 720, true),
                new DefaultAppearance());
        freeTextAnnotation.setTitle("Aspose User");
        freeTextAnnotation.setColor(Color.getLightGreen());

        document.getPages().get_Item(1).getAnnotations().add(freeTextAnnotation);
        document.save(outputFile.toString());
    }
}
```
