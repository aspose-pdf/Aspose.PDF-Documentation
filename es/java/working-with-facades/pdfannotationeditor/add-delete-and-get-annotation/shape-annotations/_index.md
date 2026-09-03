---
title: Anotaciones de forma vía Java
linktitle: Anotaciones de forma
type: docs
weight: 40
url: /es/java/pdfannotationeditor-class/shape-annotations/
description: Aprende cómo agregar, inspeccionar y eliminar anotaciones de cuadrado, círculo, polígono y polilínea en documentos PDF usando Java.
lastmod: "2026-09-03"
TechArticle: true
AlternativeHeadline: Trabaja con anotaciones PDF geométricas en Java
Abstract: Este artículo explica cómo crear, inspeccionar y eliminar anotaciones geométricas en documentos PDF usando Java. Cubre anotaciones de cuadrado, círculo, polígono y polilínea con configuración de color, opacidad, ventana emergente y punto.
---
## Agregar anotaciones de forma

1. Abra el PDF de entrada y elija la página y el rectángulo que contendrá la anotación de forma.
2. Cree la anotación de forma requerida, luego establezca su título, colores, opacidad y puntos según sea necesario.
3. Agregue la anotación a la página y guarde el PDF modificado.

```java
public static void squareAnnotationAdd(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        SquareAnnotation squareAnnotation = new SquareAnnotation(
                document.getPages().get_Item(1), new Rectangle(60, 600, 250, 450, true));
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
