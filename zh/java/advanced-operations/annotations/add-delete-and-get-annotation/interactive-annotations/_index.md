---
title: 使用 Java 的交互式注释
linktitle: 交互式注释
type: docs
weight: 60
url: /java/interactive-annotations/
description: 了解如何使用 Aspose.PDF for Java 添加、检查和删除 PDF 文档中的链接注释。
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 使用 Java 处理交互式 PDF 注释。
Abstract: 本文介绍如何使用 Aspose.PDF for Java 处理 PDF 文件中的交互式链接注释。它包括定位文本、在匹配的文本区域上创建链接注释、读取现有链接注释以及删除它们。
---
本节中的交互式注释重点关注基于链接和按钮的工作流程，这些工作流程响应 PDF 查看器内的用户操作。

## 添加链接注释

当您需要在页面上的文本上放置可单击链接时，请使用此示例。

1. 打开源 PDF [文档](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)。
1. 找到目标文本片段并在其矩形上创建一个 [LinkAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/linkannotation/)。
1. 分配 [GoToURIAction](https://reference.aspose.com/pdf/java/com.aspose.pdf/gotouriaction/) 并保存更新的文档。

```java
public static void linkAdd(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        TextFragmentAbsorber textFragmentAbsorber = new TextFragmentAbsorber("file");
        document.getPages().get_Item(1).accept(textFragmentAbsorber);

        var phoneNumberFragment = textFragmentAbsorber.getTextFragments().get_Item(1);
        LinkAnnotation linkAnnotation = new LinkAnnotation(
                document.getPages().get_Item(1),
                phoneNumberFragment.getRectangle());
        linkAnnotation.setAction(new GoToURIAction("https://www.aspose.com"));

        document.getPages().get_Item(1).getAnnotations().add(linkAnnotation);
        document.save(outputFile.toString());
    }
}
```

## 获取链接注释

此示例扫描页面注释集合并报告每个链接注释的位置。

1. 打开源 PDF [文档](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)。
1. 迭代目标页面上的注释。
1. 按 [AnnotationType](https://reference.aspose.com/pdf/java/com.aspose.pdf/annotationtype/).`Link` 过滤注释并打印其矩形。

```java
public static void linkGet(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (Annotation annotation : document.getPages().get_Item(1).getAnnotations()) {
            if (annotation.getAnnotationType() == AnnotationType.Link) {
                System.out.println(annotation.getRect());
            }
        }
    }
}
```

## 删除链接注释

当应从页面中删除现有链接注释时，请使用此方法。

1. 打开源 PDF [文档](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)。
1. 收集类型为 [AnnotationType](https://reference.aspose.com/pdf/java/com.aspose.pdf/annotationtype/).`Link` 的注释。
1. 删除收集的注释并保存输出文件。

```java
public static void linkDelete(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        List<Annotation> toDelete = new ArrayList<>();
        for (Annotation annotation : document.getPages().get_Item(1).getAnnotations()) {
            if (annotation.getAnnotationType() == AnnotationType.Link) {
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

此示例创建一个带有箭头样式、边框设置和弹出注释的交互式线条注释。

1. 打开源 PDF [文档](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)。
1. 创建一个带有起点和终点的 [LineAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/lineannotation/)。
1. 配置其外观和弹出注释，然后保存文档。

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

## 添加导航按钮

当 PDF 应包含用于交互式导航的上一页和下一页按钮时，请使用此示例。

1. 打开源 PDF [文档](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 并确保文档具有所需的页面。
1. 使用预定义的导航操作创建 [ButtonField](https://reference.aspose.com/pdf/java/com.aspose.pdf/buttonfield/) 控件。
1. 将按钮添加到表单集合并保存更新的文档。

```java
public static void navigationButtonsAdd(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.getPages().add();

        record ButtonConfig(String name, double xPos, PredefinedAction action) {}
        List<ButtonConfig> buttonConfigs = List.of(
                new ButtonConfig("Previous Page", 120.0, PredefinedAction.PrevPage),
                new ButtonConfig("Next Page", 230.0, PredefinedAction.NextPage));

        for (Page page : document.getPages()) {
            for (ButtonConfig config : buttonConfigs) {
                Rectangle rect = new Rectangle(config.xPos(), 10.0, config.xPos() + 100, 40.0, true);
                ButtonField button = new ButtonField(page, rect);
                button.setPartialName(config.name());
                button.setValue(config.name());
                button.getCharacteristics().setBorder(Color.getRed());
                button.getCharacteristics().setBackground(Color.getOrange().toRgb());
                button.getAnnotationActions().setOnReleaseMouseBtn(new NamedAction(config.action()));
                document.getForm().add(button);
            }
        }
        document.save(outputFile.toString());
    }
}
```

## 添加打印按钮

此示例创建一个按钮，当用户单击该按钮时会触发打印命令。

1. 创建新的 PDF [文档](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 并添加页面。
1. 创建一个 [ButtonField](https://reference.aspose.com/pdf/java/com.aspose.pdf/buttonfield/) 并分配打印预定义操作。
1. 配置按钮边框和背景，将其添加到表单中，然后保存文档。

```java
public static void printButtonAdd(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();

        Rectangle rect = new Rectangle(72, 748, 164, 768, true);
        ButtonField printButton = new ButtonField(page, rect);
        printButton.setAlternateName("Print current document");
        printButton.setColor(Color.getBlack());
        printButton.setPartialName("printBtn1");
        printButton.setValue("Print Document");
        printButton.getAnnotationActions().setOnReleaseMouseBtn(
                new NamedAction(PredefinedAction.File_Print));

        Border border = new Border(printButton);
        border.setStyle(BorderStyle.Solid);
        border.setWidth(2);
        printButton.setBorder(border);

        printButton.getCharacteristics().setBorder(Color.getBlue());
        printButton.getCharacteristics().setBackground(Color.getLightBlue().toRgb());

        document.getForm().add(printButton);
        document.save(outputFile.toString());
    }
}
```
