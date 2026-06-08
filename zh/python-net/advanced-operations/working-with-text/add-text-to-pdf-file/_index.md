---
title: 在 Python 中向 PDF 添加文本
linktitle: 向 PDF 添加文本
type: docs
weight: 10
url: /zh/python-net/add-text-to-pdf-file/
description: 了解如何在 Python 中向 PDF 文档添加文本、HTML 片段、列表、链接和自定义字体。
lastmod: "2026-06-08"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 使用 Python 向 PDF 文件添加文本、链接、HTML 和字体
Abstract: 本文说明了如何使用 Aspose.PDF for Python via .NET 在 PDF 文档中添加和格式化文本。它涵盖了核心技术，如定位文本、应用字体和样式设置、插入链接和列表，以及在 Python 工作流中使用 HTML、LaTeX 和自定义字体。
---

本指南介绍如何使用 Aspose.PDF for Python via .NET 向 PDF 文档添加文本内容。您将学习核心的文本插入技术——从在特定位置放置简单的文本片段，到对其进行样式设置（字体、大小、颜色、样式），处理从右到左 (RTL) 语言，嵌入超链接，以及使用段落布局、列表和透明度效果。文章还涵盖了高级场景，例如使用 HTML 或 LaTeX 片段、自定义字体以及行间距和字符间距等文本格式化选项。

无论您是构建简单的注释还是丰富的排版布局，本资源为您提供使用 Aspose.PDF 在 PDF 中处理文本的基本构建块。

## 基本文本插入

Aspose.PDF for Python via .NET 提供了强大且灵活的 API，用于处理 PDF 文件中的文本。
无论您需要简单的静态标签、丰富格式的内容、多语言文本，还是交互式超链接，该工具包都能通过简洁的 Python 代码实现所有这些功能。

### 添加文本 简单案例

Aspose.PDF for Python via .NET 显示如何在页面的特定位置添加一个简单的文本片段。您将学习如何创建一个新的 PDF 文档，添加页面，在给定坐标插入文本，并保存生成的文件。

