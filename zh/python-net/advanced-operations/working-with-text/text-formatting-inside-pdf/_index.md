---
title: 使用 Python 在 PDF 中进行文本格式化
linktitle: PDF 中的文本格式化
type: docs
weight: 70
url: /zh/python-net/text-formatting-inside-pdf/
description: 使用 Aspose.PDF 在 Python 中探索 PDF 文件的文本格式化选项，实现自定义文档样式。
lastmod: "2025-11-13"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 如何使用 Python 编辑 PDF 中的文本
Abstract: 本文提供了使用 Aspose.PDF for Python via .NET 对 PDF 文档进行多种文本格式化技术的全面指南。内容涵盖添加行缩进、创建文本边框、下划线文本以及添加删除线等功能。
---

## 行和字符间距

### 使用行间距

#### 如何在 Python 中使用自定义行间距格式化文本 - 简单示例

Aspose.PDF for Python 展示了一种通过行间距调整来控制文本布局和可读性的简便方法。

我们的代码片段展示了如何在 PDF 文档中控制行间距。它从文件读取文本（或使用备用消息），应用自定义字体大小和行间距，并将格式化的文本添加到 PDF 的新页面。

1. 创建一个新的 PDF 文档。
1. 加载源文本。
1. 初始化 TextFragment 对象并将加载的文本分配给它。
1. 为文本设置字体和间距属性。这些值决定文本行的紧凑或宽松程度：
- 字体大小：12 磅
- 行间距：16 磅
1. 将格式化的文本片段插入页面的段落集合中。
1. 保存文档。

```python

import aspose.pdf as ap
from aspose.pdf import Color
from aspose.pdf.drawing import Graph, Line
import os

# Global configuration
DATA_DIR = "your path here"

def specify_line_spacing_simple_case(outfile):
    """
    Specify custom line spacing for text in a PDF document.

    Creates a PDF document with text that has custom line spacing applied.
    Loads text content from an external file and applies 16-point line spacing
    to improve readability and text layout.

    Args:
        outfile (str): The file path where the generated PDF document will be saved.

    Returns:
        None: The function saves the document to the specified output file.

    Note:
        - Attempts to load text from "lorem.txt" file in DATA_DIR
        - Falls back to default message if file doesn't exist
        - Font size: 12 points
        - Line spacing: 16 points (increased from default for better readability)
        - Demonstrates basic line spacing control in PDF text formatting

    Example:
        >>> specify_line_spacing_simple_case("line_spacing.pdf")
        # Creates a PDF with custom 16-point line spacing
    """

    document = ap.Document()
    page = document.pages.add()

    lorem_path = os.path.join(DATA_DIR, "lorem.txt")
    text = (
        open(lorem_path, "r", encoding="utf-8").read()
        if os.path.exists(lorem_path)
        else "Lorem ipsum text not found."
    )

    text_fragment = ap.text.TextFragment(text)
    text_fragment.text_state.font_size = 12
    text_fragment.text_state.line_spacing = 16
    page.paragraphs.add(text_fragment)

    document.save(outfile)
```

#### 如何在 Python 中使用自定义行间距格式化文本 - 特定示例

让我们看看如何在 PDF 文档中使用自定义 TrueType 字体（TTF）应用不同的行间距模式。
它从文件加载文本，嵌入特定字体，并在 PDF 页面上两次渲染相同的文本——每次使用不同的行间距模式：

- FONT_SIZE 模式：行间距等于字体大小。
- FULL_SIZE 模式：行间距考虑字体的完整高度，包括上升部和下降部。

该示例展示了行间距行为如何根据所选模式而变化。

1. 创建一个新的 PDF 文档。
1. 指定自定义字体文件和文本源文件的路径。
1. 加载文本内容。
1. 打开自定义字体。
1. 创建并配置第一个 TextFragment（FONT_SIZE 模式）。将 line_spacing 设置为 'TextFormattingOptions.LineSpacingMode.FONT_SIZE'，表示行间距等于字体大小。
1. 创建并配置第二个 TextFragment（FULL_SIZE 模式）。将 line_spacing 设置为 'TextFormattingOptions.LineSpacingMode.FULL_SIZE'，该模式使用字体的完整高度。
1. 将两个文本片段追加到同一 PDF 页面。
1. 将完成的文档保存到指定的输出位置。

```python

import aspose.pdf as ap
from aspose.pdf import Color
from aspose.pdf.drawing import Graph, Line
import os

# Global configuration
DATA_DIR = "your path here"

def specify_line_spacing_specific_case(outfile):
    """
    Create a PDF document demonstrating different line spacing modes with custom font.
    This function creates a PDF with two text fragments using the same custom TTF font
    but different line spacing modes to demonstrate the visual differences between
    FONT_SIZE and FULL_SIZE line spacing options.
    Args:
        outfile (str): Path where the output PDF file will be saved.
    Notes:
        - Requires 'HPSimplified.ttf' font file in DATA_DIR
        - Requires 'lorem.txt' text file in DATA_DIR for content
        - Falls back to default text if lorem.txt is not found
        - First fragment uses FONT_SIZE line spacing mode
        - Second fragment uses FULL_SIZE line spacing mode
    Dependencies:
        - aspose.pdf (ap) library
        - os module for file path operations
        - DATA_DIR constant must be defined
    """

    document = ap.Document()
    page = document.pages.add()

    font_file = os.path.join(DATA_DIR, "HPSimplified.ttf")
    lorem_path = os.path.join(DATA_DIR, "lorem.txt")
    text = (
        open(lorem_path, "r", encoding="utf-8").read()
        if os.path.exists(lorem_path)
        else "Lorem ipsum text not found."
    )

    with open(font_file, "rb") as font_stream:
        font = ap.text.FontRepository.open_font(font_stream, ap.text.FontTypes.TTF)

        fragment1 = ap.text.TextFragment(text)
        fragment1.text_state.font = font
        fragment1.text_state.formatting_options = ap.text.TextFormattingOptions()
        fragment1.text_state.formatting_options.line_spacing = (
            ap.text.TextFormattingOptions.LineSpacingMode.FONT_SIZE
        )
        page.paragraphs.add(fragment1)

        fragment2 = ap.text.TextFragment(text)
        fragment2.text_state.font = font
        fragment2.text_state.formatting_options = ap.text.TextFormattingOptions()
        fragment2.text_state.formatting_options.line_spacing = (
            ap.text.TextFormattingOptions.LineSpacingMode.FULL_SIZE
        )
        page.paragraphs.add(fragment2)

    document.save(outfile)
```

![PDF 文档显示使用自定义行间距的文本，演示了 16 磅的行间距以提升可读性和文本布局格式化](line_spacing.png)

### 使用字符间距

#### 如何使用 TextFragment 类控制 PDF 文本的字符间距

字符间距决定了行内各字符之间的距离——用于微调文本外观或实现特定的排版效果。

