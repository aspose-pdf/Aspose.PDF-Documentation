---
title: 用 Python 格式化 PDF 文本
linktitle: PDF 中的文本格式
type: docs
weight: 70
url: /zh/python-net/text-formatting-inside-pdf/
description: 学习如何在 Python 中使用间距、边框、缩进和样式选项对 PDF 文档中的文本进行格式化。
lastmod: "2026-06-08"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 使用 Python 格式化 PDF 文件中的文本并设置其样式
Abstract: 本文介绍如何通过.NET 使用适用于 Python 的 Aspose.PDF 格式化 PDF 文档中的文本。学习如何在 Python 中控制间距、缩进、边框、下划线、删除线效果和其他文本样式选项。
---

## 行间距和字符间距

### 使用行距

#### 如何在 Python 中使用自定义行距设置文本格式-简单案例

Aspose.PDF for Python 提供了一种通过行距调整来控制文本布局和可读性的简单方法。

我们的代码片段显示了如何控制 PDF 文档中的行距。它读取文件中的文本（或使用备用消息），应用自定义字体大小和行间距，并将格式化文本添加到 PDF 中的新页面。

1. 创建新的 PDF 文档。
1. 加载源文本。
1. 初始化一个 TextFragment 对象并将加载的文本分配给它。
1. 设置文本的字体和间距属性。这些值决定了文本行显示的紧密程度或松散程度：
    -字体大小：12 点
    -行距：16 点
1. 将格式化文本片段插入页面的段落集合中。
1. 保存文档。

```python
import aspose.pdf as ap
import sys
from os import path

def specify_line_spacing_simple_case(outfile):
    document = ap.Document()
    page = document.pages.add()

    lorem_path = path.join(DATA_DIR, "lorem.txt")
    if path.exists(lorem_path):
        with open(lorem_path, "r", encoding="utf-8") as f:
            text = f.read()
    else:
        text = "Lorem ipsum text not found."

    text_fragment = ap.text.TextFragment(text)
    text_fragment.text_state.font_size = 12
    text_fragment.text_state.line_spacing = 16
    page.paragraphs.add(text_fragment)

    document.save(outfile)
```

#### 如何在 Python 中使用自定义行距设置文本格式-特定案例

让我们来看看如何使用自定义 TrueType 字体 (TTF) 在 PDF 文档中应用不同的行距模式。
它从文件加载文本，嵌入特定的字体，并在 PDF 页面上呈现两次相同的文本，每次都使用不同的行距模式：

- 字体大小模式：行距等于字体大小。
- FULL_SIZE 模式：行间距占字体的全部高度，包括上升和下降线。

该示例显示了行间距行为如何因所选模式而异。

1. 创建新的 PDF 文档。
1. 指定自定义字体文件和文本源文件的路径。
1. 加载文本内容。
1. 打开自定义字体。
1. 创建和配置第一个 TextFragment（字体大小模式）。将 line_spacing 设置为 “textFormattingOptions.linespacingMode.font_size”，这意味着行间距等于字体大小。
1. 创建和配置第二个 TextFragment（FULL_SIZE 模式）。将 line_spacing 设置为 “textFormattingOptions.linespacingMode.full_size”，它使用字体的全高。
1. 将两个文本片段附加到同一 PDF 页面。
1. 将完成的文档保存到指定的输出位置。