1. 创建一个新 [文档](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 对象。
1. 使用 `document.pages.add()` 创建一个新的空白 [页面](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/).
1. 创建一个 [`TextFragment`](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragment/) 带有文本内容。
1. 使用该方式设置文本位置 [`Position`](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/position/) 类。如果您指定 `Position`，文本将在您的文档中从左到右定位并向下偏移。
1. 自定义文本外观。您可以设置字体大小、颜色、字体样式等，通过 [`TextState`](https://reference.aspose.com/pdf/python-net/aspose.pdf/textstate/).
1. 追加 `TextFragment` 将页面的段落集合与 `page.paragraphs.add(text_fragment)`.
1. 保存文档。

以下代码片段展示了如何在现有 PDF 文件中添加文本：

```python
import math
import sys
import os
import aspose.pdf as ap

# region Basic text insertion
def add_text_simple_case(output_file_name):
    # Create a new document
    document = ap.Document()
    page = document.pages.add()

    # Add a text fragment at a specific position
    text_fragment = ap.text.TextFragment("Hello, Aspose!")
    text_fragment.position = ap.text.Position(100, 600)

    page.paragraphs.add(text_fragment)
    document.save(output_file_name)
```

此代码示例使用 TextFragment。您也可以使用 TextParagraph 向 PDF 页面添加文本。
该 **[TextFragment](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragment/)** 是单个文本块。它代表一个可以独立放置、样式化和定位的文本字符串。当您需要添加小而简单的文本内容时，它是理想的选择。

该 **[文本段落](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textparagraph/)** 是一组 TextFragments。它可以添加多行文本。TextParagraph 是一个容器或集合，包含一个或多个 TextFragment 对象。当您需要对多个片段进行分组时，它非常理想——例如，创建一个包含多行、单词或格式化元素的文本块。
TextParagraph 还管理文本对齐、行间距以及页面上的自动布局。仅在 TextParagraph 中才能使用红线。

有关文本处理的更多信息，请参阅 [PDF 中的文本格式化](/pdf/zh/python-net/text-formatting-inside-pdf/) 和 [搜索并获取 PDF 文本](/pdf/zh/python-net/search-and-get-text-from-pdf/).

### 使用 TextParagraph 添加文本

Aspose.PDF for Python via .NET 可以使用 [`TextBuilder`](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textbuilder/) 和 [`TextParagraph`](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textparagraph/) 带有换行选项。

1. 创建一个新 [文档](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 以及空白 [页面](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) 使用 `document.pages.add()`.
1. 从文件读取文本或使用默认文本。
1. 创建一个 [`TextBuilder`](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textbuilder/) 添加具有布局和换行控制的段落级内容。
1. 创建一个 [`TextParagraph`](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textparagraph/) 并设置换行模式（示例使用 `DISCRETIONARY_HYPHENATION`).
1. 创建一个 [`TextFragment`](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragment/), 应用样式，并将片段追加到段落。
1. 使用 the 将段落追加到页面 `TextBuilder`.
1. 保存文档。

```python
import math
import sys
import os
import aspose.pdf as ap

def add_paragraph(output_file_name):
    document = ap.Document()
    page = document.pages.add()

    lorem_path = LOREM_PATH
    if os.path.exists(lorem_path):
        with open(lorem_path, "r", encoding="utf-8") as file:
            text = file.read()
    else:
        text = "Lorem ipsum sample text not found."

    builder = ap.text.TextBuilder(page)
    paragraph = ap.text.TextParagraph()
    paragraph.first_line_indent = 20
    paragraph.rectangle = ap.Rectangle(80, 800, 400, 200, True)
    # paragraph.formatting_options.wrap_mode = TextFormattingOptions.WordWrapMode.BY_WORDS
    paragraph.formatting_options.wrap_mode = (
        ap.text.TextFormattingOptions.WordWrapMode.DISCRETIONARY_HYPHENATION
    )

    fragment = ap.text.TextFragment(text)
    fragment.text_state.font = ap.text.FontRepository.find_font("Times New Roman")
    fragment.text_state.font_size = 12

    paragraph.append_line(fragment)
    builder.append_paragraph(paragraph)

    document.save(output_file_name)
```

![使用 TextParagraph 添加文本](text_paragraph.png)

### 在 PDF 中添加带缩进的段落

以下代码片段展示了如何创建一个新的 PDF 文档并添加两段具有不同缩进样式的文本：

- 第一段演示了首行缩进（仅首行缩进）。

- 第二段演示了后续行缩进（首行之后的所有行都缩进）。

它使用 Aspose.PDF 中的 'TextParagraph'、'TextBuilder' 和 'TextFragment' 类来精确控制布局和格式。

```python
import math
import sys
import os
import aspose.pdf as ap

def add_paragraphs_indents(output_file_name):
    document = ap.Document()
    page = document.pages.add()

    lorem_path = LOREM_PATH
    if os.path.exists(lorem_path):
        with open(lorem_path, "r", encoding="utf-8") as file:
            text = file.read()
    else:
        text = "Lorem ipsum sample text not found."

    fragment = ap.text.TextFragment(text)
    fragment.text_state.font = ap.text.FontRepository.find_font("Times New Roman")
    fragment.text_state.font_size = 12

    builder = ap.text.TextBuilder(page)
    paragraph1 = ap.text.TextParagraph()
    paragraph1.first_line_indent = 20
    paragraph1.rectangle = ap.Rectangle(80, 800, 300, 50, True)
    paragraph1.formatting_options.wrap_mode = (
        ap.text.TextFormattingOptions.WordWrapMode.BY_WORDS
    )

    paragraph1.append_line(fragment)
    builder.append_paragraph(paragraph1)

    paragraph2 = ap.text.TextParagraph()
    paragraph2.subsequent_lines_indent = 20
    paragraph2.rectangle = ap.Rectangle(320, 800, 500, 50, True)
    paragraph2.formatting_options.wrap_mode = (
        ap.text.TextFormattingOptions.WordWrapMode.BY_WORDS
    )

    paragraph2.append_line(fragment)
    builder.append_paragraph(paragraph2)
    document.save(output_file_name)
```

### 在 PDF 中添加新行文本

Aspose.PDF for Python via .NET 允许您使用 TextFragment、TextParagraph 和 TextBuilder 类向 PDF 文档插入多行文本。

1. 创建一个新文档。
1. 定义一个包含换行符的 TextFragment。
1. 设置文本样式。
1. 将片段添加到段落中。
1. 定位段落。
1. 在页面上渲染段落。
1. 保存文档。

```python
import math
import sys
import os
import aspose.pdf as ap

def add_new_line(output_file):
    """Add a new line of text to a PDF document."""
    # Create PDF document
    document = ap.Document()
    page = document.pages.add()

    # Initialize new TextFragment with text containing required newline markers
    text_fragment = ap.text.TextFragment("Applicant Name: " + os.linesep + " Joe Smoe")

    # Set text fragment properties if necessary
    text_fragment.text_state.font_size = 12
    text_fragment.text_state.font = ap.text.FontRepository.find_font("TimesNewRoman")
    text_fragment.text_state.background_color = ap.Color.light_gray
    text_fragment.text_state.foreground_color = ap.Color.red

    # Create TextParagraph object
    par = ap.text.TextParagraph()

    # Add new TextFragment to paragraph
    par.append_line(text_fragment)

    # Set paragraph position
    par.position = ap.text.Position(100, 600)

    # Create TextBuilder object
    text_builder = ap.text.TextBuilder(page)

    # Add the TextParagraph using TextBuilder
    text_builder.append_paragraph(par)

    # Save PDF document
    document.save(output_file)
```

### 确定 PDF 中的换行符并记录通知

它展示了如何创建包含多个文本片段的 PDF 文档，并启用 Aspose.PDF 通知日志，以在渲染期间监控布局事件——例如换行和文字换行——。

1. 创建一个新的 PDF 文档。
1. 启用通知日志记录。
1. 使用 document.pages.add() 来创建第一页。
1. 添加多个文本片段。
1. 使用 page.paragraphs.add(text) 来渲染每个文本片段。
1. 保存文档。

```python
import math
import sys
import os
import aspose.pdf as ap

def determine_line_break(output_file):
    """Create a PDF document with multiple text fragments and log notifications."""
    # Create PDF document
    document = ap.Document()

    # Enable notification logging
    document.enable_notification_logging = True

    page = document.pages.add()

    for i in range(4):
        text = ap.text.TextFragment(
            "Lorem ipsum \r\ndolor sit amet, consectetur adipiscing elit, "
            "sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. "
            "Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris "
            "nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in "
            "reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla "
            "pariatur. Excepteur sint occaecat cupidatat non proident, sunt in "
            "culpa qui officia deserunt mollit anim id est laborum."
        )
        text.text_state.font_size = 20
        page.paragraphs.add(text)

    # Save PDF document
    document.save(output_file)

    notifications = document.pages[1].get_notifications()
    print(notifications)
```

### 在 PDF 中动态测量文本宽度

使用 Aspose.PDF for Python via .NET 动态测量特定字体中字符和字符串的宽度。它使用 'Font.measure_string()' 和 'TextState.measure_string()' 方法来验证测得的字符串宽度是否一致且准确。

1. 使用 'FontRepository.find_font()' 从仓库检索 Arial 字体对象。
1. 创建一个 TextState 对象来管理字体属性。
1. 测量单个字符。
1. 比较两种方法在所有字符从 'A' 到 'z' 之间的结果。
1. 确保两种测量方法得到相同的结果。

```python
import math
import sys
import os
import aspose.pdf as ap

def get_text_width_dynamically(output_file):
    font = ap.text.FontRepository.find_font("Arial")
    ts = ap.text.TextState()
    ts.font = font
    ts.font_size = 14

    if math.fabs(font.measure_string("A", 14) - 9.337) > 0.001:
        print("Unexpected font string measure!")

    if math.fabs(ts.measure_string("z") - 7.0) > 0.001:
        print("Unexpected font string measure!")

    c_code = ord("A")
    while c_code <= ord("z"):
        c = chr(c_code)

        fn_measure = font.measure_string(str(c), 14)
        ts_measure = ts.measure_string(str(c))

        if math.fabs(fn_measure - ts_measure) > 0.001:
            print("Font and state string measuring doesn't match!")

        c_code += 1
```

### 添加带超链接的文本

使用 Aspose.PDF for Python via .NET 在 PDF 中添加可点击的超链接。我们的库演示了如何在单个 TextFragment 中添加多个文本段落，并为特定段落应用超链接，以及对文本段落进行单独样式设置（例如颜色、斜体字体）。

1. 使用 'Document()' 创建新文档和页面，并使用 'document.pages.add()' 添加空白页。
1. 创建一个 TextFragment。
1. 添加多个 TextSegment 对象。每个段落都可以拥有自己的内容和样式。例如，普通文本或超链接文本。
1. 将超链接应用于一个段落。创建一个具有所需 URL 的 WebHyperlink 对象。
1. 为段落设置样式。使用 text_state 自定义颜色、字体样式、大小等。
1. 使用 'page.paragraphs.add()' 将片段添加到页面。
1. 保存 PDF。

```python
import math
import sys
import os
import aspose.pdf as ap

def add_text_with_hyperlink(output_file_name):
    document = ap.Document()
    page = document.pages.add()

    fragment = ap.text.TextFragment("Sample Text Fragment")

    segment = ap.text.TextSegment(" ... Text Segment 1...")
    fragment.segments.append(segment)

    segment = ap.text.TextSegment("Link to Aspose")
    fragment.segments.append(segment)
    segment.hyperlink = ap.WebHyperlink("https://products.aspose.com/pdf")
    segment.text_state.foreground_color = ap.Color.blue
    segment.text_state.font_style = ap.text.FontStyles.ITALIC

    segment = ap.text.TextSegment("TextSegment without hyperlink")
    fragment.segments.append(segment)

    page.paragraphs.add(fragment)
    document.save(output_file_name)
```

![在 PDF 中显示的文本片段展示了混合内容，包含 Sample Text Fragment，随后是 Text Segment 1，然后是一个蓝色超链接文本，内容为 Link to Aspose（链接到 https://products.aspose.com/pdf），并以普通黑色文本格式的 TextSegment 结尾且不带超链接](hyperlink_text.png)

### 向 PDF 文档添加从右到左 (RTL) 文本

RTL（从右到左）是一种属性，指示文本书写的方向，即文本从右侧向左侧书写。
Aspose.PDF for Python via .NET. 演示如何向 PDF 文档添加从右到左 (RTL) 文本，例如阿拉伯语或希伯来语。

1. 使用 'Document()' 创建新文档和页面，并使用 'document.pages.add()' 添加空白页。
1. 创建一个包含 RTL 内容的 TextFragment。将您的阿拉伯语、希伯来语或其他 RTL 语言文本作为片段内容插入。
设置字体和样式。选择支持 RTL 脚本的字体（例如，Tahoma，Arial Unicode MS）。根据需要设置 font_size 和 foreground_color。
1. 使用 'text_fragment.horizontal_alignment' 将水平对齐设置为右对齐。
1. 将 TextFragment 添加到页面。
1. 保存 PDF 文档。

```python
import math
import sys
import os
import aspose.pdf as ap

def add_text_with_rtl_text(output_file_name):
    document = ap.Document()
    page = document.pages.add()
    # Styled text fragment
    text_fragment = ap.text.TextFragment(
        "يعتبر خوجا نصر الدين شخصية فولكلورية من الشرق الإسلامي وبعض شعوب البحر الأبيض المتوسط ​​والبلقان، وهو بطل القصص والحكايات القصيرة الفكاهية والساخرة، وأحيانًا الحكايات اليومية."
    )
    text_fragment.text_state.font = ap.text.FontRepository.find_font("Tahoma")
    text_fragment.text_state.font_size = 14
    text_fragment.text_state.foreground_color = ap.Color.blue
    text_fragment.horizontal_alignment = ap.HorizontalAlignment.RIGHT

    page.paragraphs.add(text_fragment)
    document.save(output_file_name)
```

![从右到左文本](rtl_text.png)

## 文本样式

### 添加带字体样式的文本

这是一个更高级的示例，展示了文本样式、字体自定义以及混合格式文本（使用下标文本段）。Aspose.PDF 解释了如何将字体属性（如字体系列、大小、颜色、粗体、斜体和下划线）应用于文本片段。
此外，此代码片段展示了如何在单个片段中使用多个文本段来创建复杂的文本表达式——例如，包含下标或上标字符，这在公式或科学表示中常常需要。

1. 使用 'Document()' 创建新文档和页面，并使用 'document.pages.add()' 添加空白页。
1. 创建一个用于简单样式文本的 TextFragment。
1. 定义文本内容。
1. 使用 Position(x, y) 坐标设置位置。
1. 通过 'text_state property' 应用样式 - font、font_size、foreground_color、underline。
1. 使用多个 TextSegment 对象创建复杂表达式。每个 TextSegment 表示文本的一部分，可以拥有各自的样式。这使您能够构建表达式，例如数学或化学公式。
1. 定义多个 TextState 对象。一个用于主要文本（text_state_letters）。另一个用于下标或上标文本（text_state_index）。
1. 合并文本段。使用 'segments.append()' 将每个段追加到 'TextFragment'。
1. 将两个文本对象都添加到页面。使用 'page.paragraphs.add()' 将它们放置在文档中。
1. 保存最终文档。

```python
import math
import sys
import os
import aspose.pdf as ap

def add_text_with_font_styling(output_file_name):
    document = ap.Document()
    page = document.pages.add()

    # Initialize an empty TextFragment to build a formula using segments
    formula = ap.text.TextFragment()
    text_fragment = ap.text.TextFragment("Hello, Aspose!")
    text_fragment.position = ap.text.Position(100, 600)
    text_fragment.text_state.font = ap.text.FontRepository.find_font("Arial")
    text_fragment.text_state.font_size = 14
    text_fragment.text_state.foreground_color = ap.Color.blue
    text_fragment.text_state.font_style = (
        ap.text.FontStyles.BOLD | ap.text.FontStyles.ITALIC
    )
    text_fragment.text_state.underline = True
    text_fragment.horizontal_alignment = ap.HorizontalAlignment.LEFT

    text_state_letters = ap.text.TextState()
    text_state_letters.font = ap.text.FontRepository.find_font("Arial")
    text_state_letters.font_size = 14
    text_state_letters.foreground_color = ap.Color.blue
    text_state_letters.font_style = ap.text.FontStyles.BOLD

    text_state_index = ap.text.TextState()
    text_state_index.font = ap.text.FontRepository.find_font("Arial")
    text_state_index.font_size = 14
    text_state_index.foreground_color = ap.Color.dark_red
    # text_state_index.superscript = True
    text_state_index.subscript = True

    position = ap.text.Position(100, 500)

    # Helper function to add segments
    def add_segment(text, state):
        seg = ap.text.TextSegment(text)
        seg.text_state = state
        seg.position = position
        formula.segments.append(seg)

    add_segment("S = a", text_state_letters)
    add_segment("2n", text_state_index)
    add_segment(" + a", text_state_letters)
    add_segment("2n+1", text_state_index)
    add_segment(" + a", text_state_letters)
    add_segment("2n+2", text_state_index)
    formula.horizontal_alignment = ap.HorizontalAlignment.LEFT

    page.paragraphs.add(text_fragment)
    page.paragraphs.add(formula)
    document.save(output_file_name)
```

![文本片段使用蓝色斜体 Arial 字体显示，内容为 Hello, Aspose!，随后是一个数学公式，显示 S = a₂ₙ + a₂ₙ₊₁ + a₂ₙ₊₂，主文本为蓝色，下标为红色格式。](styled_text.png)

## 添加文本透明

使用 Aspose.PDF for Python 向 PDF 文档添加半透明形状和文本。
它创建了一个带有部分不透明度的彩色矩形，并在其上覆盖一个具有透明前景色的 TextFragment。

1. 初始化一个 Document 对象并添加一个空白页用于绘制内容。
1. 使用 'ap.drawing.Graph' 创建一个画布，以便您可以绘制形状。
1. 添加一个具有半透明填充的矩形。
1. 防止画布位置偏移。
1. 将画布添加到页面。将图形形状插入页面段落集合。
1. 创建一个透明的文本片段。
1. 将文本片段插入页面段落集合。
1. 保存 PDF 文档。

```python
import math
import sys
import os
import aspose.pdf as ap

def add_text_transparent(output_file_name):
    # Create PDF document
    document = ap.Document()
    page = document.pages.add()

    # Create Graph object
    canvas = ap.drawing.Graph(100.0, 400.0)

    # Create rectangle with semi-transparent fill
    rect = ap.drawing.Rectangle(100, 100, 400, 400)
    rect.graph_info.fill_color = ap.Color.from_argb(128, 0xC5, 0xB5, 0xFF)
    canvas.shapes.add(rect)

    # Prevent position shift
    canvas.is_change_position = False
    page.paragraphs.add(canvas)

    # Create transparent text
    text = ap.text.TextFragment(
        "This is the transparent text. "
        "This is the transparent text. "
        "This is the transparent text."
    )
    text.text_state.foreground_color = ap.Color.from_argb(30, 0, 255, 0)
    page.paragraphs.add(text)

    document.save(output_file_name)
```

### 向 PDF 添加不可见文本

本示例演示如何创建一个包含可见文本和不可见文本的 PDF 文档。不可见文本仍然是文档结构的一部分，但在视觉上被隐藏，这使其可用于嵌入元数据、可访问性标签或可搜索内容，而不会影响布局。

1. 创建 PDF 文档和页面。
1. 创建一个包含重复可见内容的文本片段。
1. 添加第二个文本片段并将其标记为不可见。
1. 保存文档。

```python
import math
import sys
import os
import aspose.pdf as ap

def add_text_invisible(output_file_name):
    # Create PDF document
    document = ap.Document()
    page = document.pages.add()

    # Add visible text
    text1 = ap.text.TextFragment(
        "This is the visible text. This is the visible text. This is the visible text."
    )
    page.paragraphs.add(text1)

    # Create transparent text
    text2 = ap.text.TextFragment(
        "This is the invisible text. "
        "This is the invisible text. "
        "This is the invisible text."
    )
    text2.text_state.invisible = True
    page.paragraphs.add(text2)

    document.save(output_file_name)
```

### 在 PDF 中添加带边框样式的文本

Aspose.PDF 库展示了如何创建包含带可见边框的样式化文本片段的 PDF 文档。该方法为文本矩形应用背景色和前景色、字体设置以及描边（边框），以增强视觉强调。

1. 创建一个 PDF 文档和一个页面。
1. 创建并定位文本片段。添加一个带有消息的文本片段并设置其位置。
1. 应用文本样式。将字体设置为 Times New Roman，大小 12。应用浅灰色背景和红色前景（文本）颜色。
1. 配置边框样式。
1. 将文本添加到页面。使用 TextBuilder 将样式化的文本追加到页面。
1. 保存文档。

```python
import math
import sys
import os
import aspose.pdf as ap

def add_text_border(output_file_name):
    # Create PDF document
    document = ap.Document()
    # Get particular page
    page = document.pages.add()
    # Create text fragment
    text_fragment = ap.text.TextFragment("This is sample text with border.")
    text_fragment.position = ap.text.Position(10, 700)

    # Set text properties
    text_fragment.text_state.font = ap.text.FontRepository.find_font("Times New Roman")
    text_fragment.text_state.font_size = 12
    text_fragment.text_state.background_color = ap.Color.light_gray
    text_fragment.text_state.foreground_color = ap.Color.red
    # Set StrokingColor property for drawing border (stroking) around text rectangle.
    # Note: This only affects the border if draw_text_rectangle_border is set to True.
    text_fragment.text_state.stroking_color = ap.Color.dark_red
    # Enable drawing of the text rectangle border
    text_fragment.text_state.draw_text_rectangle_border = True

    text_builder = ap.text.TextBuilder(page)
    text_builder.append_text(text_fragment)

    # Save PDF document
    document.save(output_file_name)
```

### 在 PDF 中添加删除线文字

在 PDF 文档中的文本片段添加删除线（划掉）格式。删除线文本对于在注释文档中指示删除、修订或强调非常有用。

1. 使用 'Document()' 创建新文档和页面，并使用 'document.pages.add()' 添加空白页。
1. 创建并样式化文本片段。
1. 应用颜色和删除线格式。将背景设为浅灰色，文字颜色设为红色，并启用删除线。
1. 定位文本。
1. 使用 'TextBuilder' 将样式化文本附加到页面。
1. 保存文档。

```python
import math
import sys
import os
import aspose.pdf as ap

def add_strikeout_text(output_file_name):
    # Create PDF document
    document = ap.Document()
    page = document.pages.add()

    # Create text fragment
    text_fragment = ap.text.TextFragment("This is sample strikeout text.")
    # Set text properties
    text_fragment.text_state.font_size = 12
    text_fragment.text_state.font = ap.text.FontRepository.find_font("TimesNewRoman")
    text_fragment.text_state.background_color = ap.Color.light_gray
    text_fragment.text_state.foreground_color = ap.Color.red
    text_fragment.text_state.strike_out = True
    text_fragment.text_state.font_style = ap.text.FontStyles.BOLD
    text_fragment.position = ap.text.Position(100, 600)

    # Create TextBuilder object
    text_builder = ap.text.TextBuilder(page)
    text_builder.append_text(text_fragment)

    # Save PDF document
    document.save(output_file_name)
```

## 高级颜色效果

### 在 PDF 中对文本应用轴向渐变

Aspose.PDF for Python via .NET 演示了如何在 PDF 文档中的文本上应用线性渐变效果。轴向渐变在文本中平滑地从红色过渡到蓝色，形成视觉上令人印象深刻的标题。此技术非常适用于样式化标题、品牌标识或 PDF 文档布局中的装饰元素。

1. 初始化一个新文档并添加一个空白页。
1. 创建并样式化文本片段。添加标题，设置位置、字体和大小。
1. 使用 'GradientAxialShading' 应用轴向渐变遮罩。使用 GradientAxialShading 将前景颜色设置为从红色到蓝色。
1. 添加下划线样式。
1. 将样式化的文本片段插入页面。
1. 保存文档。

```python
import math
import sys
import os
import aspose.pdf as ap

def apply_gradient_axial_shading_to_text(output_file_name):
    # Create PDF document
    document = ap.Document()
    page = document.pages.add()

    text_fragment = ap.text.TextFragment("PDF TITLE")
    text_fragment.position = ap.text.Position(100, 600)
    text_fragment.text_state.font_size = 36
    text_fragment.text_state.font = ap.text.FontRepository.find_font("Arial Bold")

    text_fragment.text_state.foreground_color = ap.Color()
    text_fragment.text_state.foreground_color.pattern_color_space = (
        ap.drawing.GradientAxialShading(ap.Color.red, ap.Color.blue)
    )
    text_fragment.text_state.underline = True

    page.paragraphs.add(text_fragment)
    document.save(output_file_name)
```

### 在 PDF 中对文本应用径向渐变

径向渐变在文本中心向外辐射，形成圆形的颜色过渡，为标题、页眉或装饰元素提供一种视觉上动态的样式选项。

1. 初始化一个新文档并添加一个空白页。
1. 创建并样式化文本片段。添加标题，设置位置、字体和大小。
1. 使用 'GradientRadialShading' 应用径向渐变。使用 GradientRadialShading 将前景颜色设置为从红色到蓝色。
1. 添加下划线样式。
1. 将样式化的文本片段插入页面。
1. 保存文档。

```python
import math
import sys
import os
import aspose.pdf as ap

def apply_gradient_radial_shading_to_text(output_file_name):
    # Create PDF document
    document = ap.Document()
    page = document.pages.add()

    text_fragment = ap.text.TextFragment("PDF TITLE")
    text_fragment.position = ap.text.Position(100, 600)
    text_fragment.text_state.font_size = 36
    text_fragment.text_state.font = ap.text.FontRepository.find_font("Arial Bold")

    # Apply radial gradient shading (red to blue)
    text_fragment.text_state.foreground_color = ap.Color()
    text_fragment.text_state.foreground_color.pattern_color_space = (
        ap.drawing.GradientRadialShading(ap.Color.red, ap.Color.blue)
    )
    text_fragment.text_state.underline = True

    page.paragraphs.add(text_fragment)
    document.save(output_file_name)
```

![应用径向渐变着色](gradient_radial_shading.png)

## HTML 和 LaTeX 片段

### 在 PDF 文档中添加 HTML 文本

Aspose.PDF for Python via .NET 库允许您使用 HtmlFragment 类将 HTML 格式的内容插入 PDF 文档。通过使用 HTML 标记，您可以直接在 PDF 中呈现带样式、结构化或类似公式的文本。

1. 使用 'Document()' 创建新文档和页面，并使用 'document.pages.add()' 添加空白页。
1. 创建 HtmlFragment 类的实例，并将您的 HTML 字符串作为参数传入。
1. 使用 'page.paragraphs.add()' 将片段添加到页面，以插入 HTML 内容。
1. 保存 PDF。

```python
import math
import sys
import os
import aspose.pdf as ap

def add_text_html_fragment(output_file_name):
    # Create a new document
    document = ap.Document()
    page = document.pages.add()

    # Add a text fragment at a specific position
    text_fragment = ap.HtmlFragment("<pre>S=a<sub>2n</sub>+a<sup>2</sup><pre>")

    page.paragraphs.add(text_fragment)
    document.save(output_file_name)
```

![向 PDF 文档添加 HTML 文本](html_fragment.png)

### 向 PDF 文档添加带有各种格式的样式化 HTML 片段

我们可以定义一个 HTML 片段，并直接使用 HTML 标签设置文本样式。将带样式的 HTML 内容嵌入 PDF 文档中。此代码片段创建一个新的 PDF 文件，添加一个页面，插入包含各种格式元素（标题、段落、链接和内联样式）的 HTML 片段，并将结果保存到指定路径。

1. 初始化一个新的 Document 对象来表示 PDF。
1. 在文档中追加一个空白页，HTML 内容将放置在该页上。
1. 准备 HTML 内容。HTML 字符串包含一个 h1 标题，一个绿色段落，其中包含粗体、斜体和下划线文本，以及一个字体增大的指向网站的超链接。
1. 创建 HTML 片段。将 HTML 字符串包装在 HtmlFragment 对象中。
1. 将 HTML 插入页面。将 HTML 片段添加到页面的段落集合中，将 HTML 渲染为原生 PDF 内容。
1. 保存文档。

```python
import math
import sys
import os
import aspose.pdf as ap

def add_html_fragment(output_file_name):
    document = ap.Document()
    page = document.pages.add()
    html_content = """
        <h1 style='color:blue;'>Hello, Aspose!</h1>
        <p>This is a sample paragraph with <b>bold</b>, <i>italic</i>, and <u>underlined</u> text.</p>
        <p style='color:green;'>This paragraph is green.</p>
        <a href='https://www.aspose.com' style='font-size:16px;'>Visit Aspose</a>
    """
    html_fragment = ap.HtmlFragment(html_content)
    page.paragraphs.add(html_fragment)
    document.save(output_file_name)
```

![向 PDF 文档添加 HTML 内容](html_content.png)

### 添加带有覆盖文本状态的 HTML Fragment

正如我们在前面的示例中看到的，可以直接在HTML代码中设置样式。这有其优势，但也有一些缺点。假设我们正在处理客户的HTML，并希望统一我们输出的外观。
在这种情况下，我们可以通过使用自己的 TextState 来覆盖客户的样式，如下例所示。

1. 使用 'Document()' 创建新文档和页面，并使用 'document.pages.add()' 添加空白页。
1. 准备 HTML 内容。HTML 字符串包含一个使用 Verdana 字体的 h1 标题，一个绿色段落，其中包含加粗、斜体和下划线文本，以及一个字体更大的指向网站的超链接。
1. 创建 HTML 片段。将 HTML 字符串包装在 HtmlFragment 对象中。
1. 覆盖文本格式。创建一个 TextState 对象并设置 Font、Font Size 和 Text Color。
1. 将 HTML 片段添加到页面的段落集合中。
1. 保存文档。

```python
import math
import sys
import os
import aspose.pdf as ap

def add_html_fragment_override_text_state(output_file_name):
    document = ap.Document()
    page = document.pages.add()
    html_content = """
        <h1 style='color:blue;font-family:Verdana'>Hello, Aspose!</h1>
        <p>This is a sample paragraph with <b>bold</b>, <i>italic</i>, and <u>underlined</u> text.</p>
        <p style='color:green;'>This paragraph is green.</p>
        <a href='https://www.aspose.com' style='font-size:16px;'>Visit Aspose</a>
    """
    html_fragment = ap.HtmlFragment(html_content)
    html_fragment.text_state = ap.text.TextState()
    html_fragment.text_state.font = ap.text.FontRepository.find_font("Arial")
    html_fragment.text_state.font_size = 14
    html_fragment.text_state.foreground_color = ap.Color.red

    page.paragraphs.add(html_fragment)
    document.save(output_file_name)
```

![添加 HTML 片段覆盖文本状态](html_override.png)

### 向 PDF 文档添加 LaTeX 文本

使用 Aspose.PDF for Python via .NET 中的 TeXFragment 类向 PDF 文档添加 LaTeX 格式的数学表达式。
LaTeX 是一个功能强大的排版系统，广泛用于创建科学和数学文档。通过使用 TeXFragment，您可以直接在 PDF 页面中渲染 LaTeX 数学记号和符号。

1. 使用 'Document()' 创建新文档和页面，并使用 'document.pages.add()' 添加空白页。
1. 使用 TeXFragment 类直接渲染 LaTeX 语法。
1. 使用 'page.paragraphs.add()' 将 LaTeX 内容添加到 PDF 布局中。
1. 保存 PDF。

```python
import math
import sys
import os
import aspose.pdf as ap

def add_text_latex_fragment(output_file_name):
    # Create a new document
    document = ap.Document()
    page = document.pages.add()

    # Add a text fragment at a specific position
    text_fragment = ap.TeXFragment(
        "\\underbrace{\\overbrace{a+b}^6 \\cdot \\overbrace{c+d}^7}_\\text{example of text} = 42"
    )

    page.paragraphs.add(text_fragment)
    document.save(output_file_name)
```

![复杂的数学表达式显示在 PDF 中，展示了 LaTeX 公式，对 (a+b)⁶ 使用了 overbrace（上括号）标记，对整个表达式 (a+b)⁶ · (c+d)⁷ 使用了 underbrace（下括号）标记，标记为文本示例，并等于 42。该公式展示了高级数学排版，具备 LaTeX 渲染的适当间距和括号样式。](latex_fragment.png)

## 自定义字体

### 使用文件中的自定义字体

此示例演示如何使用 Aspose.PDF for Python via .NET 中的自定义 OpenType 字体向 PDF 文件添加文本。它展示了如何创建新 PDF 文档、在页面上精确定位文本以及应用自定义格式，如字体类型、大小、颜色和斜体样式。

1. 创建一个新的 PDF 文档并添加一个页面。
1. 定义您想要添加到 PDF 的文本内容。
1. 设置文本的位置。
1. 将 TextFragment 添加到页面。
1. 保存 PDF 文档。

此函数不仅适用于 OTF，还适用于 TTF 字体。

```python
import math
import sys
import os
import aspose.pdf as ap

def use_custom_font_from_file(output_file_name):
    font_path = os.path.join(FONT_DIR, "BriosoPro Italic.otf")
    document = ap.Document()
    page = document.pages.add()

    fragment = ap.text.TextFragment("Hello, Aspose!")
    fragment.position = ap.text.Position(100, 600)
    fragment.text_state.font = ap.text.FontRepository.open_font(font_path)
    fragment.text_state.font_size = 24
    fragment.text_state.foreground_color = ap.Color.blue
    fragment.text_state.font_style = ap.text.FontStyles.ITALIC

    page.paragraphs.add(fragment)
    document.save(output_file_name)
```

![在 PDF 文档中显示的文本片段，展示 Hello, Aspose! 使用蓝色斜体 BriosoPro 字体渲染，演示了自定义 OpenType 字体集成和 PDF 文本格式化中的样式功能。](custom_font.png)

### 使用来自流的自定义 Font

此代码片段演示了如何使用 Aspose.PDF for Python via .NET，通过自定义嵌入的 OpenType (OTF) 字体向 PDF 文档添加文本。它展示了如何将字体文件以流的形式打开，将其嵌入 PDF，以确保在不同系统中字体可用，并应用诸如字体大小、颜色和斜体样式等文本格式。此方法非常适合创建视觉一致的 PDF，即使在未安装该字体的设备上共享或查看时，也能保持排版效果。

1. 将字体文件加载为二进制流。
1. 使用 'FontRepository.open_font' 打开并嵌入字体。
1. 创建一个新的 PDF 文档并添加一个页面。
1. 添加带样式的文本片段：
    - 嵌入的自定义字体。
    - 斜体样式和蓝色。
    - 特定的字体大小和位置。
1. 将最终文档保存到指定的输出路径。

```python
import math
import sys
import os
import aspose.pdf as ap

def use_custom_font_from_stream(output_file_name):
    font_path = os.path.join(FONT_DIR, "BriosoPro Italic.otf")
    with open(font_path, "rb") as font_stream:
        font = ap.text.FontRepository.open_font(font_stream, ap.text.FontTypes.OTF)
        font.is_embedded = True

        document = ap.Document()
        page = document.pages.add()

        fragment = ap.text.TextFragment("Hello, Aspose!")
        fragment.position = ap.text.Position(100, 600)
        fragment.text_state.font = font
        fragment.text_state.font_size = 14
        fragment.text_state.foreground_color = ap.Color.blue
        fragment.text_state.font_style = ap.text.FontStyles.ITALIC

        page.paragraphs.add(fragment)
        document.save(output_file_name)
```

嵌入字体可确保跨平台的一致渲染，使此方法非常适合品牌塑造、设计保真度以及多语言支持。

## 相关文本主题

- [使用 Python 在 PDF 中处理文本](/pdf/zh/python-net/working-with-text/)
- [在 Python 中格式化 PDF 文本](/pdf/zh/python-net/text-formatting-inside-pdf/)
- [通过 Python 替换 PDF 中的文本](/pdf/zh/python-net/replace-text-in-pdf/)
- [在 Python 中搜索并提取 PDF 文本](/pdf/zh/python-net/search-and-get-text-from-pdf/)