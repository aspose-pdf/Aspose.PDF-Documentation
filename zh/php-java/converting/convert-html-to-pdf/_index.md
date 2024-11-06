---
title: 将HTML转换为PDF
linktitle: 将HTML转换为PDF
type: docs
weight: 40
url: zh/php-java/convert-html-to-pdf/
lastmod: "2024-05-20"
description: 本主题向您展示如何使用Aspose.PDF将HTML和MHTML格式转换为PDF文件。
sitemap:
    changefreq: "monthly"
    priority: 0.8
---

## 概述

本文解释了如何使用PHP将HTML转换为PDF。代码非常简单，只需将HTML加载到Document类中并将其保存为输出PDF。将MHTML转换为Java中的PDF也类似。它涵盖以下主题

## Java HTML到PDF转换库

**Aspose.PDF for PHP via Java** 是一个PDF操作API，可让您无缝地将任何现有HTML文档转换为PDF。HTML到PDF的转换过程可以灵活定制。

## 将HTML转换为PDF

以下Java代码示例显示了如何将HTML文档转换为PDF。

1. 创建一个[HtmlLoadOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/HtmlLoadOptions)类的实例。

1. 初始化 [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 对象。
1. 通过调用 [Document.save(String)](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/#save-java.lang.String-) 方法保存输出 PDF 文档。

```php
    // 创建一个 HtmlLoadOptions 实例以指定 HTML 文件的加载选项
    $loadOption = new HtmlLoadOptions();

    // 创建一个新的 Document 对象并加载 HTML 文件
    $document = new Document($inputFile, $loadOption);

    // 将文档保存为 PDF 文件
    $document->save($outputFile);
```

## 从 HTML 到 PDF 的高级转换

HTML 转换引擎有多个选项，可以让我们控制转换过程。

### 媒体查询支持

1. 创建一个 HTML [LoadOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/HtmlLoadOptions)。
1. [设置打印或屏幕](https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlloadoptions/#setHtmlMediaType-int-) 模式。

1. 初始化 [Document 对象](https://reference.aspose.com/page/java/com.aspose.page/document)。
1. 保存输出的 PDF 文档。

媒体查询是一种流行的技术，用于为不同设备提供定制的样式表。我们可以使用 [HtmlMediaType](https://reference.aspose.com/pdf/java/com.aspose.pdf/HtmlMediaType) 类设置设备类型。

```php

    // 创建 HtmlLoadOptions 的实例来指定 HTML 文件的加载选项
    $htmlMediaType = new HtmlMediaType();

    // 设置打印或屏幕模式
    $loadOption->setHtmlMediaType($htmlMediaType->Print);

    // 创建一个新的 Document 对象并加载 HTML 文件
    $document = new Document($inputFile, $loadOption);

    // 将文档保存为 PDF 文件
    $document->save($outputFile);
```

### 启用（禁用）字体嵌入

1. 添加新的 Html [LoadOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/HtmlLoadOptions)。
1. 禁用字体嵌入。
1. 保存新的文档。

HTML 页面经常使用字体（例如。
 从本地文件夹、Google Fonts 等获取字体）。我们还可以使用 [setEmbedFonts](https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlloadoptions/#setEmbedFonts-boolean-) 属性控制文档中字体的嵌入。

```php

    // 创建一个 HtmlLoadOptions 实例以指定 HTML 文件的加载选项
    $loadOption = new HtmlLoadOptions();

    // 禁用字体嵌入
    $loadOption->setEmbedFonts(true);

    // 创建一个新的 Document 对象并加载 HTML 文件
    $document = new Document($inputFile, $loadOption);

    // 将文档保存为 PDF 文件
    $document->save($outputFile);
```

## 将 MHTML 转换为 PDF

<abbr title="MIME encapsulation of aggregate HTML documents">MHTML</abbr>，即 MIME HTML，是一种网页存档格式，用于将通常由外部链接表示的资源（如图像、Flash 动画、Java 小程序和音频文件）与 HTML 代码合并为一个文件。 The content of an MHTML file is encoded as if it were an HTML email message, using the MIME type multipart/related.

MHTML 文件的内容被编码为类似于 HTML 电子邮件消息，使用 MIME 类型 multipart/related。

Next code snippet show how to covert MHTML files to PDF format with Java:

下面的代码片段展示了如何使用 Java 将 MHTML 文件转换为 PDF 格式：

```php

    // Create a new instance of the MhtLoadOptions class.
    // 创建 MhtLoadOptions 类的新实例。
    $loadOption = new MhtLoadOptions();

    // Create a new instance of the Document class and load the MHTML file.
    // 创建 Document 类的新实例并加载 MHTML 文件。
    $document = new Document($inputFile, $loadOption);

    // Save the document as a PDF file.
    // 将文档保存为 PDF 文件。
    $document->save($outputFile);
```