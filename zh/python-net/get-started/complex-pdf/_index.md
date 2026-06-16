---
title: 创建复杂的 PDF
linktitle: 创建复杂的 PDF
type: docs
weight: 30
url: /zh/python-net/complex-pdf-example/
description: Aspose.PDF for Python via .NET 允许您创建包含图像、文本片段和表格的更复杂文档。
lastmod: "2026-06-08"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 使用 Python 创建复杂的 PDF
Abstract: 本文扩展了在 “Hello, World” 示例中演示的基本 PDF 创建过程，展示如何使用 Python 和 Aspose.PDF 创建更复杂的 PDF 文档。示例文档是为一家虚构的客运渡轮公司开发的，包含一幅图像、两个文本片段（标题和段落）以及一张表格。该过程包括多个步骤 - 实例化 `Document` 对象来创建空 PDF，添加 `Page`，然后在页面中插入 `Image`。使用 Arial 字体、24pt 大小并居中对齐来创建标题的 `TextFragment`，随后将其添加到页面的段落中。第二个 `TextFragment` 用于描述，采用 Times New Roman 字体、14pt 大小且左对齐。随后创建并格式化表格，包括特定的列宽、边框和内边距。表格包含带有高亮单元格的标题行以及通过迭代生成的多行数据。
---

这 [Hello, World](/pdf/zh/python-net/hello-world-example/) 示例展示了使用 Python 和 Aspose.PDF 创建 PDF 文档的简易步骤。在本文中，我们将探讨使用 Aspose.PDF for Python 创建更复杂的文档。比如，我们将使用一家虚构的客运渡轮公司文档作为案例。我们的文档将包含一张图像、两个文本片段（标题和段落）以及一个表格。

如果我们从头创建文档，需要遵循以下步骤：

1. 实例化一个 [文档](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 对象。在此步骤中，我们将创建一个没有页面但带有一些元数据的空 PDF 文档。
1. 添加一个 [页面](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) 添加到文档对象。因此，现在我们的文档将有一页。
1. 添加一个 [图像](https://reference.aspose.com/pdf/python-net/aspose.pdf/image/) 到页面。
1. 创建一个 [TextFragment](https://reference.aspose.com/pdf/python-net/aspose.pdf/texfragment/) 用于标题。我们将在标题中使用 Arial 字体，字号为 24pt，居中对齐。
1. 将标题添加到页面 [段落](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/#properties).
1. 创建一个 [TextFragment](https://reference.aspose.com/pdf/python-net/aspose.pdf/texfragment/) 用于描述。我们将在描述中使用 Arial 字体，字号为 24pt，居中对齐。
1. 将描述添加到页面段落。
1. 创建并设置表格样式。设置列宽、边框、内边距和字体。
1. 在页面上添加表格 [段落](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/#properties).
1. 保存文档 \u0022Complex.pdf\u0022。

```python
from datetime import timedelta
import aspose.pdf as ap


def run_complex(self):

    # Initialize document object
    document = ap.Document()
    # Add page
    page = document.pages.add()

    # Add image
    imageFileName = self.data_dir + "logo.png"
    page.add_image(imageFileName, ap.Rectangle(20, 730, 120, 830, True))

    # Add Header
    header = ap.text.TextFragment("New ferry routes in Fall 2029")
    header.text_state.font = ap.text.FontRepository.find_font("Arial")
    header.text_state.font_size = 24
    header.horizontal_alignment = ap.HorizontalAlignment.CENTER
    header.position = ap.text.Position(130, 720)
    page.paragraphs.add(header)

    # Add description
    descriptionText = "Visitors must buy tickets online and tickets are limited to 5,000 per day. \
    Ferry service is operating at half capacity and on a reduced schedule. Expect lineups."
    description = ap.text.TextFragment(descriptionText)
    description.text_state.font = ap.text.FontRepository.find_font("Times New Roman")
    description.text_state.font_size = 14
    description.horizontal_alignment = ap.HorizontalAlignment.LEFT
    page.paragraphs.add(description)

    # Add table
    table = ap.Table()

    table.column_widths = "200"
    table.border = ap.BorderInfo(ap.BorderSide.BOX, 1.0, ap.Color.dark_slate_gray)
    table.default_cell_border = ap.BorderInfo(ap.BorderSide.BOX, 0.5, ap.Color.black)
    table.default_cell_padding = ap.MarginInfo(4.5, 4.5, 4.5, 4.5)
    table.margin.bottom = 10
    table.default_cell_text_state.font = ap.text.FontRepository.find_font("Helvetica")

    headerRow = table.rows.add()
    headerRow.cells.add("Departs City")
    headerRow.cells.add("Departs Island")

    i = 0
    while i < headerRow.cells.count:
        headerRow.cells[i].background_color = ap.Color.gray
        headerRow.cells[
            i
        ].default_cell_text_state.foreground_color = ap.Color.white_smoke
        i += 1

    time = timedelta(hours=6, minutes=0)
    incTime = timedelta(hours=0, minutes=30)

    i = 0
    while i < 10:
        dataRow = table.rows.add()
        dataRow.cells.add(str(time))
        time = time.__add__(incTime)
        dataRow.cells.add(str(time))
        i += 1

    page.paragraphs.add(table)

    document.save(self.data_dir + "Complex.pdf")
```
