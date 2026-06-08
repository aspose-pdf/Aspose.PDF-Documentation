---
title: 在 Python 中操作 PDF 文档
linktitle: 操作 PDF 文档
type: docs
weight: 20
url: /zh/python-net/manipulate-pdf-document/
description: 学习如何在 Python 中验证、结构化和修改 PDF 文档，包括 TOC 管理和 PDF/A 检查。
lastmod: "2026-06-08"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 使用 Python 操作 PDF 文档的指南
Abstract: 这篇文章提供了一个关于使用 Python 操作 PDF 文档的综合指南，特别是使用 Aspose.PDF 库。它涵盖了多项功能，包括使用 `Document` 类的 `validate` 方法对 PDF 文档进行 PDF/A-1a 和 PDF/A-1b 合规性验证。它还详细说明了如何在 PDF 文件中添加、定制和管理目录（TOC），例如设置不同的 TabLeaderTypes、隐藏页码以及使用前缀自定义页码。此外，文章解释了如何通过嵌入 JavaScript 实现访问限制来为 PDF 文档设置过期日期，以及如何将 PDF 中的可填写表单展平为不可编辑。每个章节均附有代码片段，演示如何在 Python 中使用 Aspose.PDF 实现这些功能。
---

当您需要验证 PDF 合规性、构建或自定义目录、设置文档过期行为，或在 Python 工作流中将可填写的 PDF 扁平化时，此页面非常有用。

## 在 Python 中操作 PDF 文档

## 验证 PDF 文档是否符合 PDF/A 标准（A 1A 和 A 1B）

