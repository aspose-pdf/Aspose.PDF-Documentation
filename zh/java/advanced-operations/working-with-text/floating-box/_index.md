---
title: 在 Java 中使用 FloatingBox 进行 PDF 布局
linktitle: 使用浮动框
type: docs
weight: 30
url: /java/floating-box/
description: 了解如何使用 FloatingBox 通过 Java 在 PDF 文档中进行文本布局、多列内容和精确定位。
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.5
TechArticle: true
AlternativeHeadline: 使用 Java 在 PDF 中创建和定位样式化的 FloatingBox 容器
Abstract: 本文介绍如何在 Aspose.PDF for Java 中使用 FloatingBox。它涵盖了将文本放置在有边框的浮动容器中、创建重复的多列布局、使用背景颜色、绝对偏移以及水平或垂直对齐选项。
---
Aspose.PDF for Java 使用`FloatingBox` 构建可重用的文本容器和基于列的布局。

## 创建并添加浮动框

当文本应放置在有边框的浮动容器内时，请使用此示例。

1. 创建新的 PDF 文档并添加页面。
1. 创建一个`FloatingBox`，设置其大小和边框，并添加文本内容。
1. 将框添加到页面并保存文档。

```java
public static void createAndAddFloatingBox(Path outputFile) {
       try (Document document = new Document()) {
           Page page = document.getPages().add();

           FloatingBox box = new FloatingBox(400, 30);
           box.setBorder(new BorderInfo(BorderSide.All, 1.5f, Color.getDarkGreen()));
           box.setNeedRepeating(false);
           String phrase = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce quam odio, sollicitudin ac mauris vel, suscipit pellentesque nisi.";
           box.getParagraphs().add(new TextFragment(phrase));

           page.getParagraphs().add(box);
           document.save(outputFile.toString());
       }
   }
```

## 创建重复的多列布局

当长文本应跨一个浮动框内的多个列流动时，请使用此示例。

1. 创建页面并配置边距。
1. 计算列宽并配置`FloatingBox`列设置。
1. 将重复的文本片段添加到框中并保存文档。

```java
public static void multiColumnLayout(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();
        page.getPageInfo().setMargin(new MarginInfo(36, 18, 36, 18));

        int columnCount = 3;
        int spacing = 10;
        double width = page.getPageInfo().getWidth()
                - page.getPageInfo().getMargin().getLeft()
                - page.getPageInfo().getMargin().getRight()
                - (columnCount - 1) * spacing;
        double columnWidth = width / 3;

        FloatingBox box = new FloatingBox();
        box.setNeedRepeating(true);
        box.getColumnInfo().setColumnWidths(columnWidth + " " + columnWidth + " " + columnWidth);
        box.getColumnInfo().setColumnSpacing(String.valueOf(spacing));
        box.getColumnInfo().setColumnCount(3);

        String phrase = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce quam odio, sollicitudin ac mauris vel, suscipit pellentesque nisi.";
        for (int i = 0; i < 10; i++) {
            box.getParagraphs().add(new TextFragment(phrase));
        }

        page.getParagraphs().add(box);
        document.save(outputFile.toString());
    }
}
```

## 每个片段作为列中的第一项开始

当每个插入的片段应开始一个新的柱流段时，请使用此示例。

1. 创建页面并配置多列`FloatingBox`。
1. 创建文本片段并用 `setFirstParagraphInColumn(true)` 标记它们。
1. 将框添加到页面并保存 PDF。

