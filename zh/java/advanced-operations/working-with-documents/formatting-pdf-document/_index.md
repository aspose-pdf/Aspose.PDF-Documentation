---
title: 用 Java 格式化 PDF 文档
linktitle: 设置 PDF 文档格式
type: docs
weight: 11
url: /java/formatting-pdf-document/
description: 了解如何在 Java 中设置 PDF 文档格式、嵌入字体、控制查看器设置以及调整显示选项。
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 使用 Java 设置 PDF 文件中文档窗口、字体和缩放行为的格式
Abstract: 本文介绍如何使用 Aspose.PDF for Java 格式化 PDF 文档。它包括读取和更新文档窗口设置、嵌入字体、设置默认字体、列出字体、子集化嵌入字体以及控制初始缩放系数。
---
Aspose.PDF for Java 中的格式设置包括查看器行为、字体嵌入和显示设置。

## 获取文档窗口设置

使用此示例检查现有 PDF 文档中存储的当前查看器首选项。

1. 打开源 PDF [文档](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)。
1. 从文档中读取所需的窗口和显示属性。
1. 输出当前设置以供检查或调试。

```java
public static void getDocumentWindow(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        System.out.println("CenterWindow: " + document.isCenterWindow());
        System.out.println("Direction: " + document.getDirection());
        System.out.println("DisplayDocTitle: " + document.isDisplayDocTitle());
        System.out.println("FitWindow: " + document.isFitWindow());
        System.out.println("HideMenuBar: " + document.isHideMenubar());
        System.out.println("HideToolBar: " + document.isHideToolBar());
        System.out.println("HideWindowUI: " + document.isHideWindowUI());
        System.out.println("NonFullScreenPageMode: " + document.getNonFullScreenPageMode());
        System.out.println("PageLayout: " + document.getPageLayout());
        System.out.println("PageMode: " + document.getPageMode());
    }
}
```

## 设置文档窗口首选项

此示例更新了在兼容查看器中打开 PDF 时的显示方式。

1. 打开源 PDF [文档](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)。
1. 设置所需的窗口、布局和页面模式首选项。
1. 保存更新的 PDF [文档](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)。

```java
public static void setDocumentWindow(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.setCenterWindow(true);
        document.setDirection(Direction.R2L);
        document.setDisplayDocTitle(true);
        document.setFitWindow(true);
        document.setHideMenubar(true);
        document.setHideToolBar(true);
        document.setHideWindowUI(true);
        document.setNonFullScreenPageMode(PageMode.UseOC);
        document.setPageLayout(PageLayout.TwoColumnLeft);
        document.setPageMode(PageMode.UseThumbs);
        document.save(outputFile.toString());
    }
}
```

## 在现有 PDF 中嵌入字体

当文档应携带其所需的字体以便在其他系统上更可靠地呈现时，请使用此方法。

