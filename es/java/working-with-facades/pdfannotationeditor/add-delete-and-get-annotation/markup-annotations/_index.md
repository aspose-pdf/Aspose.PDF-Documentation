---
title: Anotaciones de marcado usando Java
linktitle: Anotaciones de marcado
type: docs
weight: 20
url: /java/pdfannotationeditor-class/markup-annotations/
description: Aprenda a agregar, inspeccionar y eliminar anotaciones resaltadas, subrayadas, garabateadas y tachadas en documentos PDF utilizando Java.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: Trabajar con anotaciones de marcado en archivos PDF usando Java
Abstract: Este artículo explica cómo crear, inspeccionar y eliminar anotaciones de marcas de texto en documentos PDF utilizando Java. Cubre anotaciones de resaltado, subrayado, garabatos y tachados basadas en los ejemplos de Java del repositorio.
---
## Agregue anotaciones resaltadas, subrayadas, garabateadas o tachadas


1. 
Abra el PDF de entrada y seleccione el área de la página donde debería aparecer la anotación de marcado.

2. 
Cree el tipo de anotación requerido y configure sus metadatos o propiedades visuales.

3. 
Agregue la anotación a la colección de páginas y guarde el documento.

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
