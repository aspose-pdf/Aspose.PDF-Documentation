---
title: Anotaciones basadas en texto usando Java
linktitle: Anotaciones de texto
type: docs
weight: 10
url: /java/pdfannotationeditor-class/text-based-annotations/
description: Aprenda a agregar, inspeccionar y eliminar texto, texto libre y anotaciones tachadas en documentos PDF utilizando Java.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: Trabajar con anotaciones de texto PDF en Java
Abstract: Este artículo explica cómo crear, leer y eliminar anotaciones basadas en texto en documentos PDF utilizando Java. Cubre anotaciones de texto, anotaciones de texto libre y anotaciones tachadas basadas en implementaciones de ejemplo de Java.
---
## Agregar una anotación de texto


1. Abra el PDF de entrada y seleccione la página donde se debe colocar la anotación de texto.

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

## 
Añadir una anotación de texto libre

1. Cargue el PDF de origen y seleccione la página de destino y el rectángulo para la nota de texto libre.

2. Cree `FreeTextAnnotation`, inicialice su apariencia predeterminada y establezca el título y el color.

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
