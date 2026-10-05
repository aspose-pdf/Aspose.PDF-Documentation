---
title: Anotaciones de marcado usando Java
linktitle: Anotaciones de marcado
type: docs
weight: 30
url: /es/java/markup-annotations/
description: Aprenda cómo agregar, inspeccionar y eliminar anotaciones de resaltado, subrayado, ondulado y tachado en documentos PDF usando Aspose.PDF for Java.
lastmod: "2026-09-29"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Trabaje con anotaciones de marcado en archivos PDF usando Java.
Abstract: Este artículo explica cómo crear, inspeccionar y eliminar anotaciones de marcado de texto en documentos PDF usando Aspose.PDF for Java. Cubre anotaciones de resaltado, subrayado, ondulado y tachado basadas en los ejemplos de Java del repositorio.
---
Los flujos de trabajo de anotaciones de marcado en esta sección se centran en comentarios de estilo de nota, marcadores de inserción y escenarios agrupados de reemplazo y revisión.

## Agregar una anotación de texto

Utiliza este ejemplo cuando necesites colocar una anotación de texto estilo nota adhesiva con metadatos emergentes en una página.

1. Abra el PDF de origen [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Cree un [`TextAnnotation`](https://reference.aspose.com/pdf/java/com.aspose.pdf/textannotation/) y configure su título, contenido, ícono y ventana emergente.
1. Agregue la anotación a la página y guarde el documento.

```java
public static void textAnnotationAdd(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        TextAnnotation textAnnotation = new TextAnnotation(
                document.getPages().get_Item(1),
                new Rectangle(299.988, 613.664, 428.708, 680.769, true));
        textAnnotation.setTitle("Aspose User");
        textAnnotation.setSubject("Sticky Note");
        textAnnotation.setContents("This is a text annotation added by Aspose.PDF for Java");
        textAnnotation.setFlags(AnnotationFlags.Print);
        textAnnotation.setColor(Color.getBlue());
        textAnnotation.setIcon(TextIcon.Help);

        PopupAnnotation popup = new PopupAnnotation(
                document.getPages().get_Item(1),
                new Rectangle(428.708, 613.664, 528.708, 713.664, true));
        popup.setOpen(true);
        textAnnotation.setPopup(popup);

        document.getPages().get_Item(1).getAnnotations().add(textAnnotation, false);
        document.save(outputFile.toString());
    }
}
```

## Obtener anotaciones de texto

Este ejemplo escanea la página e imprime el rectángulo de cada anotación de texto.

1. Abra el PDF de origen [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Itere a través de las anotaciones en la página.
1. Filtre anotaciones por [`AnnotationType`](https://reference.aspose.com/pdf/java/com.aspose.pdf/annotationtype/).`Text` e imprimir sus rectángulos.

```java
public static void textAnnotationGet(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (Annotation annotation : document.getPages().get_Item(1).getAnnotations()) {
            if (annotation.getAnnotationType() == AnnotationType.Text) {
                System.out.println(annotation.getRect());
            }
        }
    }
}
```

## Eliminar anotaciones de texto

Utilice este enfoque cuando se deben eliminar las anotaciones de texto existentes del documento.

1. Abra el PDF de origen [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Recopile anotaciones del tipo [`AnnotationType`](https://reference.aspose.com/pdf/java/com.aspose.pdf/annotationtype/).`Text`.
1. Elimine las anotaciones recopiladas y guarde el archivo de salida.

```java
public static void textAnnotationDelete(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        List<Annotation> toDelete = new ArrayList<>();
        for (Annotation annotation : document.getPages().get_Item(1).getAnnotations()) {
            if (annotation.getAnnotationType() == AnnotationType.Text) {
                toDelete.add(annotation);
            }
        }
        for (Annotation annotation : toDelete) {
            document.getPages().get_Item(1).getAnnotations().delete(annotation);
        }
        document.save(outputFile.toString());
    }
}
```

## Agregar una anotación de caret

Utilice este ejemplo cuando necesite marcar el texto insertado con una anotación de revisión de estilo caret.

1. Abra el PDF de origen [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Cree un [`CaretAnnotation`](https://reference.aspose.com/pdf/java/com.aspose.pdf/caretannotation/) y configure su ventana emergente y apariencia.
1. Agregue la anotación a la página y guarde el documento.

```java
public static void caretAnnotationsAdd(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        Page page = document.getPages().get_Item(1);

        CaretAnnotation caretAnnotation = new CaretAnnotation(
                page,
                new Rectangle(299.988, 713.664, 308.708, 720.769, true));
        caretAnnotation.setTitle("Aspose User");
        caretAnnotation.setSubject("Inserted text 1");
        caretAnnotation.setFlags(AnnotationFlags.Print);
        caretAnnotation.setColor(Color.getBlue());
        caretAnnotation.setPopup(new PopupAnnotation(
                page,
                new Rectangle(310, 713, 410, 730, true)));
        page.getAnnotations().add(caretAnnotation);

        document.save(outputFile.toString());
    }
}
```

## Obtener anotaciones de caret

Este ejemplo lee las anotaciones caret existentes e imprime sus ubicaciones.

1. Abra el PDF de origen [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Itere a través de las anotaciones de la página.
1. Filtre anotaciones por [`AnnotationType`](https://reference.aspose.com/pdf/java/com.aspose.pdf/annotationtype/).`Caret` e imprimir sus rectángulos.

```java
public static void caretAnnotationsGet(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        Page page = document.getPages().get_Item(1);
        for (Annotation annot : page.getAnnotations()) {
            if (annot.getAnnotationType() == AnnotationType.Caret) {
                System.out.println(annot.getRect());
            }
        }
    }
}
```

## Eliminar anotaciones de cursor

Utilice este enfoque cuando se deban eliminar las anotaciones de inserción de la página.

1. Abra el PDF de origen [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Recopile anotaciones cuyo tipo es [`AnnotationType`](https://reference.aspose.com/pdf/java/com.aspose.pdf/annotationtype/).`Caret`.
1. Elimine las anotaciones recopiladas y guarde el documento de salida.

```java
public static void caretAnnotationsDelete(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        Page page = document.getPages().get_Item(1);

        List<Annotation> caretAnnotations = new ArrayList<>();
        for (Annotation annot : page.getAnnotations()) {
            if (annot.getAnnotationType() == AnnotationType.Caret) {
                caretAnnotations.add(annot);
            }
        }
        for (Annotation annot : caretAnnotations) {
            page.getAnnotations().delete(annot);
        }
        document.save(outputFile.toString());
    }
}
```

## Agregar anotaciones de reemplazo agrupadas

Este ejemplo combina una anotación de inserción con una anotación de tachado para representar un comentario de revisión de estilo de reemplazo.

1. Abra el PDF de origen [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Cree la anotación caret y lo relacionado [`StrikeOutAnnotation`](https://reference.aspose.com/pdf/java/com.aspose.pdf/strikeoutannotation/).
1. Vincule las anotaciones a través de `setInReplyTo` y `setReplyType`, luego guarde el documento.

```java
public static void replaceAnnotationsAdd(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        Page page = document.getPages().get_Item(1);

        CaretAnnotation caretAnnotation = new CaretAnnotation(
                page,
                new Rectangle(361.246, 727.908, 370.081, 735.107, true));
        caretAnnotation.setFlags(AnnotationFlags.Print);
        caretAnnotation.setSubject("Inserted text 2");
        caretAnnotation.setTitle("Aspose User");
        caretAnnotation.setColor(Color.getBlue());
        caretAnnotation.setPopup(new PopupAnnotation(
                page,
                new Rectangle(310, 713, 410, 730, true)));

        StrikeOutAnnotation strikeoutAnnotation = new StrikeOutAnnotation(
                page,
                new Rectangle(318.407, 727.826, 368.916, 740.098, true));
        strikeoutAnnotation.setColor(Color.getBlue());
        strikeoutAnnotation.setQuadPoints(new Point[]{
                new Point(321.66, 739.416),
                new Point(365.664, 739.416),
                new Point(321.66, 728.508),
                new Point(365.664, 728.508)
        });
        strikeoutAnnotation.setSubject("Cross-out");
        strikeoutAnnotation.setInReplyTo(caretAnnotation);
        strikeoutAnnotation.setReplyType(ReplyType.Group);

        page.getAnnotations().add(caretAnnotation);
        page.getAnnotations().add(strikeoutAnnotation);

        document.save(outputFile.toString());
    }
}
```

## Obtener anotaciones de reemplazo agrupadas

Este ejemplo detecta anotaciones de tachado que participan en un flujo de trabajo de reemplazo agrupado.

1. Abra el PDF de origen [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Itere a través de las anotaciones de la página y seleccione anotaciones tachadas.
1. Verifique la relación de respuesta y imprima el rectángulo de las anotaciones coincidentes.

```java
public static void replaceAnnotationsGet(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        Page page = document.getPages().get_Item(1);
        for (Annotation annot : page.getAnnotations()) {
            if (annot.getAnnotationType() == AnnotationType.StrikeOut) {
                StrikeOutAnnotation sa = (StrikeOutAnnotation) annot;
                if (sa.getInReplyTo() != null && sa.getReplyType() == ReplyType.Group) {
                    System.out.println("Replace annotation rect: " + sa.getRect());
                }
            }
        }
    }
}
```

## Eliminar anotaciones de reemplazo agrupadas

Utilice este enfoque cuando se deban eliminar las anotaciones de tachado de reemplazo-revisión de la página.

1. Abra el PDF de origen [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Recopile anotaciones de tachado que representen el marcado de sustitución.
1. Elimine las anotaciones recopiladas y guarde el documento actualizado.

```java
public static void replaceAnnotationsDelete(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        Page page = document.getPages().get_Item(1);

        List<StrikeOutAnnotation> replaceAnnotations = new ArrayList<>();
        for (Annotation annot : page.getAnnotations()) {
            if (annot.getAnnotationType() == AnnotationType.StrikeOut) {
                replaceAnnotations.add((StrikeOutAnnotation) annot);
            }
        }
        for (StrikeOutAnnotation annot : replaceAnnotations) {
            page.getAnnotations().delete(annot);
        }
        document.save(outputFile.toString());
    }
}
```

## Temas relacionados de anotaciones

- [Anotaciones de texto](/pdf/es/java/text-based-annotations/)
- [Anotaciones Interactivas](/pdf/es/java/interactive-annotations/)
- [Anotaciones de forma](/pdf/es/java/shape-annotations/)
- [Anotaciones de medios](/pdf/es/java/media-annotations/)
- [Anotaciones de seguridad](/pdf/es/java/security-annotations/)
- [Anotaciones de marca de agua](/pdf/es/java/watermark-annotations/)
