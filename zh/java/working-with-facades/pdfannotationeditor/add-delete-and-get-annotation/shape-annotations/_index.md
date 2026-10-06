---
title: 通过 Java 的形状批注
linktitle: 形状批注
type: docs
weight: 40
url: /zh/java/pdfannotationeditor-class/shape-annotations/
description: 了解如何使用 Java 在 PDF 文档中添加、检查和删除方形、圆形、多边形和折线批注。
lastmod: "2026-10-06"
TechArticle: true
AlternativeHeadline: 在 Java 中使用几何 PDF 批注
Abstract: 本文解释了如何使用 Java 在 PDF 文档中创建、检查和删除几何批注。它涵盖了带有颜色、不透明度、弹出窗口和点配置的方形、圆形、多边形和折线批注。
---
## 添加形状批注

1. 打开输入 PDF 并选择将包含形状批注的页面和矩形。
2. 创建所需的形状批注，然后在需要时设置其标题、颜色、不透明度和点。
3. 将批注添加到页面并保存修改后的 PDF。

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
