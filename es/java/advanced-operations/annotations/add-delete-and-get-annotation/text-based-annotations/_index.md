---
title: Anotaciones basadas en texto usando Java
linktitle: Anotaciones de texto
type: docs
weight: 10
url: /es/java/text-based-annotations/
description: Aprenda cómo crear, inspeccionar y eliminar anotaciones PDF basadas en texto usando Aspose.PDF for Java, incluyendo texto libre, resaltado, tachado, ondulado y subrayado.
lastmod: "2026-09-03"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Trabaje con anotaciones PDF de texto en Java.
Abstract: Este artículo demuestra cómo trabajar con cinco tipos de anotaciones basadas en texto en Aspose.PDF for Java, incluyendo anotaciones de texto libre, resaltado, tachado, ondulado y subrayado. Aprenda a agregar, recuperar y eliminar anotaciones, además de técnicas avanzadas como marcar texto y aplanar el marcado interactivo.
---
Las anotaciones basadas en texto permiten a revisores y desarrolladores agregar notas interactivas, resaltados y marcas a los documentos PDF sin alterar el contenido principal. Esta sección cubre cinco tipos prácticos de anotaciones utilizados en flujos de trabajo de revisión de documentos, escenarios de cumplimiento y ciclos de retroalimentación colaborativa.

## Referencia rápida: Tipos de anotación

Este artículo cubre los siguientes tipos de anotaciones basadas en texto:

- **Texto libre**: Cuadros de texto editables para añadir notas y comentarios
- **Resaltar**: Énfasis visual en pasajes de texto importantes
- **Strikeout**: Marcar texto para eliminación o revisión durante la revisión
- **Squiggly**: Subrayado ondulado para indicar errores o preocupaciones
- **Subrayado**: Énfasis tradicional subrayado con precisión opcional de cuatro puntos

## Agregar, obtener y eliminar anotaciones de texto libre

Las anotaciones de texto libre actúan como cuadros de texto flotantes que pueden editarse sin afectar la estructura del documento. Utiliza estos ejemplos para agregar cuadros de comentarios, inspeccionar sus propiedades o eliminarlos.

### Agregar anotaciones de texto libre

