---
title: 将 PDF 转换为 HTML 在 Python 中
linktitle: 将 PDF 转换为 HTML 格式
type: docs
weight: 50
url: zh/python-java/convert-pdf-to-html/
lastmod: "2021-11-01"
description: 本主题向您展示如何使用 Aspose.PDF for Python Java 库将 PDF 文件转换为 HTML 格式。
sitemap:
    changefreq: "monthly"
    priority: 0.8
---

## 概述

本文解释了如何**使用 Python 将 PDF 转换为 HTML**。它涵盖了以下主题。

_格式_: **HTML**
- [Python PDF 转 HTML](#python-pdf-to-html)
- [Python 将 PDF 转换为 HTML](#python-pdf-to-html)
- [Python 如何将 PDF 文件转换为 HTML](#python-pdf-to-html)


## 将 PDF 转换为 HTML

**Aspose.PDF for Python via .NET** 提供了许多功能，可以将各种文件格式转换为 PDF 文档，并将 PDF 文件转换为各种输出格式。
 这篇文章讨论了如何将PDF文件转换为<abbr title="HyperText Markup Language">HTML</abbr>。你可以只用几行Python代码将PDF转换为HTML。如果你想创建一个网站或将内容添加到在线论坛，你可能需要将PDF转换为HTML。将PDF转换为HTML的一种方法是通过Python编程实现。

{{% alert color="success" %}}
**尝试在线将PDF转换为HTML**

Aspose.PDF for Python为你提供了在线免费应用程序["PDF to HTML"](https://products.aspose.app/pdf/conversion/pdf-to-html)，你可以尝试调查其功能和工作质量。

[![Aspose.PDF转换PDF为HTML的免费应用程序](pdf_to_html.png)](https://products.aspose.app/pdf/conversion/pdf-to-html)
{{% /alert %}}

<a name="csharp-pdf-to-html"><strong>步骤：在Python中将PDF转换为HTML</strong></a>

1. 使用源PDF文档创建一个[Document](https://reference.aspose.com/pdf/python-java/aspose.pdf/document/)对象的实例。
2. 通过调用 [Document.save()](https://reference.aspose.com/pdf/python-java/aspose.pdf/document/#methods) 方法保存为 [HtmlSaveOptions](https://reference.aspose.com/pdf/python-java/aspose.pdf/htmlsaveoptions/)。

```python
from asposepdf import Api

documentName = "../../testdata/source.pdf"
documentOutName = "../../testout/result.html"
# 打开 PDF 文档
document = Api.Document(documentName)

# 以 HTML 格式保存文档
save_options = Api.HtmlSaveOptions()
document.save(documentOutName, save_options)
```

## 另请参见

本文还涵盖以下主题。代码与上面相同。

_格式_：**HTML**
- [Python PDF 转换为 HTML 代码](#python-pdf-to-html)
- [Python PDF 转换为 HTML API](#python-pdf-to-html)
- [Python PDF 编程转换为 HTML](#python-pdf-to-html)
- [Python PDF 转换为 HTML 库](#python-pdf-to-html)
- [Python 保存 PDF 为 HTML](#python-pdf-to-html)
- [Python 从 PDF 生成 HTML](#python-pdf-to-html)
- [Python 从 PDF 创建 HTML](#python-pdf-to-html)

- [Python PDF 转换为 HTML 转换器](#python-pdf-to-html)