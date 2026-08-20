---
title: Anotaciones de formas a través de Java
linktitle: Anotaciones de formas
type: docs
weight: 40
url: /java/pdfannotationeditor-class/shape-annotations/
description: Aprenda a agregar, inspeccionar y eliminar anotaciones de cuadrados, círculos, polígonos y polilíneas en documentos PDF utilizando Java.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: Trabajar con anotaciones geométricas de PDF en Java
Abstract: Este artículo explica cómo crear, inspeccionar y eliminar anotaciones geométricas en documentos PDF utilizando Java. Cubre anotaciones de cuadrados, círculos, polígonos y polilíneas con color, opacidad, ventana emergente y configuración de puntos.
---
## Agregar anotaciones de forma


1. 
Abra el PDF de entrada y elija la página y el rectángulo que contendrán la anotación de forma.

2. 
Cree la anotación de forma requerida y luego establezca su título, colores, opacidad y puntos cuando sea necesario.

3. 
Agregue la anotación a la página y guarde el PDF modificado.

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
