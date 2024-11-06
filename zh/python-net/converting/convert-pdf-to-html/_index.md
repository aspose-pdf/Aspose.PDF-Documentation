---
title: 将 PDF 转换为 HTML 在 Python 中
linktitle: 将 PDF 转换为 HTML 格式
type: docs
weight: 50
url: zh/python-net/convert-pdf-to-html/
lastmod: "2021-11-01"
description: 本主题向您展示如何使用 Aspose.PDF for Python .NET 库将 PDF 文件转换为 HTML 格式。
sitemap:
    changefreq: "monthly"
    priority: 0.8
---

## 概述

本文解释了如何**使用 Python 将 PDF 转换为 HTML**。它涵盖了这些主题。

_格式_：**HTML**
- [Python PDF 转换为 HTML](#python-pdf-to-html)
- [Python 将 PDF 转换为 HTML](#python-pdf-to-html)
- [Python 如何将 PDF 文件转换为 HTML](#python-pdf-to-html)

## 将 PDF 转换为 HTML

**Aspose.PDF for Python via .NET** 提供了许多功能，用于将各种文件格式转换为 PDF 文档，并将 PDF 文件转换为各种输出格式。
 这篇文章讨论了如何将PDF文件转换为<abbr title="HyperText Markup Language">HTML</abbr>。你可以使用几行Python代码将PDF转换为HTML。如果你想创建一个网站或将内容添加到在线论坛，可能需要将PDF转换为HTML。将PDF转换为HTML的一种方法是使用Python编程。

{{% alert color="success" %}}
**尝试在线将PDF转换为HTML**

Aspose.PDF for Python为您提供了一个在线免费应用程序["PDF to HTML"](https://products.aspose.app/pdf/conversion/pdf-to-html)，您可以尝试研究其功能和工作质量。

[![Aspose.PDF Convertion PDF to HTML with Free App](pdf_to_html.png)](https://products.aspose.app/pdf/conversion/pdf-to-html)
{{% /alert %}}

<a name="csharp-pdf-to-html"><strong>步骤：在Python中将PDF转换为HTML</strong></a>

1. 创建一个[Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/)对象的实例，并使用源PDF文档。
2. 通过调用 [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) 方法，将其保存为 [HtmlSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/htmlsaveoptions/)。

```python

    import aspose.pdf as ap

    input_pdf = DIR_INPUT + "sample.pdf"
    output_pdf = DIR_OUTPUT + "convert_pdf_to_html.html"
    # 打开 PDF 文档
    document = ap.Document(input_pdf)

    # 以 HTML 格式保存文档
    save_options = ap.HtmlSaveOptions()
    document.save(output_pdf, save_options)
```

## 另请参见

本文还涵盖了以下主题。代码与上述相同。

_格式_: **HTML**
- [Python PDF 转 HTML 代码](#python-pdf-to-html)
- [Python PDF 转 HTML API](#python-pdf-to-html)
- [Python PDF 转 HTML 编程](#python-pdf-to-html)
- [Python PDF 转 HTML 库](#python-pdf-to-html)
- [Python 将 PDF 保存为 HTML](#python-pdf-to-html)
- [Python 从 PDF 生成 HTML](#python-pdf-to-html)
- [Python 从 PDF 创建 HTML](#python-pdf-to-html)

- [Python PDF 转 HTML 转换器](#python-pdf-to-html)