1. 打开源 PDF [文档](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)。
1. 启用标准字体嵌入并迭代每个[页面](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) 使用的字体。
1. 将任何非嵌入的 [Font](https://reference.aspose.com/pdf/java/com.aspose.pdf/font/) 对象标记为嵌入。
1. 保存更新的文档。

```java
public static void embeddedFonts(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.setEmbedStandardFonts(true);
        for (Page page : document.getPages()) {
            for (Font pageFont : page.getResources().getFonts()) {
                if (!pageFont.isEmbedded()) {
                    pageFont.setEmbedded(true);
                }
            }
        }
        document.save(outputFile.toString());
    }
}
```

## 创建新 PDF 时嵌入字体

此示例创建一个新的 PDF，并从一开始就为文本内容分配嵌入字体。

1. 创建新的 PDF [文档](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 并添加 [页面](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/)。
1. 创建所需的 [TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf/textfragment/)、[TextSegment](https://reference.aspose.com/pdf/java/com.aspose.pdf/textsegment/) 和 [TextState](https://reference.aspose.com/pdf/java/com.aspose.pdf/textstate/)。
1. 从存储库解析目标 [Font](https://reference.aspose.com/pdf/java/com.aspose.pdf/font/) 并将其标记为嵌入。
1. 将文本内容添加到页面并保存输出文档。

```java
public static void embeddedFontsInNewDocument(Path outputFile) {
    try (Document document = new Document()) {
        try (Page page = document.getPages().add()) {
            TextFragment fragment = new TextFragment("");
            TextSegment segment = new TextSegment(" This is a sample text using Custom font.");
            TextState textState = new TextState();
            Font font = FontRepository.findFont("Arial");
            font.setEmbedded(true);
            textState.setFont(font);
            segment.setTextState(textState);
            fragment.getSegments().add(segment);
            page.getParagraphs().add(fragment);
        }
        document.save(outputFile.toString());
    }
}
```

## 设置 PDF 输出的默认字体

当保存的文档在输出生成期间应回退到特定字体时，请使用此模式。

1. 打开源 PDF [文档](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)。
1. 创建 [PdfSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/pdfsaveoptions/) 并设置默认字体名称。
1. 使用配置的保存选项保存文档。

```java
public static void setDefaultFont(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        PdfSaveOptions saveOptions = new PdfSaveOptions();
        saveOptions.setDefaultFontName("Arial");
        document.save(outputFile.toString(), saveOptions);
    }
}
```

## 获取PDF中使用的所有字体

此示例列出了文档中检测到的每种字体，以便您可以在导出或更新文件之前审核字体使用情况。

1. 打开源 PDF [文档](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)。
1. 枚举文档字体实用程序返回的字体。
1. 输出每个检测到的[字体](https://reference.aspose.com/pdf/java/com.aspose.pdf/font/)的名称。

```java
public static void getAllFonts(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (Font font : document.getFontUtilities().getAllFonts()) {
            System.out.println(font.getFontName());
        }
    }
}
```

## 通过对字体进行子集化来改进字体嵌入

当您想要减少字体负载，同时保持嵌入字体数据与文档使用保持一致时，请使用此方法。

1. 打开源 PDF [文档](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)。
1. 通过文档字体实用程序使用所需的 [FontSubsetStrategy](https://reference.aspose.com/pdf/java/com.aspose.pdf/fontsubsetstrategy/) 值运行字体子集化。
1. 保存优化后的文档。

```java
public static void improveFontsEmbedding(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.getFontUtilities().subsetFonts(FontSubsetStrategy.SubsetAllFonts);
        document.getFontUtilities().subsetFonts(FontSubsetStrategy.SubsetEmbeddedFontsOnly);
        document.save(outputFile.toString());
    }
}
```

## 设置文档打开缩放系数

此示例配置打开 PDF 时应应用的初始缩放级别。

1. 打开源 PDF [文档](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)。
1. 创建一个带有 [XYZExplicitDestination](https://reference.aspose.com/pdf/java/com.aspose.pdf/xyzexplicitdestination/) 的 [GoToAction](https://reference.aspose.com/pdf/java/com.aspose.pdf/gotoaction/)。
1. 将该操作指定为文档打开操作并保存结果。

```java
public static void setZoomFactor(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        GoToAction action = new GoToAction(new XYZExplicitDestination(1, 0.0, 0.0, 0.5));
        document.setOpenAction(action);
        document.save(outputFile.toString());
    }
}
```

## 获取文档打开缩放系数

使用此示例检查 PDF 是否已为其打开操作定义了显式缩放级别。

1. 打开源 PDF [文档](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)。
1. 检查打开操作是否是带有 [XYZExplicitDestination](https://reference.aspose.com/pdf/java/com.aspose.pdf/xyzexplicitdestination/) 的 [GoToAction](https://reference.aspose.com/pdf/java/com.aspose.pdf/gotoaction/)。
1. 输出配置的缩放值或报告未设置缩放。

```java
public static void getZoomFactor(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        if (document.getOpenAction() instanceof GoToAction action
                && action.getDestination() instanceof XYZExplicitDestination destination) {
            System.out.println("Zoom: " + destination.getZoom());
        } else {
            System.out.println("Zoom: not set");
        }
    }
}
```
