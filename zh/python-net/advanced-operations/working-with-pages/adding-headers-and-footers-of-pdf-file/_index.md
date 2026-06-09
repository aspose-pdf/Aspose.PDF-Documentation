---
title: 在 Python 中添加 PDF 页眉和页脚
linktitle: 向 PDF 添加页眉和页脚
type: docs
weight: 50
url: /zh/python-net/add-headers-and-footers-of-pdf-file/
description: 了解如何在 Python 中使用文本、图像和结构化内容向 PDF 文件添加页眉和页脚。
lastmod: "2026-06-08"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 使用 Python 为 PDF 文件添加页眉和页脚。
Abstract: 本文展示了如何使用 Aspose.PDF for Python via .NET 为 PDF 文档添加页眉和页脚。它涵盖了文本、页码、HTML、图像、表格以及基于 LaTeX 的页眉和页脚内容。
---

使用此页面在 PDF 页面上添加一致的页眉和页脚内容，使用 **Aspose.PDF for Python via .NET**。

您可以使用来构建页眉和页脚 [`TextFragment`](https://reference.aspose.com/pdf/python-net/aspose.pdf/textfragment/), [`HtmlFragment`](https://reference.aspose.com/pdf/python-net/aspose.pdf/htmlfragment/), [`TeXFragment`](https://reference.aspose.com/pdf/python-net/aspose.pdf/texfragment/), [`Image`](https://reference.aspose.com/pdf/python-net/aspose.pdf/image/)，和 [`Table`](https://reference.aspose.com/pdf/python-net/aspose.pdf/table/) 对象，然后通过它们进行应用 [`HeaderFooter`](https://reference.aspose.com/pdf/python-net/aspose.pdf/headerfooter/) 在每页上。

## 将页眉和页脚添加为文本片段

为 PDF 的所有页面添加简易的文本页眉和页脚。它创建 [`HeaderFooter`](https://reference.aspose.com/pdf/python-net/aspose.pdf/headerfooter/) 对象，插入 [`TextFragment`](https://reference.aspose.com/pdf/python-net/aspose.pdf/textfragment/) 将元素放入它们，设置 [`MarginInfo`](https://reference.aspose.com/pdf/python-net/aspose.pdf/margininfo/) 用于正确定位，并将它们附加到文档的每一页。结果是一个 PDF，所有页面都显示一致的页眉和页脚文本。

以下代码片段演示了如何使用 Python 在 PDF 中添加作为文本片段的页眉和页脚：

1. 为页眉和页脚创建文本片段。
1. 创建 HeaderFooter 对象并将文本片段添加到它们中。
1. 定义边距设置以控制页眉和页脚的放置。
1. 从输入文件加载 PDF 文档。
1. 遍历文档中的所有页面。
1. 为每页分配页眉和页脚。
1. 将修改后的 PDF 保存到输出文件。

```python
import aspose.pdf as ap

def add_header_and_footer_as_text(input_file, output_file):
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

此方法对于在每页的顶部和底部添加统一的标题、页码指示或法律免责声明非常有用。您还可以将其扩展以包括图像或动态内容，例如页码。

## 为页码添加页眉和页脚

使用 Aspose.PDF for Python 为 PDF 文档的页眉和页脚添加自动页码。使用内置变量 $p（当前页码）和 $P（总页数），脚本在每页动态插入页码。页眉显示格式‘Page X from Y’，而页脚显示‘Page X / Y’。该 [`MarginInfo`](https://reference.aspose.com/pdf/python-net/aspose.pdf/margininfo/) 确保在每页上正确放置。

1. 使用“Page $p from $P”在页眉中创建一个 TextFragment，以显示当前页码和总页数。
1. 创建一个 HeaderFooter 对象并将页眉文本添加到其中。
1. 使用“Page $p / $P”创建一个用于页脚的 TextFragment，以实现替代编号样式。
1. 创建一个 Footer 对象并添加页脚文本。
1. 定义边距设置（左 = 50，上 = 20），并将其应用于页眉和页脚。
1. 打开输入文件中的 PDF 文档。
1. 遍历所有页面并为每个页面分配页眉和页脚。
1. 将更新后的 PDF 保存到输出路径。

```python
import aspose.pdf as ap

def using_header_and_footer_for_page_numbering(input_file, output_file):
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

使用 Aspose.PDF for Python 为 PDF 文档的每一页应用 HTML 格式的页眉和页脚。通过使用 [`HtmlFragment`](https://reference.aspose.com/pdf/python-net/aspose.pdf/htmlfragment/)，脚本允许富文本样式——如粗体和斜体——出现在页眉和页脚中。 [`MarginInfo`](https://reference.aspose.com/pdf/python-net/aspose.pdf/margininfo/) 用于正确放置，并且相同的格式化元素附加到文档中的每一页。

以下代码片段演示了如何使用 Python 将页眉和页脚作为 HTML 片段添加到 PDF 中：

1. 使用 HtmlFragment 创建 HTML 标题片段——包括诸如 ' 的样式化文本<strong>' 用于加粗。
1. 创建一个 HeaderFooter 对象并将 HTML 标头添加到它。
1. 创建一个使用 ' 的HTML页脚片段<i>' 用于斜体样式。
1. 创建一个 Footer 对象并将页脚 HTML 添加到其中。
1. 配置页边距（左 = 50，顶部 = 20），并将其分配给页眉和页脚。
1. 使用 'ap.Document()' 加载 PDF 文档。
1. 遍历所有页面并为每个页面分配页眉和页脚。
1. 将修改后的 PDF 保存到指定的输出路径。

```python
import aspose.pdf as ap

def add_header_and_footer_as_html(input_file, output_file):
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

使用 HtmlFragment 可以通过内联样式或 HTML 标记实现丰富的格式化，使您相较于纯文本拥有更大的设计灵活性。

## 将页眉和页脚添加为图像

使用 Aspose.PDF for Python 为 PDF 文档的每一页添加基于图像的页眉和页脚。每页的页眉和页脚均使用相同的图像文件。 [`MarginInfo`](https://reference.aspose.com/pdf/python-net/aspose.pdf/margininfo/) 定位图像，图像会自动调整以适应页眉/页脚区域。

以下代码片段演示了如何使用 Python 向 PDF 添加作为图像的页眉和页脚：

1. 将图像加载到 'ap.Image' 对象中，并准备将其用作标题。
1. 创建一个 HeaderFooter 对象并将页眉图像附加到它上。
1. 再次加载相同的图像以用作页脚。
1. 创建一个 Footer 对象，并将页脚图像添加到它。
1. 使用 'ap.Document()' 加载输入 PDF 文档。
1. 遍历文档的所有页面。
1. 应用边距（左 = 50）以定位页眉和页脚。
1. 为 PDF 的每一页分配页眉和页脚。
1. 将更新后的 PDF 保存到指定的输出文件。

此技术非常适合在页眉/页脚区域使用徽标或水印对文档进行品牌化。

```python
import aspose.pdf as ap

def add_header_and_footer_as_image(input_file, image_file, output_file):
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

## 将标题和页脚添加为表格

使用 Aspose.PDF for Python 为 PDF 文档的所有页面添加结构化、基于表格的页眉和页脚。 [`Table`](https://reference.aspose.com/pdf/python-net/aspose.pdf/table/) 对象提供了更好的布局控制、对齐以及对复杂页眉和页脚的一致格式。页眉文本居中，页脚文本左对齐，均使用 Arial 12pt 字体。列宽根据页面尺寸动态计算，以确保正确放置。

此代码片段使用 Aspose.PDF for Python via .NET 为 PDF 文档的每一页添加页眉和页脚（使用表格）。

1. 使用定义文本样式 [`TextState`](https://reference.aspose.com/pdf/python-net/aspose.pdf/textstate/) 用于页眉和页脚（字体、大小、对齐）。
1. 创建 [`HeaderFooter`](https://reference.aspose.com/pdf/python-net/aspose.pdf/headerfooter/) 用于页眉和页脚的对象。
1. 构建页眉 [`Table`](https://reference.aspose.com/pdf/python-net/aspose.pdf/table/) 带有单行且单元格包含标题文本。
1. 构建页脚 [`Table`](https://reference.aspose.com/pdf/python-net/aspose.pdf/table/) 包含页脚文本的单行单元格。
1. 将表格添加到相应的 [`HeaderFooter`](https://reference.aspose.com/pdf/python-net/aspose.pdf/headerfooter/) 对象。
1. 设置页脚 [`MarginInfo`](https://reference.aspose.com/pdf/python-net/aspose.pdf/margininfo/) 用于正确的水平定位。
1. 打开 [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 使用适当的方法。
1. 遍历所有页面并将基于表格的页眉和页脚分配给每个页面。
1. 保存已修改的 [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 到输出文件。

```python
import aspose.pdf as ap

def add_header_and_footer_as_table(input_file, output_file):
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

## 在 LaTeX 中添加页眉和页脚

使用 Aspose.PDF for Python 为 PDF 文档的所有页面添加包含 LaTeX 格式内容的页眉和页脚。LaTeX 可渲染数学符号、日期、版权标记以及其他高级格式。页眉包括动态日期，而页脚显示版权符号以及当前页码和总页数。

以下代码片段展示了如何使用 [`TeXFragment`](https://reference.aspose.com/pdf/python-net/aspose.pdf/texfragment/) 在 PDF 的页眉和页脚中使用 Aspose.PDF for Python via .NET。

1. 打开 [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 使用适当的方法。
1. 确定用于动态页脚的总页数。
1. 遍历文档的所有页面。
1. 创建一个 [`HeaderFooter`](https://reference.aspose.com/pdf/python-net/aspose.pdf/headerfooter/) 用于页眉的对象。
1. 创建一个 [`TeXFragment`](https://reference.aspose.com/pdf/python-net/aspose.pdf/texfragment/) 对于包含 LaTeX 命令的标题文本（例如， `\\today\\`).
1. 创建一个 [`HeaderFooter`](https://reference.aspose.com/pdf/python-net/aspose.pdf/headerfooter/) 页脚的对象。
1. 创建一个 [`TeXFragment`](https://reference.aspose.com/pdf/python-net/aspose.pdf/texfragment/) 用于包含 LaTeX 符号和页码的页脚文本。
1. 添加 [`TeXFragment`](https://reference.aspose.com/pdf/python-net/aspose.pdf/texfragment/) 到相应的页眉/页脚对象。
1. 将页眉和页脚绑定到当前页面。
1. 保存已修改的 [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 到输出文件。

```python
import aspose.pdf as ap

def add_header_and_footer_as_latex(input_file, output_file):
    # Open PDF document
    with ap.Document(input_file) as document:
        page_count = len(document.pages)
        for i in range(1, page_count + 1):
            # Create header
            header = ap.HeaderFooter()
            h_latex_text = "This is a LaTeX Header. \\today\\"
            h_l_text = ap.TeXFragment(h_latex_text, True)
            # Create footer
            footer = ap.HeaderFooter()
            f_latex_text = (
                f"\\copyright\\ 2025 My Company -- Page \\thepage\\ is {page_count}"
            )
            f_l_text = ap.TeXFragment(f_latex_text, True)

            header.paragraphs.add(h_l_text)
            footer.paragraphs.add(f_l_text)
            # Bind the header and footer to the page
            document.pages[i].header = header
            document.pages[i].footer = footer

        # Save PDF document
        document.save(output_file)
```

## 相关页面主题

- [在 Python 中处理 PDF 页面](/pdf/zh/python-net/working-with-pages/)
- [在 Python 中为 PDF 添加页码](/pdf/zh/python-net/add-page-number/)
- [在 Python 中对 PDF 页面加盖印章](/pdf/zh/python-net/stamping/)
- [在 Python 中格式化 PDF 文档](/pdf/zh/python-net/formatting-pdf-document/)