要验证 PDF 文档是否符合 PDF/A-1a 或 PDF/A-1b 兼容性，请使用 [文档](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 类 [验证](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) 方法。此方法允许您指定保存结果的文件名以及所需的验证类型 PdfFormat 枚举：PDF_A_1A 或 PDF_A_1B。

下面的代码片段向您展示如何验证 PDF 文档符合 PDF/A-1A。

```python
import sys
from os import path
import aspose.pdf as ap


def validate_pdfa_standard_a1a(input_pdf, output_pdf):
    document = ap.Document(input_pdf)
    document.validate(output_pdf, ap.PdfFormat.PDF_A_1A)
```

以下代码片段向您展示如何验证 PDF/A-1b 的 PDF 文档。

```python
import sys
from os import path
import aspose.pdf as ap


def validate_pdfa_standard_a1b(input_pdf, output_pdf):
    document = ap.Document(input_pdf)
    document.validate(output_pdf, ap.PdfFormat.PDF_A_1B)
```

## 使用 TOC

### 向现有 PDF 添加 TOC

PDF 中的 TOC 代表 “目录”。这是一个功能，允许用户通过提供文档章节和标题的概览，快速浏览文档。 

要向现有 PDF 文件添加 TOC，请使用 Heading 类 [aspose.pdf](https://reference.aspose.com/pdf/python-net/aspose.pdf/) 命名空间。该 [aspose.pdf](https://reference.aspose.com/pdf/python-net/aspose.pdf/) namespace 可以创建新的 PDF 文件，也可以操作已有的 PDF 文件。要向已有的 PDF 添加 TOC，请使用 Aspose.Pdf 命名空间。下面的代码片段展示了如何使用 Python via .NET 在已有的 PDF 文件中创建目录（table of contents）。

```python
import sys
from os import path
import aspose.pdf as ap


def add_table_of_contents(input_pdf, output_pdf):
    document = ap.Document(input_pdf)
    toc_page = document.pages.insert(1)
    toc_info = ap.TocInfo()
    title = ap.text.TextFragment("Table Of Contents")
    title.text_state.font_size = 20
    title.text_state.font_style = ap.text.FontStyles.BOLD
    toc_info.title = title
    toc_page.toc_info = toc_info

    titles = ["First page", "Second page"]
    for index, title_text in enumerate(titles[:2]):
        heading = ap.Heading(1)
        segment = ap.text.TextSegment(title_text)
        heading.toc_page = toc_page
        heading.segments.append(segment)
        destination_page = document.pages[index + 2]
        heading.destination_page = destination_page
        heading.top = destination_page.rect.height
        toc_page.paragraphs.add(heading)

    document.save(output_pdf)
```

### 为不同的 TOC 级别设置不同的 TabLeaderType

Aspose.PDF for Python 还允许为不同的 TOC 级别设置不同的 TabLeaderType。您需要设置 [线段虚线](https://reference.aspose.com/pdf/python-net/aspose.pdf/tocinfo/#properties) 的属性 [目录信息](https://reference.aspose.com/pdf/python-net/aspose.pdf/tocinfo/).

```python
import sys
from os import path
import aspose.pdf as ap


def set_toc_levels(input_pdf, output_pdf):
    document = ap.Document(input_pdf)
    toc_page = document.pages.add()
    toc_info = ap.TocInfo()
    toc_info.line_dash = ap.text.TabLeaderType.SOLID
    title = ap.text.TextFragment("Table Of Contents")
    title.text_state.font_size = 30
    toc_info.title = title
    toc_page.toc_info = toc_info

    toc_info.format_array_length = 4
    toc_info.format_array[0].margin.left = 0
    toc_info.format_array[0].margin.right = 30
    toc_info.format_array[0].line_dash = ap.text.TabLeaderType.DOT
    toc_info.format_array[0].text_state.font_style = (
        ap.text.FontStyles.BOLD | ap.text.FontStyles.ITALIC
    )
    toc_info.format_array[1].margin.left = 10
    toc_info.format_array[1].margin.right = 30
    toc_info.format_array[1].line_dash = 3
    toc_info.format_array[1].text_state.font_size = 10
    toc_info.format_array[2].margin.left = 20
    toc_info.format_array[2].margin.right = 30
    toc_info.format_array[2].text_state.font_style = ap.text.FontStyles.BOLD
    toc_info.format_array[3].line_dash = ap.text.TabLeaderType.SOLID
    toc_info.format_array[3].margin.left = 30
    toc_info.format_array[3].margin.right = 30
    toc_info.format_array[3].text_state.font_style = ap.text.FontStyles.BOLD

    page = document.pages.add()
    for level in range(1, 5):
        heading = ap.Heading(level)
        heading.is_auto_sequence = True
        heading.toc_page = toc_page
        heading.text_state.font = ap.text.FontRepository.find_font("Arial")
        segment = ap.text.TextSegment(f"Sample Heading{level}")
        heading.segments.append(segment)
        heading.is_in_list = True
        page.paragraphs.add(heading)

    document.save(output_pdf)
```

### 在目录中隐藏页码

如果您不想在目录（TOC）的标题旁显示页码，您可以使用 [是否显示页码](https://reference.aspose.com/pdf/python-net/aspose.pdf/tocinfo/#properties) 的属性 [目录信息](https://reference.aspose.com/pdf/python-net/aspose.pdf/tocinfo/) Class 为 false。请检查以下代码片段以在目录中隐藏页码：

```python
import sys
from os import path
import aspose.pdf as ap


def hide_page_numbers_in_toc(input_pdf, output_pdf):
    document = ap.Document(input_pdf)
    toc_page = document.pages.add()
    toc_info = ap.TocInfo()
    title = ap.text.TextFragment("Table Of Contents")
    title.text_state.font_size = 20
    title.text_state.font_style = ap.text.FontStyles.BOLD
    toc_info.title = title
    toc_info.is_show_page_numbers = False
    toc_page.toc_info = toc_info

    toc_info.format_array_length = 4
    toc_info.format_array[0].margin.right = 0
    toc_info.format_array[0].text_state.font_style = (
        ap.text.FontStyles.BOLD | ap.text.FontStyles.ITALIC
    )
    toc_info.format_array[1].margin.left = 30
    toc_info.format_array[1].text_state.underline = True
    toc_info.format_array[1].text_state.font_size = 10
    toc_info.format_array[2].text_state.font_style = ap.text.FontStyles.BOLD
    toc_info.format_array[3].text_state.font_style = ap.text.FontStyles.BOLD

    page = document.pages.add()
    for level in range(1, 2):
        heading = ap.Heading(level)
        heading.toc_page = toc_page
        heading.is_auto_sequence = True
        heading.is_in_list = True
        segment = ap.text.TextSegment(f"this is heading of level {level}")
        heading.segments.append(segment)
        page.paragraphs.add(heading)

    document.save(output_pdf)
```

### 在添加目录时自定义页码

在 PDF 文档中添加目录（TOC）时，通常会自定义目录中的页码。例如，我们可能需要在页码前添加前缀，如 P1、P2、P3 等。在这种情况下，Aspose.PDF for Python 提供 [页码前缀](https://reference.aspose.com/pdf/python-net/aspose.pdf/tocinfo/#properties) 的属性 [目录信息](https://reference.aspose.com/pdf/python-net/aspose.pdf/tocinfo/) 可以用来自定义页码的类，如下代码示例所示。

```python
import sys
from os import path
import aspose.pdf as ap


def customize_page_numbers_in_toc(input_pdf, output_pdf):
    document = ap.Document(input_pdf)
    toc_page = document.pages.insert(1)
    toc_info = ap.TocInfo()
    title = ap.text.TextFragment("Table Of Contents")
    title.text_state.font_size = 20
    title.text_state.font_style = ap.text.FontStyles.BOLD
    toc_info.title = title
    toc_info.page_numbers_prefix = "P"
    toc_page.toc_info = toc_info

    for index, page in enumerate(document.pages, start=1):
        heading = ap.Heading(1)
        heading.toc_page = toc_page
        heading.destination_page = page
        heading.top = page.rect.height
        segment = ap.text.TextSegment(f"Page {index}")
        heading.segments.append(segment)
        toc_page.paragraphs.add(heading)

    document.save(output_pdf)
```

## 如何设置 PDF 过期日期

我们对 PDF 文件应用访问权限，以便特定用户组能够访问 PDF 文档的特定功能/对象。为了限制 PDF 文件的访问，我们通常使用加密，并且可能需要设置 PDF 文件的到期时间，以便访问/查看文档的用户能够收到有关 PDF 文件失效的有效提示。

```python
import sys
from os import path
import aspose.pdf as ap


def set_pdf_expiry_date(input_pdf, output_pdf):
    document = ap.Document(input_pdf)
    document.pages.add()
    document.pages[1].paragraphs.add(ap.text.TextFragment("Hello World..."))
    script = ap.annotations.JavascriptAction(
        "var year=2017;"
        "var month=5;"
        "today = new Date(); today = new Date(today.getFullYear(), today.getMonth());"
        "expiry = new Date(year, month);"
        "if (today.getTime() > expiry.getTime())"
        "app.alert('The file is expired. You need a new one.');"
    )
    document.open_action = script
    document.save(output_pdf)
```

## 在Python中展平可填写的PDF

PDF 文档通常包含具备交互式可填写部件的表单，如单选按钮、复选框、文本框、列表等。为满足各种应用需求，使其不可编辑，我们需要将 PDF 文件扁平化。
Aspose.PDF 提供了在 Python 中仅需几行代码即可将 PDF 扁平化的功能：

```python
import sys
from os import path
import aspose.pdf as ap


def flatten_fillable_pdf(input_pdf, output_pdf):
    document = ap.Document(input_pdf)
    if document.form and document.form.fields:
        for field in document.form.fields:
            field.flatten()
    document.save(output_pdf)
```

## 相关文档主题

- [使用 Python 处理 PDF 文档](/pdf/zh/python-net/working-with-documents/)
- [在 Python 中格式化 PDF 文档](/pdf/zh/python-net/formatting-pdf-document/)
- [在 Python 中创建 PDF 文件](/pdf/zh/python-net/create-pdf-document/)
- [在 Python 中优化 PDF 文件](/pdf/zh/python-net/optimize-pdf/)
