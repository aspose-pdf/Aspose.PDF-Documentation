---
title: Anotaciones de seguridad usando Java
linktitle: Anotaciones de seguridad
type: docs
weight: 75
url: /java/security-annotations/
description: Aprenda a marcar texto para redacción, aplicar anotaciones de redacción y redactar áreas de páginas seleccionadas en archivos PDF utilizando Aspose.PDF para Java.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Redacte contenido PDF confidencial en Java con anotaciones de seguridad.
Abstract: Este artículo explica cómo trabajar con anotaciones de redacción en documentos PDF usando Aspose.PDF para Java. Cubre marcar texto coincidente con anotaciones de redacción, aplicar redacciones permanentemente y redactar áreas seleccionadas en función de los rectángulos de ubicación de imágenes detectadas.
---
Los flujos de trabajo de anotaciones de seguridad en esta sección se centran en preparar y aplicar redacciones a contenido PDF confidencial.


## 
Marcar texto con anotaciones de redacción



Utilice este ejemplo cuando el texto coincidente deba estar cubierto por anotaciones de redacción antes de que la redacción se aplique permanentemente.


1. 
Abra el PDF de origen [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. 
Busque el texto de destino y cree una [RedactionAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/redactionannotation/) para cada coincidencia.
1. Configure la apariencia de redacción y guarde el documento.


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

## 
Aplicar redacciones existentes



Este ejemplo aplica permanentemente anotaciones de redacción que ya existen en la página.


1. 
Abra el PDF de origen [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. 
Recopile anotaciones de tipo [AnnotationType](https://reference.aspose.com/pdf/java/com.aspose.pdf/annotationtype/).`Redaction`.
1. Llame a `redact()` en cada anotación recopilada y guarde el archivo actualizado.


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

## 
Redactar un área de página seleccionada



Utilice este enfoque cuando el contenido de destino se identifique por posición en lugar de por texto coincidente.


1. 
Abra el PDF de origen [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. 
Detecta el rectángulo de destino en la página, por ejemplo desde la ubicación de una imagen.
1. Cree una [RedactionAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/redactionannotation/) para esa área y guarde el documento.


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

## 
Temas de anotaciones relacionados


- 
[Anotaciones interactivas](/pdf/java/interactive-annotations/)

- 
[Anotaciones de marcado](/pdf/java/markup-annotations/)

- 
[Anotaciones de forma](/pdf/java/shape-annotations/)
- [Anotaciones de texto](/pdf/java/text-based-annotations/)

- 
[Anotaciones de marca de agua](/pdf/java/watermark-annotations/)

- 
[Importar y exportar anotaciones](/pdf/java/import-export-annotations/)
