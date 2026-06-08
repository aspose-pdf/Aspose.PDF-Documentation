---
title: 使用 Python 替换 PDF 中的文本
linktitle: 替换 PDF 中的文本
type: docs
weight: 40
url: /zh/python-net/replace-text-in-pdf/
description: 学习如何使用 Python 替换 PDF 文件中的文本，包括跨页替换文本、将更改限制在页面区域内、使用正则表达式以及删除文本。
lastmod: "2026-05-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
aliases:
    - /python-net/replace-text-in-a-pdf-document/
TechArticle: true
AlternativeHeadline: 使用 Python 替换和删除 PDF 文件中的文本
Abstract: 本文展示了如何使用 Aspose.PDF for Python via .NET 替换 PDF 文档中的文本。它涵盖了跨所有页面的文本替换、页面区域替换、正则表达式匹配、字体替换、文本布局调整以及删除可见或隐藏的文本。
---

此页面展示了如何 **使用 Python 替换 PDF 中的文本**，借助 Aspose.PDF for Python via .NET。

当您需要更新文本值、删除不需要的内容、在特定页面区域替换文本，或在多个 PDF 页面上应用文本替换规则时，请使用这些示例。

## 使用 Python 替换 PDF 中的文本

### 在 PDF 文档的所有页面中替换文本

{{% alert color="primary" %}}

