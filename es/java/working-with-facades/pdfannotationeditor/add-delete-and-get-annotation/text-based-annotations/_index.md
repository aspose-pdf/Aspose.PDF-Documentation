---
title: Text Based Annotations using Java
linktitle: Text Annotations
type: docs
weight: 10
url: /java/pdfannotationeditor-class/text-based-annotations/
description: Aprenda a agregar, inspeccionar y eliminar texto, texto libre y anotaciones tachadas en documentos PDF utilizando Java.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: Work with text PDF annotations in Java
Abstract: This article explains how to create, read, and remove text-based annotations in PDF documents using Java. It covers text annotations, free text annotations, and strikeout annotations based on the Java example implementations.
---
## Add a text annotation

1. Open the input PDF and target the page where the text annotation should be placed.
2. Cree `TextAnnotation`, defina su rectángulo y establezca su título, asunto, banderas y color.
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

## Añadir una anotación de texto libre

1. Cargue el PDF de origen y seleccione la página de destino y el rectángulo para la nota de texto libre.
2. Cree `FreeTextAnnotation`, inicialice su apariencia predeterminada y establezca el título y el color.
3. Add the annotation to the page and save the result.

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