1. 初始化一个新的 Document 对象并添加一个空白页以放置文本。
1. 定义 Fragment Generator。实现辅助函数 make_fragment(spacing)：
- 使用示例文本创建一个 TextFragment。
- 设置字体。
1. 添加具有不同间距值的文本片段。
1. 保存文档。

```python

import aspose.pdf as ap
from aspose.pdf import Color
from aspose.pdf.drawing import Graph, Line
import os

# Global configuration
DATA_DIR = "your path here"

def character_spacing_using_text_fragment(outfile):
    """
    Demonstrate character spacing control using TextFragment objects.

    Creates a PDF document showing different character spacing values applied
    to text fragments. Each line demonstrates progressively increased character
    spacing to illustrate the visual effect on text appearance.

    Args:
        outfile (str): The file path where the generated PDF document will be saved.

    Returns:
        None: The function saves the document to the specified output file.

    Note:
        - Creates multiple TextFragment objects with varying character spacing
        - Character spacing values: 0, 1, 2, 3, and 4 points
        - Font: Times Roman, 12 points
        - Each fragment is positioned on a new line for comparison
        - Character spacing affects only horizontal letter spacing
        - Higher values create more space between individual characters

    Example:
        >>> character_spacing_using_text_fragment("char_spacing_fragment.pdf")
        # Creates a PDF showing progressive character spacing effects
    """
    document = ap.Document()
    page = document.pages.add()

    def make_fragment(spacing):
        fragment = ap.text.TextFragment("Sample Text with character spacing")
        fragment.text_state.font = ap.text.FontRepository.find_font("Arial")
        fragment.text_state.font_size = 14
        fragment.text_state.character_spacing = spacing
        return fragment

    page.paragraphs.add(make_fragment(2.0))
    page.paragraphs.add(make_fragment(1.0))
    page.paragraphs.add(make_fragment(0.75))

    document.save(outfile)
```

![PDF 文档显示三行相同的文本 Sample Text，字符间距从上到下逐渐变紧，第一行字母间距较宽，中间行间距适中，底行间距最紧，展示 PDF 文本格式中不同字符间距值的视觉效果](character_spacing_simple.png)

#### 如何使用 TextParagraph 和 TextBuilder 控制 PDF 文本中的字符间距

Aspose.PDF 允许在使用 TextParagraph 和 TextBuilder 向 PDF 文档添加文本时应用自定义字符间距。
它在页面上定义特定区域，配置文本换行，并渲染一个具有调整后字符间距的文本片段。

在需要对文本位置和布局进行精确控制时（例如构建结构化或多列文本块），使用 TextParagraph 是理想的选择。

1. 创建一个新的 PDF 文档。
1. 为页面初始化一个 TextBuilder 实例。
1. 创建并配置一个 TextParagraph。
- 将换行模式设置为 'TextFormattingOptions.WordWrapMode.BY_WORDS'。
1. 创建一个带有自定义字符间距的 TextFragment。
- 创建一个新的 TextFragment 并设置其文本（例如 "Sample Text with character spacing"）。
- 指定字体属性，例如 Arial 和 14 磅字号。
- 应用字符间距 = 2.0，这会增加字符之间的间距。
1. 将 TextFragment 添加到 TextParagraph 中。
1. 将 TextParagraph 添加到页面。
1. 保存 PDF 文档。

```python

import aspose.pdf as ap
from aspose.pdf import Color
from aspose.pdf.drawing import Graph, Line
import os

# Global configuration
DATA_DIR = "your path here"

def character_spacing_using_text_paragraph(outfile):
    """
    Demonstrate character spacing control using TextParagraph objects.

    Creates a PDF document with text paragraph that has custom character spacing
    applied. Shows how to set character spacing at the paragraph level and
    demonstrates the visual effect on text layout.

    Args:
        outfile (str): The file path where the generated PDF document will be saved.

    Returns:
        None: The function saves the document to the specified output file.

    Note:
        - Uses TextParagraph for paragraph-level formatting
        - Character spacing: 2.0 points
        - Font: Times Roman, 12 points
        - Demonstrates paragraph-based character spacing control
        - Character spacing applies to all text within the paragraph
        - Alternative approach to fragment-based character spacing

    Example:
        >>> character_spacing_using_text_paragraph("char_spacing_paragraph.pdf")
        # Creates a PDF with paragraph-level character spacing
    """
    document = ap.Document()
    page = document.pages.add()

    builder = ap.text.TextBuilder(page)
    paragraph = ap.text.TextParagraph()
    paragraph.rectangle = ap.Rectangle(100, 700, 500, 750, True)
    paragraph.formatting_options.wrap_mode = (
        ap.text.TextFormattingOptions.WordWrapMode.BY_WORDS
    )

    fragment = ap.text.TextFragment("Sample Text with character spacing")
    fragment.text_state.font = ap.text.FontRepository.find_font("Arial")
    fragment.text_state.font_size = 14
    fragment.text_state.character_spacing = 2.0

    paragraph.append_line(fragment)
    builder.append_paragraph(paragraph)
    document.save(outfile)
```

## 创建列表

在处理 PDF 文件时，您可能需要显示结构化信息，如列表——无论是项目符号列表、编号列表，还是使用 HTML 或 LaTeX 格式化的列表。
Aspose.PDF for Python via .NET 提供多种灵活的方式，在 PDF 文档中直接创建和格式化列表，让您全面控制布局、字体和样式。

本文演示了在 PDF 中创建列表的多种方法，从纯文本格式到高级的 HTML 与 LaTeX 渲染。每种方法都有其特定的使用场景——无论您偏好精确的编程控制还是便捷的基于标记的样式。

阅读本文后，您将了解如何：

- 使用 TextParagraph 和 TextBuilder 创建自定义项目符号和编号列表。

- 使用 HTML 片段 (HtmlFragment) 在 PDF 中轻松渲染 '<ul>' 和 '<ol>' 列表。

- 利用 LaTeX 片段 (TeXFragment) 进行数学或科学列表的格式化。

- 控制页面内的文本换行、字体样式和布局定位。

- 了解手动列表构建与基于标记的方法之间的区别。

### 创建项目符号列表

使用 TextParagraph 和 TextBuilder 在 PDF 中创建自定义项目符号列表，无需依赖 HTML 或 LaTeX 格式。
每个列表项前缀为项目符号字符 (•)，并作为单独的 TextFragment 添加。

1. 初始化 Document 对象并添加空白页。
1. 定义一个 Python 字符串列表，以转换为项目符号。
1. 创建 TextBuilder 和 TextParagraph。
1. 使用 'TextBuilder' 将配置好的段落添加到页面。
1. 保存 PDF 文档。

