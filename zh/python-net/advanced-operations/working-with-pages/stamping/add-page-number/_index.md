---
title: 在 Python 中为 PDF 添加页码
linktitle: 添加页码
type: docs
weight: 30
url: /zh/python-net/add-page-number/
description: 了解如何在 Python 中向 PDF 文档添加页码戳。
lastmod: "2026-06-08"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 如何使用 Python 为 PDF 添加页码
Abstract: 本文讨论了在文档中添加页码以便更轻松导航的重要性，并介绍了 Aspose.PDF for Python via .NET 库，作为在 PDF 文件中实现此功能的工具。该库使用 PageNumberStamp 类，提供了自定义页码戳的属性，包括格式、边距、对齐方式和起始编号。该过程包括创建 Document 对象和 PageNumberStamp 对象，配置所需属性，并使用 add_stamp() 方法将戳应用于 PDF 页面。文章提供了一个 Python 代码示例，演示如何设置和应用带有可自定义字体属性的页码戳。
---

所有文档都必须包含页码。页码使读者更容易定位文档的不同部分。

**Aspose.PDF for Python via .NET** 允许您添加页码 [PageNumberStamp](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagenumberstamp/).

## 向 PDF 添加页码印章

向 PDF 添加动态页码印章 [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 使用 Aspose.PDF for Python。 [`PageNumberStamp`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagenumberstamp/) 对象允许您自动显示当前页码以及总页数。示例展示了如何使用创建页码印章，定制其外观（字体、大小、样式、颜色、对齐方式和边距） [`TextState`](https://reference.aspose.com/pdf/python-net/aspose.pdf/textstate/)，并将其应用于特定的 [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) 在 PDF 中通过 [`Page.add_stamp()`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/#methods) 方法。对齐值来自于 [`HorizontalAlignment`](https://reference.aspose.com/pdf/python-net/aspose.pdf/horizontalalignment/) 枚举，颜色/字体/样式可通过 [`Color`](https://reference.aspose.com/pdf/python-net/aspose.pdf/color/) 和 [`FontStyles`](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/fontstyles/) (通过发现的字体 [`FontRepository.find_font()`](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/fontrepository/#methods)). 此功能对于生成专业的、带编号的文档以及在 PDF 工作流中自动化分页非常有用。

1. 打开 PDF 文档。
1. 创建页码印章。
1. 设置印章属性。
1. 自定义文本样式。
1. 将印章应用于页面。
1. 保存修改后的 PDF。

```python
import sys
import aspose.pdf as ap
from os import path

def add_page_num_stamp(input_file_name, output_file_name):
    # Open document
    document = ap.Document(input_file_name)

    # Create page number stamp
    page_number_stamp = ap.PageNumberStamp()
    # Whether the stamp is background
    page_number_stamp.background = False
    page_number_stamp.format = "Page # of " + str(len(document.pages))
    page_number_stamp.bottom_margin = 10
    page_number_stamp.horizontal_alignment = ap.HorizontalAlignment.CENTER
    page_number_stamp.starting_number = 1
    # Set text properties
    page_number_stamp.text_state.font = ap.text.FontRepository.find_font("Arial")
    page_number_stamp.text_state.font_size = 14.0
    page_number_stamp.text_state.font_style = (
        ap.text.FontStyles.BOLD | ap.text.FontStyles.ITALIC
    )
    page_number_stamp.text_state.foreground_color = ap.Color.blue_violet

    # Add stamp to particular page
    document.pages[1].add_stamp(page_number_stamp)

    # Save output document
    document.save(output_file_name)
```

## 向 PDF 添加罗马数字页码

在 PDF 文档的所有页面上添加罗马数字格式的页码。页码通过使用 [`PageNumberStamp`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagenumberstamp/)，具有可自定义的字体、大小、样式、颜色和对齐方式。使用的 [`NumberingStyle`](https://reference.aspose.com/pdf/python-net/aspose.pdf/numberingstyle/) 枚举来选择罗马数字或其他编号方案。编号也可以从任意指定的值开始。

1. 打开 PDF 文档。
1. 创建页码印章。
1. 配置印章属性。
1. 设置文本外观。
1. 将印章应用于所有页面。
1. 保存修改后的 PDF。

```python
import sys
import aspose.pdf as ap
from os import path

def add_page_num_stamp_roman(input_file_name, output_file_name):
    # Open document
    document = ap.Document(input_file_name)

    # Create page number stamp
    page_number_stamp = ap.PageNumberStamp()
    # Whether the stamp is background
    page_number_stamp.background = False
    page_number_stamp.bottom_margin = 10
    page_number_stamp.horizontal_alignment = ap.HorizontalAlignment.CENTER
    page_number_stamp.starting_number = 42
    page_number_stamp.numbering_style = ap.NumberingStyle.NUMERALS_ROMAN_UPPERCASE

    # Set text properties
    page_number_stamp.text_state.font = ap.text.FontRepository.find_font("Arial")
    page_number_stamp.text_state.font_size = 14.0
    page_number_stamp.text_state.font_style = ap.text.FontStyles.BOLD
    page_number_stamp.text_state.foreground_color = ap.Color.blue_violet

    # Add stamp to particular page
    for page in document.pages:
        page.add_stamp(page_number_stamp)

    # Save output document
    document.save(output_file_name)
```

## 实时示例

[添加 PDF 页码](https://products.aspose.app/pdf/page-number) 是一个在线免费网页应用程序，允许您研究添加页码功能的工作方式。

[![如何使用 Python 在 PDF 中添加页码](page_number.png)](https://products.aspose.app/pdf/page-number)

## 相关的盖章主题

- [在 Python 中对 PDF 页面加盖印章](/pdf/zh/python-net/stamping/)
- [使用 Python 向 PDF 添加页面印章](/pdf/zh/python-net/page-stamps-in-the-pdf-file/)
- [使用 Python 向 PDF 添加图像印章](/pdf/zh/python-net/image-stamps-in-pdf-page/)
- [在 Python 中向 PDF 添加文本印章](/pdf/zh/python-net/text-stamps-in-the-pdf-file/)