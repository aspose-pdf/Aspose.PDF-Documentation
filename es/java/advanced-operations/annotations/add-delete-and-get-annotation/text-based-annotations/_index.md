---
title: Anotaciones basadas en texto usando Java
linktitle: Anotaciones de texto
type: docs
weight: 10
url: /java/text-based-annotations/
description: Aprenda a crear, inspeccionar y eliminar anotaciones de PDF basadas en texto utilizando Aspose.PDF para Java, incluido texto libre, resaltado, tachado, garabato y subrayado.
lastmod: "2026-08-19"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Trabaje con anotaciones de texto PDF en Java.
Abstract: Este artículo demuestra cómo trabajar con cinco tipos de anotaciones basadas en texto en Aspose.PDF para Java, incluidas anotaciones de texto libre, resaltado, tachado, garabateado y subrayado. Aprenda a agregar, recuperar y eliminar anotaciones, además de técnicas avanzadas como marcar texto y aplanar etiquetas interactivas.
---
Las anotaciones basadas en texto permiten a revisores y desarrolladores agregar notas interactivas, resaltar y marcar documentos PDF sin alterar el contenido principal. Esta sección cubre cinco tipos de anotaciones prácticas utilizadas en flujos de trabajo de revisión de documentos, escenarios de cumplimiento y ciclos de retroalimentación colaborativa.


## 
Referencia rápida: tipos de anotaciones



Este artículo cubre los siguientes tipos de anotaciones basadas en texto:


- **Texto libre**: cuadros de texto editables para agregar notas y comentarios

- **Destacado**: Énfasis visual en pasajes de texto importantes
- **Tachar**: marcar el texto para eliminarlo o revisarlo durante la revisión.

- **Squiggly**: subrayado ondulado para indicar errores o inquietudes

- **Subrayado**: énfasis de subrayado tradicional con precisión de cuatro puntos opcional


## 
Agregar, obtener y eliminar anotaciones de texto libre



Las anotaciones de texto libre actúan como cuadros de texto flotantes que se pueden editar sin afectar la estructura del documento. Utilice estos ejemplos para agregar cuadros de comentarios, inspeccionar sus propiedades o eliminarlos.

### Añadir anotaciones de texto libre