```python

import aspose.pdf as ap
from aspose.pdf import Color
from aspose.pdf.drawing import Graph, Line
import os

# Global configuration
DATA_DIR = "your path here"

def create_bullet_list(outfile):
    """
    Create a PDF document with a bullet list using plain text formatting.
    This function generates a PDF document containing a bullet list with predefined items.
    The list is formatted with bullet points, uses Times New Roman font, and includes
    text wrapping behavior for longer items.
    Args:
        outfile (str): The file path where the PDF document will be saved.
    Returns:
        None: The function saves the document to the specified file path.
    Note:
        The bullet list is positioned within a rectangle at coordinates (80, 200, 400, 800)
        and uses word wrapping mode for text formatting.
    """

    document = ap.Document()
    page = document.pages.add()
    items = [
        "First item in the list",
        "Second item with more text to demonstrate wrapping behavior.",
        "Third item",
        "Fourth item",
    ]

    builder = ap.text.TextBuilder(page)
    paragraph = ap.text.TextParagraph()
    paragraph.rectangle = ap.Rectangle(80, 200, 400, 800, True)
    paragraph.formatting_options.wrap_mode = (
        ap.text.TextFormattingOptions.WordWrapMode.BY_WORDS
    )

    for item in items:
        fragment = ap.text.TextFragment("• " + item)
        fragment.text_state.font = ap.text.FontRepository.find_font("Times New Roman")
        fragment.text_state.font_size = 12
        paragraph.append_line(fragment)

    builder.append_paragraph(paragraph)
    document.save(outfile)
```

### 创建编号列表

使用 TextParagraph 和 TextBuilder 在 PDF 中创建自定义编号（有序）列表，无需依赖 HTML 或 LaTeX 格式。
每个列表项前缀为其编号（例如 1., 2.），并作为单独的 TextFragment 添加。

1. 初始化 Document 对象并添加空白页。
1. 定义一个 Python 字符串列表，以转换为编号列表项。
1. 创建 TextBuilder 和 TextParagraph。
1. 将每个项目作为带编号的 TextFragment 添加。
1. 使用 TextBuilder 将配置好的段落添加到页面。
1. 保存 PDF 文档。

```python

import aspose.pdf as ap
from aspose.pdf import Color
from aspose.pdf.drawing import Graph, Line
import os

# Global configuration
DATA_DIR = "your path here"

def create_numbered_list(outfile):
    """
    Create a numbered list in a PDF document using plain text formatting.
    This function generates a PDF document containing a numbered list with predefined
    items. The list is formatted with Times New Roman font and includes text wrapping
    by words within a specified rectangular area on the page.
    Args:
        outfile (str): The file path where the generated PDF document will be saved.
    Returns:
        None: The function saves the document to the specified file path but does
              not return any value.
    Note:
        - Uses Aspose.PDF library (imported as 'ap')
        - List items are hardcoded within the function
        - Font: Times New Roman, size 12
        - Text wrapping: BY_WORDS mode
        - Rectangle bounds: (80, 200, 400, 800)
    """

    document = ap.Document()
    page = document.pages.add()
    items = [
        "First item in the list",
        "Second item with more text to demonstrate wrapping behavior.",
        "Third item",
        "Fourth item",
    ]

    builder = ap.text.TextBuilder(page)
    paragraph = ap.text.TextParagraph()
    paragraph.rectangle = ap.Rectangle(80, 200, 400, 800, True)
    paragraph.formatting_options.wrap_mode = (
        ap.text.TextFormattingOptions.WordWrapMode.BY_WORDS
    )

    for i, item in enumerate(items):
        fragment = ap.text.TextFragment(f"{i + 1}. {item}")
        fragment.text_state.font = ap.text.FontRepository.find_font("Times New Roman")
        fragment.text_state.font_size = 12
        paragraph.append_line(fragment)

    builder.append_paragraph(paragraph)
    document.save(outfile)
```

### 创建项目符号列表的 HTML 版本

我们的库展示了如何使用 HTML 片段在 PDF 文档中创建项目符号（无序）列表。它将 Python 字符串列表转换为 HTML `<ul>` 元素，并将其作为 HtmlFragment 插入 PDF 页面。使用 HTML 片段可让您直接在 PDF 中利用 HTML 格式化功能（如列表、粗体、斜体）。

1. 创建一个新的 PDF 文档并添加页面。
1. 准备列表项。
1. 将列表转换为 HTML 无序列表。
- 使用 `<ul>` 标签创建无序（项目符号）列表。
- 使用列表推导式将每个项目用 'li' 标签包裹。
1. 创建一个 HtmlFragment。将 HTML 字符串转换为可以添加到 PDF 页面中的 HtmlFragment 对象。
1. 将 HtmlFragment 插入页面的段落集合中。
1. 保存 PDF 文档。

```python

import aspose.pdf as ap
from aspose.pdf import Color
from aspose.pdf.drawing import Graph, Line
import os

# Global configuration
DATA_DIR = "your path here"

def create_bullet_list_html_version(outfile):
    """
    Create a bulleted list using HTML formatting in a PDF document.

    Generates a PDF with an unordered (bulleted) list created using HTML markup.
    Demonstrates how to use HtmlFragment to embed HTML list structures directly
    into PDF documents with proper formatting and styling.

    Args:
        outfile (str): The file path where the generated PDF document will be saved.

    Returns:
        None: The function saves the document to the specified output file.

    Note:
        - Uses HTML <ul> and <li> tags for list structure
        - Items are predefined with sample content
        - HtmlFragment automatically handles HTML rendering
        - Lists maintain proper bullet formatting and indentation
        - Simpler alternative to manual list creation with TextFragments
        - Supports nested lists and HTML styling if needed

    Example:
        >>> create_bullet_list_html_version("bullet_list_html.pdf")
        # Creates a PDF with HTML-formatted bulleted list
    """

    document = ap.Document()
    page = document.pages.add()
    items = [
        "First item in the list",
        "Second item with more text to demonstrate wrapping behavior.",
        "Third item",
        "Fourth item",
    ]
    html_list = "<ul>" + "".join([f"<li>{item}</li>" for item in items]) + "</ul>"
    html_fragment = ap.HtmlFragment(html_list)
    page.paragraphs.add(html_fragment)
    document.save(outfile)
```

![PDF 文档中显示的项目符号列表，包含四个项目：列表中的第一项，第二项包含更多文本以演示换行行为，第三项，以及第四项。每个项目都以标准项目符号开头，展示了在 PDF 结构中使用 HTML 格式的列表渲染，具有正确的缩进和间距](bullet_list_html.png)

### 创建编号列表的 HTML 版本

使用 HTML 片段在 PDF 文档中创建有序（编号）列表。它将 Python 字符串列表转换为 HTML `<ol>` 元素，并将其作为 HtmlFragment 插入 PDF 页面。

使用 HTML 片段可以直接在 PDF 中加入基于 HTML 的格式化功能，如编号列表、粗体、斜体等。