您可以尝试使用 Aspose.PDF 在线进行文本搜索和替换 [脱敏应用](https://products.aspose.app/pdf/redaction).

{{% /alert %}}

文本替换是在更新或纠正现有 PDF 文档内容时的常见需求——例如，更改产品名称、修正错别字，或在多个页面中更新术语。

Aspose.PDF for Python via .NET 提供了一种强大且高效的方法，可通过编程方式搜索和替换文本 [TextFragmentAbsorber](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragmentabsorber/) 类。

本示例演示如何在整个 PDF 文档中查找特定短语（在本例中为 "Black cat"）的所有出现位置，并将其替换为新的短语（"White dog"）。

1. 指定搜索和替换短语。设置您要查找的文本以及要替换为的文本。
1. 加载 PDF 文档。
1. 创建一个 Text Absorber。TextFragmentAbsorber 使用搜索短语进行初始化。它会扫描文档中所有给定短语的实例。
1. 将 Absorber 应用于所有页面。这会遍历所有页面并收集匹配该短语的文本片段。
1. 替换每个找到的片段。每个 “Black cat” 实例都应更改为 “White dog”。
1. 保存已更新的 PDF。

```python
import sys
import aspose.pdf as ap
from os import path

def replace_text_on_all_pages(infile, outfile):
    search_phrase = "PDF"
    replace_phrase = "pdf"

    with ap.Document(infile) as document:
        absorber = ap.text.TextFragmentAbsorber(search_phrase)
        document.pages.accept(absorber)

        for fragment in absorber.text_fragments:
            fragment.text = replace_phrase

        document.save(outfile)
```

### 在特定页面区域替换文本

有时，您可能需要仅在 PDF 页面的特定区域内替换文本，而不是搜索整个文档——例如，更新已知位置中的页眉、页脚或表格单元格。

Aspose.PDF for Python via .NET 库通过利用该功能来实现 [TextFragmentAbsorber](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragmentabsorber/) 与基于区域的文本搜索相结合。

本示例演示了如何在特定页面的已定义矩形区域内查找并替换目标短语的所有出现。

1. 指定搜索和替换短语。
1. 加载 PDF 文档。
1. 创建 Text Absorber 以进行搜索。初始化 TextFragmentAbsorber 来查找所需的文本。
1. 限制搜索区域。矩形指定页面上的 x 和 y 坐标限制。
1. 将 Absorber 应用于特定页面。此操作在指定区域内执行搜索并收集匹配的文本片段。
1. 替换已找到的文本。定义区域内的每个 'doc' 出现都变成 'DOC'。
1. 保存已更新的 PDF。

```python
import sys
import aspose.pdf as ap
from os import path

def replace_text_in_particular_page_region(infile, outfile):
    search_phrase = "doc"
    replace_phrase = "DOC"

    with ap.Document(infile) as document:
        absorber = ap.text.TextFragmentAbsorber(search_phrase)
        absorber.text_search_options.limit_to_page_bounds = True
        absorber.text_search_options.rectangle = ap.Rectangle(300, 442, 500, 742, True)
        document.pages[1].accept(absorber)

        for fragment in absorber.text_fragments:
            fragment.text = replace_phrase

        document.save(outfile)
```

### 在不更改字体大小的情况下调整和移动文本

在 PDF 中替换文本时，有时您希望在不修改字体大小的情况下，将新文本适配或重新定位到特定区域内。
Aspose.PDF for Python via .NET 提供了调整文本布局和间距的选项，同时保持原始字体大小不变。

1. 加载 PDF 文档。
1. 使用 'TextFragmentAbsorber' 收集页面上的所有文本片段。
1. 选择要修改的片段。
1. 移动并调整文本矩形的大小。
1. 调整文字间距。启用间距调整以使文字适应修改后的矩形。
1. 替换片段文本。
1. 保存已更新的 PDF。

```python
import sys
import aspose.pdf as ap
from os import path

def replace_text_and_resize_and_shift_without_changing_font_size(infile, outfile):
    with ap.Document(infile) as document:
        absorber = ap.text.TextFragmentAbsorber()
        absorber.visit(document.pages[1])
        fragment = absorber.text_fragments[1]
        text = fragment.text
        rect = fragment.rectangle
        rect.llx += 50
        rect.urx -= 50
        fragment.replace_options.rectangle = rect
        fragment.replace_options.replace_adjustment_action = (
            ap.text.TextReplaceOptions.ReplaceAdjustment.ADJUST_SPACE_WIDTH
        )
        fragment.text = f"{text} {text}"
        document.save(outfile)
```

### 在 PDF 中调整段落大小并移动

在处理 PDF 时，有时需要替换或扩展段落，同时保持其在页面布局中的视觉对齐。Aspose.PDF 允许您调整段落的边界矩形大小并调节间距以适应新文本，且无需更改字体大小。

1. 加载 PDF 文档。
1. 使用 'TextFragmentAbsorber' 在页面上收集所有文本片段。
1. 选择要修改的片段。
1. 调整并移动段落。使用页面的媒体框来确定边界并调整矩形。
1. 调整间距。此操作修改单词/字母之间的间距，而不是更改字体大小。
1. 替换片段文本。
1. 保存已修改的 PDF。

```python
import sys
import aspose.pdf as ap
from os import path

def replace_text_and_resize_and_shift_paragraph(infile, outfile):
    with ap.Document(infile) as document:
        absorber = ap.text.TextFragmentAbsorber()
        absorber.visit(document.pages[1])
        fragment = absorber.text_fragments[1]
        text = fragment.text
        rect = document.pages[1].media_box
        rect.llx += 20
        rect.urx -= 20
        rect.ury -= 20
        fragment.replace_options.rectangle = rect
        fragment.replace_options.replace_adjustment_action = (
            ap.text.TextReplaceOptions.ReplaceAdjustment.ADJUST_SPACE_WIDTH
        )
        fragment.text = f"{text} {text}"
        document.save(outfile)
```

### 替换文本并自动扩展字体以填满目标区域

在 PDF 中替换文本，同时自动调整大小并扩展字体以填满特定矩形区域。使用 Aspose.PDF for Python via .NET 库，代码会动态调整字体大小和间距，使新文本内容完美适配定义的边界框 — 无需手动计算字体。

1. 加载 PDF。
1. 捕获文本片段。
1. 选择特定片段。
1. 定义目标矩形。
1. 启用文本调整选项。
1. 替换文本。
1. 保存文档。

```python
import sys
import aspose.pdf as ap
from os import path

def replace_text_and_resize_and_expand_font(infile, outfile):
    with ap.Document(infile) as document:
        absorber = ap.text.TextFragmentAbsorber()
        absorber.visit(document.pages[1])
        fragment = absorber.text_fragments[1]
        text = fragment.text
        fragment.replace_options.rectangle = ap.Rectangle(100, 300, 512, 692, True)
        fragment.replace_options.replace_adjustment_action = (
            ap.text.TextReplaceOptions.ReplaceAdjustment.ADJUST_SPACE_WIDTH
        )
        fragment.replace_options.font_size_adjustment_action = (
            ap.text.TextReplaceOptions.FontSizeAdjustment.SCALE_TO_FILL
        )
        fragment.text = f"{text} {text}"
        document.save(outfile)
```

### 替换文本并将其适配到矩形中

在 PDF 文档中替换文本，同时确保新内容适配原始文本的矩形区域，必要时自动减小字体大小。

使用 Aspose.PDF for Python via .NET 库，此功能动态调整文本布局和字体大小，同时保持文档结构并防止溢出。

1. 创建一个 TextFragmentAbsorber 对象以提取第一页的所有文本片段。
1. 访问特定文本片段。
1. 设置替换区域。
1. 配置文本调整选项。设置两个关键的替换选项：
    - 字体大小调整 - 'SHRINK_TO_FIT' 在新文本过长时会自动缩小字体大小。
    - 间距调整 - 'ADJUST_SPACE_WIDTH' 保持间距比例。
1. 替换文本。
1. 保存已修改的 PDF。

```python
import sys
import aspose.pdf as ap
from os import path

def replace_text_and_fit_text_into_rectangle(infile, outfile):
    with ap.Document(infile) as document:
        absorber = ap.text.TextFragmentAbsorber()
        absorber.visit(document.pages[1])
        fragment = absorber.text_fragments[1]
        text = fragment.text
        fragment.replace_options.rectangle = fragment.rectangle
        fragment.replace_options.font_size_adjustment_action = (
            ap.text.TextReplaceOptions.FontSizeAdjustment.SHRINK_TO_FIT
        )
        fragment.replace_options.replace_adjustment_action = (
            ap.text.TextReplaceOptions.ReplaceAdjustment.ADJUST_SPACE_WIDTH
        )
        fragment.text = f"{text} {text}"
        document.save(outfile)
```

### 自动替换占位符文本并重新排列 PDF 布局

将 PDF（例如模板或表单）中的占位符文本替换为实际数据，如姓名或公司信息。
它会自动调整页面布局以适应新文本，同时应用自定义格式（字体、颜色、大小）。

1. 导入并加载 PDF。
1. 为占位符创建 Text Absorber。
1. 将 Absorber 应用于所有页面。
1. 循环遍历找到的文本片段。
1. 应用自定义文本格式。
1. 保存已更新的文档。

```python
import sys
import aspose.pdf as ap
from os import path

def automatically_rearrange_page_contents(input_file, output_file):
    document = ap.Document(input_file)

    absorber = ap.text.TextFragmentAbsorber("[Long_placeholder_Long_placeholder]")
    document.pages.accept(absorber)

    for text_fragment in absorber.text_fragments:
        # text_fragment.text = "John Smith"
        text_fragment.text = "John Smith, South Development Studio"
        text_fragment.text_state.font = ap.text.FontRepository.find_font("Calibri")
        text_fragment.text_state.font_size = 12
        text_fragment.text_state.foreground_color = ap.Color.navy

    # Save PDF document
    document.save(output_file)
```

### 根据正则表达式替换文本

在处理 PDF 文档时，您可能需要替换符合特定模式的文本，而不是特定短语——例如，电话号码、代码或类似日期的格式。

Aspose.PDF for Python via .NET 允许您使用 TextFragmentAbsorber 类结合正则表达式（regex）进行此类替换。

此示例演示如何查找文本模式（在本例中，任何匹配格式 ####-#### 的文本，例如 1234-5678），并将其替换为格式化字符串 'ABC1-2XZY'。它还展示了如何自定义替换后文本的字体、颜色和大小。

以下代码片段展示了如何基于正则表达式替换文本。

1. 加载 PDF 文档。
1. 创建一个基于正则表达式的 Text Absorber。使用正则表达式模式初始化 TextFragmentAbsorber。
1. 启用正则表达式模式。'True' 参数会激活正则表达式搜索模式。
1. 将 Absorber 应用于页面。这将在页面上扫描所有与定义的正则表达式模式匹配的文本片段。
1. 将每个匹配项替换为新文本并应用自定义样式。
1. 保存已修改的文档。

```python
import sys
import aspose.pdf as ap
from os import path

def replace_text_based_on_regex(infile, outfile):
    with ap.Document(infile) as document:
        absorber = ap.text.TextFragmentAbsorber(r"\d{4}-\d{4}")
        absorber.text_search_options = ap.text.TextSearchOptions(True)
        document.pages[1].accept(absorber)

        for fragment in absorber.text_fragments:
            fragment.text = "ABC1-2XZY"
            fragment.text_state.font = ap.text.FontRepository.find_font("Verdana")
            fragment.text_state.font_size = 12
            fragment.text_state.foreground_color = ap.Color.blue
            fragment.text_state.background_color = ap.Color.light_green

        document.save(outfile)
```

## 替换字体或删除未使用的字体

### 替换现有 PDF 文件中的字体

有时，您需要在 PDF 中统一或更新字体——例如，用更易获取的字体替换过时或专有的字体。Aspose.PDF for Python via .NET 库允许您以编程方式检测并替换字体，确保排版一致性和文档兼容性。

本示例演示如何在整个 PDF 文档中将特定字体的所有实例（例如 'Arial-BoldMT'）替换为另一种字体（例如 'Verdana'）。

以下代码片段展示了如何在 PDF 文档中替换 Font：

1. 打开 PDF 文档。
1. 初始化 TextFragmentAbsorber。
1. 使用 Absorber 从文档的每一页中提取文本片段。
1. 识别并替换字体。脚本检查片段的当前字体是否为 'Arial-BoldMT'。如果是，则使用 FontRepository.find_font() 方法将其替换为 'Verdana' 字体。
1. 保存已修改的文档。

```python
import sys
import aspose.pdf as ap
from os import path

def replace_fonts(infile, outfile):
    with ap.Document(infile) as document:
        absorber = ap.text.TextFragmentAbsorber()
        document.pages.accept(absorber)

        for fragment in absorber.text_fragments:
            if fragment.text_state.font.font_name == "Arial-BoldMT":
                fragment.text_state.font = ap.text.FontRepository.find_font("Verdana")

        document.save(outfile)
```

### 删除未使用的字体

随着时间的推移，PDF 文档可能会积累未使用或嵌入的字体，这会增加文件大小并降低处理速度。这些未使用的字体即使在进行文本编辑或替换后仍常常保留，尤其是在处理大型或复杂的 PDF 时。

Aspose.PDF for Python via .NET 库提供了一种使用 TextEditOptions 类删除此类冗余字体的高效方法。这不仅优化了您的文档，还确保仅使用实际应用于可见文本的字体。

‘remove_unused_fonts()’ 方法是一种简单但强大的方式，通过删除冗余字体数据来优化 PDF 文件。

本示例演示如何：

- 扫描 PDF 以查找未使用的字体。
- 安全地将它们移除。
- 将活动文本片段重新分配为一致的字体（例如，Times New Roman）。

1. 打开 PDF 文档。
1. 配置文本编辑选项。这指示引擎删除任何当前未在可见文本中使用的嵌入字体。
1. 创建一个带有选项的 Text Absorber。TextFragmentAbsorber 从文档中提取文本片段以进行编辑。
1. 重新分配标准字体。一旦吸收器收集了所有片段，遍历它们并应用一致的字体。
1. 保存已清理的 PDF。

```python
import sys
import aspose.pdf as ap
from os import path

def remove_unused_fonts(input_file, output_file):
    # Open PDF document
    document = ap.Document(input_file)

    # Initialize text edit options to remove unused fonts
    options = ap.text.TextEditOptions(
        ap.text.TextEditOptions.FontReplace.REMOVE_UNUSED_FONTS
    )

    # Create a TextFragmentAbsorber with the specified options
    absorber = ap.text.TextFragmentAbsorber(options)
    document.pages.accept(absorber)

    # Iterate through all TextFragments
    for text_fragment in absorber.text_fragments:
        text_fragment.text_state.font = ap.text.FontRepository.find_font(
            "TimesNewRoman"
        )

    # Save the updated PDF document
    document.save(output_file)
```

## 删除所有文本

### 从 PDF 中删除文本

从 PDF 文件中删除所有文本内容，同时保留图像、形状和布局结构完整。
通过使用 TextFragmentAbsorber，代码能够高效地扫描整个文档并删除每页上找到的所有文本片段。

1. 加载 PDF 文档。
1. 创建一个 TextFragmentAbsorber 对象以检测并处理 PDF 中的文本片段。
1. 删除所有文本内容。方法 ‘absorber.remove_all_text()’ 会从已加载的文档中移除所有文本元素，保持非文本组件不受影响。
1. 保存已更新的文档。

```python
import sys
import aspose.pdf as ap
from os import path

def remove_all_text_using_absorber1(infile, outfile):
    with ap.Document(infile) as document:
        absorber = ap.text.TextFragmentAbsorber()
        absorber.remove_all_text(document)
        document.save(outfile)
```

### 删除特定页面上的所有文本

使用 Aspose.PDF 中的 TextFragmentAbsorber 类从 PDF 文档的单页中删除所有文本。
与全文删除不同，此方法执行页面级文本清理，仅删除所选页面的文本，而保持其他所有页面不受影响。

1. 加载 PDF 文件。
1. 创建一个 TextFragmentAbsorber 实例。
1. 删除第一页的所有文本。
1. 保存已修改的 PDF。

```python
import sys
import aspose.pdf as ap
from os import path

def remove_all_text_using_absorber2(infile, outfile):
    with ap.Document(infile) as document:
        absorber = ap.text.TextFragmentAbsorber()
        absorber.remove_all_text(document.pages[1])
        document.save(outfile)
```

### 从 PDF 页面中的特定区域删除所有文本

使用 Aspose.PDF 的 TextFragmentAbsorber 从页面的特定矩形区域中删除所有文本。
此方法不是清除整页，而是执行针对性的文本删除，允许精确控制受影响的页面部分。

1. 加载 PDF 文档。
1. 创建一个 TextFragmentAbsorber。
1. 定义目标区域（矩形）。
1. 从指定区域删除文本。
1. 保留文档的其余部分。
1. 保存已修改的 PDF。

```python
import sys
import aspose.pdf as ap
from os import path

def remove_all_text_using_absorber3(infile, outfile):
    with ap.Document(infile) as document:
        absorber = ap.text.TextFragmentAbsorber()
        absorber.remove_all_text(
            document.pages[1], ap.Rectangle(10, 200, 120, 600, True)
        )
        document.save(outfile)
```

### 从 PDF 文档中移除所有隐藏的 Text

使用 Aspose.PDF 的 TextFragmentAbsorber 从页面的特定矩形区域中删除所有文本。
此方法不是清除整页，而是执行针对性的文本删除，允许精确控制受影响的页面部分。

1. 加载 PDF 文档。
1. 创建一个 TextFragmentAbsorber。
1. 定义目标区域（矩形）。
1. 从指定区域删除文本。
1. 保留文档的其余部分。
1. 保存已修改的 PDF。

```python
import sys
import aspose.pdf as ap
from os import path

def remove_hidden_text(infile, outfile):
    # Open PDF document
    with ap.Document(infile) as document:
        text_absorber = ap.text.TextFragmentAbsorber()
        # This option can be used to prevent other text fragments from moving after hidden text replacement
        text_absorber.text_replace_options = ap.text.TextReplaceOptions(
            ap.text.TextReplaceOptions.ReplaceAdjustment.NONE
        )
        document.pages.accept(text_absorber)
        # Remove hidden text
        for fragment in text_absorber.text_fragments:
            if fragment.text_state.invisible:
                fragment.text = ""
        # Save PDF document
        document.save(outfile)
```

## 相关文本主题

- [使用 Python 在 PDF 中处理文本](/pdf/zh/python-net/working-with-text/)
- [向 PDF 添加文本](/pdf/zh/python-net/add-text-to-pdf-file/)
- [在 Python 中搜索并提取 PDF 文本](/pdf/zh/python-net/search-and-get-text-from-pdf/)
- [在 Python 中格式化 PDF 文本](/pdf/zh/python-net/text-formatting-inside-pdf/)