```python
import aspose.pdf as ap
import sys
from os import path

def specify_line_spacing_specific_case(outfile):
    document = ap.Document()
    page = document.pages.add()

    font_file = path.join(DATA_DIR, "HPSimplified.ttf")
    lorem_path = path.join(DATA_DIR, "lorem.txt")
    if path.exists(lorem_path):
        with open(lorem_path, "r", encoding="utf-8") as f:
            text = f.read()
    else:
        text = "Lorem ipsum text not found."

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

![PDF 文档使用自定义行距显示文本，显示行间距 16 点，以提高可读性和文本布局格式](line_spacing.png)

### 使用字符间距

#### 如何使用 TextFragment 类控制 PDF 文本中的字符间距

字符间距决定一行文本中各个字符之间的距离，这对于微调文本外观或实现特定的排版效果很有用。

1. 初始化一个新的 Document 对象并添加一个用于放置文本的空白页面。
1. 定义片段生成器。实现辅助函数 make_fragment（间距）：
    -使用示例文本创建 TextFragment。
    -设置字体。
1. 添加具有不同间距值的文本片段。
1. 保存文档。

```python
import aspose.pdf as ap
import sys
from os import path

def character_spacing_using_text_fragment(outfile):
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

![显示三行相同文本的 PDF 文档带有字符间距的示例文本显示自上而下的字符间距逐渐缩小，第一行字母之间的间距更宽，中行的间距适中，底行的字符间距最近，说明了 PDF 文本格式中不同字符间距值的视觉效果](character_spacing_simple.png)

#### 如何使用文本段落和文本生成器控制 PDF 文本中的字符间距

Aspose.PDF 允许在使用文本段落和文本生成器向 PDF 文档添加文本时应用自定义字符间距。
它定义页面上的特定区域，配置文本换行，并使用调整后的字符间距呈现文本片段。

当您需要精确控制文本放置和布局时，例如在构建结构化或多列文本块时，使用 TextProagragh 是理想的选择。

1. 创建新的 PDF 文档。
1. 为该页面初始化一个 TextBuilder 实例。
1. 创建和配置文本段落。
    -将自动换行模式设置为 “textFormattingOptions.Wordwrapmode.by_Words”。
1. 创建具有自定义字符间距的 TextFragment。
    -创建一个新的 TextFragment 并设置其文本（例如，“带字符间距的示例文本”）。
    -指定字体属性，例如 Arial 和字体大小 14 pt。
    -应用字符间距 = 2.0，这会增加字符之间的间距。
1. 将 TextFragment 添加到文本段落中。
1. 将文本段落添加到页面。
1. 保存 PDF 文档。

```python
import aspose.pdf as ap
import sys
from os import path

def character_spacing_using_text_paragraph(outfile):
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

## 创建清单

处理 PDF 文件时，您可能需要显示结构化信息，例如列表，无论它们是项目符号的、编号的，还是使用 HTML 或 LaTeX 格式化的。
通过.NET for Python 的 Aspose.PDF 提供了几种灵活的方法来直接在 PDF 文档中创建和格式化列表，使您可以完全控制布局、字体和样式。

本文演示了在 PDF 中创建列表的多种方法，从纯文本格式到高级 HTML 和 LaTeX 呈现。每种方法都有特定的用例——无论你喜欢精确的编程控制还是基于标记的便捷样式。

在本文结束时，您将知道如何：

- 使用文本段落和文本生成器创建自定义项目符号和编号列表。

- 使用 HTML 片段 (HtmlFragment) 可以轻松地在 PDF 中呈现 ul 和 ol 列表。

- 利用 LaTeX 片段 (TexFragment) 进行数学或科学列表格式。

- 控制页面内的文本包装、字体样式和布局定位。

- 了解手动列表构造和标记驱动方法之间的区别。

### 创建编号列表

```python
import aspose.pdf as ap
import sys
from os import path

def create_bullet_list(outfile):
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

### 创建项目符号清单

