---
title: 在 Java 中使用 PDF 操作
linktitle: 行动
type: docs
weight: 20
url: /java/actions/
description: 了解如何使用 Java 添加、更新和删除 PDF 文件中的文档、页面和表单操作。
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.5
TechArticle: true
AlternativeHeadline: 使用 Java 将文档、页面和表单操作添加到 PDF 文件
Abstract: 本文介绍如何使用 Aspose.PDF for Java 处理 PDF 文档中的操作。它涵盖了用于打印和页面导航、隐藏表单字段、提交表单、分配 JavaScript 启动操作以及添加或删除页面打开和关闭操作的命名操作。
---
Aspose.PDF for Java 允许您将操作分配给按钮、文档和页面，以使 PDF 文件具有交互性。

## 添加命名打印操作

当页面上的按钮应触发打印命令时使用此示例。

1. 打开源 PDF [文档](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 并选择目标页面。
1. 创建一个 [ButtonField](https://reference.aspose.com/pdf/java/com.aspose.pdf/buttonfield/) 并分配一个 [NamedAction](https://reference.aspose.com/pdf/java/com.aspose.pdf/namedaction/) 进行打印。
1. 将按钮添加到表单并保存文档。

```java
public static void addNamedActionPrint(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        Page page = document.getPages().get_Item(1);

        Rectangle rect = new Rectangle(10, 10, 100, 40, true);
        ButtonField printButton = new ButtonField(page, rect);
        printButton.setPartialName("printButton");
        printButton.setValue("Print");
        printButton.getAnnotationActions().setOnReleaseMouseBtn(
                new NamedAction(PredefinedAction.File_Print));

        Border border = new Border(printButton);
        border.setWidth(1);
        printButton.setBorder(border);

        document.getForm().add(printButton, 1);
        document.save(outputFile.toString());
    }
}
```

## 添加隐藏动作

当按钮应显示或隐藏一组表单字段（例如复选框）时，请使用此示例。

1. 打开源 PDF [文档](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 并收集目标表单小部件。
1. 创建一个按钮并为其分配一个 [HideAction](https://reference.aspose.com/pdf/java/com.aspose.pdf/hideaction/)。
1. 将按钮添加到表单并保存更新的文档。

```java
public static void addNamedActionHide(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        List<WidgetAnnotation> checkboxes = new ArrayList<>();
        for (WidgetAnnotation field : document.getForm()) {
            if (field instanceof CheckboxField) {
                checkboxes.add(field);
            }
        }

        Rectangle rect = new Rectangle(10, 410, 140, 440, true);
        ButtonField hideButton = new ButtonField(document.getPages().get_Item(1), rect);
        hideButton.setPartialName("HideButton");
        hideButton.setValue("Hide Checkboxes");
        hideButton.getAnnotationActions().setOnReleaseMouseBtn(
                new HideAction(checkboxes.toArray(new WidgetAnnotation[0]), true));

        document.getForm().add(hideButton, 1);
        document.save(outputFile.toString());
    }
}
```

## 添加页面导航按钮

此示例在整个文档中创建第一页、上一页、下一页和最后一页按钮。

1. 打开源 PDF [文档](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)。
1. 为每个页面创建导航按钮并分配匹配的预定义操作。
1. 将按钮添加到表单并保存文档。

```java
public static void addNavigationButtons(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        int totalPages = document.getPages().size();

        for (Page page : document.getPages()) {
            ButtonField firstPageButton = new ButtonField(page, new Rectangle(10, 10, 110, 40, true));
            firstPageButton.setPartialName("First Page");
            firstPageButton.setValue("First Page");
            firstPageButton.getCharacteristics().setBorder(com.aspose.pdf.Color.getRed());
            firstPageButton.getCharacteristics().setBackground(com.aspose.pdf.Color.getOrange().toRgb());
            firstPageButton.setReadOnly(document.getPages().indexOf(page) == 1);
            firstPageButton.getAnnotationActions().setOnReleaseMouseBtn(
                    new NamedAction(PredefinedAction.FirstPage));
            document.getForm().add(firstPageButton);

            ButtonField previousPageButton = new ButtonField(page, new Rectangle(120, 10, 220, 40, true));
            previousPageButton.setPartialName("Previous Page");
            previousPageButton.setValue("Previous Page");
            previousPageButton.getCharacteristics().setBorder(com.aspose.pdf.Color.getRed());
            previousPageButton.getCharacteristics().setBackground(com.aspose.pdf.Color.getOrange().toRgb());
            previousPageButton.setReadOnly(document.getPages().indexOf(page) == 1);
            previousPageButton.getAnnotationActions().setOnReleaseMouseBtn(
                    new NamedAction(PredefinedAction.PrevPage));
            document.getForm().add(previousPageButton);

            ButtonField nextPageButton = new ButtonField(page, new Rectangle(230, 10, 330, 40, true));
            nextPageButton.setPartialName("Next Page");
            nextPageButton.setValue("Next Page");
            nextPageButton.getCharacteristics().setBorder(com.aspose.pdf.Color.getRed());
            nextPageButton.getCharacteristics().setBackground(com.aspose.pdf.Color.getOrange().toRgb());
            nextPageButton.setReadOnly(document.getPages().indexOf(page) == totalPages);
            nextPageButton.getAnnotationActions().setOnReleaseMouseBtn(
                    new NamedAction(PredefinedAction.NextPage));
            document.getForm().add(nextPageButton);

            ButtonField lastPageButton = new ButtonField(page, new Rectangle(340, 10, 440, 40, true));
            lastPageButton.setPartialName("Last Page");
            lastPageButton.setValue("Last Page");
            lastPageButton.getCharacteristics().setBorder(com.aspose.pdf.Color.getRed());
            lastPageButton.getCharacteristics().setBackground(com.aspose.pdf.Color.getOrange().toRgb());
            lastPageButton.setReadOnly(document.getPages().indexOf(page) == totalPages);
            lastPageButton.getAnnotationActions().setOnReleaseMouseBtn(
                    new NamedAction(PredefinedAction.LastPage));
            document.getForm().add(lastPageButton);
        }

        document.save(outputFile.toString());
    }
}
```

## 添加提交操作

当按钮应将表单数据提交到 URL 时，请使用此示例。

1. 打开源 PDF [文档](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)。
1. 使用目标 URL 和标志创建 [SubmitFormAction](https://reference.aspose.com/pdf/java/com.aspose.pdf/submitformaction/)。
1. 将操作分配给按钮字段并保存文档。

```java
public static void addSubmitAction(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        SubmitFormAction submitAction = new SubmitFormAction();
        FileSpecification submitUrl = new FileSpecification();
        submitUrl.setFileSystem("URL");
        submitUrl.setName("http://localhost:3000/submit");
        submitAction.setUrl(submitUrl);
        submitAction.setFlags(SubmitFormAction.EXPORT_FORMAT | SubmitFormAction.SUBMIT_COORDINATES);

        Rectangle rect = new Rectangle(10, 10, 100, 40, true);
        ButtonField submitButton = new ButtonField(document.getPages().get_Item(1), rect);
        submitButton.setPartialName("SubmitButton");
        submitButton.setValue("Submit");
        submitButton.getAnnotationActions().setOnReleaseMouseBtn(submitAction);

        document.getForm().add(submitButton, 1);
        document.save(outputFile.toString());
    }
}
```

## 添加文档级启动操作

此示例分配在打开、保存或打印文档时运行的 JavaScript 操作。

1. 打开源 PDF [文档](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)。
1. 为文档事件创建所需的 [JavascriptAction](https://reference.aspose.com/pdf/java/com.aspose.pdf/javascriptaction/) 对象。
1. 分配操作并保存文档。

```java
public static void addLaunchActions(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.setOpenAction(new JavascriptAction("app.launchURL('http://localhost:3000/open');"));
        document.getActions().setBeforeSaving(
                new JavascriptAction("app.launchURL('http://localhost:3000/save');"));
        document.getActions().setBeforePrinting(
                new JavascriptAction("app.launchURL('http://localhost:3000/print');"));

        document.save(outputFile.toString());
    }
}
```

## 添加页面打开和关闭操作

当特定页面应触发打开和关闭操作时，请使用此示例。

1. 打开源 PDF [文档](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 并确保目标页面存在。
1. 创建页面导航和 JavaScript 操作。
1. 分配页面操作并保存文档。

```java
public static void addPageActions(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        if (document.getPages().size() < 3) {
            System.out.println("Error: The document does not have at least 3 pages.");
            return;
        }

        Page page = document.getPages().get_Item(3);
        GoToAction action = new GoToAction(page);
        action.setDestination(new XYZExplicitDestination(page, 0, page.getPageInfo().getHeight(), 1));
        page.getActions().setOnOpen(action);
        page.getActions().setOnClose(
                new JavascriptAction("app.launchURL('http://localhost:3000/page/3');"));

        document.save(outputFile.toString());
    }
}
```

## 删除页面操作

当应从页面中清除先前分配的打开和关闭操作时，请使用此方法。

1. 打开源 PDF [文档](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 并确保目标页面存在。
1. 删除该页面上的所有操作。
1. 保存更新的文档。

```java
public static void removePageActions(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        if (document.getPages().size() < 3) {
            System.out.println("Error: The document does not have at least 3 pages.");
            return;
        }

        Page page = document.getPages().get_Item(3);
        page.getActions().removeActions();

        document.save(outputFile.toString());
    }
}
```
