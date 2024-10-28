---
title: 将HTML转换为PDF文件在Java中
linktitle: 将HTML转换为PDF文件
type: docs
weight: 40
url: /java/convert-html-to-pdf/
lastmod: "2021-11-19"
description: 本主题向您展示如何使用Aspose.PDF将HTML和MHTML格式转换为PDF文件。
sitemap:
    changefreq: "monthly"
    priority: 0.8
---

## 概述

本文解释了如何使用Java将HTML转换为PDF。代码非常简单，只需将HTML加载到Document类并保存为输出PDF。在Java中将MHTML转换为PDF也类似。它涵盖以下主题

- [Java HTML到PDF](#convert-html-to-pdf)
- [Java MHTML到PDF](#convert-mhtml-to-pdf)
- [Java 转换HTML到PDF](#convert-html-to-pdf)
- [Java 转换MHTML到PDF](#convert-mhtml-to-pdf)
- [Java 从HTML到PDF](#convert-html-to-pdf)
- [Java 从MHTML到PDF](#convert-mhtml-to-pdf)
- [Java HTML到PDF转换器 - 如何将网页转换为PDF](#convert-html-to-pdf)

- [Java HTML到PDF库、API或代码以编程方式从HTML渲染、保存、生成或创建PDF](#convert-html-to-pdf)

## Java HTML to PDF Converter Library

**Aspose.PDF for Java** 是一个PDF操作API，可以让您将任何现有的HTML文档无缝转换为PDF。HTML到PDF的转换过程可以灵活定制。

## Convert HTML to PDF

以下Java代码示例展示了如何将HTML文档转换为PDF。

1. 创建一个 [HtmlLoadOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/HtmlLoadOptions) 类的实例。
1. 初始化 [Document](https://reference.aspose.com/page/java/com.aspose.page/document) 对象。
1. 通过调用 **Document.save(String)** 方法保存输出PDF文档。

```java
// 打开源PDF文档
Document document = new Document(DATA_DIR + "PDFToHTML.pdf")

// 实例化HTML SaveOptions对象
HtmlSaveOptions htmlsaveOptions = new HtmlSaveOptions();

// 保存文档
document.save(DATA_DIR + "MultiPageHTML_out.html", htmlsaveOptions);
```

{{% alert color="success" %}}
**尝试在线将HTML转换为PDF**

Aspose为您提供在线免费应用程序 ["HTML to PDF"](https://products.aspose.app/html/en/conversion/html-to-pdf)，您可以尝试调查其功能和工作质量。

[![Aspose.PDF 转换 HTML 到 PDF 使用免费应用程序](html.png)](https://products.aspose.app/html/en/conversion/html-to-pdf)
{{% /alert %}}

## 从 HTML 到 PDF 的高级转换

HTML 转换引擎具有多个选项，允许我们控制转换过程。

### 媒体查询支持

1. 创建一个 HTML [LoadOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/HtmlLoadOptions)。
1. 设置打印或屏幕模式。
1. 初始化 [Document 对象](<https://reference.aspose.com/page/java/com.aspose.page/document>)。
1. 保存输出 PDF 文档。

媒体查询是一种流行的技术，用于为不同设备提供定制的样式表。我们可以使用 [HtmlMediaType](https://reference.aspose.com/pdf/java/com.aspose.pdf/HtmlMediaType) 属性设置设备类型。

```java
// 创建一个 HTML LoadOptions
HtmlLoadOptions options = new HtmlLoadOptions();

// 设置打印或屏幕模式
options.setHtmlMediaType(HtmlMediaType.Print);

// 初始化文档对象
String htmlFileName = Paths.get(DATA_DIR.toString(), "test.html").toString();
Document document = new Document(htmlFileName, options);

// 保存输出 PDF 文档
document.save(Paths.get(DATA_DIR.toString(), "HTMLtoPDF.pdf").toString());
document.close();
```


### 启用（禁用）字体嵌入

1. 添加新的 Html [LoadOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/HtmlLoadOptions)。
1. 启用/禁用字体嵌入。
1. 保存新的文档。

HTML 页面通常使用字体（例如，从本地文件夹、Google Fonts 等获取的字体）。我们还可以使用 [IsEmbedFonts](https://reference.aspose.com/pdf/java/com.aspose.pdf/HtmlLoadOptions#isEmbedFonts--) 属性来控制文档中字体的嵌入。

```java
HtmlLoadOptions options = new HtmlLoadOptions();
// 启用/禁用字体嵌入
options.setEmbedFonts(true);

Document document = new Document(DATA_DIR + "test_fonts.html", options);
document.save(DATA_DIR + "html_test.PDF");
document.close();
```

### 管理外部资源加载

转换引擎提供了一种机制，允许您控制与 HTML 文档相关联的某些资源的加载。

[HtmlLoadOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/HtmlLoadOptions) 类具有属性 [CustomLoaderOfExternalResources](https://reference.aspose.com/pdf/java/com.aspose.pdf/HtmlLoadOptions#setCustomLoaderOfExternalResources-com.aspose.pdf.LoadOptions.ResourceLoadingStrategy-)，我们可以用它来定义资源加载器的行为。

```java
HtmlLoadOptions options = new HtmlLoadOptions();

options.setCustomLoaderOfExternalResources(
        new LoadOptions.ResourceLoadingStrategy() {
            public LoadOptions.ResourceLoadingResult invoke(String resourceURI) {
                // 创建明确的模板资源以替换：
                LoadOptions.ResourceLoadingResult res = new LoadOptions.ResourceLoadingResult(new byte[] {});
                // 如果 i.imgur.com 服务器返回空字节数组
                if (resourceURI.contains("i.imgur.com")) {
                    return res;
                } else {
                    // 使用默认资源加载器处理资源
                    res.setLoadingCancelled(true);
                    return res;
                }
            }   
});

Document document = new Document(DATA_DIR + "test.html", options);
document.save(DATA_DIR + "html_test.PDF");
document.close();    
```

## 将 MHTML 转换为 PDF

{{% alert color="success" %}}
**尝试在线将 MHTML 转换为 PDF**


Aspose.PDF for Java 提供了一个在线免费应用程序 ["MHTML to PDF"](https://products.aspose.app/pdf/conversion/mhtml-to-pdf)，您可以在此尝试调查其功能和工作质量。

[![Aspose.PDF Convertion MHTML to PDF using Free App](mhtml.png)](https://products.aspose.app/pdf/conversion/mhtml-to-pdf)
{{% /alert %}}

<abbr title="MIME encapsulation of aggregate HTML documents">MHTML</abbr>，即 MIME HTML，是一种网页存档格式，用于将通常由外部链接（如图像、Flash 动画、Java 小程序和音频文件）表示的资源与 HTML 代码合并为单个文件。MHTML 文件的内容编码方式如同是一个 HTML 电子邮件消息，使用 MIME 类型 multipart/related。

下一个代码片段展示了如何使用 Java 将 MHTML 文件转换为 PDF 格式：

```java
// 创建一个 MhtLoadOptions 实例以指定 MHTML 文件的加载选项。
MhtLoadOptions options = new MhtLoadOptions();

// 设置 MHTML 文件的路径。
String mhtmlFileName = Paths.get(DATA_DIR.toString(), "samplefile.mhtml").toString();

// 将 MHTML 文件加载到 Document 对象中。
Document document = new Document(mhtmlFileName, options);

// 将文档保存为 PDF 文件。
document.save(Paths.get(DATA_DIR.toString(), "MarkdowntoPDF.pdf").toString());

// 关闭文档。
document.close();
```