```python
import aspose.pdf as ap
import sys
from os import path

def create_numbered_list(outfile):
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

### 创建编号列表 HTML 版本

使用 HTML 片段在 PDF 文档中创建带编号（有序）的列表。它将 Python 字符串列表转换为 HTML 元素，并将其作为 HTMLFragment 插入 PDF 页面。

使用 HTML 片段可以将基于 HTML 的格式化功能，例如编号列表、粗体、斜体等，直接整合到 PDF 中。

1. 创建新的 PDF 文档并添加页面。
1. 准备清单项目。
1. 将列表转换为 HTML 有序列表。
    -使用 ol 标签获取编号列表。
    -使用列表推导将每个项目包含 “li” 标签。
1. 将 HTML 字符串转换为可以添加到 PDF 页面的 HTMLFragment 对象。
1. 将 HTMLFragment 插入到页面的段落集合中。
1. 保存 PDF 文档。

```python
import aspose.pdf as ap
import sys
from os import path

def create_numbered_list_html_version(outfile):
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

![在 PDF 文档中显示的编号列表显示了四个自动编号的项目：1.列表中的第一项，2。第二项包含更多用于演示包装行为的文本，3。第三项，以及 4.第四项。该列表演示了在 PDF 结构中使用 HTML 格式的有序列表呈现，并采用了正确的数字顺序、缩进和项目间距](numbered_list_html.png)

### 创建项目符号列表 HTML 版本

我们的库展示了如何使用 HTML 片段在 PDF 文档中创建项目符号（无序）列表。它将 Python 字符串列表转换为 HTML ul 元素，并将其作为 HTMLFragment 插入 PDF 页面。使用 HTML 片段可以直接在 PDF 中利用 HTML 格式化功能（如列表、粗体、斜体）。

1. 创建新的 PDF 文档并添加页面。
1. 准备清单项目。
1. 将该列表转换为 HTML 无序列表。
    -使用 ul 标签获取无序（项目符号）列表。
    -使用列表推导将每个项目包含 “li” 标签。
1. 创建一个 HTMLFragment。将 HTML 字符串转换为可以添加到 PDF 页面的 HTMLFragment 对象。
1. 将 HTMLFragment 插入到页面的段落集合中。
1. 保存 PDF 文档。

```python
import aspose.pdf as ap
import sys
from os import path

def create_bullet_list_html_version(outfile):
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

![项目符号列表显示在 PDF 文档中，显示四个项目：列表中的第一项、包含更多用于演示包装行为的第二项、第三项和第四项。每个项目前面都有一个标准项目符号，并演示了在 PDF 结构中以适当的缩进和间距呈现 HTML 格式的列表](bullet_list_html.png)

### 创建项目符号清单 LaTeX 版本

使用 LaTeX 片段 (TexFragment) 在 PDF 中创建项目符号（无序）列表。它将 Python 字符串列表转换为 LaTeX 逐项列出环境并将其插入到 PDF 页面中。当你想呈现具有精确格式的数学公式、符号或结构化列表时，使用 LaTeX 片段是理想的选择。

1. 创建新的 PDF 文档并添加页面。
1. 定义一个 Python 字符串列表，这些字符串将成为 LaTeX 逐项列出环境中的要点。
1. 将列表转换为 LaTeX 逐项列出环境：
    -用\ begin {itemize} 和\ end {itemize} 包装商品。
    -使用列表推导，每个项目都以\ item 作为前缀。
1. 将 LaTeX 字符串转换为可以在 PDF 中呈现的 TexFragment 对象。
1. 将 LaTeX 片段添加到页面。
1. 保存 PDF 文档。

```python
import aspose.pdf as ap
import sys
from os import path

def create_bullet_list_latex_version(outfile):
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

![在 PDF 中显示的项目符号列表显示了 LaTex 渲染的格式和文本列表很容易创建：其次是四个带有项目符号的项目：第一项、第二项（包含更多用于演示包装行为的文本）、第三项和第四项。该清单演示了专业的 LaTeX 排版，在简洁的 PDF 文档布局中具有正确的项目符号格式、一致的间距和文本包装功能](bullet_list_latex.png)

### 创建编号列表 LaTeX 版本

使用 LaTeX 片段 (TexFragment) 在 PDF 中创建带编号（有序）的列表。它将 Python 字符串列表转换为 LaTeX 枚举环境并将其插入到 PDF 页面中。当你想在 PDF 中进行精确的格式、结构化列表或数学表示法时，使用 LaTeX 片段是理想的选择。