```java
public static void multiColumnLayout2(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();
        page.getPageInfo().setMargin(new MarginInfo(36, 18, 36, 18));

        int columnCount = 3;
        int spacing = 10;
        double width = page.getPageInfo().getWidth()
                - page.getPageInfo().getMargin().getLeft()
                - page.getPageInfo().getMargin().getRight()
                - (columnCount - 1) * spacing;
        double columnWidth = width / 3;

        FloatingBox box = new FloatingBox();
        box.setNeedRepeating(true);
        box.getColumnInfo().setColumnWidths(columnWidth + " " + columnWidth + " " + columnWidth);
        box.getColumnInfo().setColumnSpacing(String.valueOf(spacing));
        box.getColumnInfo().setColumnCount(3);

        String phrase = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce quam odio, sollicitudin ac mauris vel, suscipit pellentesque nisi.";
        for (int i = 0; i < 10; i++) {
            TextFragment text = new TextFragment(phrase);
            text.setFirstParagraphInColumn(true);
            box.getParagraphs().add(text);
        }

        page.getParagraphs().add(box);
        document.save(outputFile.toString());
    }
}
```

## 添加带有背景颜色的浮动框

当浮动容器应具有可见的背景填充时，请使用此示例。

1. 创建新的 PDF 文档并添加页面。
1. 创建一个`FloatingBox`，设置其背景颜色并添加文本。
1. 将框放在页面上并保存文档。

```java
public static void backgroundSupport(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();

        FloatingBox box = new FloatingBox(400, 30);
        box.setBackgroundColor(Color.getLightGreen());
        box.setNeedRepeating(false);
        box.getParagraphs().add(new TextFragment("text example"));

        page.getParagraphs().add(box);
        document.save(outputFile.toString());
    }
}
```

## 使用绝对偏移定位浮动框

当浮动框必须出现在页面上的精确偏移处时，请使用此示例。

1. 创建一个页面并准备周围的文本内容。
1. 创建`FloatingBox`，设置绝对定位，并分配顶部和左侧偏移量。
1. 将内容添加到页面并保存文档。

```java
public static void offsetSupport(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();

        FloatingBox box = new FloatingBox(400, 30);
        box.setTop(45);
        box.setLeft(15);
        box.setPositioningMode(ParagraphPositioningMode.Absolute);
        box.setBorder(new BorderInfo(BorderSide.All, 1.5f, Color.getDarkGreen()));
        box.getParagraphs().add(new TextFragment("text example 1"));

        page.getParagraphs().add(new TextFragment("text example 2"));
        page.getParagraphs().add(box);
        page.getParagraphs().add(new TextFragment("text example 3"));

        document.save(outputFile.toString());
    }
}
```

## 对齐浮动框中的文本

当浮动框应展示具有相同水平对齐方式的不同垂直对齐方式时，请使用此示例。

1. 创建新的 PDF 文档并添加页面。
1. 创建多个具有不同对齐设置的`FloatingBox` 对象。
1. 将它们添加到页面并保存结果。

```java
public static void alignTextToFloat(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();

        FloatingBox floatBox = new FloatingBox(100, 100);
        floatBox.setVerticalAlignment(VerticalAlignment.Bottom);
        floatBox.setHorizontalAlignment(HorizontalAlignment.Right);
        floatBox.getParagraphs().add(new TextFragment("FloatingBox_bottom"));
        floatBox.setBorder(new BorderInfo(BorderSide.All, Color.getBlue()));
        page.getParagraphs().add(floatBox);

        FloatingBox floatBox2 = new FloatingBox(100, 100);
        floatBox2.setVerticalAlignment(VerticalAlignment.Center);
        floatBox2.setHorizontalAlignment(HorizontalAlignment.Right);
        floatBox2.getParagraphs().add(new TextFragment("FloatingBox_center"));
        floatBox2.setBorder(new BorderInfo(BorderSide.All, Color.getBlue()));
        page.getParagraphs().add(floatBox2);

        FloatingBox floatBox3 = new FloatingBox(100, 100);
        floatBox3.setVerticalAlignment(VerticalAlignment.Top);
        floatBox3.setHorizontalAlignment(HorizontalAlignment.Right);
        floatBox3.getParagraphs().add(new TextFragment("FloatingBox_top"));
        floatBox3.setBorder(new BorderInfo(BorderSide.All, Color.getBlue()));
        page.getParagraphs().add(floatBox3);

        document.save(outputFile.toString());
    }
}
```
