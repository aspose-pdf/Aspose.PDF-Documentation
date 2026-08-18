---
title: 在 Java 中将 HTML 转换为 PDF
linktitle: 将 HTML 转换为 PDF 文件
type: docs
weight: 40
url: /java/convert-html-to-pdf/
lastmod: "2026-06-16"
description: 了解如何使用 Aspose.PDF 将 HTML、MHTML 和网页转换为 Java 中的 PDF，包括媒体设置、CSS 页面规则、字体嵌入、SVG 内容和单页输出。
sitemap:
    changefreq: "monthly"
    priority: 0.8
TechArticle: true
AlternativeHeadline: 如何在 Java 中使用 Aspose.PDF 将 HTML 转换为 PDF
Abstract: 本文介绍如何使用 Aspose.PDF for Java 将 HTML 和 MHTML 文件转换为 PDF。它涵盖了基本的 HTML 到 PDF 工作流程，并展示了如何控制媒体类型、CSS 页面规则优先级、嵌入字体、SVG 内容、单页输出以及从实时网页的直接转换的渲染。
---
Aspose.PDF for Java 可以将本地 HTML 文件、存档的 MHTML 内容和实时网页转换为 PDF 文档。您可以使用 `HtmlLoadOptions` 和 `MhtLoadOptions` 控制转换管道，以影响布局缩放、CSS 媒体处理、页面规则优先级、字体嵌入、资源分辨率和单页渲染行为。

## 将 HTML 转换为 PDF

当应将本地 HTML 文件直接转换为 PDF 文档时，请使用此示例。

