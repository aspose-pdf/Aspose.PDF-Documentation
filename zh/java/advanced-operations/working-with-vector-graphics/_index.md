---
title: 在 Java 中使用矢量图形
linktitle: 使用矢量图形
type: docs
weight: 100
url: /java/working-with-vector-graphics/
description: 了解如何使用 Java 提取、移动、删除、复制和导出 PDF 文档中的矢量图形。
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 使用 GraphicsAbsorber 在 Java 中检查和操作 PDF 矢量图形
Abstract: 本文介绍如何使用 GraphicsAbsorber 类在 Aspose.PDF for Java 中处理矢量图形。了解如何检查页面上的矢量元素、移动或删除它们、在页面之间复制图形以及将矢量内容导出到 SVG。
---
Aspose.PDF for Java 通过`GraphicsAbsorber` 和`GraphicElement` 对象公开矢量内容。这使您可以检查页面上的低级矢量元素，然后更新、删除、复制或导出它们。

## 检查页面上的矢量图形

当您需要枚举向量元素并检查其页面、位置和运算符计数时，请使用此示例。

1. 打开源 PDF [文档](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)。
1. 创建一个[GraphicsAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/vector/graphicsabsorber/)并访问目标页面。
1. 迭代吸收的 [GraphicElement](https://reference.aspose.com/pdf/java/com.aspose.pdf/vector/graphicelement/) 对象并输出它们的属性。

```java
public static void usingGraphicsAbsorber(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        GraphicsAbsorber graphicsAbsorber = new GraphicsAbsorber();
        try {
            Page page = document.getPages().get_Item(1);
            graphicsAbsorber.visit(page);
            for (GraphicElement element : graphicsAbsorber.getElements()) {
                System.out.println("Page Number: " + element.getSourcePage().getNumber());
                System.out.println("Position: (" + element.getPosition().getX() + ", "
                        + element.getPosition().getY() + ")");
                System.out.println("Number of Operators: " + element.getOperators().size());
            }
        } finally {
            graphicsAbsorber.dispose();
        }
    }
}
```

## 在页面上移动矢量图形

当所有检测到的向量元素都应移动到新位置时，请使用此示例。

1. 打开源 PDF [文档](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)。
1. 使用 [GraphicsAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/vector/graphicsabsorber/) 访问目标页面并暂时抑制更新。
1. 更改每个吸收元素的位置，恢复更新并保存文档。

```java
public static void moveGraphics(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        GraphicsAbsorber graphicsAbsorber = new GraphicsAbsorber();
        try {
            Page page = document.getPages().get_Item(1);
            graphicsAbsorber.visit(page);
            graphicsAbsorber.suppressUpdate();
            for (GraphicElement element : graphicsAbsorber.getElements()) {
                Point position = element.getPosition();
                element.setPosition(new Point(position.getX() + 150, position.getY() - 10));
            }
            graphicsAbsorber.resumeUpdate();
        } finally {
            graphicsAbsorber.dispose();
        }
        document.save(outputFile.toString());
    }
    System.out.println("Vector graphics moved in " + outputFile);
}
```

## 通过元素删除按位置删除矢量图形

当需要一一删除特定矩形内的向量元素时，请使用此示例。

1. 打开源 PDF [文档](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)。
1. 使用 [GraphicsAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/vector/graphicsabsorber/) 访问页面并定义目标 [矩形](https://reference.aspose.com/pdf/java/com.aspose.pdf/rectangle/)。
1. 删除匹配的元素，恢复更新，然后保存文档。

```java
public static void removeGraphicsMethod1(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        GraphicsAbsorber graphicsAbsorber = new GraphicsAbsorber();
        try {
            Page page = document.getPages().get_Item(1);
            Rectangle rectangle = new Rectangle(70, 248, 170, 252, true);
            graphicsAbsorber.visit(page);
            graphicsAbsorber.suppressUpdate();
            for (GraphicElement element : graphicsAbsorber.getElements()) {
                if (rectangle.contains(element.getPosition(), false)) {
                    element.remove();
                }
            }
            graphicsAbsorber.resumeUpdate();
        } finally {
            graphicsAbsorber.dispose();
        }
        document.save(outputFile.toString());
    }
    System.out.println("Vector graphics removed with method 1 in " + outputFile);
}
```

## 通过删除集合来删除矢量图形

当应首先收集匹配的向量元素，然后在一页操作中删除时，请使用此示例。

1. 打开源 PDF [文档](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)。
1. 使用 [GraphicsAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/vector/graphicsabsorber/) 访问页面并收集匹配的元素。
1. 从页面内容中删除收集的图形并保存更新的文档。

```java
public static void removeGraphicsMethod2(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        GraphicsAbsorber graphicsAbsorber = new GraphicsAbsorber();
        try {
            Page page = document.getPages().get_Item(1);
            Rectangle rectangle = new Rectangle(70, 248, 170, 252, true);
            graphicsAbsorber.visit(page);
            GraphicElementCollection removedElements = new GraphicElementCollection();
            for (GraphicElement element : graphicsAbsorber.getElements()) {
                if (rectangle.contains(element.getPosition(), false)) {
                    removedElements.add(element);
                }
            }
            page.getContents().suppressUpdate();
            page.deleteGraphics(removedElements);
            page.getContents().resumeUpdate();
        } finally {
            graphicsAbsorber.dispose();
        }
        document.save(outputFile.toString());
    }
    System.out.println("Vector graphics removed with method 2 in " + outputFile);
}
```

## Copy vector graphics to another page element by element

当每个吸收的向量元素应单独添加到新页面时，请使用此示例。

1. Open the source PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) and add a destination page.
1. 使用 [GraphicsAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/vector/graphicsabsorber/) 访问源页面。
1. 将每个 [GraphicElement](https://reference.aspose.com/pdf/java/com.aspose.pdf/vector/graphicelement/) 添加到目标页面并保存文档。

```java
public static void addToAnotherPageMethod1(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        GraphicsAbsorber graphicsAbsorber = new GraphicsAbsorber();
        try {
            Page page1 = document.getPages().get_Item(1);
            Page page2 = document.getPages().add();
            graphicsAbsorber.visit(page1);
            page2.getContents().suppressUpdate();
            for (GraphicElement element : graphicsAbsorber.getElements()) {
                element.addOnPage(page2);
            }
            page2.getContents().resumeUpdate();
        } finally {
            graphicsAbsorber.dispose();
        }
        document.save(outputFile.toString());
    }
    System.out.println("Vector graphics copied with method 1 in " + outputFile);
}
```

## 将矢量图形作为集合复制到另一个页面

当应在一次调用中将整个吸收的矢量图形集合复制到新页面时，请使用此示例。

1. 打开源 PDF [文档](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 并添加目标页面。
1. 使用 [GraphicsAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/vector/graphicsabsorber/) 访问源页面。
1. 将吸收的图形集合添加到目标页面并保存文档。

```java
public static void addToAnotherPageMethod2(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        GraphicsAbsorber graphicsAbsorber = new GraphicsAbsorber();
        try {
            Page page1 = document.getPages().get_Item(1);
            Page page2 = document.getPages().add();
            graphicsAbsorber.visit(page1);
            page2.getContents().suppressUpdate();
            page2.addGraphics(graphicsAbsorber.getElements());
            page2.getContents().resumeUpdate();
        } finally {
            graphicsAbsorber.dispose();
        }
        document.save(outputFile.toString());
    }
    System.out.println("Vector graphics copied with method 2 in " + outputFile);
}
```
