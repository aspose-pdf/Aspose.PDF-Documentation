---
title: Anotaciones de marcas de agua usando Java
linktitle: Anotaciones de marca de agua
type: docs
weight: 70
url: /java/watermark-annotations/
description: Aprenda a agregar, inspeccionar y eliminar anotaciones de marcas de agua en documentos PDF usando Aspose.PDF para Java.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Trabaje con anotaciones de marcas de agua en archivos PDF utilizando Java.
Abstract: Este artículo explica cómo crear, inspeccionar y eliminar anotaciones de marcas de agua en documentos PDF utilizando Aspose.PDF para Java. Cubre agregar una anotación de marca de agua de texto con opacidad y estado de texto personalizados, leer áreas de anotación de marca de agua existentes y eliminar anotaciones de marca de agua.
---
Las anotaciones de marca de agua le permiten colocar contenido superpuesto reutilizable en una página y al mismo tiempo administrarlo a través de la colección de anotaciones.


## 
Agregar una anotación de marca de agua



Utilice este ejemplo cuando necesite una anotación de marca de agua de texto con configuración de fuente y opacidad personalizadas.


1. Abra el PDF de origen [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. Cree una [Anotación de marca de agua](https://reference.aspose.com/pdf/java/com.aspose.pdf/watermarkannotation/) y agréguela a la página.
1. Configure el [TextState](https://reference.aspose.com/pdf/java/com.aspose.pdf/textstate/), el texto de la marca de agua y la opacidad, luego guarde el documento.


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

## 
Obtener anotaciones de marcas de agua



Este ejemplo escanea la colección de anotaciones e imprime el rectángulo de cada anotación de marca de agua.


1. Abra el PDF de origen [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. Repita las anotaciones en la página de destino.
1. Filtre las anotaciones por [AnnotationType](https://reference.aspose.com/pdf/java/com.aspose.pdf/annotationtype/).`Watermark` e imprima sus rectángulos.


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

## 
Eliminar anotaciones de marcas de agua



Utilice este enfoque cuando las anotaciones de marcas de agua existentes deban eliminarse del documento.


1. Abra el PDF de origen [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. Recopile anotaciones de tipo [AnnotationType](https://reference.aspose.com/pdf/java/com.aspose.pdf/annotationtype/).`Watermark`.
1. Elimine las anotaciones recopiladas y guarde el archivo de salida.


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

## 
Temas de anotaciones relacionados


- [Anotaciones interactivas](/pdf/java/interactive-annotations/)

- [Anotaciones de marcado](/pdf/java/markup-annotations/)

- [Anotaciones de seguridad](/pdf/java/security-annotations/)
- [Anotaciones de forma](/pdf/java/shape-annotations/)

- [Anotaciones de texto](/pdf/java/text-based-annotations/)

- [Importar y exportar anotaciones](/pdf/java/import-export-annotations/)
