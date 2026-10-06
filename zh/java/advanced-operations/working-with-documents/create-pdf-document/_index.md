---
title: 在 Java 中创建 PDF 文件
linktitle: 创建 PDF 文档
type: docs
weight: 10
url: /zh/java/create-pdf-document/
description: 了解如何使用 Aspose.PDF 在 Java 中创建 PDF 文件并生成可搜索的 PDF。
lastmod: "2026-10-06"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 使用 Java 创建 PDF 文件和可搜索的 PDF 文档
Abstract: 本文展示了如何使用 Aspose.PDF for Java 创建 PDF 文档。它涵盖了从头开始创建新的 PDF，以及通过提供来自外部 OCR 引擎的 HOCR 输出，将基于图像的文档转换为可搜索的 PDF。
---
Aspose.PDF for Java 支持简单文档创建以及 OCR 辅助的可搜索 PDF 工作流。

## 创建一个新的 PDF 文档

当您需要从头创建一个简单的 PDF 文件时，请使用此方法。

1. 创建一个新的 PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. 添加一个 [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) 到文档。
1. 创建一个 [TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf/textfragment/) 并将其添加到页面。
1. 保存输出 PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

```java
public static void createNewDocument(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();
        page.getParagraphs().add(new TextFragment("Hello World!"));
        document.save(outputFile.toString());
    }
}
```

## 创建可搜索的 PDF

这 `createSearchablePdf` 示例用法 `Document.convert(...)` 带有 a `CallBackGetHocr` 实现。回调将源图像写入临时文件，并使用 Tesseract `hocr` 选项，读取生成的 HOCR 标记，并将其返回给 Aspose.PDF。

1. 打开源 PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. 创建 `CallBackGetHocr` 回调并将源文档转换为可搜索的 PDF 内容。
1. 保存已更新的 PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

```java
public static void createSearchablePdf(Path inputFile, Path outputFile) {
    Path tempDir = outputFile.getParent().resolve("ocr-temp");
    CallBackGetHocr cbgh = new CallBackGetHocr() {
        @Override
        public String invoke(java.awt.image.BufferedImage img) {
            // save the image, run Tesseract with "hocr", and return the HOCR text
            return fileContents.toString();
        }
    };
    try (Document document = new Document(inputFile.toString())) {
        document.convert(cbgh);
        document.save(outputFile.toString());
    }
}
```

## 获取文档窗口设置

使用此示例检查已存在 PDF 文档中存储的当前查看器首选项。

1. 打开源 PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. 从文档中读取所需的窗口和显示属性。
1. 输出当前设置以进行检查或调试。

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

此示例更新了在兼容的查看器中打开 PDF 时的显示方式。

1. 打开源 PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. 设置所需的窗口、布局和页面模式首选项。
1. 保存已更新的 PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

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

当文档需要携带其必需的字体以在其他系统上实现更可靠的渲染时，请使用此方法。

1. 打开源 PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. 启用标准字体嵌入并遍历每个使用的字体 [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/).
1. 标记任何未嵌入的 [Font](https://reference.aspose.com/pdf/java/com.aspose.pdf/font/) 用于嵌入的对象。
1. 保存更新后的文档。

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

## 在创建新 PDF 时嵌入字体

此示例从一开始就创建一个新的 PDF，并将嵌入式字体分配给文本内容。

1. 创建一个新的 PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 并添加一个 [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/).
1. 创建所需的 [TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf/textfragment/), [TextSegment](https://reference.aspose.com/pdf/java/com.aspose.pdf/textsegment/)，和 [TextState](https://reference.aspose.com/pdf/java/com.aspose.pdf/textstate/).
1. 解析目标 [Font](https://reference.aspose.com/pdf/java/com.aspose.pdf/font/) 从存储库中获取并将其标记为嵌入。
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

## 为 PDF 输出设置默认字体

在输出生成期间，如果已保存的文档需要回退到特定字体，请使用此模式。

1. 打开源 PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
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

## 获取 PDF 中使用的所有字体

此示例列出文档中检测到的每种字体，以便您在导出或更新文件之前审计字体使用情况。

1. 打开源 PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. 枚举文档字体实用程序返回的字体。
1. 输出每个检测到的名称 [Font](https://reference.aspose.com/pdf/java/com.aspose.pdf/font/).

```java
public static void getAllFonts(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (Font font : document.getFontUtilities().getAllFonts()) {
            System.out.println(font.getFontName());
        }
    }
}
```

## 通过子集化字体改进字体嵌入

当您希望在降低字体负载的同时保持嵌入的字体数据与文档使用保持一致时，请使用此方法。

1. 打开源 PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. 使用文档字体实用工具运行字体子集化，并满足所需 [FontSubsetStrategy](https://reference.aspose.com/pdf/java/com.aspose.pdf/fontsubsetstrategy/) 值。
1. 保存已优化的文档。

```java
public static void improveFontsEmbedding(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.getFontUtilities().subsetFonts(FontSubsetStrategy.SubsetAllFonts);
        document.getFontUtilities().subsetFonts(FontSubsetStrategy.SubsetEmbeddedFontsOnly);
        document.save(outputFile.toString());
    }
}
```

## 设置文档打开时的缩放比例

此示例配置在打开 PDF 时应应用的初始缩放级别。

1. 打开源 PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. 创建一个 [GoToAction](https://reference.aspose.com/pdf/java/com.aspose.pdf/gotoaction/) 带一个 [XYZExplicitDestination](https://reference.aspose.com/pdf/java/com.aspose.pdf/xyzexplicitdestination/).
1. 将操作指定为文档打开操作并保存结果。

```java
public static void setZoomFactor(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        GoToAction action = new GoToAction(new XYZExplicitDestination(1, 0.0, 0.0, 0.5));
        document.setOpenAction(action);
        document.save(outputFile.toString());
    }
}
```

## 获取文档打开时的缩放比例

使用此示例检查 PDF 是否已经为其打开操作定义了明确的缩放级别。

1. 打开源 PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. 检查打开操作是否为 a [GoToAction](https://reference.aspose.com/pdf/java/com.aspose.pdf/gotoaction/) 带一个 [XYZExplicitDestination](https://reference.aspose.com/pdf/java/com.aspose.pdf/xyzexplicitdestination/).
1. 输出已配置的缩放值，或者报告未设置缩放。

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
