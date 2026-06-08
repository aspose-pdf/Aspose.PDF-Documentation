---
title: 在 Python 中将 HTML 转换为 PDF
linktitle: 将 HTML 转换为 PDF 文件
type: docs
weight: 40
url: /zh/python-net/convert-html-to-pdf/
lastmod: "2026-06-08"
description: 了解如何在 Python 中使用 Aspose.PDF for Python via .NET 将 HTML 和 MHTML 转换为 PDF，包括 CSS 媒体设置、嵌入式字体和标记 PDF 输出。
sitemap:
    changefreq: "monthly"
    priority: 0.8
TechArticle: true
AlternativeHeadline: 如何在 Python 中使用 Aspose.PDF 将 HTML 转换为 PDF
Abstract: 本文解释了如何使用 Aspose.PDF for Python via .NET 将 HTML 和 MHTML 文件转换为 PDF。它涵盖了基本的 HTML 转 PDF 工作流，并展示了如何通过媒体类型、CSS 页面规则优先级、嵌入字体、单页输出以及逻辑结构生成来控制渲染，以创建可访问的标记 PDF。
---

## Python HTML 转 PDF 转换

**Aspose.PDF for Python via .NET** 允许您将现有的 HTML 文档转换为 PDF，并提供灵活的渲染选项。您可以微调输出的生成方式，以符合您的布局、样式、可访问性和归档要求。

## 将HTML转换为PDF

以下 Python 示例展示了将 HTML 文档转换为 PDF 的基本工作流程。

