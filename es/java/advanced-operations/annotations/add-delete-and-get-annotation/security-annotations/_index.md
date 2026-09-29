---
title: Anotaciones de seguridad usando Java
linktitle: Anotaciones de seguridad
type: docs
weight: 75
url: /es/java/security-annotations/
description: Aprenda cómo marcar texto para la redacción, aplicar anotaciones de redacción y redactar áreas de página seleccionadas en archivos PDF usando Aspose.PDF for Java.
lastmod: "2026-09-29"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Redacte contenido sensible de PDF en Java con anotaciones de seguridad.
Abstract: Este artículo explica cómo trabajar con anotaciones de redacción en documentos PDF usando Aspose.PDF for Java. Cubre el marcado de texto coincidente con anotaciones de redacción, la aplicación permanente de redacciones y la redacción de áreas seleccionadas basadas en los rectángulos de ubicación de imágenes detectados.
---
Los flujos de trabajo de anotaciones de seguridad en esta sección se centran en preparar y aplicar redacciones a contenido PDF sensible.

## Marcar texto con anotaciones de redacción

Utilice este ejemplo cuando el texto coincidente debe estar cubierto por anotaciones de redacción antes de que la redacción se aplique de forma permanente.

1. Abra el PDF de origen [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Busque el texto objetivo y cree un [`RedactionAnnotation`](https://reference.aspose.com/pdf/java/com.aspose.pdf/redactionannotation/) para cada coincidencia.
1. Configure la apariencia del redactado y guarde el documento.

```java
public static void markTextRedaction(Path inputFile, Path outputFile, String searchTerm) {
    try (Document document = new Document(inputFile.toString())) {
        TextFragmentAbsorber textFragmentAbsorber = new TextFragmentAbsorber(searchTerm);
        TextSearchOptions textSearchOptions = new TextSearchOptions(true);
        textFragmentAbsorber.setTextSearchOptions(textSearchOptions);
        document.getPages().accept(textFragmentAbsorber);

        for (var textFragment : textFragmentAbsorber.getTextFragments()) {
            Page page = textFragment.getPage();
            RedactionAnnotation redactionAnnotation = new RedactionAnnotation(page, textFragment.getRectangle());
            redactionAnnotation.setFillColor(Color.getGray());
            redactionAnnotation.setBorderColor(Color.getRed());
            redactionAnnotation.setColor(Color.getWhite());
            redactionAnnotation.setOverlayText("REDACTED");
            redactionAnnotation.setTextAlignment(HorizontalAlignment.Center);
            redactionAnnotation.setRepeat(true);
            page.getAnnotations().add(redactionAnnotation, true);
        }
        document.save(outputFile.toString());
    }
}
```

## Aplicar redacciones existentes

Este ejemplo aplica de forma permanente anotaciones de redacción que ya existen en la página.

1. Abra el PDF de origen [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Recopile anotaciones de tipo [`AnnotationType`](https://reference.aspose.com/pdf/java/com.aspose.pdf/annotationtype/).`Redaction`.
1. Llame `redact()` en cada anotación recopilada y guarde el archivo actualizado.

```java
public static void applyRedaction(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        List<RedactionAnnotation> redactionAnnotations = new ArrayList<>();
        for (Annotation annotation : document.getPages().get_Item(1).getAnnotations()) {
            if (annotation.getAnnotationType() == AnnotationType.Redaction) {
                redactionAnnotations.add((RedactionAnnotation) annotation);
            }
        }
        for (RedactionAnnotation redactionAnnotation : redactionAnnotations) {
            redactionAnnotation.redact();
        }
        document.save(outputFile.toString());
    }
}
```

## Redactar un área de página seleccionada

Utilice este enfoque cuando el contenido objetivo se identifique por posición en lugar de por coincidencia de texto.

1. Abra el PDF de origen [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Detecte el rectángulo objetivo en la página, por ejemplo a partir de una ubicación de imagen.
1. Cree un [`RedactionAnnotation`](https://reference.aspose.com/pdf/java/com.aspose.pdf/redactionannotation/) para esa área y guarde el documento.

```java
public static void redactArea(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        ImagePlacementAbsorber imagePlacementAbsorber = new ImagePlacementAbsorber();
        Page page = document.getPages().get_Item(1);
        page.accept(imagePlacementAbsorber);

        com.aspose.pdf.Rectangle targetRect = imagePlacementAbsorber.getImagePlacements().get_Item(2).getRectangle();
        RedactionAnnotation redactionAnnotation = new RedactionAnnotation(page, targetRect);
        redactionAnnotation.setFillColor(Color.getGray());
        redactionAnnotation.setBorderColor(Color.getRed());
        redactionAnnotation.setColor(Color.getWhite());
        redactionAnnotation.setOverlayText("REDACTED");
        redactionAnnotation.setTextAlignment(HorizontalAlignment.Center);
        redactionAnnotation.setRepeat(true);

        page.getAnnotations().add(redactionAnnotation, true);
        document.save(outputFile.toString());
    }
}
```

## Temas relacionados de anotación

- [Anotaciones interactivas](/pdf/es/java/interactive-annotations/)
- [Anotaciones de marcado](/pdf/es/java/markup-annotations/)
- [Anotaciones de forma](/pdf/es/java/shape-annotations/)
- [Anotaciones de Texto](/pdf/es/java/text-based-annotations/)
- [Anotaciones de Marca de Agua](/pdf/es/java/watermark-annotations/)
- [Importar y Exportar Anotaciones](/pdf/es/java/import-export-annotations/)