1. Abra el PDF de origen [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. Cree una [FreeTextAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/freetextannotation/) con un rectángulo y configuraciones de apariencia.

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

### 
Obtenga anotaciones de texto gratis

1. Abra el PDF de origen [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. Repita las anotaciones en la página y filtre por [AnnotationType.FreeText](https://reference.aspose.com/pdf/java/com.aspose.pdf/annotationtype/).

1. Recupera las propiedades o límites de la anotación.


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

### 
Eliminar anotaciones de texto libre


1. Abra el PDF de origen [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Encuentre anotaciones de texto libre recorriendo las anotaciones de la página y filtrando por tipo.

1. Agregue anotaciones coincidentes a una lista de eliminación y elimínelas de la página.

1. Guarde el documento actualizado.


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

## 
Agregar, obtener y eliminar anotaciones destacadas



Las anotaciones destacadas marcan pasajes importantes con una superposición semitransparente. Utilice estos ejemplos para crear resaltados para revisión de documentos, localizar resaltados existentes y limpiar marcas.

### Agregar anotaciones resaltadas


1. Abra el PDF de origen [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. Cree una [HighlightAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/highlightannotation/) con un rectángulo que defina el área resaltada.

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

### 
Obtener anotaciones destacadas

1. Abra el PDF de origen [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. Itere a través de las anotaciones y filtre por [AnnotationType.Highlight](https://reference.aspose.com/pdf/java/com.aspose.pdf/annotationtype/).

1. Lea las propiedades de anotación, como límites o color.


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

### 
Eliminar anotaciones resaltadas


1. Abra el PDF de origen [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Recopile anotaciones destacadas filtrándolas por tipo.

1. Elimine cada anotación de la página.

1. Guarde el documento actualizado.


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

## 
Agregar, obtener y eliminar anotaciones tachadas



Las anotaciones tachadas tachan el texto para indicar eliminación, rechazo o revisión. Utilice estos ejemplos para aplicar marcado tachado durante la revisión de documentos, buscar texto marcado y eliminar anotaciones tachadas.

### Agregar anotaciones tachadas


1. Abra el PDF de origen [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. Cree una [StrikeOutAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/strikeoutannotation/) con un rectángulo, título y color.

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

### 
Obtener anotaciones tachadas

1. Abra el PDF de origen [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. Repita las anotaciones y filtre por [AnnotationType.StrikeOut](https://reference.aspose.com/pdf/java/com.aspose.pdf/annotationtype/).

1. Leer metadatos o límites de anotaciones.


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

### 
Eliminar anotaciones tachadas


1. Abra el PDF de origen [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Recopile anotaciones tachadas filtrando por tipo.

1. Elimine cada anotación de la página.

1. Guarde el documento actualizado.


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

## 
Agregar, obtener y eliminar anotaciones onduladas



Las anotaciones onduladas (subrayados ondulados) resaltan posibles errores, inquietudes o elementos que requieren atención. Utilice estos ejemplos para marcar texto problemático, inspeccionar anotaciones onduladas y eliminarlas de los documentos.

### Agregar anotaciones onduladas


1. Abra el PDF de origen [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. Cree una [SquigglyAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/squigglyannotation/) con un rectángulo y un título.

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

### 
Obtener anotaciones onduladas

1. Abra el PDF de origen [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. Itere a través de las anotaciones y filtre por [AnnotationType.Squiggly](https://reference.aspose.com/pdf/java/com.aspose.pdf/annotationtype/).

1. Leer límites de anotaciones o metadatos.


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

### 
Eliminar anotaciones onduladas


1. Abra el PDF de origen [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Recopile anotaciones onduladas filtrando por tipo.

1. Elimine cada anotación de la página.

1. Guarde el documento actualizado.


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

## 
Agregar, obtener y eliminar anotaciones subrayadas



Las anotaciones subrayadas enfatizan pasajes importantes con un subrayado tradicional. Utilice estos ejemplos para crear subrayados, leer contenido de texto marcado y eliminar anotaciones subrayadas de las páginas.

### Agregar anotaciones subrayadas


1. Abra el PDF de origen [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. Cree una [Anotación subrayada](https://reference.aspose.com/pdf/java/com.aspose.pdf/underlineannotation/) con un rectángulo y un color.

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

### 
Obtener anotaciones subrayadas

1. Abra el PDF de origen [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. Repita las anotaciones y filtre por [AnnotationType.Underline](https://reference.aspose.com/pdf/java/com.aspose.pdf/annotationtype/).

1. Leer propiedades o límites de anotación.


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

### 
Eliminar anotaciones subrayadas


1. Abra el PDF de origen [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Recopile anotaciones subrayadas filtrando por tipo.

1. Elimine cada anotación de la página.

1. Guarde el documento actualizado.


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

## 
Agregar una anotación subrayada con puntos cuádruples



Este ejemplo define el área subrayada explícitamente mediante puntos cuádruples derivados de un rectángulo.

1. Abra el PDF de origen [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. Cree una [Anotación subrayada](https://reference.aspose.com/pdf/java/com.aspose.pdf/underlineannotation/) y calcule sus puntos cuádruples.

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

## 
Obtener texto marcado a partir de anotaciones subrayadas



Recupere el contenido del texto real cubierto por anotaciones subrayadas. Estos ejemplos muestran dos enfoques: leer el texto marcado completo como una sola cadena o procesar fragmentos de texto individualmente para un análisis detallado.

1. Abra el PDF de origen [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. Repita las anotaciones subrayadas en la página.

1. Lea `getMarkedText()` o `getMarkedTextFragments()` e imprima los resultados.


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

## 
Eliminar anotaciones subrayadas por título



Elimine anotaciones de forma selectiva filtrando propiedades de metadatos como el título. Este enfoque permite la limpieza específica de anotaciones por autor o propósito.

1. Abra el PDF de origen [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. Filtre las anotaciones subrayadas por título.

1. Elimine las anotaciones coincidentes y guarde el documento actualizado.


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

## 
Agregar y aplanar una anotación subrayada



Convierta una anotación subrayada interactiva en contenido de página permanente aplanándola. Esto evita más ediciones y al mismo tiempo conserva la apariencia subrayada en cualquier visor de PDF.

1. Abra el PDF de origen [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. Agregue una [Anotación subrayada](https://reference.aspose.com/pdf/java/com.aspose.pdf/underlineannotation/) a la página.

1. Llame a `flatten()` en la anotación y guarde el archivo de salida.


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

## 
Temas de anotaciones relacionados


- [Anotaciones interactivas](/pdf/java/interactive-annotations/)
- [Anotaciones de marcado](/pdf/java/markup-annotations/)

- [Anotaciones de seguridad](/pdf/java/security-annotations/)

- [Anotaciones de forma](/pdf/java/shape-annotations/)

- [Anotaciones de marca de agua](/pdf/java/watermark-annotations/)

- [Importar y exportar anotaciones](/pdf/java/import-export-annotations/)
