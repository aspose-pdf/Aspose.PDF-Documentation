---
title: 将PDF文件转换为HTML格式
linktitle: 将PDF文件转换为HTML格式
type: docs
weight: 50
url: /php-java/convert-pdf-to-html/
lastmod: "2024-05-20"
description: 本主题向您展示如何使用Aspose.PDF通过PHP库将PDF文件转换为HTML格式。
sitemap:
    changefreq: "monthly"
    priority: 0.8
---

Aspose.PDF for PHP提供了许多功能，可以将各种文件格式转换为PDF文档，并将PDF文件转换为各种输出格式。本文讨论了如何将PDF文件转换为HTML格式，并将PDF文件中的图像保存在特定文件夹中。

{{% alert color="success" %}}
**尝试在线将PDF转换为HTML**

Aspose.PDF for PHP为您提供在线免费应用程序["PDF to HTML"](https://products.aspose.app/pdf/conversion/pdf-to-html)，您可以尝试研究其功能和工作质量。

[![Aspose.PDF 使用免费应用将PDF转换为HTML](pdf_to_html.png)](https://products.aspose.app/pdf/conversion/pdf-to-html)

{{% /alert %}}

当将多个页面的大型 PDF 文件转换为 HTML 格式时，输出显示为单个 HTML 页面。它可能会变得非常长。为了控制页面大小，可以在 PDF 到 HTML 转换过程中将输出拆分为多个页面。

## 将 PDF 页面转换为 HTML

Aspose.PDF for PHP 提供了许多功能，用于将各种文件格式转换为 PDF 文档，并将 PDF 文件转换为各种输出格式。本文讨论了如何将 PDF 文件转换为 HTML 格式，并将 PDF 文件中的图像保存在特定文件夹中。

以下代码片段向您展示了在将 PDF 转换为 HTML 时可以使用的所有可能选项。

```php
// 创建一个新的 Document 对象并加载输入的 PDF 文件
$document = new Document($inputFile);

// 创建一个新的 HtmlSaveOptions 对象，用于将文档保存为 HTML
$saveOption = new HtmlSaveOptions();

// 使用指定的保存选项将文档保存为 HTML
$document->save($outputFile, $saveOption);
```

## 将 PDF 转换为 HTML - 将输出拆分为多页 HTML

Aspose.PDF for PHP 支持将 PDF 文档转换为包括 HTML 在内的各种输出格式。然而，当转换大型 PDF 文件（包含多个页面）时，您可能需要将每个单独的 PDF 页面保存为单独的 HTML 文件。

当将包含多个页面的大型 PDF 文件转换为 HTML 格式时，输出显示为单个 HTML 页面。它可能会变得非常长。为了控制页面大小，可以在 PDF 到 HTML 转换过程中将输出拆分为多个页面。请尝试使用以下代码片段。

```php
// 创建一个新的 Document 对象并加载输入的 PDF 文件
$document = new Document($inputFile);

// 创建一个新的 HtmlSaveOptions 对象用于将文档保存为 HTML
$saveOption = new HtmlSaveOptions();

// 指定将输出拆分为多个页面
$saveOption->setSplitIntoPages(true);

// 使用指定的保存选项将文档保存为 HTML
$document->save($outputFile, $saveOption);
```

## 将 PDF 转换为 HTML - 避免将图像保存为 SVG 格式


默认情况下，将PDF转换为HTML时保存图像的输出格式为SVG。在转换过程中，某些来自PDF的图像会被转换为SVG矢量图像。这可能会很慢。相反，可以将图像转换为PNG。为此，Aspose.PDF提供了使用SVG矢量或创建PNG的选项。

为了在将PDF文件转换为HTML格式时完全删除图像作为SVG格式的渲染，请尝试使用以下代码片段。

```php
// 创建一个新的Document对象并加载输入的PDF文件
$document = new Document($inputFile);

// 创建一个新的HtmlSaveOptions对象用于将文档保存为HTML
$saveOption = new HtmlSaveOptions();

// 指定在PDF转换为HTML过程中保存SVG图像的文件夹
$saveOption->setSpecialFolderForSvgImages(DATA_DIR);

// 使用指定的保存选项将文档保存为HTML
$document->save($outputFile, $saveOption);
```

## 在转换过程中压缩SVG图像

为了在PDF转换为HTML的过程中压缩SVG图像，请尝试使用以下代码：

```php
// 创建一个新的 Document 对象并加载输入的 PDF 文件
$document = new Document($inputFile);

// 创建一个新的 HtmlSaveOptions 对象用于将文档保存为 HTML
$saveOptions = new HtmlSaveOptions();
$saveOptions = setCompressSvgGraphicsIfAny(true);

// 使用指定的保存选项将文档保存为 HTML
$document->save($outputFile, $saveOptions);
```

## 将 PDF 转换为 HTML - 指定图像文件夹

默认情况下，将 PDF 文件转换为 HTML 时，PDF 中的图像会保存在与输出 HTML 创建在同一目录的单独文件夹中。但有时，需要在生成 HTML 文件时为保存图像指定不同的文件夹。为此，我们引入了 [SaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/SaveOptions)。

[setSpecialFolderForAllImages 方法](https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlsaveoptions/#setSpecialFolderForSvgImages-java.lang.String-) 用于指定存储图像的目标文件夹。


```php
// 创建一个新的 Document 对象并加载输入的 PDF 文件
$document = new Document($inputFile);

// 创建一个新的 HtmlSaveOptions 对象用于将文档保存为 HTML
$saveOptions = new HtmlSaveOptions();
$saveOptions->setSpecialFolderForAllImages(DATA_DIR);

// 使用指定的保存选项将文档保存为 HTML
$document->save($outputFile, $saveOptions);
```

## 透明文本渲染

如果源/输入 PDF 文件包含被前景图像遮挡的透明文本，则可能会出现文本渲染问题。因此，为了应对这种情况，可以使用 SaveShadowedTextsAsTransparentTexts 和 SaveTransparentTexts 属性。

```php
// 创建一个新的 Document 对象并加载输入的 PDF 文件
$document = new Document($inputFile);

// 创建一个新的 HtmlSaveOptions 对象用于将文档保存为 HTML
$saveOptions = new HtmlSaveOptions();
$saveOptions->setSaveShadowedTextsAsTransparentTexts(true);
$saveOptions->setTransparentTexts(true);

// 使用指定的保存选项将文档保存为 HTML
$document->save($outputFile, $saveOptions);
```


## PDF 文档图层渲染

我们可以在 PDF 到 HTML 转换过程中，在单独的图层类型元素中渲染 PDF 文档图层：

```php
// 创建一个新的 Document 对象并加载输入的 PDF 文件
$document = new Document($inputFile);

// 创建一个新的 HtmlSaveOptions 对象，用于将文档保存为 HTML
$saveOptions = new HtmlSaveOptions();
$saveOptions->setConvertMarkedContentToLayers(true);

// 使用指定的保存选项将文档保存为 HTML
$document->save($outputFile, $saveOptions);
```

PDF 到 HTML 转换是 Aspose.PDF 的最受欢迎功能之一，因为它可以在各种平台上查看 PDF 文件的内容而无需使用 PDF 文档查看器。输出的 HTML 符合万维网标准，可以轻松地在所有网页浏览器中显示。利用此功能，可以在手持设备上查看 PDF 文件，因为您无需安装任何 PDF 查看应用程序，只需使用简单的网页浏览器即可。