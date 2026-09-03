---
title: Anotaciones de seguridad usando Java
linktitle: Anotaciones de seguridad
type: docs
weight: 60
url: /es/java/pdfannotationeditor-class/security-annotations/
description: Aprenda cómo marcar texto para redactar, aplicar anotaciones de redacción y redactar áreas seleccionadas de la página en archivos PDF usando Java.
lastmod: "2026-09-03"
TechArticle: true
AlternativeHeadline: Redactar contenido PDF confidencial en Java con anotaciones de seguridad
Abstract: Este artículo explica cómo trabajar con anotaciones de redacción en documentos PDF usando Java. Cubre la marcación de texto coincidente con anotaciones de redacción, la aplicación permanente de redacciones y la redacción de áreas seleccionadas basadas en rectángulos de ubicación de imágenes detectados.
---
## Marcar texto para redacción

1. Cargue el PDF y busque en todas las páginas el texto que debe ser redactado.
2. Crear un `RedactionAnnotation` para cada fragmento de texto coincidente y configure su apariencia.
3. Agregue las anotaciones de redacción a sus páginas y guarde el documento.

```java
public static void markTextRedaction(Path inputFile, Path outputFile, String searchTerm) {
    try (Document document = new Document(inputFile.toString())) {
        TextFragmentAbsorber textFragmentAbsorber = new TextFragmentAbsorber(searchTerm);
        TextSearchOptions textSearchOptions = new TextSearchOptions(true);
        textFragmentAbsorber.setTextSearchOptions(textSearchOptions);
        document.getPages().accept(textFragmentAbsorber);

        for (TextFragment textFragment : textFragmentAbsorber.getTextFragments()) {
            Page page = textFragment.getPage();
            Rectangle annotationRectangle = textFragment.getRectangle();
            RedactionAnnotation annotation = new RedactionAnnotation(page, annotationRectangle);
            annotation.setFillColor(Color.getGray());
            annotation.setBorderColor(Color.getRed());
            annotation.setColor(Color.getWhite());
            annotation.setOverlayText("REDACTED");
            annotation.setTextAlignment(HorizontalAlignment.Center);
            annotation.setRepeat(true);
            page.getAnnotations().add(annotation, true);
        }

        document.save(outputFile.toString());
    }
}
```
