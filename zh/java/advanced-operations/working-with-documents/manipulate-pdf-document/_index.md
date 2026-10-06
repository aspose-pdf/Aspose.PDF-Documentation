---
title: 在 Java 中操作 PDF 文档
linktitle: 操作 PDF 文档
type: docs
weight: 20
url: /zh/java/manipulate-pdf-document/
description: 了解如何在 Java 中验证、结构化并修改 PDF 文档，包括 TOC 管理和 PDF/A 检查。
lastmod: "2026-10-06"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 使用 Java 验证、重构并扁平化 PDF 文档。
Abstract: 本文介绍了如何使用 Aspose.PDF for Java 操作 PDF 文档。它涵盖了验证 PDF/A 合规性、添加和自定义目录、隐藏或自定义目录页码、分配到期脚本以及展平交互式表单字段。
---
Aspose.PDF for Java 包含超出简单页面编辑的文档结构操作。

## 验证 PDF/A-1a 合规性

在需要检查文档是否符合 PDF/A-1a 存档标准时，请使用此示例。

1. 打开源 PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. 对必需项运行验证 [PdfFormat](https://reference.aspose.com/pdf/java/com.aspose.pdf/pdfformat/) 目标。
1. 将验证报告保存到指定的输出路径。

```java
public static void validatePdfaStandardA1a(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.validate(outputFile.toString(), PdfFormat.PDF_A_1A);
    }
}
```

## 验证 PDF/A-1b 合规性

此变体将相同的源文档针对 PDF/A-1b 合规级别进行验证。

1. 打开源 PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. 使用验证方法 [PdfFormat](https://reference.aspose.com/pdf/java/com.aspose.pdf/pdfformat/) PDF/A-1b 的值。
1. 将验证结果写入输出报告文件。

```java
public static void validatePdfaStandardA1b(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.validate(outputFile.toString(), PdfFormat.PDF_A_1B);
    }
}
```

## 添加目录

当文档应包含生成的 TOC 页面并带有指向内容页面的链接时，请使用此方法。

1. 打开源 PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. 插入一个新的 TOC [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) 并配置它的 [TocInfo](https://reference.aspose.com/pdf/java/com.aspose.pdf/tocinfo/).
1. 创建 [Heading](https://reference.aspose.com/pdf/java/com.aspose.pdf/heading/) 指向目标页面的条目。
1. 保存更新后的文档。

```java
public static void addTableOfContents(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        Page tocPage = document.getPages().insert(1);
        TocInfo tocInfo = new TocInfo();
        TextFragment title = new TextFragment("Table Of Contents");
        title.getTextState().setFontSize(20);
        title.getTextState().setFontStyle(FontStyles.Bold);
        tocInfo.setTitle(title);
        tocPage.setTocInfo(tocInfo);

        String[] titles = {"First page", "Second page"};
        for (int index = 0; index < titles.length && index + 2 <= document.getPages().size(); index++) {
            Heading heading = new Heading(1);
            TextSegment segment = new TextSegment(titles[index]);
            heading.setTocPage(tocPage);
            heading.getSegments().add(segment);
            Page destinationPage = document.getPages().get_Item(index + 2);
            heading.setDestinationPage(destinationPage);
            heading.setTop(destinationPage.getRect().getHeight());
            tocPage.getParagraphs().add(heading);
        }

        document.save(outputFile.toString());
    }
}
```

## 自定义 TOC 级别和格式

此示例展示了如何为多个目录层级分配不同的视觉设置。

1. 打开源 PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. 添加 TOC [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) 并配置 [TocInfo](https://reference.aspose.com/pdf/java/com.aspose.pdf/tocinfo/) 格式化数组。
1. 创建示例 [Heading](https://reference.aspose.com/pdf/java/com.aspose.pdf/heading/) 不同级别的条目。
1. 保存带有格式化 TOC 的文档。

```java
public static void setTocLevels(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        Page tocPage = document.getPages().add();
        TocInfo tocInfo = new TocInfo();
        tocInfo.setLineDash(TabLeaderType.Solid);
        TextFragment title = new TextFragment("Table Of Contents");
        title.getTextState().setFontSize(30);
        tocInfo.setTitle(title);
        tocPage.setTocInfo(tocInfo);

        tocInfo.setFormatArrayLength(4);
        tocInfo.getFormatArray()[0].getMargin().setLeft(0);
        tocInfo.getFormatArray()[0].getMargin().setRight(30);
        tocInfo.getFormatArray()[0].setLineDash(TabLeaderType.Dot);
        tocInfo.getFormatArray()[0].getTextState().setFontStyle(FontStyles.Bold | FontStyles.Italic);
        tocInfo.getFormatArray()[1].getMargin().setLeft(10);
        tocInfo.getFormatArray()[1].getMargin().setRight(30);
        tocInfo.getFormatArray()[1].setLineDash(3);
        tocInfo.getFormatArray()[1].getTextState().setFontSize(10);
        tocInfo.getFormatArray()[2].getMargin().setLeft(20);
        tocInfo.getFormatArray()[2].getMargin().setRight(30);
        tocInfo.getFormatArray()[2].getTextState().setFontStyle(FontStyles.Bold);
        tocInfo.getFormatArray()[3].setLineDash(TabLeaderType.Solid);
        tocInfo.getFormatArray()[3].getMargin().setLeft(30);
        tocInfo.getFormatArray()[3].getMargin().setRight(30);
        tocInfo.getFormatArray()[3].getTextState().setFontStyle(FontStyles.Bold);

        try (Page page = document.getPages().add()) {
            for (int level = 1; level < 5; level++) {
                Heading heading = new Heading(level);
                heading.setAutoSequence(true);
                heading.setTocPage(tocPage);
                heading.getTextState().setFont(FontRepository.findFont("Arial"));
                heading.getSegments().add(new TextSegment("Sample Heading" + level));
                heading.setInList(true);
                page.getParagraphs().add(heading);
            }
        }

        document.save(outputFile.toString());
    }
}
```

## 在目录中隐藏页码

当目录应仅显示条目标题而不显示页码时，请使用此示例。

1. 打开源 PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. 添加 TOC [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) 并在...中禁用页码 [TocInfo](https://reference.aspose.com/pdf/java/com.aspose.pdf/tocinfo/).
1. 创建所需的 [Heading](https://reference.aspose.com/pdf/java/com.aspose.pdf/heading/) 条目并将其添加到内容页。
1. 保存更新后的文档。

```java
public static void hidePageNumbersInToc(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        Page page;
        Heading heading;
        try (Page tocPage = document.getPages().add()) {
            TocInfo tocInfo = new TocInfo();
            TextFragment title = new TextFragment("Table Of Contents");
            title.getTextState().setFontSize(20);
            title.getTextState().setFontStyle(FontStyles.Bold);
            tocInfo.setTitle(title);
            tocInfo.setShowPageNumbers(false);
            tocPage.setTocInfo(tocInfo);

            tocInfo.setFormatArrayLength(4);
            tocInfo.getFormatArray()[0].getMargin().setRight(0);
            tocInfo.getFormatArray()[0].getTextState().setFontStyle(FontStyles.Bold | FontStyles.Italic);
            tocInfo.getFormatArray()[1].getMargin().setLeft(30);
            tocInfo.getFormatArray()[1].getTextState().setUnderline(true);
            tocInfo.getFormatArray()[1].getTextState().setFontSize(10);
            tocInfo.getFormatArray()[2].getTextState().setFontStyle(FontStyles.Bold);
            tocInfo.getFormatArray()[3].getTextState().setFontStyle(FontStyles.Bold);

            page = document.getPages().add();
            heading = new Heading(1);
            heading.setTocPage(tocPage);
        }
        heading.setAutoSequence(true);
        heading.setInList(true);
        heading.getSegments().add(new TextSegment("this is heading of level 1"));
        page.getParagraphs().add(heading);

        document.save(outputFile.toString());
    }
}
```

## 自定义 TOC 页码前缀

此示例向生成的目录中显示的页码添加自定义前缀。

1. 打开源 PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. 插入目录 [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) 并在其中设置所需的页码前缀 [TocInfo](https://reference.aspose.com/pdf/java/com.aspose.pdf/tocinfo/).
1. 创建 [Heading](https://reference.aspose.com/pdf/java/com.aspose.pdf/heading/) 指向每页的条目。
1. 保存更新后的文档。

```java
public static void customizePageNumbersInToc(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        Page tocPage = document.getPages().insert(1);
        TocInfo tocInfo = new TocInfo();
        TextFragment title = new TextFragment("Table Of Contents");
        title.getTextState().setFontSize(20);
        title.getTextState().setFontStyle(FontStyles.Bold);
        tocInfo.setTitle(title);
        tocInfo.setPageNumbersPrefix("P");
        tocPage.setTocInfo(tocInfo);

        for (int index = 1; index <= document.getPages().size(); index++) {
            Page page = document.getPages().get_Item(index);
            Heading heading = new Heading(1);
            heading.setTocPage(tocPage);
            heading.setDestinationPage(page);
            heading.setTop(page.getRect().getHeight());
            heading.getSegments().add(new TextSegment("Page " + index));
            tocPage.getParagraphs().add(heading);
        }

        document.save(outputFile.toString());
    }
}
```

## 添加 PDF 过期脚本

当文档应在打开时运行 JavaScript，并在特定日期后显示到期警告时，请使用此方法。

1. 打开源 PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 并添加任何必需的内容。
1. 创建一个 [JavascriptAction](https://reference.aspose.com/pdf/java/com.aspose.pdf/javascriptaction/) 带有过期逻辑。
1. 将脚本分配为文档打开操作并保存输出文件。

```java
public static void setPdfExpiryDate(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        try (Page page = document.getPages().add()) {
            page.getParagraphs().add(new TextFragment("Hello World..."));
        }
        JavascriptAction script = new JavascriptAction(
                "var year=2017;"
                        + "var month=5;"
                        + "today = new Date(); today = new Date(today.getFullYear(), today.getMonth());"
                        + "expiry = new Date(year, month);"
                        + "if (today.getTime() > expiry.getTime())"
                        + "app.alert('The file is expired. You need a new one.');");
        document.setOpenAction(script);
        document.save(outputFile.toString());
    }
}
```

## 将可填写的 PDF 表单扁平化

此示例将交互式表单字段转换为静态页面内容，从而生成的文档不再可作为表单进行编辑。

1. 打开源 PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. 检查文档是否包含表单小部件。
1. 扁平化每个 [Field](https://reference.aspose.com/pdf/java/com.aspose.pdf/field/) 由 a 表示 [WidgetAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/widgetannotation/).
1. 保存已展平的文档。

```java
public static void flattenFillablePdf(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        if (document.getForm() != null && document.getForm().size() > 0) {
            for (WidgetAnnotation annotation : document.getForm()) {
                if (annotation instanceof Field field) {
                    field.flatten();
                }
            }
        }
        document.save(outputFile.toString());
    }
}
```