1. 创建新的 PDF 文档并添加页面。
1. 定义一个 Python 字符串列表，这些字符串将在 LaTeX 枚举环境中成为编号项目。
1. 将列表转换为 LaTeX 枚举环境。
1. 将 LaTeX 字符串转换为可以在 PDF 中呈现的 TexFragment 对象。
1. 将 LaTeX 片段添加到页面。
1. 保存 PDF 文档。

```python
import aspose.pdf as ap
import sys
from os import path

def create_numbered_list_latex_version(outfile):
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

![PDF 中显示的编号列表显示了 LaTeX 渲染的格式，其中包含第 1 项。第一项，2。第二项包含更多用于演示包装行为的文本，3。第三项，以及 4.第四项，前面是文本列表，易于创建](numbered_list_latex.png)

## 脚注和尾注

### 添加脚注

脚注用于通过在相关文本旁边放置连续的上标数字来引用文档正文中的注释。这些数字对应于详细注释，这些注释通常缩进并位于同一页面的底部，提供额外的背景信息、引文或评论。

通过.NET 使用适用于 Python 的 Aspose.PDF 为 PDF 文档中的文本片段添加脚注。脚注可用于在不混乱主要内容的情况下提供补充信息、引文或澄清。这种方法可确保脚注在视觉和结构上集成到 PDF 布局中。

1. 创建新文档。
1. 使用主要内容创建一个 TextFragment。
1. 添加行内文本。创建另一个 TextFragment，该文本片段继续出现在同一段落中。
1. 保存文档。

```python
import aspose.pdf as ap
import sys
from os import path

def add_footnote(outfile):
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

### 在 PDF 中添加带有自定义样式的脚注

1. 初始化新的 PDF 文档并添加空白页面。
1. 创建正文片段。
1. 创建脚注并设置其样式（字体、大小、颜色、样式）。
1. 将带有脚注的样式文本片段插入页面。
1. 添加另一个不带脚注的文本片段。
1. 保存文档。

```python
import aspose.pdf as ap
import sys
from os import path

def add_footnote_custom_text_style(outfile):
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

### 在 PDF 中添加带有自定义符号的脚注

使用适用于 Python 的 Aspose.PDF 通过.NET 向 PDF 文档中的文本片段添加脚注，并能够自定义脚注标记符号。

1. 创建 PDF 文档和页面。
1. 添加第一个带有自定义脚注符号的文本片段。
1. 添加另一个不带脚注的文本片段，继续执行该段落。
1. 添加第二个带有默认脚注的文本片段。
1. 保存文档。

```python
import aspose.pdf as ap
import sys
from os import path

def add_footnote_custom_text(outfile):
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

### 在 PDF 中添加带有自定义线条样式的脚注

使用 Python 库自定义 PDF 文档中脚注行的视觉外观。自定义脚注行可增强视觉清晰度，并使报告、学术论文和带注释的出版物等文档的风格保持一致。

1. 创建新的 PDF 文档并添加页面。
1. 为脚注连接器定义自定义线条样式（颜色、宽度和短划线图案）。
1. 添加多个带脚注的文本片段。
1. 保存最终文档。

```python
import aspose.pdf as ap
import sys
from os import path

def add_footnote_with_custom_line_style(outfile):
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

### 在 PDF 中添加带有图像和表格的脚注

如何通过.NET 使用 Aspose.PDF for Python 嵌入图像、样式化文本和表格来丰富 PDF 文档中的脚注？

1. 创建新的 PDF 文档并添加页面。
1. 添加带有附加脚注的文本片段。
1. 在脚注中嵌入图像、样式文本和表格。
1. 保存文档。

```python
import aspose.pdf as ap
import sys
from os import path

