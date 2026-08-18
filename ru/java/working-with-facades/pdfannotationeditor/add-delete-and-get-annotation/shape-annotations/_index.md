---
title: Аннотации формы через Java
linktitle: Аннотации формы
type: docs
weight: 40
url: /java/pdfannotationeditor-class/shape-annotations/
description: Узнайте, как добавлять, проверять и удалять квадратные, круговые, многоугольные и полилинейные аннотации в документах PDF с помощью Java.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: Работа с геометрическими аннотациями PDF в Java
Abstract: В этой статье объясняется, как создавать, проверять и удалять геометрические аннотации в документах PDF с помощью Java. Он охватывает квадратные, круговые, многоугольные и полилинейные аннотации с цветом, непрозрачностью, всплывающими окнами и конфигурацией точек.
---
## Добавьте аннотации к форме

1. Откройте входной PDF-файл и выберите страницу и прямоугольник, которые будут содержать аннотацию формы.
2. Создайте необходимую аннотацию формы, затем при необходимости задайте ее заголовок, цвета, непрозрачность и точки.
3. Добавьте аннотацию на страницу и сохраните измененный PDF-файл.

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
