---
title: Anotaciones de seguridad usando Java
linktitle: Anotaciones de seguridad
type: docs
weight: 75
url: /es/java/security-annotations/
description: Aprenda cómo marcar texto para redacción, aplicar anotaciones de redacción y redactar áreas seleccionadas de la página en archivos PDF usando Aspose.PDF for Java.
lastmod: "2026-09-03"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Redacte contenido PDF confidencial en Java con anotaciones de seguridad.
Abstract: Este artículo explica cómo trabajar con anotaciones de redacción en documentos PDF usando Aspose.PDF for Java. Cubre la marcación de texto coincidente con anotaciones de redacción, la aplicación permanente de redacciones y la redacción de áreas seleccionadas basándose en los rectángulos de ubicación de imágenes detectados.
---
Los flujos de trabajo de anotaciones de seguridad en esta sección se centran en preparar y aplicar redacciones al contenido sensible de PDF.

## Marcar texto con anotaciones de redacción

Utilice este ejemplo cuando el texto coincidente debe estar cubierto por anotaciones de redacción antes de que la redacción se aplique permanentemente.

1. Abra el PDF de origen [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Busque el texto objetivo y cree un [RedactionAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/redactionannotation/) para cada coincidencia.
1. Configure la apariencia de la redactación y guarde el documento.

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

Este ejemplo aplica permanentemente anotaciones de redacción que ya existen en la página.

1. Abra el PDF de origen [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Recopilar anotaciones del tipo [AnnotationType](https://reference.aspose.com/pdf/java/com.aspose.pdf/annotationtype/).`Redaction`.
1. Llamada `redact()` en cada anotación recopilada y guarda el archivo actualizado.

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

1. Abra el PDF de origen [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Detecte el rectángulo objetivo en la página, por ejemplo a partir de una ubicación de imagen.
1. Crear un [RedactionAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/redactionannotation/) para esa área y guardar el documento.

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

## Temas relacionados de anotaciones

- [Anotaciones interactivas](/pdf/es/java/interactive-annotations/)
- [Anotaciones de marcado](/pdf/es/java/markup-annotations/)
- [Anotaciones de forma](/pdf/es/java/shape-annotations/)
- [Anotaciones de texto](/pdf/es/java/text-based-annotations/)
- [Anotaciones de marca de agua](/pdf/es/java/watermark-annotations/)
- [Importar y exportar anotaciones](/pdf/es/java/import-export-annotations/)