1. 创建一个新的 PDF 文档并添加页面。
1. 准备列表项。
1. 将列表转换为 HTML 有序列表。
- 使用 `<ol>` 标签创建编号列表。
- 使用列表推导式将每个项目包裹在 'li' 标签中。
1. 将 HTML 字符串转换为可以添加到 PDF 页面中的 HtmlFragment 对象。
1. 将 HtmlFragment 插入页面的段落集合中。
1. 保存 PDF 文档。

```python

import aspose.pdf as ap
from aspose.pdf import Color
from aspose.pdf.drawing import Graph, Line
import os

# Global configuration
DATA_DIR = "your path here"

def create_numbered_list_html_version(outfile):
    """
    Create a numbered list using HTML formatting in a PDF document.

    Generates a PDF with an ordered (numbered) list created using HTML markup.
    Demonstrates how to use HtmlFragment to embed HTML ordered list structures
    directly into PDF documents with automatic numbering and formatting.

    Args:
        outfile (str): The file path where the generated PDF document will be saved.

    Returns:
        None: The function saves the document to the specified output file.

    Note:
        - Uses HTML <ol> and <li> tags for ordered list structure
        - Items are predefined with sample content
        - HtmlFragment automatically handles HTML rendering and numbering
        - Lists maintain proper numeric formatting and indentation
        - Numbers are automatically generated (1, 2, 3, etc.)
        - Supports nested lists and custom numbering styles if needed

    Example:
        >>> create_numbered_list_html_version("numbered_list_html.pdf")
        # Creates a PDF with HTML-formatted numbered list
    """

    document = ap.Document()
    page = document.pages.add()
    items = [
        "First item in the list",
        "Second item with more text to demonstrate wrapping behavior.",
        "Third item",
        "Fourth item",
    ]
    html_list = "<ol>" + "".join([f"<li>{item}</li>" for item in items]) + "</ol>"
    html_fragment = ap.HtmlFragment(html_list)
    page.paragraphs.add(html_fragment)
    document.save(outfile)
```

![PDF 文档中显示的编号列表，包含四个自动编号的项目：1. 列表中的第一项，2. 第二项包含更多文本以演示换行行为，3. 第三项，和 4. 第四项。该列表展示了在 PDF 结构中使用 HTML 格式的有序列表渲染，具有正确的数字顺序、缩进以及项目之间的间距](numbered_list_html.png)

### 创建项目符号列表的 LaTeX 版本

使用 LaTeX 片段（TeXFragment）在 PDF 中创建无序（项目符号）列表。它将 Python 字符串列表转换为 LaTeX 的 itemize 环境并插入 PDF 页面。当您需要渲染数学公式、符号或具备精确格式的结构化列表时，使用 LaTeX 片段是理想的选择。

1. 创建一个新的 PDF 文档并添加页面。
1. 定义一个 Python 字符串列表，这些字符串将在 LaTeX 的 itemize 环境中成为项目符号。
1. 将列表转换为 LaTeX 的 itemize 环境：
- 使用 \begin{itemize} 和 \end{itemize} 包裹项目。
- 使用列表推导式在每个项目前加上 \item 前缀。
1. 将 LaTeX 字符串转换为可在 PDF 中渲染的 TeXFragment 对象。
1. 将 LaTeX 片段添加到页面。
1. 保存 PDF 文档。

```python

import aspose.pdf as ap
from aspose.pdf import Color
from aspose.pdf.drawing import Graph, Line
import os

# Global configuration
DATA_DIR = "your path here"

def create_bullet_list_latex_version(outfile):
    """
    Create a bulleted list using LaTeX formatting in a PDF document.

    Generates a PDF with an unordered list created using LaTeX markup.
    Demonstrates how to use TeXFragment to embed LaTeX itemize environments
    directly into PDF documents with proper mathematical and scientific formatting.

    Args:
        outfile (str): The file path where the generated PDF document will be saved.

    Returns:
        None: The function saves the document to the specified output file.

    Note:
        - Uses LaTeX \\begin{itemize} and \\item commands
        - TeXFragment handles LaTeX compilation and rendering
        - Supports mathematical expressions and scientific notation
        - Lists maintain proper bullet formatting and indentation
        - More powerful than HTML for mathematical content
        - Can include LaTeX math modes and special symbols

    Example:
        >>> create_bullet_list_latex_version("bullet_list_latex.pdf")
        # Creates a PDF with LaTeX-formatted bulleted list
    """

    document = ap.Document()
    page = document.pages.add()
    items = [
        "First item",
        "Second item with more text to demonstrate wrapping behavior.",
        "Third item",
        "Fourth item",
    ]
    tex_list = (
        "Lists are easy to create: \\begin{itemize}"
        + "".join([f"\\item {i}" for i in items])
        + "\\end{itemize}"
    )
    tex_fragment = ap.TeXFragment(tex_list)
    page.paragraphs.add(tex_fragment)
    document.save(outfile)
```

![PDF 中显示的项目符号列表，展示了 LaTeX 渲染的格式，文本为 “Lists are easy to create:” 后面跟随四个项目符号项：第一项，第二项包含更多文本以演示换行行为，第三项，以及第四项。该列表展示了专业的 LaTeX 排版，具有正确的项目符号格式、统一的间距以及在整洁的 PDF 文档布局中的文本换行能力](bullet_list_latex.png)

### 创建编号列表的 LaTeX 版本

使用 LaTeX 片段（TeXFragment）在 PDF 中创建有序（编号）列表。它将 Python 字符串列表转换为 LaTeX 的 enumerate 环境并插入 PDF 页面。当您需要精确的格式、结构化列表或数学符号在 PDF 中呈现时，使用 LaTeX 片段是理想的选择。

1. 创建一个新的 PDF 文档并添加页面。
1. 定义一个 Python 字符串列表，这些字符串将在 LaTeX 的 enumerate 环境中成为编号项。
1. 将列表转换为 LaTeX 的 enumerate 环境。
1. 将 LaTeX 字符串转换为可在 PDF 中渲染的 TeXFragment 对象。
1. 将 LaTeX 片段添加到页面。
1. 保存 PDF 文档。

```python

import aspose.pdf as ap
from aspose.pdf import Color
from aspose.pdf.drawing import Graph, Line
import os

# Global configuration
DATA_DIR = "your path here"

def create_numbered_list_latex_version(outfile):
    """Create a numbered list using LaTeX."""

    document = ap.Document()
    page = document.pages.add()
    items = [
        "First item",
        "Second item with more text to demonstrate wrapping behavior.",
        "Third item",
        "Fourth item",
    ]
    tex_list = (
        "Lists are easy to create: \\begin{enumerate}"
        + "".join([f"\\item {i}" for i in items])
        + "\\end{enumerate}"
    )
    tex_fragment = ap.TeXFragment(tex_list)
    page.paragraphs.add(tex_fragment)
    document.save(outfile)
```

