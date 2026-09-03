---
title: Anotaciones de seguridad usando Java
linktitle: Anotaciones de seguridad
type: docs
weight: 60
url: /java/pdfannotationeditor-class/security-annotations/
description: Aprenda a marcar texto para redacción, aplicar anotaciones de redacción y redactar áreas de página seleccionadas en archivos PDF utilizando Java.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: Redactar contenido PDF confidencial en Java con anotaciones de seguridad
Abstract: Este artículo explica cómo trabajar con anotaciones de redacción en documentos PDF usando Java. Cubre marcar texto coincidente con anotaciones de redacción, aplicar redacciones permanentemente y redactar áreas seleccionadas en función de los rectángulos de ubicación de imágenes detectadas.
---
## Marcar texto para redacción


1. Cargue el PDF y busque en todas las páginas el texto que debe redactarse.

2. Cree un `RedactionAnnotation` para cada fragmento de texto coincidente y configure su apariencia.

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
