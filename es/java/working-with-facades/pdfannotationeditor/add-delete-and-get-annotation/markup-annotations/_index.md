---
title: Anotaciones de marcado usando Java
linktitle: Anotaciones de marcado
type: docs
weight: 20
url: /es/java/pdfannotationeditor-class/markup-annotations/
description: Aprenda cómo agregar, inspeccionar y eliminar anotaciones de resaltado, subrayado, ondulado y tachado en documentos PDF usando Java.
lastmod: "2026-09-03"
TechArticle: true
AlternativeHeadline: Trabaje con anotaciones de marcado en archivos PDF usando Java
Abstract: Este artículo explica cómo crear, inspeccionar y eliminar anotaciones de marcado de texto en documentos PDF usando Java. Cubre anotaciones de resaltado, subrayado, ondulado y tachado basadas en los ejemplos de Java del repositorio.
---
## Agregar anotaciones de resaltado, subrayado, ondulado o tachado

1. Abra el PDF de entrada y seleccione el área de la página donde debe aparecer la anotación de marcado.
2. Cree el tipo de anotación requerido y configure sus metadatos o propiedades visuales.
3. Agregue la anotación a la colección de páginas y guarde el documento.

```java
public static void addTextHighlightAnnotation(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        HighlightAnnotation highlightAnnotation = new HighlightAnnotation(
                document.getPages().get_Item(1), new Rectangle(300, 750, 320, 770, true));
        document.getPages().get_Item(1).getAnnotations().add(highlightAnnotation);
        document.save(outputFile.toString());
    }
}
```

```java
public static void addTextUnderlineAnnotation(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        UnderlineAnnotation underlineAnnotation = new UnderlineAnnotation(
                document.getPages().get_Item(1), new Rectangle(299.988, 713.664, 308.708, 720.769, true));
        underlineAnnotation.setTitle("Aspose User");
        underlineAnnotation.setSubject("Inserted Underline 1");
        underlineAnnotation.setFlags(AnnotationFlags.Print);
        underlineAnnotation.setColor(Color.getBlue());
        document.getPages().get_Item(1).getAnnotations().add(underlineAnnotation);
        document.save(outputFile.toString());
    }
}
```