![PDF 中显示的编号列表，展示了 LaTeX 渲染的格式，项目包括 1. 第一项，2. 第二项包含更多文本以演示换行行为，3. 第三项，和 4. 第四项，前面的文本为 “Lists are easy to create”](numbered_list_latex.png)

## 脚注和尾注

### 添加脚注

脚注用于在文档正文中通过在相关文本旁放置连续的上标数字来引用注释。这些数字对应于详细的注释，通常缩进并位于同页底部，提供额外的上下文、引用或评论。

使用 Aspose.PDF for Python via .NET 在 PDF 文档的文本片段中添加脚注。脚注可用于提供补充信息、引用或说明，而不会使主体内容显得杂乱。此方法确保脚注在视觉和结构上都集成到 PDF 布局中。

1. 创建新文档。
1. 使用主要内容创建 TextFragment。
1. 添加内联文本。创建另一个在同一段落中继续的 TextFragment。
1. 保存文档。

```python

import aspose.pdf as ap
from aspose.pdf import Color
from aspose.pdf.drawing import Graph, Line
import os

# Global configuration
DATA_DIR = "your path here"

def add_footnote(outfile):
    """Add footnote to a PDF document."""

    document = ap.Document()
    page = document.pages.add()

    text_fragment = ap.text.TextFragment("This is a sample text with a footnote.")
    text_fragment.text_state.font = ap.text.FontRepository.find_font("Arial")
    text_fragment.text_state.font_size = 14
    text_fragment.foot_note = ap.Note("This is the footnote content.")
    page.paragraphs.add(text_fragment)

    inline_text = ap.text.TextFragment(
        " This is another text after footnote in the same paragraph."
    )
    inline_text.is_in_line_paragraph = True
    inline_text.text_state.font = ap.text.FontRepository.find_font("Arial")
    inline_text.text_state.font_size = 14
    page.paragraphs.add(inline_text)

    document.save(outfile)
```

### 在 PDF 中添加自定义样式的脚注

1. 初始化一个新的 PDF 文档并添加空白页。
1. 创建主文本片段。
1. 创建并设置脚注样式（字体、大小、颜色、样式）。
1. 将带有脚注的已样式化文本片段插入页面。
1. 再添加一个没有脚注的文本片段。
1. 保存文档。

```python

import aspose.pdf as ap
from aspose.pdf import Color
from aspose.pdf.drawing import Graph, Line
import os

# Global configuration
DATA_DIR = "your path here"

def add_footnote_custom_text_style(outfile):
    """Add footnote with custom text style."""

    document = ap.Document()
    page = document.pages.add()

    text_fragment = ap.text.TextFragment("This is a sample text with a footnote.")
    text_fragment.text_state.font = ap.text.FontRepository.find_font("Arial")
    text_fragment.text_state.font_size = 14

    note = ap.Note("This is the footnote content with custom text style.")
    note.text_state = ap.text.TextState()
    note.text_state.font = ap.text.FontRepository.find_font("Times New Roman")
    note.text_state.font_size = 10
    note.text_state.foreground_color = ap.Color.red
    note.text_state.font_style = ap.text.FontStyles.ITALIC
    text_fragment.foot_note = note

    page.paragraphs.add(text_fragment)

    another_text = ap.text.TextFragment(" This is another text without footnote.")
    another_text.text_state.font = ap.text.FontRepository.find_font("Arial")
    another_text.text_state.font_size = 14
    page.paragraphs.add(another_text)

    document.save(outfile)
```

### 在 PDF 中添加自定义符号的脚注

使用 Aspose.PDF for Python via .NET 在 PDF 文档中向文本片段添加脚注，并能够自定义脚注标记符号。

1. 创建 PDF 文档和页面。
1. 添加第一个带自定义脚注符号的文本片段。
1. 添加另一个继续段落且没有脚注的文本片段。
1. 添加第二个带默认脚注的文本片段。
1. 保存文档。

```python

import aspose.pdf as ap
from aspose.pdf import Color
from aspose.pdf.drawing import Graph, Line
import os

# Global configuration
DATA_DIR = "your path here"

def add_footnote_custom_text(outfile):
    """
    Add footnote with custom text marker to a PDF document.
    Creates a PDF document with text fragments that include footnotes with custom
    styling. The function demonstrates how to add footnotes with custom text markers
    and standard footnotes to different text fragments within the same document.
    Args:
        outfile (str): The output file path where the PDF document will be saved.
    Returns:
        None: The function saves the document to the specified output file.
    Example:
        add_footnote_custom_text("output_with_footnotes.pdf")
    Note:
        The document will contain:
        - Text with a custom footnote marker ("*")
        - Text without footnotes
        - Text with a standard footnote
    """

    document = ap.Document()
    page = document.pages.add()

    text_fragment = ap.text.TextFragment("This is a sample text with a footnote.")
    text_fragment.text_state.font = ap.text.FontRepository.find_font("Arial")
    text_fragment.text_state.font_size = 14

    note = ap.Note("This is the footnote content with custom text style.")
    note.text = "*"
    text_fragment.foot_note = note
    page.paragraphs.add(text_fragment)

    another_text = ap.text.TextFragment(" This is another text without footnote.")
    another_text.text_state.font = ap.text.FontRepository.find_font("Arial")
    another_text.text_state.font_size = 14
    page.paragraphs.add(another_text)

    text_fragment = ap.text.TextFragment("This is a sample text with a footnote.")
    text_fragment.text_state.font = ap.text.FontRepository.find_font("Arial")
    text_fragment.text_state.font_size = 14
    text_fragment.foot_note = ap.Note("This is the footnote content.")
    page.paragraphs.add(text_fragment)

    document.save(outfile)
```

### 在 PDF 中添加自定义线条样式的脚注

使用 Python 库自定义 PDF 文档中脚注线的视觉外观。自定义脚注线可提升视觉清晰度，并在报告、学术论文和带注释的出版物等文档中实现样式一致性。

1. 创建一个新的 PDF 文档并添加页面。
1. 为脚注连接线定义自定义线条样式（颜色、宽度和虚线模式）。
1. 添加多个带脚注的文本片段。
1. 保存最终文档。

```python

import aspose.pdf as ap
from aspose.pdf import Color
from aspose.pdf.drawing import Graph, Line
import os

# Global configuration
DATA_DIR = "your path here"

def add_footnote_with_custom_line_style(outfile):
    """
    Add footnotes with custom line style to a PDF document.
    Creates a PDF document with text fragments that have footnotes and applies
    a custom line style for the footnote separator line. The custom style includes
    red color, increased line width, and dashed pattern.
    Args:
        outfile (str): Path where the generated PDF document will be saved.
    Returns:
        None: The function saves the document to the specified output file.
    Example:
        >>> add_footnote_with_custom_line_style("output.pdf")
        # Creates a PDF with footnoted text and custom separator line styling
    """

    document = ap.Document()
    page = document.pages.add()

    # Define custom line style
    graph_info = ap.GraphInfo()
    graph_info.line_width = 2
    graph_info.color = ap.Color.red
    graph_info.dash_array = [3]
    graph_info.dash_phase = 1
    page.note_line_style = graph_info

    # First text fragment with footnote
    text1 = ap.text.TextFragment("This is a sample text with a footnote.")
    text1.foot_note = ap.Note("foot note for text 1")
    page.paragraphs.add(text1)

    # Second text fragment with footnote
    text2 = ap.text.TextFragment("This is yet another sample text with a footnote.")
    text2.foot_note = ap.Note("foot note for text 2")
    page.paragraphs.add(text2)

    document.save(outfile)
```