1. 创建该实例 [HtmlLoadOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/htmlloadoptions/) 类。
1. 初始化一个 [文档](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 包含源 HTML 文件的对象。
1. 通过调用保存输出的 PDF 文档 `document.save()`.

```python
from os import path
import aspose.pdf as ap

path_infile = path.join(self.data_dir, infile)
path_outfile = path.join(self.data_dir, "python", outfile)

load_options = ap.HtmlLoadOptions()
load_options.page_layout_option = ap.HtmlPageLayoutOption.SCALE_TO_PAGE_WIDTH
document = ap.Document(path_infile, load_options)
document.save(path_outfile)
print(infile + " converted into " + outfile)
```

## 相关转换

- [将 PDF 转换为 HTML](/pdf/zh/python-net/convert-pdf-to-html/) 当您需要从现有 PDF 文件生成适用于 Web 的输出时。
- [将其他文件格式转换为 PDF](/pdf/zh/python-net/convert-other-files-to-pdf/) 用于 EPUB、XPS、文本和 PostScript 的转换工作流。
- [将图像转换为 PDF](/pdf/zh/python-net/convert-images-format-to-pdf/) 当您的源内容是基于图像而不是 HTML 标记时。

{{% alert color="success" %}}
**尝试在线将HTML转换为PDF**

Aspose 推出在线应用程序 ["HTML 转 PDF"](https://products.aspose.app/html/en/conversion/html-to-pdf), 您可以在此测试转换质量和输出。

[![使用 App 将 HTML 转换为 PDF 的 Aspose.PDF](html.png)](https://products.aspose.app/html/en/conversion/html-to-pdf)
{{% /alert %}}

## 使用媒体类型将HTML转换为PDF

此示例展示了如何使用特定的渲染选项将 HTML 文件转换为 PDF。

1. 创建该实例 [HtmlLoadOptions()](https://reference.aspose.com/pdf/python-net/aspose.pdf/htmlloadoptions/) 类。
1. 设置 `html_media_type` 应用针对屏幕或打印布局的 CSS 规则，例如 `HtmlMediaType.SCREEN` 或 `HtmlMediaType.PRINT`.
1. 将 HTML 加载到一个 `ap.Document` 使用加载选项。
1. 将文档保存为 PDF。

```python
from os import path
import aspose.pdf as ap

path_infile = path.join(self.data_dir, infile)
path_outfile = path.join(self.data_dir, "python", outfile)

load_options = ap.HtmlLoadOptions()
load_options.html_media_type = ap.HtmlMediaType.SCREEN
document = ap.Document(path_infile, load_options)
document.save(path_outfile)
print(infile + " converted into " + outfile)
```

## 优先处理 CSS `@page` HTML 转 PDF 转换期间的规则

有些文档使用 [这个 `@page` 规则](https://developer.mozilla.org/en-US/docs/Web/CSS/@page) 用于页面布局。如果这些样式与其他设置冲突，您可以使用 `is_priority_css_page_rule`.

1. 创建该实例 [HtmlLoadOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/htmlloadoptions/) 类。
1. 设置 `is_priority_css_page_rule = False` 让其他样式获得更高的优先级 `@page` 规则。
1. 将 HTML 加载到一个 `ap.Document` 使用已配置的选项。
1. 将文档保存为 PDF。

```python
from os import path
import aspose.pdf as ap

path_infile = path.join(self.data_dir, infile)
path_outfile = path.join(self.data_dir, "python", outfile)

load_options = ap.HtmlLoadOptions()
# load_options.is_priority_css_page_rule = False
document = ap.Document(path_infile, load_options)
document.save(path_outfile)
print(infile + " converted into " + outfile)
```

## 将 HTML 转换为带嵌入字体的 PDF

本示例展示了如何在嵌入字体的同时将 HTML 文件转换为 PDF。如果您需要输出 PDF 保留原始排版，请设置 `is_embed_fonts` 到 `True`.

1. 创建 `HtmlLoadOptions()` 配置 HTML 到 PDF 转换。
1. 设置 `is_embed_fonts = True` 将HTML中使用的字体直接嵌入PDF。
1. 将 HTML 加载到一个 `ap.Document` 使用这些选项。
1. 将文档保存为 PDF。

```python
from os import path
import aspose.pdf as ap

path_infile = path.join(self.data_dir, infile)
path_outfile = path.join(self.data_dir, "python", outfile)

load_options = ap.HtmlLoadOptions()
load_options.is_embed_fonts = True
document = ap.Document(path_infile, load_options)
document.save(path_outfile)
print(infile + " converted into " + outfile)
```

## 在单个 PDF 页面上渲染 HTML 内容

本示例演示如何使用 Aspose.PDF for Python via .NET 将 HTML 文件转换为单页 PDF。使用 `is_render_to_single_page` 属性，当您希望将完整的 HTML 内容渲染到同一连续页面时。

1. 创建实例 `HtmlLoadOptions()` 配置转换过程。
1. 启用 `is_render_to_single_page` 将在单页上渲染完整的HTML内容。
1. 使用已配置的选项加载文档到一个 `ap.Document`.
1. 将结果保存为 PDF 文件。

```python
from os import path
import aspose.pdf as ap

path_infile = path.join(self.data_dir, infile)
path_outfile = path.join(self.data_dir, "python", outfile)

options = ap.HtmlLoadOptions()
options.is_render_to_single_page = True

doc = ap.Document(path_infile, options)
doc.save(path_outfile)
```

## 从 HTML 标记创建逻辑结构

逻辑结构，也称为 Tagged PDF，保留了原始 HTML 的语义层次结构，例如标题、段落和列表。这使得生成的 PDF 更具可访问性、可搜索性，并适用于结构化文档工作流。

通过在转换过程中启用逻辑结构，HTML DOM 被映射到 PDF 标记树中，而不是仅作为可视内容进行渲染。

为了满足可访问性要求，PDF 应该包含定义阅读顺序的逻辑结构元素，提供屏幕阅读器的替代文本，并保留内容的层次结构。

> 输出 PDF 中逻辑结构的质量直接取决于原始 HTML 标记的质量。结构不良或无效的 HTML 可能导致转换后的 PDF 中标记不完整或不准确。

1. 创建一个 HtmlLoadOptions 实例，以控制 HTML 的转换方式。
1. 激活语义标记，使 PDF 包含结构化元素。
1. 使用配置的选项打开 HTML 文件。
1. 保存结构化的 PDF。

```python
import aspose.pdf as ap

# Path to the source HTML
input_html_path = "input.html"
# Path for the Logical Structure PDF
output_pdf_path = "output_logical_structure.pdf"
# Initialize HtmlLoadOptions
options = ap.HtmlLoadOptions()
# Convert HTML markup to PDF logical structure elements
options.create_logical_structure = True
# Open PDF document
with ap.Document(input_html_path, options) as document:
    # Save PDF document
    document.save(output_pdf_path)
```

## 将 MHTML 转换为 PDF

此示例演示如何使用 Aspose.PDF for Python via .NET 将 MHT 或 MHTML 文件转换为具有特定页面尺寸的 PDF 文档。

1. 创建实例 `ap.MhtLoadOptions()` 配置 MHTML 文件处理。
1. 设置各种参数，例如页面大小。
1. 使用输入文件和配置的加载选项初始化文档。
1. 将生成的文档保存为 PDF。

```python
from os import path
import aspose.pdf as ap

path_infile = path.join(self.data_dir, infile)
path_outfile = path.join(self.data_dir, "python", outfile)
load_options = ap.MhtLoadOptions()
load_options.page_info.width = 842
load_options.page_info.height = 1191
document = ap.Document(path_infile, load_options)
document.save(path_outfile)
print(infile + " converted into " + outfile)
```
