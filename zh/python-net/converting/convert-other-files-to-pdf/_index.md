---
title: 在 Python 中将其他文件格式转换为 PDF
linktitle: 将其他文件格式转换为 PDF
type: docs
weight: 80
url: /zh/python-net/convert-other-files-to-pdf/
lastmod: "2026-06-08"
description: 了解如何使用 Aspose.PDF for Python via .NET 在 Python 中将 EPUB、Markdown、PCL、XPS、PostScript、XML 和 LaTeX 文件转换为 PDF。
sitemap:
    changefreq: "monthly"
    priority: 0.5
TechArticle: true
AlternativeHeadline: 如何在 Python 中将其他文件格式转换为 PDF
Abstract: 本文提供了一份使用 Python 将各种文件格式转换为 PDF 的综合指南，利用 Aspose.PDF for Python via .NET 的功能。文档概述了多个格式的转换过程，包括 EPUB、Markdown、PCL、Text、XPS、PostScript、XML、XSL-FO 和 LaTeX/TeX。每个章节提供了具体的代码片段和实现这些转换的说明。文章强调了 Aspose.PDF 的特性，例如针对每种文件类型定制的加载选项，以确保转换的准确性和高效性。此外，还突出在线转换应用的可用性，供用户亲自体验该功能。该指南是开发者在其 Python 应用中集成 PDF 转换能力的实用资源。
---

本文解释了如何 **使用 Python 将各种其他文件格式转换为 PDF**。它涵盖以下主题。

## 将 OFD 转换为 PDF

OFD 代表开放固定布局文档（也称为开放固定文档格式）。它是中国国家标准（GB/T 33190-2016），用于电子文档，被作为 PDF 的替代方案引入。

在 Python 中将 OFD 转换为 PDF 的步骤：

1. 使用 OfdLoadOptions() 来设置 OFD 加载选项。
1. 加载 OFD 文档。
1. 另存为 PDF。

```python
from os import path, remove
import aspose.pdf as ap
import sys

def convert_OFD_to_PDF(infile, outfile):
    load_options = ap.OfdLoadOptions()
    document = ap.Document(infile, load_options)
    document.save(outfile)

    print(infile + " converted into " + outfile)
```

## 将 LaTeX/TeX 转换为 PDF

LaTeX 文件格式是一种文本文件格式，使用 TeX 系列语言的 LaTeX 派生标记，并且 LaTeX 是 TeX 系统的派生格式。LaTeX（ˈleɪtɛk/lay-tek 或 lah-tek）是一种文档排版系统和文档标记语言。它被广泛用于许多领域的科学文献的交流和出版，包括数学、物理和计算机科学。它在包含复杂多语言材料的书籍和文章的编写和出版中也发挥关键作用，如韩文、日文、汉字和阿拉伯文，以及特刊。

LaTeX 使用 TeX 排版程序来格式化其输出，并且它本身是用 TeX 宏语言编写的。

{{% alert color="success" %}}
**尝试在线将 LaTeX/TeX 转换为 PDF**