### 在 PDF 中添加带图片和表格的脚注

如何使用 Aspose.PDF for Python via .NET 在 PDF 文档中通过嵌入图片、样式化文本和表格来丰富脚注？

1. 创建一个新的 PDF 文档并添加页面。
1. 添加一个带附加脚注的文本片段。
1. 在脚注中嵌入图片、样式化文本和表格。
1. 保存文档。

```python

import aspose.pdf as ap
from aspose.pdf import Color
from aspose.pdf.drawing import Graph, Line
import os

# Global configuration
DATA_DIR = "your path here"

def add_footnote_with_image_and_table(outfile):
    """
    Add a footnote containing an image and table to a PDF document.
    Creates a new PDF document with sample text that includes a footnote. The footnote
    contains three elements: an image (logo.jpg), descriptive text, and a simple table
    with two cells. The image is resized to 20x20 pixels and the footnote text uses
    a 20pt font size.
    Args:
        outfile (str): The file path where the generated PDF document will be saved.
    Returns:
        None: The function saves the document to the specified output file.
    Note:
        - Requires the logo.jpg file to be present in the DATA_DIR directory
        - Uses the Aspose.PDF library (imported as 'ap')
        - The footnote is attached to the main text fragment on the page
    """

    document = ap.Document()
    page = document.pages.add()

    text = ap.text.TextFragment("This is a sample text with a footnote.")
    page.paragraphs.add(text)

    note = ap.Note()

    # Add image
    image_note = ap.Image()
    image_note.file = os.path.join(DATA_DIR, "logo.jpg")
    image_note.fix_height = 20
    image_note.fix_width = 20
    note.paragraphs.add(image_note)

    # Add text
    text_note = ap.text.TextFragment("This is the footnote content.")
    text_note.text_state.font_size = 20
    text_note.is_in_line_paragraph = True
    note.paragraphs.add(text_note)

    # Add table
    table = ap.Table()
    table.rows.add().cells.add("Cell 1,1")
    table.rows.add().cells.add("Cell 1,2")
    note.paragraphs.add(table)

    text.foot_note = note

    document.save(outfile)
```

### 向 PDF 文档添加尾注

尾注是一种引用类型，引导读者前往文档末尾的指定章节，在那里可以找到引用、改写的想法或概要内容的完整参考。当使用尾注时，引用材料后面会立即放置一个上标数字，引导读者到文稿末尾对应的注释。

此代码片段演示了如何在 PDF 文档中的文本片段添加尾注。与出现在引用文本附近的脚注不同，尾注通常放置在文档或章节的末尾。此方法还模拟了更长的文档，以展示尾注在扩展内容中的表现。

1. 创建 PDF 文档和页面。
1. 添加带尾注的文本片段。
1. 加载外部文本内容。
1. 模拟长文档。多次添加已加载的文本以模拟更长的文档。
1. 保存文档。

```python

import aspose.pdf as ap
from aspose.pdf import Color
from aspose.pdf.drawing import Graph, Line
import os

# Global configuration
DATA_DIR = "your path here"

def add_endnote(outfile):
    """Add endnote to a PDF document.
    Creates a new PDF document with a text fragment containing an endnote,
    followed by additional lorem ipsum content to simulate a longer document.
    The endnote is attached to the first text fragment and will be displayed
    according to the PDF viewer's endnote handling.
    Args:
        outfile (str): The file path where the generated PDF document will be saved.
    Returns:
        None: The function saves the document to the specified output file path.
    Note:
        This function requires the aspose-pdf library and assumes the existence
        of a DATA_DIR variable pointing to a directory containing 'lorem.txt'.
        If the lorem.txt file is not found, fallback text will be used.
    """

    document = ap.Document()
    page = document.pages.add()

    text_fragment = ap.text.TextFragment("This is a sample text with an endnote.")
    text_fragment.text_state.font = ap.text.FontRepository.find_font("Arial")
    text_fragment.text_state.font_size = 14
    text_fragment.end_note = ap.Note("This is the EndNote content.")
    page.paragraphs.add(text_fragment)

    lorem_path = os.path.join(DATA_DIR, "lorem.txt")
    text_content = (
        open(lorem_path, encoding="utf-8").read()
        if os.path.exists(lorem_path)
        else "Lorem ipsum sample text not found."
    )

    # Simulate long text
    for _ in range(5):
        tf = ap.text.TextFragment(text_content)
        tf.text_state.font = ap.text.FontRepository.find_font("Arial")
        tf.text_state.font_size = 14
        page.paragraphs.add(tf)

    document.save(outfile)
```

### 在 PDF 中添加带自定义标记文本的尾注

在 PDF 文档的文本片段中添加尾注，并使用自定义标记符号（例如 "***"）。尾注通常放置在文档或章节的末尾，可用于提供额外的上下文、引用或评论。

1. 创建 PDF 文档和页面。
1. 添加带尾注的样式化文本片段。
1. 自定义尾注标记文本。
1. 从 .txt 文件加载外部内容。
1. 模拟长篇内容以说明尾注位置。
1. 保存 PDF 文档。

```python

import aspose.pdf as ap
from aspose.pdf import Color
from aspose.pdf.drawing import Graph, Line
import os

# Global configuration
DATA_DIR = "your path here"

def add_endnote_custom_text(outfile):
    """
    Add endnote with custom text marker to a PDF document.
    Creates a PDF document with a text fragment that contains an endnote with
    a custom marker ("***"). The document is populated with sample text content
    from a lorem.txt file, repeated multiple times to simulate a longer document.
    Args:
        outfile (str): Path where the generated PDF document will be saved.
    Returns:
        None: The function saves the document to the specified output file path.
    Note:
        - Requires lorem.txt file in DATA_DIR for sample content
        - Falls back to default text if lorem.txt is not found
        - Uses Arial font with 14pt size for all text elements
        - The endnote marker is set to "***" instead of default numbering
    """

    document = ap.Document()
    page = document.pages.add()

    text_fragment = ap.text.TextFragment("This is a sample text with an endnote.")
    text_fragment.text_state.font = ap.text.FontRepository.find_font("Arial")
    text_fragment.text_state.font_size = 14
    text_fragment.end_note = ap.Note("This is the EndNote content.")
    text_fragment.end_note.text = "***"
    page.paragraphs.add(text_fragment)

    lorem_path = os.path.join(DATA_DIR, "lorem.txt")
    text_content = (
        open(lorem_path, encoding="utf-8").read()
        if os.path.exists(lorem_path)
        else "Lorem ipsum sample text not found."
    )

    # Simulate long text
    for _ in range(5):
        tf = ap.text.TextFragment(text_content)
        tf.text_state.font = ap.text.FontRepository.find_font("Arial")
        tf.text_state.font_size = 14
        page.paragraphs.add(tf)

    document.save(outfile)
```

