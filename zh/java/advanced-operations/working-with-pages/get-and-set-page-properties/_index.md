---
title: 在 Java 中获取和设置 PDF 页面属性
linktitle: 获取和设置页面属性
type: docs
weight: 90
url: /zh/java/get-and-set-page-properties/
description: 了解如何在 Java 中检查 PDF 页面属性，如页数、盒子、旋转和颜色信息。
lastmod: "2026-10-06"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 使用 Java 检查 PDF 文件的页数、盒子和颜色类型
Abstract: 本文解释了如何使用 Aspose.PDF for Java 检查页面属性。它涵盖了读取页面计数、生成段落并在保存前检查生成的计数、打印所有主要页面框的值，以及识别每个页面的颜色类型。
---
Aspose.PDF for Java 可以检查页面计数、页面框、旋转以及页面颜色类型。

## 获取页面计数

当您需要读取 PDF 的总页数时，请使用此示例。

1. 打开源 PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)。
1. 读取页面集合的大小。
1. 输出总页数。

```java
public static void getPageCount(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        System.out.println("Page Count: " + document.getPages().size());
    }
}
```

## 获取保存前的页数

在需要在写入文件之前了解生成的内容将产生多少页时使用此示例。

1. 创建一个新 PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 并向页面添加内容。
1. 处理段落以强制进行布局计算。
1. 读取生成的页数并输出。

```java
public static void getPageCountWithoutSaving(Path inputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();
        for (int i = 0; i < 300; i++) {
            page.getParagraphs().add(new TextFragment("Pages count test"));
        }
        document.processParagraphs();
        System.out.println("Number of pages in document = " + document.getPages().size());
    }
}
```

## 获取页面框属性

当您需要检查所有主要框尺寸和页面旋转值时，请使用此示例。

1. 打开源 PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 并访问目标页面。
1. 将页面框的值收集到映射中。
1. 输出尺寸和页面旋转信息。

```java
public static void getPageProperties(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        Page page = document.getPages().get_Item(1);
        Map<String, Rectangle> boxes = new LinkedHashMap<>();
        boxes.put("ArtBox", page.getArtBox());
        boxes.put("BleedBox", page.getBleedBox());
        boxes.put("CropBox", page.getCropBox());
        boxes.put("MediaBox", page.getMediaBox());
        boxes.put("TrimBox", page.getTrimBox());
        boxes.put("Rect", page.getRect());

        for (Map.Entry<String, Rectangle> entry : boxes.entrySet()) {
            Rectangle box = entry.getValue();
            System.out.println(entry.getKey() + " : Height=" + box.getHeight()
                    + ",Width=" + box.getWidth()
                    + ",LLX=" + box.getLLX()
                    + ",LLY=" + box.getLLY()
                    + ",URX=" + box.getURX()
                    + ",URY=" + box.getURY());
        }

        System.out.println("Page Number : " + page.getNumber());
        System.out.println("Rotate : " + page.getRotate());
    }
}
```

## 获取每页的颜色类型

当需要识别页面是黑白、灰度还是 RGB 时，请使用此示例。

1. 打开源 PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)。
1. 遍历所有页面并读取每页 [ColorType](https://reference.aspose.com/pdf/java/com.aspose.pdf/colortype/)。
1. 将枚举值转换为可读文本并输出结果。

```java
public static void getPageColorType(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (int pageNumber = 1; pageNumber <= document.getPages().size(); pageNumber++) {
            ColorType pageColorType = document.getPages().get_Item(pageNumber).getColorType();
            String colorDescription = switch (pageColorType) {
                case BlackAndWhite -> "Black and white";
                case Grayscale -> "Gray Scale";
                case Rgb -> "RGB";
                case Undefined -> "undefined";
            };
            System.out.println("Page # " + pageNumber + " is " + colorDescription + ".");
        }
    }
}
```