Aspose.PDF for Python via .NET 为您呈现在线应用程序 ["LaTex 转 PDF"](https://products.aspose.app/pdf/conversion/tex-to-pdf)，在此您可以尝试调查其功能以及其工作质量。

[![Aspose.PDF 将 LaTeX/TeX 转换为 PDF（使用 App）](latex.png)](https://products.aspose.app/pdf/conversion/tex-to-pdf)
{{% /alert %}}

步骤 将 TEX 转换为 PDF（在 Python 中）:

1. 使用 LatexLoadOptions() 设置 LaTeX 加载选项。
1. 加载 LaTeX 文档。
1. 另存为 PDF。

```python
from os import path, remove
import aspose.pdf as ap
import sys

def convert_TEX_to_PDF(infile, outfile):
    load_options = ap.LatexLoadOptions()
    document = ap.Document(infile, load_options)
    document.save(outfile)

    print(infile + " converted into " + outfile)
```

## 将 EPUB 转换为 PDF

**Aspose.PDF for Python via .NET** 允许您轻松将 EPUB 文件转换为 PDF 格式。

EPUB（全称 electronic publication，电子出版物）是一种由国际数字出版论坛（IDPF）推出的免费且开放的电子书标准。文件的扩展名为 .epub。EPUB 旨在支持可重排内容，这意味着 EPUB 阅读器可以针对特定显示设备优化文本。

<abbr title="electronic publication">EPUB</abbr> 也支持固定布局内容。该格式旨在作为出版商和转换公司内部使用的统一格式，也用于分发和销售。它取代了 Open eBook 标准。EPUB 3 版本也得到图书行业研究集团（BISG）的认可，BISG 是一个领先的图书行业协会，致力于标准化最佳实践、研究、信息和活动，用于内容包装。

{{% alert color="success" %}}
**尝试在线将 EPUB 转换为 PDF**

Aspose.PDF for Python via .NET 为您呈现在线应用程序 ["EPUB 转 PDF"](https://products.aspose.app/pdf/conversion/epub-to-pdf)，在此您可以尝试调查其功能以及其工作质量。

[![Aspose.PDF 将 EPUB 转换为 PDF（使用 App）](epub.png)](https://products.aspose.app/pdf/conversion/epub-to-pdf)
{{% /alert %}}

在 Python 中将 EPUB 转换为 PDF 的步骤：

1. 使用 EpubLoadOptions() 加载 EPUB 文档。
1. 将 EPUB 转换为 PDF。
1. 打印确认。

下面的代码片段向您展示如何使用Python将 EPUB 文件转换为 PDF 格式。

```python
from os import path, remove
import aspose.pdf as ap
import sys

def convert_EPUB_to_PDF(infile, outfile):
    load_options = ap.EpubLoadOptions()
    document = ap.Document(infile, load_options)

    document.save(outfile)
    print(infile + " converted into " + outfile)
```

## 将 Markdown 转换为 PDF

**此功能在 19.6 版或更高版本中受支持。**

{{% alert color="success" %}}
**尝试在线将 Markdown 转换为 PDF**

Aspose.PDF for Python via .NET 为您呈现在线应用程序 ["Markdown 转 PDF"](https://products.aspose.app/pdf/conversion/md-to-pdf)，在此您可以尝试调查其功能以及其工作质量。

[![Aspose.PDF 将 Markdown 转换为 PDF 的应用](markdown.png)](https://products.aspose.app/pdf/conversion/md-to-pdf)
{{% /alert %}}

这段由 Aspose.PDF for Python via .NET 提供的代码片段可帮助将 Markdown 文件转换为 PDF，实现更好的文档共享、格式保留以及打印兼容性.o

以下代码片段展示了如何使用 Aspose.PDF 库实现此功能：

```python
from os import path, remove
import aspose.pdf as ap
import sys

def convert_MD_to_PDF(infile, outfile):
    load_options = ap.MdLoadOptions()
    document = ap.Document(infile, load_options)
    document.save(outfile)
    print(infile + " converted into " + outfile)
```

## 将 PCL 转换为 PDF

<abbr title="Printer Command Language">PCL</abbr> （Printer Command Language）是一种惠普（Hewlett-Packard）开发的打印机语言，用于访问标准打印机功能。PCL 1 至 5e/5c 级别是基于命令的语言，使用控制序列，按接收顺序进行处理和解释。在消费者层面，PCL 数据流由打印驱动程序生成。自定义应用程序也可以轻松生成 PCL 输出。

{{% alert color="success" %}}
**尝试在线将 PCL 转换为 PDF**

Aspose.PDF for .NET 为您呈现在线应用 ["PCL 转 PDF"](https://products.aspose.app/pdf/conversion/pcl-to-pdf)，在此您可以尝试调查其功能以及其工作质量。

[![Aspose.PDF 将 PCL 转换为 PDF 的应用](pcl_to_pdf.png)](https://products.aspose.app/pdf/conversion/pcl-to-pdf)
{{% /alert %}}

为了允许将 PCL 转换为 PDF，Aspose.PDF 拥有该类 [`PclLoadOptions`](https://reference.aspose.com/pdf/net/aspose.pdf/pclloadoptions) 它用于初始化 LoadOptions 对象。随后在 Document 对象初始化期间，该对象作为参数传入，帮助 PDF 渲染引擎确定源文档的输入格式。

以下代码片段展示了将 PCL 文件转换为 PDF 格式的过程。

在 Python 中将 PCL 转换为 PDF 的步骤：

1. 使用 PclLoadOptions() 加载 PCL 的选项。
1. 加载文档。
1. 另存为 PDF。

```python
from os import path, remove
import aspose.pdf as ap
import sys

def convert_PCL_to_PDF(infile, outfile):
    load_options = ap.PclLoadOptions()
    load_options.supress_errors = True

    document = ap.Document(infile, load_options)
    document.save(outfile)

    print(infile + " converted into " + outfile)
```

## 将预格式化文本转换为 PDF

**Aspose.PDF for Python via .NET** 支持将纯文本和预格式化文本文件转换为 PDF 格式的功能。

将文本转换为 PDF 意味着向 PDF 页面添加文本片段。对于文本文件，我们处理两种类型的文本：预格式化（例如，25 行，每行 80 个字符）和非格式化文本（纯文本）。根据我们的需求，我们可以自行控制此添加，或将其委托给库的算法。

{{% alert color="success" %}}
**尝试在线将 TEXT 转换为 PDF**

Aspose.PDF for Python via .NET 为您呈现在线应用程序 ["文本转PDF"](https://products.aspose.app/pdf/conversion/txt-to-pdf)，在此您可以尝试调查其功能以及其工作质量。

[![使用 App 将文本转换为 PDF 的 Aspose.PDF](text_to_pdf.png)](https://products.aspose.app/pdf/conversion/txt-to-pdf)
{{% /alert %}}

在 Python 中将 TEXT 转换为 PDF 的步骤：

1. 逐行读取输入文本文件。
1. 设置等宽字体（Courier New），以实现一致的文本对齐。
1. 创建一个新的 PDF 文档，并添加第一页，使用自定义的边距和字体设置。
1. 遍历文本文件的行。为了模拟打字机，我们使用 'monospace_font' 字体，大小为 12。
1. 将页面创建限制为4页。
1. 将最终的 PDF 保存到指定路径。

```python
from os import path, remove
import aspose.pdf as ap
import sys

def convert_TXT_to_PDF(infile, outfile):
    with open(infile, "r") as file:
        lines = file.readlines()

    monospace_font = ap.text.FontRepository.find_font("Courier New")

    document = ap.Document()
    page = document.pages.add()

    page.page_info.margin.left = 20
    page.page_info.margin.right = 10
    page.page_info.default_text_state.font = monospace_font
    page.page_info.default_text_state.font_size = 12
    count = 1
    for line in lines:
        if line != "" and line[0] == "\x0c":
            page = document.pages.add()
            page.page_info.margin.left = 20
            page.page_info.margin.right = 10
            page.page_info.default_text_state.font = monospace_font
            page.page_info.default_text_state.font_size = 12
            count = count + 1
        else:
            text = ap.text.TextFragment(line)
            page.paragraphs.add(text)

        if count == 4:
            break

    document.save(outfile)

    print(infile + " converted into " + outfile)
```

## 将 PostScript 转换为 PDF

本示例演示如何使用 Aspose.PDF for Python via .NET 将 PostScript 文件转换为 PDF 文档。

1. 创建一个 'PsLoadOptions' 实例以正确解释 PS 文件。
1. 使用加载选项将 'PostScript' 文件加载到 Document 对象中。
1. 将文档以 PDF 格式保存到所需的输出路径。

```python
from os import path, remove
import aspose.pdf as ap
import sys

def convert_PS_to_PDF(infile, outfile):
    load_options = ap.PsLoadOptions()

    document = ap.Document(infile, load_options)
    document.save(outfile)

    print(infile + " converted into " + outfile)
```

## 将 XPS 转换为 PDF

**Aspose.PDF for Python via .NET** 支持功能转换 <abbr title="XML Paper Specification">XPS</abbr> 文件转换为 PDF 格式。查看本文以解决您的任务。

XPS 文件类型主要与微软公司的 XML Paper Specification 相关。XML Paper Specification（XPS），前身代号为 Metro，并包含下一代打印路径（NGPP）营销概念，是微软将文档创建和查看集成到其 Windows 操作系统中的倡议。

以下代码片段展示了使用 Python 将 XPS 文件转换为 PDF 格式的过程。

```python
from os import path, remove
import aspose.pdf as ap
import sys

def convert_XPS_to_PDF(infile, outfile):
    load_options = ap.XpsLoadOptions()
    document = ap.Document(infile, load_options)
    document.save(outfile)

    print(infile + " converted into " + outfile)
```

{{% alert color="success" %}}
**尝试在线将 XPS 格式转换为 PDF**

Aspose.PDF for Python via .NET 为您呈现在线应用程序 ["XPS 转 PDF"](https://products.aspose.app/pdf/conversion/xps-to-pdf/)，在此您可以尝试调查其功能以及其工作质量。

[![Aspose.PDF 将 XPS 转换为 PDF 的应用程序](xps_to_pdf.png)](https://products.aspose.app/pdf/conversion/xps-to-pdf/)
{{% /alert %}}

## 将 XSL-FO 转换为 PDF

以下代码片段可用于使用 Aspose.PDF for Python via .NET 将 XSLFO 转换为 PDF 格式：

```python
from os import path, remove
import aspose.pdf as ap
import sys

def convert_XSLFO_to_PDF(xsltfile, xmlfile, outfile):
    load_options = ap.XslFoLoadOptions(xsltfile)
    load_options.parsing_errors_handling_type = (
        ap.XslFoLoadOptions.ParsingErrorsHandlingTypes.THROW_EXCEPTION_IMMEDIATELY
    )
    document = ap.Document(xmlfile, load_options)
    document.save(outfile)

    print(xmlfile + " converted into " + outfile)
```

## 使用 XSLT 将 XML 转换为 PDF

本示例演示了如何通过先使用 XSLT 模板将 XML 文件转换为 HTML，然后将 HTML 加载到 Aspose.PDF 中，从而将 XML 文件转换为 PDF。

1. 创建一个 'HtmlLoadOptions' 实例以配置 HTML 到 PDF 的转换。
1. 将转换后的 HTML 文件加载到 Aspose.PDF Document 对象中。
1. 将文档保存为 PDF 到指定的输出路径。
1. 成功转换后删除临时 HTML 文件。

```python
from os import path, remove
import aspose.pdf as ap
import sys

def convert_XSLFO_to_PDF(xsltfile, xmlfile, outfile):
    load_options = ap.XslFoLoadOptions(xsltfile)
    load_options.parsing_errors_handling_type = (
        ap.XslFoLoadOptions.ParsingErrorsHandlingTypes.THROW_EXCEPTION_IMMEDIATELY
    )
    document = ap.Document(xmlfile, load_options)
    document.save(outfile)

    print(xmlfile + " converted into " + outfile)
```

## 相关转换

- [将HTML转换为PDF](/pdf/zh/python-net/convert-html-to-pdf/) 用于 HTML 和 MHTML 转换场景。
- [将图像格式转换为 PDF](/pdf/zh/python-net/convert-images-format-to-pdf/) 当您的输入是 PNG、JPEG、TIFF、SVG 或其他图像时。
- [将 PDF 转换为其他格式](/pdf/zh/python-net/convert-pdf-to-other-files/) 如果您还需要反向转换，例如 PDF 到 EPUB、Markdown 或文本。