## 布局与页面控制

### 强制表格在 PDF 中新页开始

使用 Aspose.PDF for Python via .NET 将特定内容添加到 PDF 文档中，使其在新页面开始。
通过设置属性 'is_in_new_page'，您可以精确控制页面布局和结构，确保特定部分（如表格、报告或摘要）始终在新页面开始——这对于文档格式化、打印准备报告或有序输出生成非常理想。

1. 创建并配置表格。
1. 向表格添加数据。
1. 为表格强制新页面。这可确保表格在新页面顶部开始，即使当前页面已有内容。
1. 将表格添加到页面。使用 'page.paragraphs.add()' 将表格包含在 PDF 布局中。
1. 保存文档。

```python

import aspose.pdf as ap
from aspose.pdf import Color
from aspose.pdf.drawing import Graph, Line
import os

# Global configuration
DATA_DIR = "your path here"

def force_new_page(output_file_name):
    """
    Create a PDF document demonstrating forced page breaks with tables.

    Creates a PDF document with a table that is forced to start on a new page
    using the is_in_new_page property. This is useful for controlling page layout
    and ensuring specific content starts on fresh pages.

    Args:
        output_file_name (str): The file path where the generated PDF document will be saved.

    Returns:
        None: The function saves the document to the specified output file.

    Note:
        - Creates a 3-column table with 5 rows of sample data
        - Table uses uniform column widths of 150 units each
        - All cells have borders for clear visual separation
        - is_in_new_page=True forces the table to start on a new page
        - Useful for reports, documents with sections, or content organization

    Example:
        >>> force_new_page("new_page_table.pdf")
        # Creates a PDF with a table that starts on a new page
    """
    # Create new PDF document
    document = ap.Document()
    page = document.pages.add()

    # Create a table
    table = ap.Table()
    table.column_widths = "150 150 150"
    table.default_cell_border = ap.BorderInfo(ap.BorderSide.ALL)

    # Add rows with sample data
    for i in range(5):
        row = table.rows.add()
        row.cells.add(f"Row {i + 1} - Col 1")
        row.cells.add(f"Row {i + 1} - Col 2")
        row.cells.add(f"Row {i + 1} - Col 3")

    # --- Key part: force table to start on a new PDF page ---
    table.is_in_new_page = True

    # Add table to page
    page.paragraphs.add(table)

    # Save the PDF
    document.save(output_file_name)
```

### 在 PDF 中使用 Inline Paragraph 属性

我们的库允许您使用 'is_in_line_paragraph' 属性来控制 PDF 中文本和图像之间的行内流动。
通常情况下，当您添加新元素（如文本片段或图像）时，每个元素都会在新行或新段落开始。
通过设置 'is_in_line_paragraph = True'，您可以让元素出现在同一行或同一段落中，创建流畅的行内布局——非常适合在句子中内嵌文字和图像，例如添加徽标、图标或符号。

第一个文本片段、图像和第二个文本片段出现在同一行，形成连续的行内段落。
第三个文本片段开始一个新段落，演示默认的换行行为。

1. 创建一个新的 PDF 文档。
1. 添加第一个文本片段。
1. 插入内联图像。
1. 添加更多内联文本。
1. 添加一个新段落。
1. 保存 PDF。

```python

import aspose.pdf as ap
from aspose.pdf import Color
from aspose.pdf.drawing import Graph, Line
import os

# Global configuration
DATA_DIR = "your path here"

def using_inline_paragraph_property(output_file_name):
    """
    Demonstrate inline paragraph behavior in PDF document layout.

    Creates a PDF document showing how the is_in_line_paragraph property affects
    the flow of text and images. Elements with this property continue the flow
    of the previous paragraph instead of starting a new one.

    Args:
        output_file_name (str): The file path where the generated PDF document will be saved.

    Returns:
        None: The function saves the document to the specified output file.

    Note:
        - First text fragment starts a new paragraph
        - Image with is_in_line_paragraph=True continues the same line
        - Second text fragment also continues the same paragraph line
        - Third text fragment starts a new paragraph (default behavior)
        - Demonstrates inline flow control for mixed content (text + images)
        - Image is resized to 30x30 pixels and flows inline with text

    Example:
        >>> using_inline_paragraph_property("inline_paragraph.pdf")
        # Creates a PDF demonstrating inline paragraph flow
    """
    # Create a PDF document
    document = ap.Document()
    page = document.pages.add()

    # --- First text fragment (normal paragraph) ---
    fragment1 = ap.text.TextFragment("This is the first part of the paragraph. ")
    fragment1.text_state.font = ap.text.FontRepository.find_font("Arial")
    fragment1.text_state.font_size = 14
    page.paragraphs.add(fragment1)

    # --- Inline image (continues same paragraph flow) ---
    image = ap.Image()
    image.is_in_line_paragraph = True  # Makes image inline with previous paragraph
    image.file = os.path.join(DATA_DIR, "logo.jpg")
    image.fix_height = 30
    image.fix_width = 30
    page.paragraphs.add(image)

    # --- Second inline text fragment (keeps same paragraph flow) ---
    fragment2 = ap.text.TextFragment("This is the second part of the same paragraph.")
    fragment2.is_in_line_paragraph = True
    fragment2.text_state.font = ap.text.FontRepository.find_font("Arial")
    fragment2.text_state.font_size = 14
    page.paragraphs.add(fragment2)

    # --- Third fragment (starts new paragraph automatically) ---
    fragment3 = ap.text.TextFragment("This is a new paragraph.")
    fragment3.text_state.font = ap.text.FontRepository.find_font("Arial")
    fragment3.text_state.font_size = 14
    page.paragraphs.add(fragment3)

    # Save PDF
    document.save(output_file_name)
```

### 创建多栏 PDF

使用 Aspose.PDF for Python via .NET 在 PDF 中创建多栏报纸式布局。
它展示了如何在 FloatingBox 中结合文本、HTML 格式和图形，实现类似多栏杂志或时事通讯设计的高级布局控制。

1. 初始化 PDF 文档。
1. 在顶部添加水平分隔线。
1. 添加样式化的 HTML 标题。
1. 创建用于布局控制的 FloatingBox。
1. 配置多栏布局。
1. 添加作者信息。
1. 绘制另一条内部水平线。
1. 添加文章文本。
1. 保存最终的 PDF。

