---
title: 使用 Python 为 PDF 添加页眉和页脚
linktitle: 为 PDF 添加页眉和页脚
type: docs
weight: 50
url: /zh/python-net/add-headers-and-footers-of-pdf-file/
description: Aspose.PDF for Python via .NET 允许您使用 TextStamp 类向 PDF 文件添加页眉和页脚。
lastmod: "2025-11-16"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 如何使用 Python 为 PDF 添加页眉和页脚
Abstract: 本文提供了使用 **Aspose.PDF for Python via .NET** 向 PDF 文件添加页眉和页脚的完整指南，支持插入文本或图像。文章首先详细说明了使用 `TextStamp` 类在 PDF 文档的页眉中插入文本。可以调节字体大小、样式和颜色等关键属性，并通过 Python 代码示例演示了向页眉添加文本的方法。文章同样解释了如何向页脚添加文本，遵循相同的步骤。要添加图像，则使用 `ImageStamp` 类，并对页眉和页脚的图像添加过程进行说明，同样配有 Python 示例代码。此外，本文还讨论了在单个 PDF 文件中添加多个页眉的方式。这包括创建多个 `TextStamp` 对象，每个对象具有不同的格式，并将其应用于不同的页面。解释内容辅以详细的代码片段，演示了该功能。
---

