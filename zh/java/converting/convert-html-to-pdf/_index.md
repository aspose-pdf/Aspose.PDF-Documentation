---
title: 在 Java 中将 HTML 转换为 PDF
linktitle: 将 HTML 转换为 PDF 文件
type: docs
weight: 40
url: /zh/java/convert-html-to-pdf/
lastmod: "2026-10-06"
description: 了解如何在 Java 中使用 Aspose.PDF 将 HTML、MHTML 和网页转换为 PDF，包括媒体设置、CSS 页面规则、字体嵌入、SVG 内容以及单页输出。
sitemap:
    changefreq: "monthly"
    priority: 0.8
TechArticle: true
AlternativeHeadline: 如何在 Java 中使用 Aspose.PDF 将 HTML 转换为 PDF
Abstract: 本文介绍了如何使用 Aspose.PDF for Java 将 HTML 和 MHTML 文件转换为 PDF。它涵盖了基本的 HTML 转 PDF 工作流，并展示了如何通过媒体类型、CSS 页面规则优先级、嵌入字体、SVG 内容、单页输出以及直接从实时网页转换来控制渲染。
---
Aspose.PDF for Java 可以将本地 HTML 文件、归档的 MHTML 内容以及实时网页转换为 PDF 文档。您可以使用以下方式控制转换管道 `HtmlLoadOptions` 和 `MhtLoadOptions` 影响布局缩放、CSS 媒体处理、页面规则优先级、字体嵌入、资源解析以及单页渲染行为。

## 将 HTML 转换为 PDF

当需要将本地 HTML 文件直接转换为 PDF 文档时，请使用此示例。

1. 创建一个 [`HtmlLoadOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlloadoptions/) 用于配置在导入期间如何解释 HTML 源的实例。
1. 设置 [`HtmlPageLayoutOption`](https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlpagelayoutoption/) 到 `ScaleToPageWidth` 如此宽的 HTML 内容会被缩放至目标 PDF 页面宽度，而不是被裁剪。
1. 通过将其路径和配置的加载选项传入，打开源 HTML 文件 [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 构造函数。
1. 保存生成的 [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 作为目标输出路径中的 PDF 文件。

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

## 将 HTML 转换为 PDF 并使用媒体类型选项

在 HTML 转换期间应控制 CSS 媒体类型处理时，请使用此示例。

1. 创建一个 [`HtmlLoadOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlloadoptions/) 转换设置的实例。
1. 设置 [`HtmlMediaType`](https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlmediatype/) 到 `Screen` 当 HTML 应该使用针对屏幕显示而非打印媒体的 CSS 规则进行渲染时。
1. 打开带有配置加载选项的 HTML 文件，以便在转换期间应用基于媒体查询的样式。
1. 保存结果 [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 作为 PDF 文件。

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

## 使用 CSS 页面规则优先级将 HTML 转换为 PDF

在使用 CSS 时使用此示例 `@page` 规则应影响最终的 PDF 页面布局。

1. 创建一个 [`HtmlLoadOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlloadoptions/) 在打开 HTML 文件之前的实例。
1. 配置 `setPriorityCssPageRule(false)` 当其他布局设置应优先于 CSS 时 `@page` 源标记中的声明。
1. 将 HTML 内容加载到一个 [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 使用已配置的选项，以便在导入期间解析页面布局。
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

## 将 HTML 转换为带嵌入字体的 PDF

当输出 PDF 应通过嵌入来保留 HTML 字体时，请使用此示例。

1. 创建一个 [`HtmlLoadOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlloadoptions/) HTML 导入配置的实例。
1. 启用 `setEmbedFonts(true)` 因此，在 HTML 渲染期间解析的字体会存储在输出 PDF 中。
1. 使用这些加载选项打开 HTML 源，以在最终文档中保留原始排版。
1. 保存 [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 作为包含嵌入字体资源的 PDF。

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

## 在单个 PDF 页面上渲染 HTML 内容

当需要将长 HTML 内容保留在一页 PDF 上，而不是跨越多页时，请使用此示例。

1. 创建一个 [`HtmlLoadOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlloadoptions/) 转换设置的实例。
1. 启用 `setRenderToSinglePage(true)` 因此，导入的 HTML 被布局在单个 PDF 页面上，而不是分布在多个页面上。
1. 使用已配置的加载选项打开源 HTML，并让 Aspose.PDF 在 [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 中构建页面布局。
1. 保存输出 PDF 文件。

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

当 HTML 源包含必须在 PDF 中渲染的内联 SVG 数据时，请使用此示例。

1. 创建一个 [`HtmlLoadOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlloadoptions/) 实例使用 HTML 文件的父目录作为基路径，以便在转换期间能够一致地解析相关资源。
1. 通过将源路径和加载选项传递给，打开包含内联 SVG 标记的 HTML 文件 [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 构造函数。
1. 让 Aspose.PDF 将 HTML DOM 与嵌入的 SVG 元素一起渲染到 PDF 页面内容中。
1. 保存生成的 PDF 文档。

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

当需要将实时网页 URL 渲染并保存为 PDF 文档时，请使用此示例。

1. 创建一个 [`HtmlLoadOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlloadoptions/) 实例使用目标 URL，这样相对资源（例如样式表和图像）就可以相对于该地址进行解析。
1. 将 URL 字符串转换为 `URL` 对象并打开其输入流以获取实时 HTML 内容。
1. 创建一个 [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 从响应流和配置的加载选项中，以便下载的页面使用正确的基本 URL 进行处理。
1. 使用 try-with-resources 将渲染的网页保存为 PDF 文件并自动关闭流资源。

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

当需要将归档的 MHTML 文件转换为 PDF 文档时，请使用此示例。

1. 创建一个 [`MhtLoadOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/mhtloadoptions/) 用于让 Aspose.PDF 将源加载为 MIME HTML 内容的实例。
1. 打开 `.mht` 或 `.mhtml` 通过传递文件路径和 MHTML 加载选项来 [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 构造函数。
1. 让 Aspose.PDF 将归档的 HTML 内容及其嵌入的资源解析为 PDF 文档模型。
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