def add_footnote_with_image_and_table(outfile):
    document = ap.Document()
    page = document.pages.add()

    text = ap.text.TextFragment("This is a sample text with a footnote.")
    page.paragraphs.add(text)

    note = ap.Note()

    # Add image
    image_note = ap.Image()
    image_note.file = path.join(DATA_DIR, "logo.jpg")
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

Endnote是一种引文，它引导读者进入文档末尾的指定部分，在那里他们可以找到引文、释义想法或摘要内容的完整参考资料。使用尾注时，在参考材料之后立即放置一个上标编号，引导读者阅读论文末尾的相应注释。

此代码片段演示了如何向 PDF 文档中的文本片段添加尾注。与脚注不同，脚注出现在引用文本附近，而尾注通常位于文档或章节的末尾。此方法还模拟了较长的文档，以说明尾注在扩展内容中的表现。

1. 创建 PDF 文档和页面。
1. 使用 Endnote 添加文本片段。
1. 加载外部文本内容。
1. 模拟长文档。多次添加加载的文本以模拟更长的文档。
1. 保存文档。

```python
import aspose.pdf as ap
import sys
from os import path

def add_endnote(outfile):
    document = ap.Document()
    page = document.pages.add()

    text_fragment = ap.text.TextFragment("This is a sample text with an endnote.")
    text_fragment.text_state.font = ap.text.FontRepository.find_font("Arial")
    text_fragment.text_state.font_size = 14
    text_fragment.end_note = ap.Note("This is the EndNote content.")
    page.paragraphs.add(text_fragment)

    lorem_path = path.join(DATA_DIR, "lorem.txt")
    if path.exists(lorem_path):
        with open(lorem_path, encoding="utf-8") as f:
            text_content = f.read()
    else:
        text_content = "Lorem ipsum sample text not found."

    # Simulate long text
    for _ in range(5):
        tf = ap.text.TextFragment(text_content)
        tf.text_state.font = ap.text.FontRepository.find_font("Arial")
        tf.text_state.font_size = 14
        page.paragraphs.add(tf)

    document.save(outfile)
```

### 在 PDF 中添加带有自定义标记文本的尾注

在 PDF 文档的文本片段中添加尾注，并使用自定义标记符号（例如 “***”）。尾注通常放在文档或章节的末尾，可用于提供其他上下文、引文或评论。

1. 创建 PDF 文档和页面。
1. 添加带有尾注的样式文本片段。
1. 自定义尾注标记文本。
1. 从 .txt 文件加载外部内容。
1. 模拟长篇内容以说明尾注的位置。
1. 保存 PDF 文档。

```python
import aspose.pdf as ap
import sys
from os import path

def add_endnote_custom_text(outfile):
    document = ap.Document()
    page = document.pages.add()

    text_fragment = ap.text.TextFragment("This is a sample text with an endnote.")
    text_fragment.text_state.font = ap.text.FontRepository.find_font("Arial")
    text_fragment.text_state.font_size = 14
    text_fragment.end_note = ap.Note("This is the EndNote content.")
    text_fragment.end_note.text = "***"
    page.paragraphs.add(text_fragment)

    lorem_path = path.join(DATA_DIR, "lorem.txt")
    if path.exists(lorem_path):
        with open(lorem_path, encoding="utf-8") as f:
            text_content = f.read()
    else:
        text_content = "Lorem ipsum sample text not found."

    # Simulate long text
    for _ in range(5):
        tf = ap.text.TextFragment(text_content)
        tf.text_state.font = ap.text.FontRepository.find_font("Arial")
        tf.text_state.font_size = 14
        page.paragraphs.add(tf)

    document.save(outfile)
```

## 布局和页面控制

### 强制表格从 PDF 中的新页面开始

