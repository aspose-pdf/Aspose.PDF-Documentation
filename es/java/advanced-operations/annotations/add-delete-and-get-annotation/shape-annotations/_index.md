---
title: Anotaciones de formas a través de Java
linktitle: Anotaciones de formas
type: docs
weight: 20
url: /java/shape-annotations/
description: Aprenda a agregar, inspeccionar y eliminar anotaciones de cuadrados, círculos, polígonos y polilíneas en documentos PDF utilizando Aspose.PDF para Java.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.5
TechArticle: true
AlternativeHeadline: Trabajar con anotaciones geométricas de PDF en Java.
Abstract: Este artículo explica cómo crear, inspeccionar y eliminar anotaciones geométricas en documentos PDF utilizando Aspose.PDF para Java. Cubre anotaciones de cuadrados, círculos, polígonos y polilíneas con color, opacidad, ventana emergente y configuración de puntos.
---
Las anotaciones de formas en esta sección cubren tipos de anotaciones geométricas como cuadrados, círculos, polígonos, polilíneas y líneas.


## 
Agregue anotaciones de cuadrados, círculos, polígonos y polilíneas



Utilice estos ejemplos cuando necesite colocar anotaciones geométricas con colores personalizados, opacidad, datos emergentes o matrices de puntos.


1. 
Abra el PDF de origen [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. 
Cree la anotación de forma requerida y configure su rectángulo, puntos y propiedades visuales.
1. Agregue la anotación a la página y guarde el documento actualizado.


```java
public static void squareAnnotationAdd(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        SquareAnnotation squareAnnotation = new SquareAnnotation(
                document.getPages().get_Item(1),
                new Rectangle(60, 600, 250, 450, true));
        squareAnnotation.setTitle("John Smith");
        squareAnnotation.setColor(Color.getBlue());
        squareAnnotation.setInteriorColor(Color.getBlueViolet());
        squareAnnotation.setOpacity(0.25);

        document.getPages().get_Item(1).getAnnotations().add(squareAnnotation);
        document.save(outputFile.toString());
    }
}
```

```java
public static void circleAnnotationAdd(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        CircleAnnotation circleAnnotation = new CircleAnnotation(
                document.getPages().get_Item(1),
                new Rectangle(270, 160, 483, 383, true));
        circleAnnotation.setTitle("John Smith");
        circleAnnotation.setColor(Color.getRed());
        circleAnnotation.setInteriorColor(Color.getMistyRose());
        circleAnnotation.setOpacity(0.5);
        circleAnnotation.setPopup(new PopupAnnotation(
                document.getPages().get_Item(1),
                new Rectangle(842, 316, 1021, 459, true)));

        document.getPages().get_Item(1).getAnnotations().add(circleAnnotation);
        document.save(outputFile.toString());
    }
}
```

```java
public static void polygonAnnotationAdd(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        PolygonAnnotation polygonAnnotation = new PolygonAnnotation(
                document.getPages().get_Item(1),
                new Rectangle(200, 300, 400, 400, true),
                new Point[]{
                        new Point(200, 300),
                        new Point(220, 300),
                        new Point(250, 330),
                        new Point(300, 304),
                        new Point(300, 400)
                });
        polygonAnnotation.setTitle("John Smith");
        polygonAnnotation.setColor(Color.getBlue());
        polygonAnnotation.setInteriorColor(Color.getBlueViolet());
        polygonAnnotation.setOpacity(0.25);

        document.getPages().get_Item(1).getAnnotations().add(polygonAnnotation);
        document.save(outputFile.toString());
    }
}
```

```java
public static void polylineAnnotationAdd(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        PolylineAnnotation polylineAnnotation = new PolylineAnnotation(
                document.getPages().get_Item(1),
                new Rectangle(270, 193, 571, 383, true),
                new Point[]{
                        new Point(545, 150),
                        new Point(545, 190),
                        new Point(667, 190),
                        new Point(667, 110),
                        new Point(626, 111)
                });
        polylineAnnotation.setTitle("John Smith");
        polylineAnnotation.setColor(Color.getRed());
        polylineAnnotation.setPopup(new PopupAnnotation(
                document.getPages().get_Item(1),
                new Rectangle(842, 196, 1021, 338, true)));

        document.getPages().get_Item(1).getAnnotations().add(polylineAnnotation);
        document.save(outputFile.toString());
    }
}
```

## 
Obtenga anotaciones de cuadrados, círculos, polígonos y polilíneas



Estos ejemplos inspeccionan la colección de anotaciones de página e imprimen los rectángulos de anotaciones geométricas por tipo.


1. 
Abra el PDF de origen [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. 
Iterar a través de las anotaciones de la página.
1. Filtre por el valor [AnnotationType](https://reference.aspose.com/pdf/java/com.aspose.pdf/annotationtype/) requerido e imprima el rectángulo.


```java
public static void squareAnnotationGet(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (Annotation annotation : document.getPages().get_Item(1).getAnnotations()) {
            if (annotation.getAnnotationType() == AnnotationType.Square) {
                System.out.println(annotation.getRect());
            }
        }
    }
}
```

```java
public static void circleAnnotationGet(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (Annotation annotation : document.getPages().get_Item(1).getAnnotations()) {
            if (annotation.getAnnotationType() == AnnotationType.Circle) {
                System.out.println(annotation.getRect());
            }
        }
    }
}
```

```java
public static void polygonAnnotationGet(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (Annotation annotation : document.getPages().get_Item(1).getAnnotations()) {
            if (annotation.getAnnotationType() == AnnotationType.Polygon) {
                System.out.println(annotation.getRect());
            }
        }
    }
}
```

```java
public static void polylineAnnotationGet(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (Annotation annotation : document.getPages().get_Item(1).getAnnotations()) {
            if (annotation.getAnnotationType() == AnnotationType.PolyLine) {
                System.out.println(annotation.getRect());
            }
        }
    }
}
```

## 
Eliminar anotaciones de cuadrados, círculos, polígonos y polilíneas



Utilice estos ejemplos cuando las anotaciones de formas de un tipo específico deban eliminarse de la página.


1. 
Abra el PDF de origen [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. 
Recopile anotaciones del tipo geométrico requerido.
1. Elimine las anotaciones recopiladas y guarde el archivo de salida.


```java
public static void squareAnnotationDelete(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        List<Annotation> toDelete = new ArrayList<>();
        for (Annotation annotation : document.getPages().get_Item(1).getAnnotations()) {
            if (annotation.getAnnotationType() == AnnotationType.Square) {
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

```java
public static void circleAnnotationDelete(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        List<Annotation> toDelete = new ArrayList<>();
        for (Annotation annotation : document.getPages().get_Item(1).getAnnotations()) {
            if (annotation.getAnnotationType() == AnnotationType.Circle) {
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

```java
public static void polygonAnnotationDelete(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        List<Annotation> toDelete = new ArrayList<>();
        for (Annotation annotation : document.getPages().get_Item(1).getAnnotations()) {
            if (annotation.getAnnotationType() == AnnotationType.Polygon) {
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

```java
public static void polylineAnnotationDelete(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        List<Annotation> toDelete = new ArrayList<>();
        for (Annotation annotation : document.getPages().get_Item(1).getAnnotations()) {
            if (annotation.getAnnotationType() == AnnotationType.PolyLine) {
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
Agregar una anotación de línea



Este ejemplo crea una anotación de línea con finales de flecha, formato de borde y una nota emergente.


1. 
Abra el PDF de origen [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. 
Cree una [LineAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/lineannotation/) con puntos de inicio y finalización.
1. Configure la apariencia, agregue la ventana emergente y guarde el documento.


```java
public static void lineAnnotationAdd(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        LineAnnotation lineAnnotation = new LineAnnotation(
                document.getPages().get_Item(1),
                new Rectangle(550, 93, 562, 439, true),
                new Point(556, 99),
                new Point(556, 443));
        lineAnnotation.setTitle("John Smith");
        lineAnnotation.setColor(Color.getRed());
        lineAnnotation.setStartingStyle(LineEnding.OpenArrow);
        lineAnnotation.setEndingStyle(LineEnding.OpenArrow);

        Border border = new Border(lineAnnotation);
        border.setWidth(3);
        lineAnnotation.setBorder(border);

        PopupAnnotation popup = new PopupAnnotation(
                document.getPages().get_Item(1),
                new Rectangle(842, 124, 1021, 266, true));
        lineAnnotation.setPopup(popup);

        document.getPages().get_Item(1).getAnnotations().add(lineAnnotation);
        document.save(outputFile.toString());
    }
}
```

## 
Obtener anotaciones de línea



Este ejemplo lee anotaciones de línea e imprime sus coordenadas iniciales y finales.


1. 
Abra el PDF de origen [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. 
Repita las anotaciones de la página y seleccione [AnnotationType](https://reference.aspose.com/pdf/java/com.aspose.pdf/annotationtype/).`Line`.
1. Transmita cada coincidencia a [LineAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/lineannotation/) e imprima sus coordenadas.


```java
public static void lineAnnotationsGet(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (Annotation annotation : document.getPages().get_Item(1).getAnnotations()) {
            if (annotation.getAnnotationType() == AnnotationType.Line) {
                LineAnnotation la = (LineAnnotation) annotation;
                System.out.printf("[%s,%s]-[%s,%s]%n",
                        la.getStarting().getX(), la.getStarting().getY(),
                        la.getEnding().getX(), la.getEnding().getY());
            }
        }
    }
}
```

## 
Eliminar anotaciones de línea



Utilice este enfoque cuando las anotaciones de línea deban eliminarse de la página.


1. 
Abra el PDF de origen [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. 
Recopile anotaciones de tipo [AnnotationType](https://reference.aspose.com/pdf/java/com.aspose.pdf/annotationtype/).`Line`.
1. Elimine las anotaciones recopiladas y guarde el documento.


```java
public static void lineAnnotationsDelete(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        Page page = document.getPages().get_Item(1);
        List<Annotation> toDelete = new ArrayList<>();
        for (Annotation annotation : page.getAnnotations()) {
            if (annotation.getAnnotationType() == AnnotationType.Line) {
                toDelete.add(annotation);
            }
        }
        for (Annotation annotation : toDelete) {
            page.getAnnotations().delete(annotation);
        }
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
[Anotaciones de seguridad](/pdf/java/security-annotations/)
- [Anotaciones de texto](/pdf/java/text-based-annotations/)

- 
[Anotaciones de marca de agua](/pdf/java/watermark-annotations/)

- 
[Importar y exportar anotaciones](/pdf/java/import-export-annotations/)