```python

import aspose.pdf as ap
from aspose.pdf import Color
from aspose.pdf.drawing import Graph, Line
import os

# Global configuration
DATA_DIR = "your path here"

def create_multi_column_pdf(output_file_name):
    """
    Create a PDF document with multi-column layout using FloatingBox.

    Creates a professional-looking PDF with a multi-column newspaper-style layout.
    Demonstrates advanced layout techniques including floating boxes, column
    configuration, and mixed content with graphics and text.

    Args:
        output_file_name (str): The file path where the generated PDF document will be saved.

    Returns:
        None: The function saves the document to the specified output file.

    Note:
        - Document margins: 40 points left and right
        - Top horizontal line for visual separation
        - HTML-formatted heading with custom styling
        - FloatingBox with 2-column layout (105 units wide each)
        - Column spacing: 5 units between columns
        - Includes author attribution with italic styling
        - Internal horizontal line within the floating box
        - Long text content automatically flows between columns
        - Demonstrates professional document layout techniques

    Example:
        >>> create_multi_column_pdf("multi_column_layout.pdf")
        # Creates a PDF with newspaper-style multi-column layout
    """
    # Create PDF document
    document = ap.Document()

    # Set margins
    document.page_info.margin.left = 40
    document.page_info.margin.right = 40

    page = document.pages.add()

    #
    # Draw horizontal line at the top
    #
    graph1 = ap.drawing.Graph(500.0, 2.0)
    page.paragraphs.add(graph1)

    pos_arr = [1.0, 2.0, 500.0, 2.0]
    line1 = ap.drawing.Line(pos_arr)
    graph1.shapes.add(line1)

    #
    # Add HTML heading text
    #
    html = "<span style=\"font-family: 'Times New Roman'; font-size: 18px;\"><strong>How to Steer Clear of money scams</strong></span>"
    heading_text = ap.HtmlFragment(html)
    page.paragraphs.add(heading_text)

    #
    # Floating box: enables multi-column layout
    #
    box = ap.FloatingBox()

    box.column_info.column_count = 2  # Two columns
    box.column_info.column_spacing = "5"  # Space between columns
    box.column_info.column_widths = "105 105"  # Width of each column

    #
    # Add title text to the FloatingBox
    #
    text1 = ap.text.TextFragment("By A Googler (The Official Google Blog)")
    text1.text_state.font_size = 8
    text1.text_state.line_spacing = 2
    box.paragraphs.add(text1)

    text1.text_state.font_size = 10
    text1.text_state.font_style = ap.text.FontStyles.ITALIC

    #
    # Add another horizontal line inside the box
    #
    graph2 = ap.drawing.Graph(50.0, 10.0)

    pos_arr2 = [1.0, 10.0, 100.0, 10.0]
    line2 = ap.drawing.Line(pos_arr2)
    graph2.shapes.add(line2)

    box.paragraphs.add(graph2)

    #
    # Add long text content
    #
    lorem_path = os.path.join(DATA_DIR, "lorem.txt")
    lorem_text = (
        open(lorem_path, "r", encoding="utf-8").read()
        if os.path.exists(lorem_path)
        else "Lorem ipsum text not found."
    )
    text2 = ap.text.TextFragment(lorem_text * 5)
    box.paragraphs.add(text2)

    page.paragraphs.add(box)

    # Save PDF
    document.save(output_file_name)
```

### PDF 中文本对齐的自定义制表位

使用自定义制表位在 PDF 中创建类似表格的文本布局——无需依赖表格结构。
通过定义制表位位置、对齐方式和前导符样式，可以在列间精确对齐文本。这对于发票、报告或结构化文本数据非常有用。

1. 创建一个新的 PDF 文档。
1. 定义自定义制表位。
1. 在文本中使用 #$TAB 占位符。
1. 向 PDF 添加文本。
1. 保存 PDF。

```python

import aspose.pdf as ap
from aspose.pdf import Color
from aspose.pdf.drawing import Graph, Line
import os

# Global configuration
DATA_DIR = "your path here"

def custom_tab_stops(output_file_name):
    """
    Create a PDF document demonstrating custom tab stops for table-like formatting.

    Creates a PDF document that uses custom tab stops to format text in a table-like
    structure without using actual table elements. This demonstrates advanced text
    formatting with precise positioning and leader styles.

    Args:
        output_file_name (str): The file path where the generated PDF document will be saved.

    Returns:
        None: The function saves the document to the specified output file.

    Note:
        - Tab stop 1: Position 100, right-aligned, solid leader line
        - Tab stop 2: Position 200, center-aligned, dashed leader line
        - Tab stop 3: Position 300, left-aligned, dotted leader line
        - Uses #$TAB placeholder for tab positions in text
        - Creates table-like structure with headers and data rows
        - Demonstrates mixing TextFragment and TextSegment approaches
        - Leader lines provide visual guides between columns
        - Alternative to HTML tables for precise text positioning

    Example:
        >>> custom_tab_stops("custom_tabs.pdf")
        # Creates a PDF with custom tab stop formatting
    """
    # Create PDF document
    document = ap.Document()
    page = document.pages.add()

    # Define tab stops
    tab_stops = ap.text.TabStops()

    tab_stop1 = tab_stops.add(100)
    tab_stop1.alignment_type = ap.text.TabAlignmentType.RIGHT
    tab_stop1.leader_type = ap.text.TabLeaderType.SOLID

    tab_stop2 = tab_stops.add(200)
    tab_stop2.alignment_type = ap.text.TabAlignmentType.CENTER
    tab_stop2.leader_type = ap.text.TabLeaderType.DASH

    tab_stop3 = tab_stops.add(300)
    tab_stop3.alignment_type = ap.text.TabAlignmentType.LEFT
    tab_stop3.leader_type = ap.text.TabLeaderType.DOT

    # Create TextFragments with tab placeholders
    header = ap.text.TextFragment(
        "This is an example of forming table with TAB stops", tab_stops
    )
    text0 = ap.text.TextFragment("#$TABHead1 #$TABHead2 #$TABHead3", tab_stops)
    text1 = ap.text.TextFragment("#$TABdata11 #$TABdata12 #$TABdata13", tab_stops)

    text2 = ap.text.TextFragment("#$TABdata21 ", tab_stops)
    text2.segments.append(ap.text.TextSegment("#$TAB"))
    text2.segments.append(ap.text.TextSegment("data22 "))
    text2.segments.append(ap.text.TextSegment("#$TAB"))
    text2.segments.append(ap.text.TextSegment("data23"))

    # Add text fragments to page
    page.paragraphs.add(header)
    page.paragraphs.add(text0)
    page.paragraphs.add(text1)
    page.paragraphs.add(text2)

    # Save PDF document
    document.save(output_file_name)
```