本页简要概述了使用 Aspose.PDF for Python via .NET 向 PDF 文档添加页眉和页脚，涵盖文本、HTML、LaTeX、图像和基于表格的方法，以及动态页码和每页多个页眉；它解释了如何创建和样式化 [`HeaderFooter`](https://reference.aspose.com/pdf/python-net/aspose.pdf/headerfooter/) 对象（使用 [`TextFragment`](https://reference.aspose.com/pdf/python-net/aspose.pdf/textfragment/)、[`HtmlFragment`](https://reference.aspose.com/pdf/python-net/aspose.pdf/htmlfragment/)、[`TeXFragment`](https://reference.aspose.com/pdf/python-net/aspose.pdf/texfragment/)、[`Image`](https://reference.aspose.com/pdf/python-net/aspose.pdf/image/)、[`Table`](https://reference.aspose.com/pdf/python-net/aspose.pdf/table/) 等），调整 [`MarginInfo`](https://reference.aspose.com/pdf/python-net/aspose.pdf/margininfo/) 和 [`TextState`](https://reference.aspose.com/pdf/python-net/aspose.pdf/textstate/) 以实现精确定位，并使用实用的 Python 代码示例将结果附加到页面。

**Aspose.PDF for Python via .NET** 允许您在现有的[`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 中添加页眉和页脚。您可以向 PDF 文档添加图像或文本。同样，尝试使用 Python 在一个 PDF 文件中添加不同的页眉。

## 将页眉和页脚添加为文本片段

向 PDF 的所有页面添加简单的文本页眉和页脚。它创建 [`HeaderFooter`](https://reference.aspose.com/pdf/python-net/aspose.pdf/headerfooter/) 对象，将 [`TextFragment`](https://reference.aspose.com/pdf/python-net/aspose.pdf/textfragment/) 元素插入其中，设置 [`MarginInfo`](https://reference.aspose.com/pdf/python-net/aspose.pdf/margininfo/) 以实现正确定位，并将它们附加到文档的每一页。结果是每页都显示一致的页眉和页脚文本的 PDF。

以下代码片段演示了如何使用 Python 在 PDF 中将页眉和页脚添加为文本片段：

1. 为页眉和页脚创建文本片段。
1. 创建 HeaderFooter 对象并将文本片段添加进去。
1. 定义边距设置以控制页眉和页脚的位置。
1. 从输入文件加载 PDF 文档。
1. 遍历文档中的所有页面。
1. 将页眉和页脚分配给每一页。
1. 将修改后的 PDF 保存到输出文件。

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def add_header_and_footer_as_text(input_file, output_file):
    """
    Add simple text headers and footers to all pages of a PDF document.

    Creates basic text-based headers and footers that appear on every page
    of the PDF document. Headers show "header" text and footers show "footer" text.

    Args:
        input_file (str): Path to the input PDF file.
        output_file (str): Path where the modified PDF will be saved.

    Returns:
        None: The function modifies the PDF and saves it to the output path.

    Note:
        - Adds identical headers and footers to all pages
        - Sets margins of 50 units left and 20 units top
        - Uses simple TextFragment elements for content
        - Headers and footers are created separately for each page

    Example:
        >>> add_header_and_footer_as_text("input.pdf", "output.pdf")
        # Adds text headers and footers to all pages
    """
    # Create header text
    header_text = ap.text.TextFragment("Demo header")
    # Create header
    header = ap.HeaderFooter()
    header.paragraphs.add(header_text)

    # Create footer text
    footer_text = ap.text.TextFragment("Demo footer")

    # Create footer
    footer = ap.HeaderFooter()
    footer.paragraphs.add(footer_text)

    # Set header margin
    margin = ap.MarginInfo()
    margin.left = 50
    margin.top = 20
    header.margin = margin

    # Set footer margin
    footer.margin = margin

    # Open PDF document
    with ap.Document(input_file) as document:
        for i in range(1, len(document.pages) + 1):
            # Bind the header and footer to the page
            document.pages[i].header = header
            document.pages[i].footer = footer

        # Save PDF document
        document.save(output_file)
```

此方法可用于在每页的顶部和底部添加一致的标题、页码指示或法律免责声明。您还可以扩展它以包含图像或动态内容，例如页码。

## 为页码添加页眉和页脚

使用 Aspose.PDF for Python 为 PDF 文档的页眉和页脚添加自动页码。通过使用内置变量 $p（当前页码）和 $P（总页数），脚本会在每页动态插入页码。页眉显示格式为 “Page X from Y”，而页脚显示 “Page X / Y”。[`MarginInfo`](https://reference.aspose.com/pdf/python-net/aspose.pdf/margininfo/) 确保在每页上的正确放置。

1. 创建一个 TextFragment 作为页眉，使用 "Page $p from $P" 显示当前页码和总页数。
1. 创建 HeaderFooter 对象并将页眉文本添加进去。
1. 创建一个 TextFragment 作为页脚，使用 "Page $p / $P" 作为另一种编号样式。
1. 创建 Footer 对象并添加页脚文本。
1. 定义边距设置（左 = 50，顶部 = 20），并将其应用于页眉和页脚。
1. 从输入文件打开 PDF 文档。
1. 循环遍历所有页面，将页眉和页脚分配给每一页。
1. 将更新后的 PDF 保存到输出路径。

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def using_header_and_footer_for_page_numbering(input_file, output_file):
    """
    Add page numbering headers and footers to all pages of a PDF document.

    Creates headers and footers with dynamic page numbering using special variables.
    The $p variable represents the current page number and $P represents the total
    number of pages in the document.

    Args:
        input_file (str): Path to the input PDF file.
        output_file (str): Path where the modified PDF will be saved.

    Returns:
        None: The function modifies the PDF and saves it to the output path.

    Note:
        - Uses $p for current page number and $P for total pages
        - Header shows "Page X from Y" format
        - Footer shows "Page X / Y" format
        - Variables are automatically replaced by Aspose.PDF
        - Sets margins of 50 units left and 20 units top
        - Page numbering updates dynamically for each page

    Example:
        >>> using_header_and_footer_for_page_numbering("input.pdf", "output.pdf")
        # Adds page numbering headers and footers to all pages
    """
    # Create header text
    header_text = ap.text.TextFragment("Page $p from $P")
    # Create header
    header = ap.HeaderFooter()
    header.paragraphs.add(header_text)

    # Create footer text
    footer_text = ap.text.TextFragment("Page $p / $P")

    # Create footer
    footer = ap.HeaderFooter()
    footer.paragraphs.add(footer_text)

    # Create margins
    margin = ap.MarginInfo()
    margin.left = 50
    margin.top = 20

    # Set header margin
    header.margin = margin
    # Set footer margin
    footer.margin = margin

    # Open PDF document
    with ap.Document(input_file) as document:
        for i in range(1, len(document.pages) + 1):
            # Bind the header and footer to the page
            document.pages[i].header = header
            document.pages[i].footer = footer

        # Save PDF document
        document.save(output_file)
```

## 将页眉和页脚添加为 HTML 片段

使用 Aspose.PDF for Python 将 HTML 格式的页眉和页脚应用于 PDF 文档的每一页。通过使用 [`HtmlFragment`](https://reference.aspose.com/pdf/python-net/aspose.pdf/htmlfragment/)，脚本可以在页眉和页脚中显示富文本样式——例如粗体和斜体。使用 [`MarginInfo`](https://reference.aspose.com/pdf/python-net/aspose.pdf/margininfo/) 进行正确的定位，并将相同的格式化元素附加到文档的每一页。

以下代码片段演示了如何使用 Python 将页眉和页脚添加为 HTML 片段到 PDF 中：

1. 使用 HtmlFragment 创建 HTML 页眉片段——包括诸如 '<strong>' 用于加粗的样式化文本。
1. 创建 HeaderFooter 对象并将 HTML 页眉添加进去。
1. 使用 '<i>' 创建 HTML 页脚片段以实现斜体样式。
1. 创建 Footer 对象并将页脚 HTML 添加进去。
1. 配置边距（左 = 50，顶部 = 20），并将其分配给页眉和页脚。
1. 使用 'ap.Document()' 加载 PDF 文档。
1. 循环遍历所有页面，并将页眉和页脚分配给每一页。
1. 将修改后的 PDF 保存到指定的输出路径。

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def add_header_and_footer_as_html(input_file, output_file):
    """
    Add HTML-formatted headers and footers to all pages of a PDF document.

    Creates rich HTML-based headers and footers with formatting like bold
    and italic text. Demonstrates how to use HtmlFragment for styled content.

    Args:
        input_file (str): Path to the input PDF file.
        output_file (str): Path where the modified PDF will be saved.

    Returns:
        None: The function modifies the PDF and saves it to the output path.

    Note:
        - Uses HtmlFragment for rich text formatting
        - Header includes HTML with <strong> tag for bold text
        - Footer includes HTML with <i> tag for italic text
        - Sets margins of 50 units left and 20 units top
        - HTML tags are rendered properly in the PDF

    Example:
        >>> add_header_and_footer_as_html("input.pdf", "output.pdf")
        # Adds HTML-formatted headers and footers to all pages
    """
    # Create header HTML
    header_html = ap.HtmlFragment("This is an HTML <strong>Header</strong>")
    # Create header
    header = ap.HeaderFooter()
    header.paragraphs.add(header_html)

    # Create footer HTML
    footer_html = ap.HtmlFragment("Powered by <i>Aspose.PDF</i>")

    # Create footer
    footer = ap.HeaderFooter()
    footer.paragraphs.add(footer_html)

    # Set header margin
    margin = ap.MarginInfo()
    margin.left = 50
    margin.top = 20
    header.margin = margin

    # Set footer margin
    footer.margin = margin

    # Open PDF document
    with ap.Document(input_file) as document:
        for i in range(1, len(document.pages) + 1):
            # Bind the header and footer to the page
            document.pages[i].header = header
            document.pages[i].footer = footer

        # Save PDF document
        document.save(output_file)
```

使用 HtmlFragment 可通过内联样式或 HTML 标记实现丰富的格式化，相比纯文本提供了更大的设计灵活性。

## 将页眉和页脚添加为图像

使用 Aspose.PDF for Python 为 PDF 文档的每一页添加基于图像的页眉和页脚。相同的图像文件在每页的页眉和页脚中使用。[`MarginInfo`](https://reference.aspose.com/pdf/python-net/aspose.pdf/margininfo/) 用于定位图像，且图像会自动调整以适应页眉/页脚区域。

以下代码片段演示了如何使用 Python 将页眉和页脚作为图像添加到 PDF 中：

1. 将图像加载到 'ap.Image' 对象中，并准备将其用作页眉。
1. 创建一个 HeaderFooter 对象，并将页眉图像附加到该对象上。
1. 再次加载相同的图像以用作页脚。
1. 创建一个 Footer 对象，并将页脚图像添加到其中。
1. 使用 'ap.Document()' 加载输入的 PDF 文档。
1. 遍历文档的所有页面。
1. 应用边距（左 = 50）以定位页眉和页脚。
1. 将页眉和页脚分配给 PDF 中的每一页。
1. 将更新后的 PDF 保存到指定的输出文件。

此技术非常适合在页眉/页脚区域使用徽标或水印对文档进行品牌化。

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def add_header_and_footer_as_image(input_file, image_file, output_file):
    """
    Add image-based headers and footers to all pages of a PDF document.

    Creates headers and footers using image files. The same image is used
    for both header and footer positioning on each page.

    Args:
        input_file (str): Path to the input PDF file.
        image_file (str): Path to the image file to use for headers and footers.
        output_file (str): Path where the modified PDF will be saved.

    Returns:
        None: The function modifies the PDF and saves it to the output path.

    Note:
        - Uses the same image file for both header and footer
        - Creates separate Image objects for header and footer
        - Sets margin of 50 units left for positioning
        - Image files should be in supported formats (PNG, JPG, etc.)
        - Images are automatically sized to fit header/footer areas

    Example:
        >>> add_header_and_footer_as_image("input.pdf", "logo.png", "output.pdf")
        # Adds image headers and footers using logo.png
    """

    # Create header image
    header_image = ap.Image()
    header_image.file = image_file
    # Create header
    header = ap.HeaderFooter()
    header.paragraphs.add(header_image)

    # Create footer image
    footer_image = ap.Image()
    footer_image.file = image_file

    # Create footer
    footer = ap.HeaderFooter()
    footer.paragraphs.add(footer_image)

    # Open PDF document
    with ap.Document(input_file) as document:
        for i in range(1, len(document.pages) + 1):
            # Set header margin
            margin = ap.MarginInfo()
            margin.left = 50
            header.margin = margin

            # Set footer margin
            footer.margin = margin

            # Bind the header and footer to the page
            document.pages[i].header = header
            document.pages[i].footer = footer

        # Save PDF document
        document.save(output_file)
```

## 以表格形式添加页眉和页脚

使用 Aspose.PDF for Python 将结构化的基于表格的页眉和页脚添加到 PDF 文档的所有页面。`[表格]` 对象提供更好的布局控制、对齐和一致的格式化，用于复杂的页眉和页脚。页眉文字居中，而页脚文字左对齐，均使用 Arial 12pt 字体。列宽根据页面尺寸动态计算，以确保正确放置。

此代码片段使用 Aspose.PDF for Python via .NET 向 PDF 文档的每一页添加页眉和页脚（使用表格）。

1. 定义文本样式，使用 [`文本状态`](https://reference.aspose.com/pdf/python-net/aspose.pdf/textstate/) 为页眉和页脚设置字体、大小、对齐方式。
1. 为页眉和页脚创建 [`页眉页脚`](https://reference.aspose.com/pdf/python-net/aspose.pdf/headerfooter/) 对象。
1. 使用单行且单元格包含页眉文本的 [`表格`](https://reference.aspose.com/pdf/python-net/aspose.pdf/table/) 构建页眉。
1. 使用单行且单元格包含页脚文本的 [`表格`](https://reference.aspose.com/pdf/python-net/aspose.pdf/table/) 构建页脚。
1. 将表格添加到相应的 [`页眉页脚`](https://reference.aspose.com/pdf/python-net/aspose.pdf/headerfooter/) 对象中。
1. 为页脚设置 [`边距信息`](https://reference.aspose.com/pdf/python-net/aspose.pdf/margininfo/) 以获得适当的水平定位。
1. 使用适当的方法打开 [`文档`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/)。
1. 遍历所有页面，并将基于表格的页眉和页脚分配给每一页。
1. 将修改后的 [`文档`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 保存到输出文件。

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def add_header_and_footer_as_table(input_file, output_file):
    """
    Add table-based headers and footers to all pages of a PDF document.

    Creates headers and footers using table structures for better layout
    control and alignment. Demonstrates advanced formatting with text states.

    Args:
        input_file (str): Path to the input PDF file.
        output_file (str): Path where the modified PDF will be saved.

    Returns:
        None: The function modifies the PDF and saves it to the output path.

    Note:
        - Uses Table objects for structured layout
        - Header table has centered Arial 12pt text
        - Footer table has left-aligned Arial 12pt text
        - Column width calculated based on page width minus margins
        - Provides more precise control over text positioning

    Example:
        >>> add_header_and_footer_as_table("input.pdf", "output.pdf")
        # Adds table-structured headers and footers to all pages
    """
    text_state_header = ap.text.TextState()
    text_state_header.font = ap.text.FontRepository.find_font("Arial")
    text_state_header.font_size = 12
    text_state_header.horizontal_alignment = ap.HorizontalAlignment.CENTER
    text_state_footer = ap.text.TextState()
    text_state_footer.font = ap.text.FontRepository.find_font("Arial")
    text_state_footer.font_size = 12
    text_state_footer.horizontal_alignment = ap.HorizontalAlignment.LEFT
    # Create header
    header = ap.HeaderFooter()
    # Create footer
    footer = ap.HeaderFooter()
    # Create header Table
    table_header = ap.Table()
    table_header.column_widths = str(594 - header.margin.left - header.margin.right)
    header_row = table_header.rows.add()
    header_row.cells.add("This is a Table Header", text_state_header)
    # Create footer Table
    table = ap.Table()
    table.column_widths = str(594 - footer.margin.left - footer.margin.right)
    table.rows.add().cells.add("Powered by Aspose.PDF", text_state_footer)
    header.paragraphs.add(table_header)
    footer.paragraphs.add(table)
    # Set footer margin
    footer.margin.left = 150

    # Open PDF document
    with ap.Document(input_file) as document:
        for i in range(1, len(document.pages) + 1):
            # Bind the header and footer to the page
            document.pages[i].header = header
            document.pages[i].footer = footer

        # Save PDF document
        document.save(output_file)
```

## 以 LaTeX 形式添加页眉和页脚

使用 Aspose.PDF for Python 将包含 LaTeX 格式内容的页眉和页脚添加到 PDF 文档的所有页面。LaTeX 可渲染数学符号、日期、版权标记以及其他高级格式。页眉包括动态日期，而页脚显示版权符号以及当前页码和总页数。

以下代码片段展示了如何在使用 Aspose.PDF for Python via .NET 的 PDF 的页眉和页脚中使用 [`TeX片段`](https://reference.aspose.com/pdf/python-net/aspose.pdf/texfragment/)。

1. 使用适当的方法打开 [`文档`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/)。
1. 确定总页数以在动态页脚中使用。
1. 遍历文档的所有页面。
1. 为页眉创建一个 [`页眉页脚`](https://reference.aspose.com/pdf/python-net/aspose.pdf/headerfooter/) 对象。
1. 为包含 LaTeX 命令（例如 `\\today\\`）的页眉文本创建一个 [`TeX片段`](https://reference.aspose.com/pdf/python-net/aspose.pdf/texfragment/)。
1. 为页脚创建一个 [`页眉页脚`](https://reference.aspose.com/pdf/python-net/aspose.pdf/headerfooter/) 对象。
1. 为包含 LaTeX 符号和页码的页脚文本创建一个 [`TeX片段`](https://reference.aspose.com/pdf/python-net/aspose.pdf/texfragment/)。
1. 将 [`TeX片段`](https://reference.aspose.com/pdf/python-net/aspose.pdf/texfragment/) 添加到相应的页眉/页脚对象中。
1. 将页眉和页脚绑定到当前页面。
1. 将修改后的 [`文档`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 保存到输出文件。

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def add_header_and_footer_as_latex(input_file, output_file):
    """
    Add LaTeX-formatted headers and footers to all pages of a PDF document.

    Creates headers and footers using LaTeX markup for mathematical expressions,
    symbols, and advanced formatting. Demonstrates TeXFragment usage.

    Args:
        input_file (str): Path to the input PDF file.
        output_file (str): Path where the modified PDF will be saved.

    Returns:
        None: The function modifies the PDF and saves it to the output path.

    Note:
        - Uses TeXFragment for LaTeX rendering
        - Header includes LaTeX date command (\\today\\)
        - Footer includes copyright symbol and page numbering
        - LaTeX commands are processed and rendered properly
        - Page count is dynamically calculated and inserted

    Example:
        >>> add_header_and_footer_as_latex("input.pdf", "output.pdf")
        # Adds LaTeX-formatted headers and footers with symbols and page numbers
    """
    # Open PDF document
    with ap.Document(input_file) as document:
        page_count = len(document.pages)
        for i in range(1, page_count + 1):
            # Create header
            header = ap.HeaderFooter()
            h_latex_text = "This is a LaTex Header. \\today\\"
            h_l_text = ap.TeXFragment(h_latex_text, True)
            # Create footer
            footer = ap.HeaderFooter()
            f_latex_text = f"\\copyright\\ 2025 My Company -- Page \\thepage\\ is {page_count}"
            f_l_text = ap.TeXFragment(f_latex_text, True)

            header.paragraphs.add(h_l_text)
            footer.paragraphs.add(f_l_text)
            # Bind the header and footer to the page
            document.pages[i].header = header
            document.pages[i].footer = footer

        # Save PDF document
        document.save(output_file)
```
