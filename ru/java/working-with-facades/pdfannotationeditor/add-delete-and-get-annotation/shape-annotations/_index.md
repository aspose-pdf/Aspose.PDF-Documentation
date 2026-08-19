---
title: Фигурные аннотации через Java
linktitle: Фигурные аннотации
type: docs
weight: 40
url: /ru/java/pdfannotationeditor-class/shape-annotations/
description: Узнайте, как добавлять, просматривать и удалять аннотации квадратов, кругов, полигонов и полилиний в PDF‑документах с помощью Java.
lastmod: "2026-08-19"
TechArticle: true
AlternativeHeadline: Работа с геометрическими PDF‑аннотациями в Java
Abstract: В этой статье объясняется, как создавать, просматривать и удалять геометрические аннотации в PDF‑документах с использованием Java. Описываются аннотации квадратов, кругов, полигонов и полилиний с настройкой цвета, непрозрачности, всплывающих окон и точек конфигурации.
---
## Добавьте фигурные аннотации

1. Откройте входной PDF и выберите страницу и прямоугольник, которые будут содержать аннотацию формы.
2. Создайте необходимую аннотацию формы, затем при необходимости установите её заголовок, цвета, непрозрачность и точки.
3. Добавьте аннотацию на страницу и сохраните изменённый PDF.

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

