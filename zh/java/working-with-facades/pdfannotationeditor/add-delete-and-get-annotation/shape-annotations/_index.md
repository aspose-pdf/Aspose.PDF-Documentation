---
title: 通过 Java 进行形状注释
linktitle: 形状注释
type: docs
weight: 40
url: /java/pdfannotationeditor-class/shape-annotations/
description: 了解如何使用 Java 在 PDF 文档中添加、检查和删除正方形、圆形、多边形和折线注释。
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: 在 Java 中使用几何 PDF 注释
Abstract: 本文介绍如何使用 Java 创建、检查和删除 PDF 文档中的几何注释。它涵盖了带有颜色、不透明度、弹出窗口和点配置的正方形、圆形、多边形和折线注释。
---
## 添加形状注释

1. 打开输入 PDF 并选择将包含形状注释的页面和矩形。
2. 创建所需的形状注释，然后根据需要设置其标题、颜色、不透明度和点。
3. Add the annotation to the page and save the modified PDF.

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
