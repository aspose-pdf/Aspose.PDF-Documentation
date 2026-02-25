---
title: 使用 Python 为 PDF 添加页码
linktitle: 添加页码
type: docs
weight: 30
url: /zh/python-net/add-page-number/
description: Aspose.PDF for Python via .NET 允许您使用 PageNumber Stamp 类向 PDF 文件添加页码水印。
lastmod: "2025-11-16"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 如何使用 Python 为 PDF 添加页码
Abstract: 本文讨论了在文档中添加页码以便于导航的重要性，并介绍了 Aspose.PDF for Python via .NET 库作为在 PDF 文件中实现此功能的工具。该库使用 PageNumberStamp 类，该类提供了自定义页码水印的属性，包括格式、边距、对齐方式和起始编号。过程包括创建 Document 对象和 PageNumberStamp 对象，配置所需属性，并使用 add_stamp() 方法将水印应用到 PDF 页面。文章提供了一个 Python 代码示例，演示如何设置并应用具有可自定义字体属性的页码水印。
---

所有文档都必须有页码。页码使读者更容易定位文档的不同部分。

**Aspose.PDF for Python via .NET** 允许您使用 [PageNumberStamp](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagenumberstamp/) 添加页码。

## 向 PDF 添加页码水印

使用 Aspose.PDF for Python 向 PDF 添加动态页码水印 [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/)。[`PageNumberStamp`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagenumberstamp/) 对象可自动显示当前页码以及总页数。示例展示了如何创建页码水印，使用 [`TextState`](https://reference.aspose.com/pdf/python-net/aspose.pdf/textstate/) 自定义其外观（字体、大小、样式、颜色、对齐方式和边距），并通过 [`Page.add_stamp()`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/#methods) 方法将其应用于 PDF 中的特定 [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/)。对齐值来自 [`HorizontalAlignment`](https://reference.aspose.com/pdf/python-net/aspose.pdf/horizontalalignment/) 枚举，颜色/字体/样式可通过 [`Color`](https://reference.aspose.com/pdf/python-net/aspose.pdf/color/) 和 [`FontStyles`](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/fontstyles/)（通过 [`FontRepository.find_font()`](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/fontrepository/#methods) 可发现字体）获得。此功能对于生成专业的编号文档以及在 PDF 工作流中实现自动分页非常有用。

1. 打开 PDF 文档。
1. 创建页码水印。
1. 设置水印属性。
1. 自定义文本样式。
1. 将水印应用到页面。
1. 保存修改后的 PDF。

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

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
    page_number_stamp.text_state.font_style = ap.text.FontStyles.BOLD
    page_number_stamp.text_state.font_style = ap.text.FontStyles.ITALIC
    page_number_stamp.text_state.foreground_color = ap.Color.blue_violet

    # Add stamp to particular page
    document.pages[1].add_stamp(page_number_stamp)

    # Save output document
    document.save(output_file_name)
```

## 向 PDF 添加罗马数字页码

向 PDF 文档的所有页面添加罗马数字格式的页码。页码通过使用 [`PageNumberStamp`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagenumberstamp/) 作为水印添加，可自定义字体、大小、样式、颜色和对齐方式。使用 [`NumberingStyle`](https://reference.aspose.com/pdf/python-net/aspose.pdf/numberingstyle/) 枚举可选择罗马数字或其他编号方案。编号也可以从任意指定的值开始。

1. 打开 PDF 文档。
1. 创建页码水印。
1. 配置水印属性。
1. 设置文本外观。
1. 将水印应用到所有页面。
1. 保存修改后的 PDF。

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

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

[添加 PDF 页码](https://products.aspose.app/pdf/page-number) 是一个在线免费网页应用，允许您了解页码添加功能的工作原理。

[![如何使用 Python 在 pdf 中添加页码](page_number.png)](https://products.aspose.app/pdf/page-number)


