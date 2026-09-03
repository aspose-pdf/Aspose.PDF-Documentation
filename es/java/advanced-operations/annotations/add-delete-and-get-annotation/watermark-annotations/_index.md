---
title: Anotaciones de marca de agua usando Java
linktitle: Anotaciones de marca de agua
type: docs
weight: 70
url: /es/java/watermark-annotations/
description: Aprenda cómo agregar, inspeccionar y eliminar anotaciones de marca de agua en documentos PDF usando Aspose.PDF for Java.
lastmod: "2026-09-03"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Trabaje con anotaciones de marca de agua en archivos PDF usando Java.
Abstract: Este artículo explica cómo crear, inspeccionar y eliminar anotaciones de marca de agua en documentos PDF utilizando Aspose.PDF for Java. Cubre la adición de una anotación de marca de agua de texto con estado de texto personalizado y opacidad, la lectura de áreas de anotaciones de marca de agua existentes y la eliminación de anotaciones de marca de agua.
---
Las anotaciones de marca de agua le permiten colocar contenido superpuesto reutilizable en una página mientras lo administra a través de la colección de anotaciones.

## Agregar una anotación de marca de agua

Utilice este ejemplo cuando necesite una anotación de marca de agua de texto con configuraciones de fuente personalizadas y opacidad.

1. Abrir el PDF de origen [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Crear un [WatermarkAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/watermarkannotation/) y añádelo a la página.
1. Configure el [TextState](https://reference.aspose.com/pdf/java/com.aspose.pdf/textstate/), texto de marca de agua, y opacidad, luego guarda el documento.

```java
public static void watermarkAdd(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        Page page = document.getPages().get_Item(1);

        WatermarkAnnotation watermarkAnnotation = new WatermarkAnnotation(
                page,
                new Rectangle(100, 100, 400, 200, true));

        page.getAnnotations().add(watermarkAnnotation);

        TextState textState = new TextState();
        textState.setForegroundColor(Color.getBlue());
        textState.setFontSize(25);
        textState.setFont(FontRepository.findFont("Arial"));

        watermarkAnnotation.setOpacity(0.5);
        watermarkAnnotation.setTextAndState(new String[]{"HELLO", "Line 1", "Line 2"}, textState);

        document.save(outputFile.toString());
    }
}
```

## Obtener anotaciones de marca de agua

Este ejemplo escanea la colección de anotaciones y muestra el rectángulo de cada anotación de marca de agua.

1. Abrir el PDF de origen [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Itera a través de las anotaciones en la página de destino.
1. Filtrar anotaciones por [AnnotationType](https://reference.aspose.com/pdf/java/com.aspose.pdf/annotationtype/).`Watermark` y imprimir sus rectángulos.

```java
public static void watermarkGet(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (Annotation a : document.getPages().get_Item(1).getAnnotations()) {
            if (a.getAnnotationType() == AnnotationType.Watermark) {
                System.out.println(a.getRect());
            }
        }
    }
}
```

## Eliminar anotaciones de marca de agua

Utilice este enfoque cuando se deban eliminar las anotaciones de marca de agua existentes del documento.

1. Abrir el PDF de origen [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Recopilar anotaciones del tipo [AnnotationType](https://reference.aspose.com/pdf/java/com.aspose.pdf/annotationtype/).`Watermark`.
1. Elimina las anotaciones recopiladas y guarda el archivo de salida.

```java
public static void watermarkDelete(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        List<Annotation> toDelete = new ArrayList<>();
        for (Annotation a : document.getPages().get_Item(1).getAnnotations()) {
            if (a.getAnnotationType() == AnnotationType.Watermark) {
                toDelete.add(a);
            }
        }
        for (Annotation a : toDelete) {
            document.getPages().get_Item(1).getAnnotations().delete(a);
        }
        document.save(outputFile.toString());
    }
}
```

## Temas relacionados con anotaciones

- [Interactive Annotations](/pdf/es/java/interactive-annotations/)
- [Markup Annotations](/pdf/es/java/markup-annotations/)
- [Security Annotations](/pdf/es/java/security-annotations/)
- [Shape Annotations](/pdf/es/java/shape-annotations/)
- [Text Annotations](/pdf/es/java/text-based-annotations/)
- [Import and Export Annotations](/pdf/es/java/import-export-annotations/)
