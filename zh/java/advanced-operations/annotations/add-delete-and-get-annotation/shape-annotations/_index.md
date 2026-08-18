---
title: 通过 Java 进行形状注释
linktitle: 形状注释
type: docs
weight: 20
url: /java/shape-annotations/
description: 了解如何使用 Aspose.PDF for Java 在 PDF 文档中添加、检查和删除正方形、圆形、多边形和折线注释。
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.5
TechArticle: true
AlternativeHeadline: 在 Java 中使用几何 PDF 注释。
Abstract: 本文介绍如何使用 Aspose.PDF for Java 创建、检查和删除 PDF 文档中的几何注释。它涵盖了带有颜色、不透明度、弹出窗口和点配置的正方形、圆形、多边形和折线注释。
---
本节中的形状注释涵盖几何注释类型，例如正方形、圆形、多边形、折线和直线。

## 添加正方形、圆形、多边形和折线注释

当您需要使用自定义颜色、不透明度、弹出数据或点数组放置几何注释时，请使用这些示例。

1. 打开源 PDF [文档](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)。
1. 创建所需的形状注释并配置其矩形、点和视觉属性。
1. 将注释添加到页面并保存更新的文档。

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

## 获取正方形、圆形、多边形和折线注释

这些示例检查页面注释集合并按类型打印几何注释的矩形。

1. 打开源 PDF [文档](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)。
1. 迭代页面注释。
1. 按所需的 [AnnotationType](https://reference.aspose.com/pdf/java/com.aspose.pdf/annotationtype/) 值进行过滤并打印矩形。

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

## 删除正方形、圆形、多边形和折线注释

当应从页面中删除特定类型的形状注释时，请使用这些示例。

1. 打开源 PDF [文档](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)。
1. 收集所需几何类型的注释。
1. 删除收集的注释并保存输出文件。

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

## 添加线条注释

此示例创建带有箭头结尾、边框格式和弹出注释的线条注释。

1. 打开源 PDF [文档](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)。
1. 创建一个带有起点和终点的 [LineAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/lineannotation/)。
1. 配置外观、添加弹出窗口并保存文档。

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

## 获取线路注释

此示例读取行注释并打印其开始和结束坐标。

1. 打开源 PDF [文档](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)。
1. 遍历页面注释并选择 [AnnotationType](https://reference.aspose.com/pdf/java/com.aspose.pdf/annotationtype/).`Line`。
1. 将每个匹配项投射到 [LineAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/lineannotation/) 并打印其坐标。

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

## 删除线注释

当应从页面中删除行注释时，请使用此方法。

1. 打开源 PDF [文档](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)。
1. 收集 [AnnotationType](https://reference.aspose.com/pdf/java/com.aspose.pdf/annotationtype/).`Line` 类型的注释。
1. 删除收集的注释并保存文档。

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

## 相关注释主题

- [交互式注释](/pdf/java/interactive-annotations/)
- [标记注释](/pdf/java/markup-annotations/)
- [安全注释](/pdf/java/security-annotations/)
- [文字注释](/pdf/java/text-based-annotations/)
- [水印注释](/pdf/java/watermark-annotations/)
- [导入和导出注释](/pdf/java/import-export-annotations/)