1. Abrir el PDF de origen [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Crear un [FreeTextAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/freetextannotation/) con un rectángulo y configuraciones de apariencia.
1. Agregue la anotación a la página y guarde el documento.

```java
public static void freeTextAnnotationAdd(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        FreeTextAnnotation freeTextAnnotation = new FreeTextAnnotation(
                document.getPages().get_Item(1),
                new Rectangle(299, 713, 308, 720, true),
                new DefaultAppearance());
        freeTextAnnotation.setTitle("Aspose User");
        freeTextAnnotation.setColor(Color.getLightGreen());

        document.getPages().get_Item(1).getAnnotations().add(freeTextAnnotation);
        document.save(outputFile.toString());
    }
}
```

### Obtener anotaciones de texto libre

1. Abrir el PDF de origen [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Iterar a través de las anotaciones en la página y filtrar por [AnnotationType.FreeText](https://reference.aspose.com/pdf/java/com.aspose.pdf/annotationtype/).
1. Recuperar las propiedades de la anotación o los límites.

```java
public static void freeTextAnnotationGet(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (Annotation annotation : document.getPages().get_Item(1).getAnnotations()) {
            if (annotation.getAnnotationType() == AnnotationType.FreeText) {
                System.out.println(annotation.getRect());
            }
        }
    }
}
```

### Eliminar anotaciones de texto libre

1. Abrir el PDF de origen [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Encuentre anotaciones de texto libre iterando a través de las anotaciones de la página y filtrando por tipo.
1. Agrega las anotaciones coincidentes a una lista de eliminación y elimínalas de la página.
1. Guarda el documento actualizado.

```java
public static void freeTextAnnotationDelete(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        List<Annotation> toDelete = new ArrayList<>();
        for (Annotation annotation : document.getPages().get_Item(1).getAnnotations()) {
            if (annotation.getAnnotationType() == AnnotationType.FreeText) {
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

## Agregar, obtener y eliminar anotaciones de resaltado

Las anotaciones de resaltado marcan pasajes importantes con una superposición semitransparente. Usa estos ejemplos para crear resaltados para la revisión de documentos, localizar los resaltados existentes y limpiar el marcado.

### Agregar anotaciones de resaltado

1. Abrir el PDF de origen [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Crear un [HighlightAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/highlightannotation/) con un rectángulo que define el área resaltada.
1. Agregue la anotación a la página y guarde el documento.

```java
public static void textHighlightAnnotationAdd(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        HighlightAnnotation highlightAnnotation = new HighlightAnnotation(
                document.getPages().get_Item(1),
                new Rectangle(300, 750, 320, 770, true));

        document.getPages().get_Item(1).getAnnotations().add(highlightAnnotation);
        document.save(outputFile.toString());
    }
}
```

### Obtener anotaciones resaltadas

1. Abrir el PDF de origen [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Iterar a través de anotaciones y filtrar por [AnnotationType.Highlight](https://reference.aspose.com/pdf/java/com.aspose.pdf/annotationtype/).
1. Lea las propiedades de la anotación, como los límites o el color.

```java
public static void textHighlightAnnotationGet(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (Annotation annotation : document.getPages().get_Item(1).getAnnotations()) {
            if (annotation.getAnnotationType() == AnnotationType.Highlight) {
                System.out.println(annotation.getRect());
            }
        }
    }
}
```

### Eliminar anotaciones de resaltado

1. Abrir el PDF de origen [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Recopilar anotaciones resaltadas filtrando las anotaciones por tipo.
1. Elimine cada anotación de la página.
1. Guarda el documento actualizado.

```java
public static void textHighlightAnnotationDelete(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        List<Annotation> toDelete = new ArrayList<>();
        for (Annotation annotation : document.getPages().get_Item(1).getAnnotations()) {
            if (annotation.getAnnotationType() == AnnotationType.Highlight) {
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

## Agregar, obtener y eliminar anotaciones de tachado

Las anotaciones de tachado cruzan el texto para indicar eliminación, rechazo o revisión. Use estos ejemplos para aplicar el marcado de tachado durante la revisión de documentos, encontrar texto marcado y eliminar las anotaciones de tachado.

### Agregar anotaciones de tachado

1. Abrir el PDF de origen [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Crear un [StrikeOutAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/strikeoutannotation/) con un rectángulo, título y color.
1. Agregue la anotación a la página y guarde el documento.

```java
public static void textStrikeoutAnnotationAdd(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        StrikeOutAnnotation strikeoutAnnotation = new StrikeOutAnnotation(
                document.getPages().get_Item(1),
                new Rectangle(299.988, 713.664, 308.708, 720.769, true));
        strikeoutAnnotation.setTitle("Aspose User");
        strikeoutAnnotation.setSubject("Inserted text 1");
        strikeoutAnnotation.setFlags(AnnotationFlags.Print);
        strikeoutAnnotation.setColor(Color.getBlue());

        document.getPages().get_Item(1).getAnnotations().add(strikeoutAnnotation);
        document.save(outputFile.toString());
    }
}
```

### Obtener anotaciones tachadas

1. Abrir el PDF de origen [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Iterar a través de anotaciones y filtrar por [AnnotationType.StrikeOut](https://reference.aspose.com/pdf/java/com.aspose.pdf/annotationtype/).
1. Leer metadatos o límites de la anotación.

```java
public static void textStrikeoutAnnotationGet(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (Annotation annotation : document.getPages().get_Item(1).getAnnotations()) {
            if (annotation.getAnnotationType() == AnnotationType.StrikeOut) {
                System.out.println(annotation.getRect());
            }
        }
    }
}
```

### Eliminar anotaciones tachadas

1. Abrir el PDF de origen [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Recopile anotaciones tachadas filtrando por tipo.
1. Elimine cada anotación de la página.
1. Guarda el documento actualizado.

```java
public static void textStrikeoutAnnotationDelete(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        List<Annotation> toDelete = new ArrayList<>();
        for (Annotation annotation : document.getPages().get_Item(1).getAnnotations()) {
            if (annotation.getAnnotationType() == AnnotationType.StrikeOut) {
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

## Agregar, obtener y eliminar anotaciones onduladas

Las anotaciones onduladas (subrayados ondulados) resaltan errores potenciales, inquietudes o elementos que requieren atención. Utilice estos ejemplos para marcar texto problemático, inspeccionar anotaciones onduladas y eliminarlas de los documentos.

### Agregar anotaciones onduladas

1. Abrir el PDF de origen [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Crear un [SquigglyAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/squigglyannotation/) con un rectángulo y título.
1. Agregue la anotación a la página y guarde el documento.

```java
public static void textSquigglyAnnotationAdd(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        Page page = document.getPages().get_Item(1);
        SquigglyAnnotation squigglyAnnotation = new SquigglyAnnotation(
                page,
                new Rectangle(67, 317, 261, 459, true));
        squigglyAnnotation.setTitle("John Smith");
        squigglyAnnotation.setColor(Color.getBlue());

        page.getAnnotations().add(squigglyAnnotation);
        document.save(outputFile.toString());
    }
}
```

### Obtener anotaciones onduladas

1. Abrir el PDF de origen [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Iterar a través de anotaciones y filtrar por [AnnotationType.Squiggly](https://reference.aspose.com/pdf/java/com.aspose.pdf/annotationtype/).
1. Leer los límites de la anotación o los metadatos.

```java
public static void textSquigglyAnnotationGet(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (Annotation annotation : document.getPages().get_Item(1).getAnnotations()) {
            if (annotation.getAnnotationType() == AnnotationType.Squiggly) {
                System.out.println(annotation.getRect());
            }
        }
    }
}
```

### Eliminar anotaciones onduladas

1. Abrir el PDF de origen [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Recopila anotaciones onduladas filtrando por tipo.
1. Elimine cada anotación de la página.
1. Guarda el documento actualizado.

```java
public static void textSquigglyAnnotationDelete(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        List<Annotation> toDelete = new ArrayList<>();
        for (Annotation annotation : document.getPages().get_Item(1).getAnnotations()) {
            if (annotation.getAnnotationType() == AnnotationType.Squiggly) {
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

## Agregar, obtener y eliminar anotaciones subrayadas

Las anotaciones de subrayado resaltan pasajes importantes con un subrayado tradicional. Utiliza estos ejemplos para crear subrayados, leer el contenido del texto marcado y eliminar las anotaciones de subrayado de las páginas.

### Agregar anotaciones de subrayado

1. Abrir el PDF de origen [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Crear un [UnderlineAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/underlineannotation/) con un rectángulo y color.
1. Agregue la anotación a la página y guarde el documento.

```java
public static void textUnderlineAnnotationAdd(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        UnderlineAnnotation underlineAnnotation = new UnderlineAnnotation(
                document.getPages().get_Item(1),
                new Rectangle(299.988, 713.664, 308.708, 720.769, true));
        underlineAnnotation.setTitle("Aspose User");
        underlineAnnotation.setSubject("Inserted Underline 1");
        underlineAnnotation.setFlags(AnnotationFlags.Print);
        underlineAnnotation.setColor(Color.getBlue());

        document.getPages().get_Item(1).getAnnotations().add(underlineAnnotation);
        document.save(outputFile.toString());
    }
}
```

### Obtener anotaciones subrayadas

1. Abrir el PDF de origen [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Iterar a través de anotaciones y filtrar por [AnnotationType.Underline](https://reference.aspose.com/pdf/java/com.aspose.pdf/annotationtype/).
1. Leer propiedades o límites de la anotación.

```java
public static void textUnderlineAnnotationGet(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (Annotation annotation : document.getPages().get_Item(1).getAnnotations()) {
            if (annotation.getAnnotationType() == AnnotationType.Underline) {
                System.out.println(annotation.getRect());
            }
        }
    }
}
```

### Eliminar anotaciones subrayadas

1. Abrir el PDF de origen [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Recopile anotaciones subrayadas filtrando por tipo.
1. Elimine cada anotación de la página.
1. Guarda el documento actualizado.

```java
public static void textUnderlineAnnotationDelete(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        List<Annotation> toDelete = new ArrayList<>();
        for (Annotation annotation : document.getPages().get_Item(1).getAnnotations()) {
            if (annotation.getAnnotationType() == AnnotationType.Underline) {
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

## Agregar una anotación subrayada con quad points

Este ejemplo define el área subrayada explícitamente mediante puntos cuádruples derivados de un rectángulo.

1. Abrir el PDF de origen [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Crear un [UnderlineAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/underlineannotation/) y calcular sus puntos quad.
1. Agregue la anotación a la página y guarde el documento.

```java
public static void textUnderlineWithQuadPointsAdd(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        Rectangle rect = new Rectangle(299.988, 713.664, 308.708, 720.769, true);
        UnderlineAnnotation underlineAnnotation = new UnderlineAnnotation(
                document.getPages().get_Item(1), rect);
        underlineAnnotation.setTitle("Aspose User");
        underlineAnnotation.setSubject("Inserted Underline with Quad Points");
        underlineAnnotation.setFlags(AnnotationFlags.Print);
        underlineAnnotation.setColor(Color.getBlue());
        underlineAnnotation.setQuadPoints(new com.aspose.pdf.Point[]{
                new com.aspose.pdf.Point(rect.getLLX(), rect.getLLY()),
                new com.aspose.pdf.Point(rect.getURX(), rect.getLLY()),
                new com.aspose.pdf.Point(rect.getURX(), rect.getURY()),
                new com.aspose.pdf.Point(rect.getLLX(), rect.getURY())
        });

        document.getPages().get_Item(1).getAnnotations().add(underlineAnnotation);
        document.save(outputFile.toString());
    }
}
```

## Obtener texto marcado de anotaciones subrayadas

Recupera el contenido de texto real cubierto por anotaciones de subrayado. Estos ejemplos muestran dos enfoques: leer el texto marcado completo como una única cadena, o procesar los fragmentos de texto individualmente para un análisis detallado.

1. Abrir el PDF de origen [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Iterar a través de las anotaciones de subrayado en la página.
1. Leer cualquiera `getMarkedText()` o `getMarkedTextFragments()` y imprime los resultados.

```java
public static void textUnderlineMarkedTextGet(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (Annotation annotation : document.getPages().get_Item(1).getAnnotations()) {
            if (annotation.getAnnotationType() == AnnotationType.Underline) {
                UnderlineAnnotation ua = (UnderlineAnnotation) annotation;
                System.out.println("Marked text: " + ua.getMarkedText());
            }
        }
    }
}
```

```java
public static void textUnderlineMarkedFragmentsGet(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (Annotation annotation : document.getPages().get_Item(1).getAnnotations()) {
            if (annotation.getAnnotationType() == AnnotationType.Underline) {
                UnderlineAnnotation ua = (UnderlineAnnotation) annotation;
                for (TextFragment fragment : ua.getMarkedTextFragments()) {
                    System.out.println("Fragment text: " + fragment.getText());
                }
            }
        }
    }
}
```

## Eliminar anotaciones subrayadas por título

Elimine anotaciones de forma selectiva filtrando por propiedades de metadatos como el título. Este enfoque permite una limpieza dirigida de anotaciones por autor o propósito.

1. Abrir el PDF de origen [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Filtrar anotaciones subrayadas por título.
1. Elimina las anotaciones coincidentes y guarda el documento actualizado.

```java
public static void textUnderlineByTitleDelete(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        List<UnderlineAnnotation> toDelete = new ArrayList<>();
        for (Annotation annotation : document.getPages().get_Item(1).getAnnotations()) {
            if (annotation.getAnnotationType() == AnnotationType.Underline) {
                UnderlineAnnotation ua = (UnderlineAnnotation) annotation;
                if ("Aspose User".equals(ua.getTitle())) {
                    toDelete.add(ua);
                }
            }
        }
        for (UnderlineAnnotation ua : toDelete) {
            document.getPages().get_Item(1).getAnnotations().delete(ua);
        }
        document.save(outputFile.toString());
    }
}
```

## Agregar y aplanar una anotación de subrayado

Convierta una anotación interactiva de subrayado en contenido permanente de la página aplanándola. Esto evita la edición posterior mientras conserva la apariencia del subrayado en cualquier visor de PDF.

1. Abrir el PDF de origen [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Agregar un [UnderlineAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/underlineannotation/) a la página.
1. Llamar `flatten()` en la anotación y guarde el archivo de salida.

```java
public static void textUnderlineFlattenAdd(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        UnderlineAnnotation underlineAnnotation = new UnderlineAnnotation(
                document.getPages().get_Item(1),
                new Rectangle(299.988, 713.664, 308.708, 720.769, true));
        underlineAnnotation.setTitle("Aspose User");
        underlineAnnotation.setSubject("Inserted Underline to Flatten");
        underlineAnnotation.setFlags(AnnotationFlags.Print);
        underlineAnnotation.setColor(Color.getBlue());

        document.getPages().get_Item(1).getAnnotations().add(underlineAnnotation);
        underlineAnnotation.flatten();

        document.save(outputFile.toString());
    }
}
```

## Temas relacionados con anotaciones

- [Interactive Annotations](/pdf/es/java/interactive-annotations/)
- [Markup Annotations](/pdf/es/java/markup-annotations/)
- [Security Annotations](/pdf/es/java/security-annotations/)
- [Shape Annotations](/pdf/es/java/shape-annotations/)
- [Watermark Annotations](/pdf/es/java/watermark-annotations/)
- [Import and Export Annotations](/pdf/es/java/import-export-annotations/)