通过.NET 使用适用于 Python 的 Aspose.PDF 在 PDF 文档的新页面上添加特定内容。
通过设置属性 “is_in_new_page”，您可以精确控制页面布局和结构，确保特定部分（例如表格、报告或摘要）始终从新页面开始，非常适合文档格式、打印就绪报告或有组织的输出生成。

1. 创建和配置表。
1. 向表中添加数据。
1. 强制表格换一个新页面。这样可以确保表格从新页面的顶部开始，即使当前页面上有现有内容也是如此。
1. 将表格添加到页面。使用 “page.parage.paraghs.add ()” 将表格包含在 PDF 布局中。
1. 保存文档。

```python
import aspose.pdf as ap
import sys
from os import path

def force_new_page(output_file_name):
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

### 在 PDF 中使用行内段落属性

我们的库允许您使用 “is_in_line_paragraph” 属性来控制 PDF 中文本和图像之间的内联流动。
通常，当您添加新元素（例如文本片段或图像）时，每个元素都从新行或新段落开始。
通过设置 “is_in_line_paragraparage = True”，您可以使元素出现在同一行或同一段落中，从而创建流畅的行内布局——非常适合内联组合文本和图像，例如在句子中添加徽标、图标或符号。

第一个文本片段、图像和第二个文本片段出现在同一行上，形成一个连续的行内段落。
第三个文本片段开始了一个新段落，演示了默认的换行行为。

1. 创建新的 PDF 文档。
1. 添加第一个文本片段。
1. 插入行内图片。
1. 添加更多行内文本。
1. 添加新段落。
1. 保存 PDF。

```python
import aspose.pdf as ap
import sys
from os import path

def using_inline_paragraph_property(output_file_name):
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
    image.file = path.join(DATA_DIR, "logo.jpg")
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

### 创建多列 PDF

通过 .NET 使用 Aspose.PDF for Python 在 PDF 中创建多栏报纸样式布局。
它展示了如何在 FloatingBox 中组合文本、HTML 格式和图形，从而实现类似于多栏杂志或时事通讯设计的高级版面控制。

1. 初始化 PDF 文档。
1. 在顶部添加一条水平分隔线。
1. 添加样式化的 HTML 标题。
1. 为布局控制创建 FloatingBox。
1. 配置多列布局。
1. 添加作者信息。
1. 画另一条内部水平线。
1. 添加文章文本。
1. 保存最终的 PDF。

```python
import aspose.pdf as ap
import sys
from os import path

def create_multi_column_pdf(output_file_name):
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
    lorem_path = path.join(DATA_DIR, "lorem.txt")
    if path.exists(lorem_path):
        with open(lorem_path, "r", encoding="utf-8") as f:
            lorem_text = f.read()
    else:
        lorem_text = "Lorem ipsum text not found."
    text2 = ap.text.TextFragment(lorem_text * 5)
    box.paragraphs.add(text2)

    page.paragraphs.add(box)

    # Save PDF
    document.save(output_file_name)
```

### 在 PDF 中使用自定义制表位来对齐文本

使用自定义制表位在 PDF 中创建类似表格的文本布局，无需依赖表格结构。
通过定义制表位位置、对齐方式和引线样式，您可以精确地在各列之间对齐文本。这对于发票、报告或结构化文本数据很有用。

1. 创建新的 PDF 文档。
1. 定义自定义制表位。
1. 在文本中使用 #$TAB占位符。
1. 向 PDF 添加文本。
1. 保存 PDF。

```python
import aspose.pdf as ap
import sys
from os import path

def custom_tab_stops(output_file_name):
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

### 相关文字主题

- [使用 Python 处理 PDF 中的文本](/pdf/zh/python-net/working-with-text/)
- [向 PDF 添加文本](/pdf/zh/python-net/add-text-to-pdf-file/)
- [使用 Python 旋转 PDF 中的文本](/pdf/zh/python-net/rotate-text-inside-pdf/)
- [通过 Python 替换 PDF 中的文本](/pdf/zh/python-net/replace-text-in-pdf/)