---
title: 在 Python 中将 PDF 转换为 EPUB、文本、XPS 等
linktitle: 将 PDF 转换为其他格式
type: docs
weight: 90
url: /zh/python-net/convert-pdf-to-other-files/
lastmod: "2026-06-08"
description: 了解如何在 Python 中使用 Aspose.PDF for Python via .NET 将 PDF 文件转换为 EPUB、LaTeX、Markdown、文本、XPS 和 MobiXML。
sitemap:
    changefreq: "monthly"
    priority: 0.8
TechArticle: true
AlternativeHeadline: 如何在 Python 中将 PDF 转换为其他格式
Abstract: 本文提供了使用 Aspose.PDF for Python 将 PDF 文件转换为多种格式的全面指南。它涵盖了将 PDF 转换为 EPUB、LaTeX/TeX、Text、XPS 和 XML 格式。每个章节都以邀请尝试 Aspose 提供的在线应用程序将 PDF 转换为相应格式开始，强调这些工具的易用性和质量。
---

## 将 PDF 转换为 EPUB

{{% alert color="success" %}}
**尝试在线将 PDF 转换为 EPUB**

Aspose.PDF for Python 为您呈现在线应用 ["PDF 转 EPUB"](https://products.aspose.app/pdf/conversion/pdf-to-epub)，在此您可以尝试调查其功能以及其工作质量。

[![Aspose.PDF 转换 PDF 为 EPUB 的应用](pdf_to_epub.png)](https://products.aspose.app/pdf/conversion/pdf-to-epub)
{{% /alert %}}

<abbr title="Electronic Publication">EPUB</abbr> 是由国际数字出版论坛（IDPF）推出的免费且开放的电子书标准。文件的扩展名为 .epub。
EPUB 旨在用于可重排内容，这意味着 EPUB 阅读器可以针对特定显示设备优化文本。EPUB 也支持固定布局内容。该格式旨在作为出版商和转换公司内部使用的单一格式，同时用于分发和销售。它取代了 Open eBook 标准。

Aspose.PDF for Python 也支持将 PDF 文档转换为 EPUB 格式的功能。Aspose.PDF for Python 有一个名为 \u0027EpubSaveOptions\u0027 的类，可用作第二个参数 [document.save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) 方法，用于生成 EPUB 文件。
请尝试使用以下代码片段来实现此需求，使用 Python。

```python
import aspose.pdf as ap
from os import path
import sys

def convert_PDF_to_EPUB(infile, outfile):
    document = ap.Document(infile)
    save_options = ap.EpubSaveOptions()
    save_options.content_recognition_mode = ap.EpubSaveOptions.RecognitionMode.FLOW
    document.save(outfile, save_options)

    print(infile + " converted into " + outfile)
```

## 相关转换

- [转换 PDF 为 Word](/pdf/zh/python-net/convert-pdf-to-word/) 用于可编辑的 Office 文档输出。
- [将 PDF 转换为 HTML](/pdf/zh/python-net/convert-pdf-to-html/) 用于面向浏览器的输出。
- [将 PDF 转换为 PDF/A、PDF/E 和 PDF/X](/pdf/zh/python-net/convert-pdf-to-pdf_x/) 用于归档和符合标准的转换工作流。

## 将 PDF 转换为 LaTeX/TeX

**Aspose.PDF for Python via .NET** 支持将 PDF 转换为 LaTeX/TeX。
LaTeX 文件格式是一种文本文件格式，具备特殊标记，用于基于 TeX 的文档排版系统，以实现高质量的排版。

{{% alert color="success" %}}
**尝试在线将 PDF 转换为 LaTeX/TeX**

Aspose.PDF for Python 为您呈现在线应用 ["PDF 转 LaTeX"](https://products.aspose.app/pdf/conversion/pdf-to-tex)，在此您可以尝试调查其功能以及其工作质量。

[![Aspose.PDF 使用应用将 PDF 转换为 LaTeX/TeX](pdf_to_latex.png)](https://products.aspose.app/pdf/conversion/pdf-to-tex)
{{% /alert %}}

要将 PDF 文件转换为 TeX，Aspose.PDF 提供了一个类 [LaTeX 保存选项](https://reference.aspose.com/pdf/python-net/aspose.pdf/latexsaveoptions/) 它提供属性 OutDirectoryPath，用于在转换过程中保存临时图像。

以下代码片段展示了使用 Python 将 PDF 文件转换为 TEX 格式的过程。

```python
import aspose.pdf as ap
from os import path
import sys

def convert_PDF_to_TeX(infile, outfile):
    document = ap.Document(infile)
    save_options = ap.LaTeXSaveOptions()
    document.save(outfile, save_options)

    print(infile + " converted into " + outfile)
```

## 将 PDF 转换为文本

**Aspose.PDF for Python** 支持将整个 PDF 文档和单页转换为文本文件。您可以使用 'TextDevice' 类将 PDF 文档转换为 TXT 文件。以下代码片段说明了如何从所有页面提取文本。

```python
import aspose.pdf as ap
from os import path
import sys

def convert_PDF_to_TXT(infile, outfile):
    document = ap.Document(infile)
    device = ap.devices.TextDevice()
    device.process(document.pages[1], outfile)

    print(infile + " converted into " + outfile)
```

{{% alert color="success" %}}
**尝试将 PDF 转换为文本在线**

Aspose.PDF for Python 为您呈现在线应用 ["PDF 转文本"](https://products.aspose.app/pdf/conversion/pdf-to-txt)，在此您可以尝试调查其功能以及其工作质量。

[![Aspose.PDF 将 PDF 转换为文本的应用](pdf_to_text.png)](https://products.aspose.app/pdf/conversion/pdf-to-txt)
{{% /alert %}}

## 将 PDF 转换为 XPS

**Aspose.PDF for Python** 提供了将 PDF 文件转换为 XPS 格式的可能性。让我们尝试使用示例代码片段在 Python 中将 PDF 文件转换为 XPS 格式。

{{% alert color="success" %}}
**尝试在线将 PDF 转换为 XPS**

Aspose.PDF for Python 为您呈现在线应用 ["PDF 转 XPS"](https://products.aspose.app/pdf/conversion/pdf-to-xps)，在此您可以尝试调查其功能以及其工作质量。

[![Aspose.PDF 使用应用程序将 PDF 转换为 XPS](pdf_to_xps.png)](https://products.aspose.app/pdf/conversion/pdf-to-xps)
{{% /alert %}}

XPS 文件类型主要与微软公司的 XML Paper Specification（XML 纸张规范）相关联。XML Paper Specification（XPS），此前代号为 Metro，并整合了下一代打印路径（NGPP）营销概念，是微软将文档创建和查看集成到 Windows 操作系统中的倡议。

要将 PDF 文件转换为 XPS，Aspose.PDF 提供了该类 [XpsSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/xpssaveoptions/) 被用作第二个参数 [document.save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) 生成 XPS 文件的方法。

以下代码片段展示了将 PDF 文件转换为 XPS 格式的过程。

```python
import aspose.pdf as ap
from os import path
import sys

def convert_PDF_to_XPS(infile, outfile):
    document = ap.Document(infile)
    save_options = ap.XpsSaveOptions()
    save_options.use_new_imaging_engine = True
    document.save(outfile, save_options)

    print(infile + " converted into " + outfile)
```

## 将 PDF 转换为 MD

Aspose.PDF有类‘MarkdownSaveOptions()’，它可以将PDF文档转换为Markdown（MD）格式，同时保留图像和资源。

1. 使用 'ap.Document' 加载源 PDF。
1. 创建一个 'MarkdownSaveOptions' 的实例。
1. 将 'resources_directory_name' 设置为 'images' – 提取的图像将存储在此文件夹中。
1. 使用配置的选项保存转换后的 Markdown 文档。
1. 在转换后打印确认消息。

```python
import aspose.pdf as ap
from os import path
import sys

def convert_PDF_to_MD(infile, outfile):
    document = ap.Document(infile)
    save_options = ap.MarkdownSaveOptions()
    save_options.resources_directory_name = "images"
    save_options.use_image_html_tag = True
    document.save(outfile, save_options)

    print(infile + " converted into " + outfile)
```

一个 Markdown 文件，包含文本和链接的图片，存放在指定的 images 文件夹中。

## 将 PDF 转换为 MobiXML

此方法将 PDF 文档转换为 MOBI（MobiXML）格式，该格式常用于 Kindle 设备上的电子书。

1. 使用 'ap.Document' 加载源 PDF 文档。
1. 使用格式 'ap.SaveFormat.MOBI_XML' 保存文档。
1. 转换完成后打印确认消息。

```python
import aspose.pdf as ap
from os import path
import sys

def convert_PDF_to_MobiXML(infile, outfile):
    document = ap.Document(infile)
    document.save(outfile, ap.SaveFormat.MOBI_XML)

    print(infile + " converted into " + outfile)
```
