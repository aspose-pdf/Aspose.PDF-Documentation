---
title: 使用 Python 的 Hello World 示例
linktitle: Hello World 示例
type: docs
weight: 20
url: /zh/python-net/hello-world-example/
description: 此示例演示如何使用 Aspose.PDF for Python via .NET 创建包含 Hello World 文本的简单 PDF 文档。
lastmod: "2025-02-27"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 通过 Python 的 Hello World 示例
Abstract: 本文提供了一个使用 Aspose.PDF for Python via .NET 库创建 PDF 文档的 Hello World 示例。该示例演示了通过生成包含 “Hello World!” 文本的 PDF 来使用 Aspose.PDF API 的基本步骤。过程包括实例化 `Document` 对象、添加 `Page`、创建 `TextFragment` 对象、设置字体大小和颜色等文本属性，并使用 `TextBuilder` 将文本添加到页面。生成的 PDF 随后保存为 "HelloWorld_out.pdf"。文章还包含完整的 Python 代码片段，展示这些步骤，作为库使用的入门指南。
---

一个 “Hello World” 示例展示了任何编程语言中最简单的语法和程序。开发者通过学习如何在设备屏幕上打印 “Hello World”，来了解基本的编程语言语法。因此，我们通常从它开始熟悉我们的库。

在本文中，我们创建一个包含文本 “Hello World!” 的 PDF 文档。 在你的环境中安装 **Aspose.PDF for Python via .NET** 后，你可以运行以下代码示例，了解 Aspose.PDF API 的工作方式。

下面的代码片段遵循以下步骤：

1. 实例化一个 [文档](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 对象
1. 向文档对象添加一个 [页面](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/)
1. 创建一个 [文本片段](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragment/) 对象
1. 设置文本颜色
1. 创建文本构建器
1. 将 [文本片段](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragment/) 添加到页面
1. [document.save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) 生成的 PDF 文档

以下代码片段是一个 “Hello World” 程序，演示了 Aspose.PDF for Python via .NET API 的功能。

```python

from datetime import timedelta
import aspose.pdf as ap

def run_simple(self):
    # Initialize document object
    document = ap.Document()
    # Add page
    page = document.pages.add()
    # Add text to new page
    textFragment = ap.text.TextFragment("Hello, world!")
    textFragment.position = ap.text.Position(100, 600)

    textFragment.text_state.font_size = 12
    textFragment.text_state.font = ap.text.FontRepository.find_font(
        "TimesNewRoman"
    )
    textFragment.text_state.background_color = ap.Color.blue
    textFragment.text_state.foreground_color = ap.Color.yellow

    # Create TextBuilder object
    textBuilder = ap.text.TextBuilder(page)

    # Append the text fragment to the PDF page
    textBuilder.append_text(textFragment)

    document.save(self.data_dir + "HelloWorld_out.pdf")
```