1. 创建一个 [`HtmlLoadOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlloadoptions/) 实例以配置导入期间如何解释 HTML 源。
1. 将 [`HtmlPageLayoutOption`](https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlpagelayoutoption/) 设置为`ScaleToPageWidth`，以便宽 HTML 内容缩放到目标 PDF 页面宽度而不是被剪裁。
1. 通过将源 HTML 文件的路径和配置的加载选项传递到 [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 构造函数来打开源 HTML 文件。
1. 将生成的 [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 作为 PDF 文件保存在目标输出路径中。

```java
public static void convertHtmlToPdf(Path inputFile, Path outputFile) {
    HtmlLoadOptions loadOptions = new HtmlLoadOptions();
    loadOptions.setPageLayoutOption(HtmlPageLayoutOption.ScaleToPageWidth);
    try (Document document = new Document(inputFile.toString(), loadOptions)) {
        document.save(outputFile.toString());
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## 使用媒体类型选项将 HTML 转换为 PDF

当应在 HTML 转换期间控制 CSS 媒体类型处理时，请使用此示例。

1. 为转换设置创建一个 [`HtmlLoadOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlloadoptions/) 实例。
1. 当应使用用于屏幕显示而非打印媒体的 CSS 规则呈现 HTML 时，将 [`HtmlMediaType`](https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlmediatype/) 设置为 `Screen`。
1. 使用配置的加载选项打开 HTML 文件，以便在转换过程中应用依赖于媒体查询的样式。
1. 将生成的 [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 保存为 PDF 文件。

```java
public static void convertHtmlToPdfMediaType(Path inputFile, Path outputFile) {
    HtmlLoadOptions loadOptions = new HtmlLoadOptions();
    loadOptions.setHtmlMediaType(HtmlMediaType.Screen);
    try (Document document = new Document(inputFile.toString(), loadOptions)) {
        document.save(outputFile.toString());
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## 使用 CSS 页面规则优先将 HTML 转换为 PDF

当 CSS `@page` 规则应影响最终 PDF 页面布局时，请使用此示例。

1. 在打开 HTML 文件之前创建一个 [`HtmlLoadOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlloadoptions/) 实例。
1. 当其他布局设置应优先于源标记中的 CSS `@page` 声明时，配置`setPriorityCssPageRule(false)`。
1. 使用配置的选项将 HTML 内容加载到 [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 中，以便在导入期间解析页面布局。
1. 保存生成的 PDF 文件。

```java
public static void convertHtmlToPdfPriorityCssPageRule(Path inputFile, Path outputFile) {
    HtmlLoadOptions loadOptions = new HtmlLoadOptions();
    loadOptions.setPriorityCssPageRule(false);
    try (Document document = new Document(inputFile.toString(), loadOptions)) {
        document.save(outputFile.toString());
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## 将 HTML 转换为带有嵌入字体的 PDF

当输出 PDF 应通过嵌入 HTML 字体来保留 HTML 字体时，请使用此示例。

1. 为 HTML 导入配置创建一个 [`HtmlLoadOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlloadoptions/) 实例。
1. 启用`setEmbedFonts(true)`，以便在 HTML 渲染期间解析的字体存储在输出 PDF 中。
1. 使用这些加载选项打开 HTML 源，以在最终文档中保留原始排版。
1. 将 [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 保存为包含嵌入字体资源的 PDF。

```java
public static void convertHtmlToPdfEmbedFonts(Path inputFile, Path outputFile) {
    HtmlLoadOptions loadOptions = new HtmlLoadOptions();
    loadOptions.setEmbedFonts(true);
    try (Document document = new Document(inputFile.toString(), loadOptions)) {
        document.save(outputFile.toString());
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## 在单个 PDF 页面上呈现 HTML 内容

当较长的 HTML 内容应保留在一个 PDF 页面上而不是跨多个页面流动时，请使用此示例。

1. 为转换设置创建一个 [`HtmlLoadOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlloadoptions/) 实例。
1. 启用`setRenderToSinglePage(true)`，以便将导入的 HTML 布局在一个 PDF 页面上，而不是拆分到多个页面上。
1. 使用配置的加载选项打开源 HTML，并让 Aspose.PDF 在 [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 中构建页面布局。
1. 保存输出的 PDF 文件。

```java
public static void convertHtmlToPdfRenderContentToSamePage(Path inputFile, Path outputFile) {
    HtmlLoadOptions loadOptions = new HtmlLoadOptions();
    loadOptions.setRenderToSinglePage(true);
    try (Document document = new Document(inputFile.toString(), loadOptions)) {
        document.save(outputFile.toString());
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## 转换包含内联 SVG 的 HTML

当 HTML 源包含必须在 PDF 中呈现的内联 SVG 数据时，请使用此示例。

1. 创建一个以 HTML 文件的父目录为基本路径的 [`HtmlLoadOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlloadoptions/) 实例，以便在转换过程中可以一致地解析相关资源。
1. 通过将源路径和加载选项传递到 [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 构造函数来打开包含内联 SVG 标记的 HTML 文件。
1. 让 Aspose.PDF 将 HTML DOM 与嵌入的 SVG 元素一起渲染到 PDF 页面内容中。
1. 保存生成的PDF文档。

```java
public static void convertHtmlToPdfWithSvgData(Path inputFile, Path outputFile) {
    HtmlLoadOptions loadOptions = new HtmlLoadOptions(inputFile.getParent().toString());
    try (Document document = new Document(inputFile.toString(), loadOptions)) {
        document.save(outputFile.toString());
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## 将网页转换为 PDF

当应呈现实时 Web URL 并将其保存为 PDF 文档时，请使用此示例。

1. 使用目标 URL 创建一个 [`HtmlLoadOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlloadoptions/) 实例，以便可以根据该地址解析相关资源（例如样式表和图像）。
1. 将 URL 字符串转换为 `URL` 对象并打开其输入流以获取实时 HTML 内容。
1. 根据响应流和配置的加载选项创建 [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)，以便使用正确的基本 URL 处理下载的页面。
1. 将渲染的网页保存为 PDF 文件，并使用 try-with-resources 自动关闭流资源。

```java
public static void convertWebPageToPdf(String urlString, Path outputFile) {
    HtmlLoadOptions loadOptions = new HtmlLoadOptions(urlString);
    try {
        URL url = URI.create(urlString).toURL();

        try (InputStream inputStream = url.openStream()) {
            try (Document document = new Document(inputStream, loadOptions)) {
                document.save(outputFile.toString());
            }
        }
        System.out.println(url + " converted into " + outputFile);
    } catch (Exception e) {
        e.printStackTrace();
    }
}
```

## 将 MHTML 转换为 PDF

当应将存档的 MHTML 文件转换为 PDF 文档时，请使用此示例。

1. 创建一个 [`MhtLoadOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/mhtloadoptions/) 实例来告诉 Aspose.PDF 将源作为 MIME HTML 内容加载。
1. 通过将`.mht` 或`.mhtml` 文件的路径和MHTML 加载选项传递到[`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 构造函数中来打开`.mht` 或`.mhtml` 文件。
1. 让 Aspose.PDF 将存档的 HTML 内容及其嵌入资源解析为 PDF 文档模型。
1. 保存生成的 PDF 文件。

```java
public static void convertMhtmlToPdf(Path inputFile, Path outputFile) {
    MhtLoadOptions loadOptions = new MhtLoadOptions();
    try (Document document = new Document(inputFile.toString(), loadOptions)) {
        document.save(outputFile.toString());
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```
