---
title: 将 HTML 转换为 PDF 在 Python 中
linktitle: 将 HTML 转换为 PDF 文件
type: docs
weight: 40
url: zh/python-net/convert-html-to-pdf/
lastmod: "2022-12-22"
description: 本主题向您展示如何使用 Aspose.PDF 将 HTML 转换为 PDF 和 MHTML 转换为 PDF 在 Python 中。
sitemap:
    changefreq: "monthly"
    priority: 0.8
---

## 概述

Aspose.PDF for Python via .NET 是一个专业解决方案，可让您在应用程序中从网页和原始 HTML 代码创建 PDF 文件。

本文解释了如何 **使用 Python 将 HTML 转换为 PDF**。它涵盖以下主题。

_格式_：**HTML**
- [Python HTML 转换为 PDF](#python-html-to-pdf)
- [Python 转换 HTML 为 PDF](#python-html-to-pdf)
- [Python 如何将 HTML 转换为 PDF](#python-html-to-pdf)

## Python HTML 转 PDF 转换

**Aspose.PDF for Python** 是一个 PDF 操作 API，它可以让您无缝地将任何现有的 HTML 文档转换为 PDF。HTML 转换为 PDF 的过程可以灵活定制。

## 将 HTML 转换为 PDF

以下 Python 代码示例展示了如何将 HTML 文档转换为 PDF。

1. 创建一个 [HtmlLoadOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/htmlloadoptions/) 类的实例。
2. 初始化 [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 对象。
3. 通过调用 **Document.Save()** 方法保存输出 PDF 文档。

```python

    import aspose.pdf as ap

    input_pdf = DIR_INPUT + "little_html.html"
    output_pdf = DIR_OUTPUT + "convert_html_to_pdf.pdf"
    options = ap.HtmlLoadOptions()
    document = ap.Document(input_pdf, options)
    document.save(output_pdf)
```

{{% alert color="success" %}}
**尝试在线将 HTML 转换为 PDF**

Aspose 向您展示在线免费应用程序 ["HTML to PDF"](https://products.aspose.app/html/en/conversion/html-to-pdf)，您可以在其中尝试研究其功能和工作质量。

[![Aspose.PDF 转换 HTML 为 PDF 使用免费应用](html.png)](https://products.aspose.app/html/en/conversion/html-to-pdf)
{{% /alert %}}