---
title: 通过 Python 替换 PDF 中的文本
linktitle: 替换 PDF 中的文本
type: docs
weight: 40
url: /zh/python-net/replace-text-in-pdf/
description: 了解使用 Aspose.PDF for Python via .NET 库替换和删除文本的各种方法。
lastmod: "2025-10-13"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
aliases: 
    - /python-net/replace-text-in-a-pdf-document/
TechArticle: true
AlternativeHeadline: 如何使用 Python 替换 PDF 中的文本
Abstract: 本文提供了一份全面指南，介绍了使用 Aspose.PDF for Python via .NET 在 PDF 文档中进行各种文本操作的技术。内容涵盖了多种文本替换策略，包括在所有页面中替换文本、在特定页面区域内替换以及使用正则表达式进行替换。文章还说明了如何在 PDF 中替换字体，确保删除未使用的字体，以及如何管理文本替换以自动重新排列页面内容。此外，还深入探讨了在 PDF 创建过程中渲染可替换符号，包括在页眉/页脚区域的使用，以提升文档定制化。最后，详细介绍了从 PDF 文档中删除所有文本的方法，以在需要完全删除文本的场景中优化操作。每个章节均配有 Python 及其他支持语言的代码示例，以展示实际实现。
---

这些示例演示了如何 **修改或删除现有 PDF 中的文本**。

## 替换已有文本

### 替换 PDF 文档所有页面中的文本

{{% alert color="primary" %}}

您可以尝试使用 Aspose.PDF 在文档中查找并替换文本，并通过此 [链接](https://products.aspose.app/pdf/redaction) 在线获取结果

{{% /alert %}}

在更新或纠正现有 PDF 文档的内容时，文本替换是一项常见需求——例如，更改产品名称、修正拼写错误或在多个页面中更新术语。

Aspose.PDF for Python via .NET 提供了一种强大且高效的方法，可通过 [TextFragmentAbsorber](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragmentabsorber/) 类以编程方式搜索和替换文本。

本示例演示了如何在整个 PDF 文档中查找特定短语（本例中为“Black cat”）的所有出现，并将其替换为新短语（“White dog”）。

1. 指定搜索和替换短语。设置要查找的文本以及要替换成的文本。
1. 加载 PDF 文档。
1. 创建文本吸收器。使用搜索短语初始化 TextFragmentAbsorber。它会扫描文档中该短语的所有实例。
1. 将吸收器应用于所有页面。遍历所有页面并收集匹配该短语的文本片段。
1. 替换每个找到的片段。所有“Black cat”的实例都应更改为“White dog”。
1. 保存更新后的 PDF。

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def replace_text_on_all_pages(infile, outfile):
    """
    Replace text on all pages of a PDF document.

    Searches for a specific text phrase throughout all pages of a PDF document
    and replaces all occurrences with a new phrase. This function demonstrates
    global text replacement using TextFragmentAbsorber.

    Args:
        infile (str): Path to the input PDF file to process.
        outfile (str): Path where the modified PDF will be saved.

    Returns:
        None: The function modifies the PDF and saves it to the output path.

    Note:
        - Replaces "Black cat" with "White dog" as demonstration
        - Searches across all pages in the document
        - Preserves original formatting and layout
        - Uses TextFragmentAbsorber for efficient text search

    Example:
        >>> replace_text_on_all_pages("input.pdf", "output.pdf")
        # Replaces all instances of "Black cat" with "White dog"
    """
    search_phrase = "Black cat"
    replace_phrase = "White dog"

    with ap.Document(infile) as document:
        absorber = ap.text.TextFragmentAbsorber(search_phrase)
        document.pages.accept(absorber)

        for fragment in absorber.text_fragments:
            fragment.text = replace_phrase

        document.save(outfile)
```

### 在特定页面区域替换文本

有时，您可能只需要在 PDF 页面特定区域内替换文本，而不是搜索整个文档——例如，更新已知位置的页眉、页脚或表格单元格。

Aspose.PDF for Python via .NET 库通过结合使用基于区域的文本搜索和 [TextFragmentAbsorber](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragmentabsorber/) 实现了此功能。

本示例演示了如何在特定页面的定义矩形区域内查找并替换目标短语的所有出现。

1. 指定搜索和替换短语。
1. 加载 PDF 文档。
1. 创建用于搜索的文本吸收器。初始化 TextFragmentAbsorber 以查找所需的文本。
1. 限制搜索区域。矩形定义了页面上的 x 和 y 坐标范围。
1. 将吸收器应用于特定页面。在指定区域内执行搜索并收集匹配的文本片段。
1. 替换找到的文本。定义区域内的每个 'doc' 都将变为 'DOC'。
1. 保存更新后的 PDF。

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def replace_text_in_particular_page_region(infile, outfile):
    """
    Replace text in a particular region of a page.

    Performs targeted text replacement within a specific rectangular region
    on the first page of a PDF document. This allows for precise control
    over which text gets replaced based on its location.

    Args:
        infile (str): Path to the input PDF file to process.
        outfile (str): Path where the modified PDF will be saved.

    Returns:
        None: The function modifies the PDF and saves it to the output path.

    Note:
        - Replaces "doc" with "DOC" within the specified region
        - Only affects text within coordinates (300, 442, 500, 742)
        - Uses limit_to_page_bounds for precise region control
        - Only processes the first page (pages[1])

    Example:
        >>> replace_text_in_particular_page_region("input.pdf", "output.pdf")
        # Replaces "doc" with "DOC" only in the specified rectangular area
    """
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

### 在不更改字体大小的情况下调整大小和移动文本

在 PDF 中替换文本时，有时您希望在不更改字体大小的情况下，将新文本适配或重新定位到特定区域。
Aspose.PDF for Python via .NET 提供了在保持原始字体大小不变的情况下调整文本布局和间距的选项。

1. 加载 PDF 文档。
1. 使用 'TextFragmentAbsorber' 收集页面上的所有文本片段。
1. 选择要修改的片段。
1. 移动并调整文本矩形的大小。
1. 调整文本间距。启用间距调整以使文本适应修改后的矩形。
1. 替换片段文本。
1. 保存更新后的 PDF。

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def replace_text_and_resize_and_shift_without_changing_font_size(infile, outfile):
    """
    Resize and shift text without changing the font size.

    Demonstrates how to replace text content while adjusting its position
    and width within a modified rectangular area. The font size remains
    unchanged, but spacing is adjusted to fit the new content.

    Args:
        infile (str): Path to the input PDF file to process.
        outfile (str): Path where the modified PDF will be saved.

    Returns:
        None: The function modifies the PDF and saves it to the output path.

    Note:
        - Targets the second text fragment on the first page
        - Narrows the text rectangle by 50 units on each side
        - Duplicates the original text content
        - Uses ADJUST_SPACE_WIDTH for proper spacing
        - Maintains original font size and style

    Example:
        >>> replace_text_and_resize_and_shift_without_changing_font_size("input.pdf", "output.pdf")
        # Duplicates text in a narrower space with adjusted spacing
    """
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

### 在 PDF 中调整段落大小和位置

在处理 PDF 时，有时需要替换或扩展段落，同时保持其在页面布局中的视觉对齐。Aspose.PDF 允许您调整段落的边界矩形并修改间距以适应新文本，且无需更改字体大小。

1. 加载 PDF 文档。
1. 使用 “TextFragmentAbsorber” 收集页面上的所有文本片段。
1. 选择要修改的片段。
1. 调整段落大小并移动位置。使用页面的媒体框确定边界并调整矩形。
1. 调整间距。这会修改单词/字母之间的间距，而不是改变字体大小。
1. 替换片段文本。
1. 保存修改后的 PDF。

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def replace_text_and_resize_and_shift_paragraph(infile, outfile):
    """
    Resize and shift a paragraph in the document.

    Demonstrates paragraph-level text replacement with automatic resizing
    to fit within the page's media box boundaries. Adjusts the text area
    to provide margins while duplicating content.

    Args:
        infile (str): Path to the input PDF file to process.
        outfile (str): Path where the modified PDF will be saved.

    Returns:
        None: The function modifies the PDF and saves it to the output path.

    Note:
        - Uses page media box as base rectangle
        - Adds 20-unit margins on left, right, and top
        - Targets the second text fragment on the first page
        - Duplicates original text content
        - Automatically adjusts space width for proper fit

    Example:
        >>> replace_text_and_resize_and_shift_paragraph("input.pdf", "output.pdf")
        # Resizes paragraph to fit within page margins with duplicated text
    """
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

### 替换文本并自动扩大字体以填满目标区域

在 PDF 中替换文本，同时自动调整和扩展字体以填满特定矩形区域。使用 Aspose.PDF for Python via .NET 库，代码会动态调整字体大小和间距，使新文本内容恰好适应定义的边界框——无需手动计算字体。

1. 加载 PDF。
1. 捕获文本片段。
1. 选择特定片段。
1. 定义目标矩形。
1. 启用文本调整选项。
1. 替换文本。
1. 保存文档。

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def replace_text_and_resize_and_expand_font(infile, outfile):
    """
    Resize and expand font to fill target area.

    Demonstrates automatic font scaling to fill a specified rectangular area.
    The font size is dynamically adjusted to make the text content fit
    perfectly within the defined target rectangle.

    Args:
        infile (str): Path to the input PDF file to process.
        outfile (str): Path where the modified PDF will be saved.

    Returns:
        None: The function modifies the PDF and saves it to the output path.

    Note:
        - Defines target rectangle at coordinates (100, 300, 512, 692)
        - Uses SCALE_TO_FILL for automatic font size adjustment
        - Duplicates original text content
        - Adjusts space width for optimal text distribution
        - Font size scales up or down to fill the entire rectangle

    Example:
        >>> replace_text_and_resize_and_expand_font("input.pdf", "output.pdf")
        # Scales font to completely fill the specified rectangular area
    """
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

在 PDF 文档中替换文本，同时确保新内容在原始文本的矩形区域内适配，必要时自动缩小字体大小。

使用 Aspose.PDF for Python via .NET 库，此功能会动态调整文本布局和字体大小，保持文档结构并防止溢出。

1. 创建一个 TextFragmentAbsorber 对象，以提取第一页的所有文本片段。
1. 访问特定文本片段。
1. 设置替换区域。
1. 配置文本调整选项。设置两个关键替换选项：
- 字体大小调整 - “SHRINK_TO_FIT” 在新文本过长时自动缩小字体大小。
- 间距调整 - “ADJUST_SPACE_WIDTH” 保持间距比例。
1. 替换文本。
1. 保存修改后的 PDF。

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def replace_text_and_fit_text_into_rectangle(infile, outfile):
    """
    Fit text into a rectangle by adjusting font size.

    Demonstrates how to ensure text content fits within its original
    rectangle by automatically shrinking the font size when the new
    content is longer than the original.

    Args:
        infile (str): Path to the input PDF file to process.
        outfile (str): Path where the modified PDF will be saved.

    Returns:
        None: The function modifies the PDF and saves it to the output path.

    Note:
        - Uses original text fragment rectangle as target area
        - Employs SHRINK_TO_FIT to reduce font size if needed
        - Duplicates original text content (making it longer)
        - Adjusts space width for proper text distribution
        - Prevents text overflow by automatic font scaling

    Example:
        >>> replace_text_and_fit_text_into_rectangle("input.pdf", "output.pdf")
        # Shrinks font size to fit doubled text content in original space
    """
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

### 自动替换占位符文本并重新布局 PDF

将 PDF 中的占位符文本（例如模板或表单）替换为实际数据，如姓名或公司信息。
它会自动调整页面布局以适应新文本，并应用自定义格式（字体、颜色、大小）。

1. 导入并加载 PDF。
1. 为占位符创建文本吸收器。
1. 将吸收器应用于所有页面。
1. 遍历找到的文本片段。
1. 应用自定义文本格式。
1. 保存更新后的文档。

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def automatically_rearrange_page_contents(input_file, output_file):
    """
    Replace placeholder text in PDF with actual content.

    Demonstrates how to replace long placeholder text with actual content
    and automatically rearrange page layout. Shows dynamic content replacement
    with custom formatting applied to the new text.

    Args:
        input_file (str): Path to the input PDF file containing placeholders.
        output_file (str): Path where the modified PDF will be saved.

    Returns:
        None: The function modifies the PDF and saves it to the output path.

    Note:
        - Searches for "[Long_placeholder_Long_placeholder]" placeholders
        - Replaces with either "John Smith" or extended version with studio info
        - Applies Calibri font, size 12, navy blue color
        - Automatically adjusts page layout to accommodate content changes
        - Demonstrates real-world template filling scenarios

    Example:
        >>> automatically_rearrange_page_contents("template.pdf", "filled.pdf")
        # Replaces placeholders with formatted actual content
    """
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

### 基于正则表达式替换文本

在处理 PDF 文档时，您可能需要替换符合模式的文本，而不是特定短语——例如电话号码、代码或类似日期的格式。

Aspose.PDF for Python via .NET 允许您使用 TextFragmentAbsorber 类结合正则表达式（regex）进行此类替换。

此示例演示如何查找符合特定格式（例如 ####-####，如 1234-5678）的文本模式，并将其替换为格式化字符串 “ABC1-2XZY”。它还展示了如何自定义替换后文本的字体、颜色和大小。

以下代码片段展示了如何基于正则表达式替换文本。

1. 加载 PDF 文档。
1. 创建基于正则表达式的文本吸收器。使用正则表达式模式初始化 TextFragmentAbsorber。
1. 启用正则表达式模式。参数 “True” 激活正则表达式搜索模式。
1. 将吸收器应用于页面。这会扫描页面中所有匹配定义正则表达式模式的文本片段。
1. 用新文本替换每个匹配项并应用自定义样式。
1. 保存修改后的文档。

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def replace_text_based_on_regex(infile, outfile):
    """
    Replace text based on a regular expression pattern.

    Demonstrates pattern-based text replacement using regular expressions
    to find and replace text that matches specific formats. Also shows
    how to apply formatting changes to the replaced text.

    Args:
        infile (str): Path to the input PDF file to process.
        outfile (str): Path where the modified PDF will be saved.

    Returns:
        None: The function modifies the PDF and saves it to the output path.

    Note:
        - Uses regex pattern r"\\d{4}-\\d{4}" to find 4-digit-4-digit patterns
        - Replaces matched patterns with "ABC1-2XZY"
        - Applies custom formatting: Verdana font, size 12, blue text
        - Sets light green background color for replaced text
        - Enables regex mode with TextSearchOptions(True)

    Example:
        >>> replace_text_based_on_regex("input.pdf", "output.pdf")
        # Replaces patterns like "1234-5678" with formatted "ABC1-2XZY"
    """
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

## 替换字体或移除未使用的字体

### 替换现有 PDF 文件中的字体

有时，您需要在 PDF 中统一或更新字体，例如将过时或专有的字体替换为更易获取的字体。Aspose.PDF for Python via .NET 库允许您通过编程方式检测并替换字体，确保排版一致性和文档兼容性。

本示例演示如何在整个 PDF 文档中将特定字体的所有实例（例如 'Arial-BoldMT'）替换为另一种字体（例如 'Verdana'）。

以下代码片段展示了如何在 PDF 文档中替换字体：

1. 打开 PDF 文档。
1. 初始化 TextFragmentAbsorber。
1. 使用吸收器从文档的每一页提取文本片段。
1. 识别并替换字体。脚本检查片段的当前字体是否为 'Arial-BoldMT'。如果是，则使用 FontRepository.find_font() 方法将其替换为 'Verdana' 字体。
1. 保存修改后的文档。

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def replace_fonts(infile, outfile):
    """
    Replace specific fonts in a PDF document.

    Demonstrates how to find and replace specific fonts throughout a PDF
    document. Searches for text using a particular font and changes it
    to a different font while preserving the text content.

    Args:
        infile (str): Path to the input PDF file to process.
        outfile (str): Path where the modified PDF will be saved.

    Returns:
        None: The function modifies the PDF and saves it to the output path.

    Note:
        - Searches for text using "Arial-BoldMT" font
        - Replaces font with "Verdana" while keeping text content
        - Processes all text fragments across all pages
        - Maintains original text size and formatting properties
        - Useful for font standardization across documents

    Example:
        >>> replace_fonts("input.pdf", "output.pdf")
        # Changes all Arial-BoldMT text to use Verdana font instead
    """
    with ap.Document(infile) as document:
        absorber = ap.text.TextFragmentAbsorber()
        document.pages.accept(absorber)

        for fragment in absorber.text_fragments:
            if fragment.text_state.font.font_name == "Arial-BoldMT":
                fragment.text_state.font = ap.text.FontRepository.find_font("Verdana")

        document.save(outfile)
```

### 删除未使用的字体

随着时间的推移，PDF 文档可能会累积未使用或嵌入的字体，这会增加文件大小并降低处理速度。这些未使用的字体即使在文本编辑或替换后仍然存在，尤其是在处理大型或复杂 PDF 时。

Aspose.PDF for Python via .NET 库提供了一种使用 TextEditOptions 类高效删除此类冗余字体的方法。这不仅优化了文档，还确保仅使用实际应用于可见文本的字体。

'remove_unused_fonts()' 方法是一种通过删除冗余字体数据来优化 PDF 文件的简便而强大的方式。

本示例演示如何：

- 扫描 PDF 中未使用的字体。
- 安全地删除它们。
- 将活动文本片段重新分配为统一的字体（例如 Times New Roman）。

1. 打开 PDF 文档。
1. 配置文本编辑选项。此操作指示引擎消除任何未在可见文本中使用的嵌入字体。
1. 使用选项创建 Text Absorber。TextFragmentAbsorber 从文档中提取文本片段以供编辑。
1. 重新分配标准字体。吸收器收集所有片段后，遍历它们并应用统一的字体。
1. 保存清理后的 PDF。

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def remove_unused_fonts(input_file, output_file):
    """
    Remove unused fonts from a PDF document.

    Optimizes PDF file size by removing fonts that are embedded but not
    actually used in the document. Also demonstrates how to standardize
    all text to use a specific font family.

    Args:
        input_file (str): Path to the input PDF file to optimize.
        output_file (str): Path where the optimized PDF will be saved.

    Returns:
        None: The function modifies the PDF and saves it to the output path.

    Note:
        - Uses REMOVE_UNUSED_FONTS option for optimization
        - Changes all text to use TimesNewRoman font
        - Processes all text fragments across the document
        - Reduces file size by eliminating unnecessary font data
        - Useful for PDF optimization and standardization

    Example:
        >>> remove_unused_fonts("input.pdf", "optimized.pdf")
        # Removes unused fonts and standardizes text to TimesNewRoman
    """

    # Open PDF document
    document = ap.Document(input_file)

    # Initialize text edit options to remove unused fonts
    options = ap.text.TextEditOptions(ap.text.TextEditOptions.FontReplace.REMOVE_UNUSED_FONTS)

    # Create a TextFragmentAbsorber with the specified options
    absorber = ap.text.TextFragmentAbsorber(options)
    document.pages.accept(absorber)

    # Iterate through all TextFragments
    for text_fragment in absorber.text_fragments:
        text_fragment.text_state.font = ap.text.FontRepository.find_font("TimesNewRoman")

    # Save the updated PDF document
    document.save(output_file)
```

## 删除所有文本

### 从 PDF 中删除文本

在保持图像、形状和布局结构完整的情况下，删除 PDF 文件中的所有文本内容。
通过使用 TextFragmentAbsorber，代码能够高效扫描整个文档并删除每页上找到的所有文本片段。

1. 加载 PDF 文档。
1. 创建 TextFragmentAbsorber 对象以检测和处理 PDF 中的文本片段。
1. 删除所有文本内容。方法 'absorber.remove_all_text()' 会删除加载文档中的每个文本元素，保持非文本组件不受影响。
1. 保存更新后的文档。

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def remove_all_text_using_absorber1(infile, outfile):
    """
    Remove all text from a PDF using TextFragmentAbsorber.

    Demonstrates complete text removal from an entire PDF document,
    leaving only non-text elements like images, shapes, and layout
    structures intact.

    Args:
        infile (str): Path to the input PDF file to process.
        outfile (str): Path where the text-free PDF will be saved.

    Returns:
        None: The function modifies the PDF and saves it to the output path.

    Note:
        - Removes all text content from the entire document
        - Preserves images, graphics, and page structure
        - Uses document-level text removal for complete cleanup
        - Useful for creating templates or removing sensitive text
        - Maintains page layout and non-text elements

    Example:
        >>> remove_all_text_using_absorber1("input.pdf", "no_text.pdf")
        # Creates a PDF with all text removed but graphics preserved
    """
    with ap.Document(infile) as document:
        absorber = ap.text.TextFragmentAbsorber()
        absorber.remove_all_text(document)
        document.save(outfile)
```

### 从特定页面删除所有文本

使用 Aspose.PDF 中的 TextFragmentAbsorber 类，从 PDF 文档的单个页面删除所有文本。
不同于整篇文档的删除，此方法执行页面级别的文本清理，仅删除所选页面的文本，而保持其他页面不变。

1. 加载 PDF 文件。
1. 创建 TextFragmentAbsorber 实例。
1. 删除第一页的所有文本。
1. 保存修改后的 PDF。

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def remove_all_text_using_absorber2(infile, outfile):
    """
    Remove all text from page using TextFragmentAbsorber.

    Demonstrates text removal from a specific page while leaving text
    on other pages intact. Useful for selective text cleanup or
    creating mixed-content documents.

    Args:
        infile (str): Path to the input PDF file to process.
        outfile (str): Path where the modified PDF will be saved.

    Returns:
        None: The function modifies the PDF and saves it to the output path.

    Note:
        - Removes text only from the first page (pages[1])
        - Preserves text content on all other pages
        - Maintains page structure and non-text elements
        - Useful for page-specific text removal operations
        - Images and graphics on the target page remain intact

    Example:
        >>> remove_all_text_using_absorber2("input.pdf", "first_page_clean.pdf")
        # Removes all text from first page only
    """
    with ap.Document(infile) as document:
        absorber = ap.text.TextFragmentAbsorber()
        absorber.remove_all_text(document.pages[1])
        document.save(outfile)
```

### 从 PDF 页面特定区域删除所有文本

使用 Aspose.PDF 的 TextFragmentAbsorber 从页面的特定矩形区域删除所有文本。
此方法不是清除整页，而是进行针对性的文本删除，允许精确控制页面的哪一部分受到影响。

1. 加载 PDF 文档。
1. 创建 TextFragmentAbsorber。
1. 定义目标区域（矩形）。
1. 从指定区域删除文本。
1. 保留文档的其余部分。
1. 保存修改后的 PDF。

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def remove_all_text_using_absorber3(infile, outfile):
    """
    Remove all text from particular area on PDF page using TextFragmentAbsorber.

    Demonstrates precise text removal from a specific rectangular region
    on a page. Allows for surgical text removal while preserving text
    outside the target area.

    Args:
        infile (str): Path to the input PDF file to process.
        outfile (str): Path where the modified PDF will be saved.

    Returns:
        None: The function modifies the PDF and saves it to the output path.

    Note:
        - Removes text only within rectangle (10, 200, 120, 600)
        - Targets the first page only (pages[1])
        - Preserves text outside the specified rectangle
        - Maintains all non-text elements in the region
        - Useful for removing watermarks, headers, or specific sections

    Example:
        >>> remove_all_text_using_absorber3("input.pdf", "region_clean.pdf")
        # Removes text only from the specified rectangular area
    """
    with ap.Document(infile) as document:
        absorber = ap.text.TextFragmentAbsorber()
        absorber.remove_all_text(document.pages[1], ap.Rectangle(10, 200, 120, 600))
        document.save(outfile)
```

### 从 PDF 文档中删除所有隐藏文本

使用 Aspose.PDF 的 TextFragmentAbsorber 从页面的特定矩形区域删除所有文本。
此方法不是清除整页，而是进行针对性的文本删除，允许精确控制页面的哪一部分受到影响。

1. 加载 PDF 文档。
1. 创建 TextFragmentAbsorber。
1. 定义目标区域（矩形）。
1. 删除指定区域的文本。
1. 保留文档的其余部分。
1. 保存修改后的 PDF。

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def remove_hidden_text(infile, outfile):
    """
    Remove all hidden (invisible) text from a PDF document.

    Identifies and removes text that has been marked as invisible while
    preserving all visible text content. Useful for cleaning documents
    that may contain hidden tracking text or metadata.

    Args:
        infile (str): Path to the input PDF file to process.
        outfile (str): Path where the cleaned PDF will be saved.

    Returns:
        None: The function modifies the PDF and saves it to the output path.

    Note:
        - Detects text fragments with invisible text state
        - Replaces hidden text with empty strings
        - Uses NONE replacement adjustment to prevent layout shifts
        - Preserves all visible text and document structure
        - Useful for privacy and security document cleanup

    Example:
        >>> remove_hidden_text("input.pdf", "no_hidden_text.pdf")
        # Removes all invisible text while keeping visible content intact
    """
    # Open PDF document
    with ap.Document(infile) as document:
        text_absorber = ap.text.TextFragmentAbsorber()
        # This option can be used to prevent other text fragments from moving after hidden text replacement
        text_absorber.text_replace_options = ap.text.TextReplaceOptions(ap.text.TextReplaceOptions.ReplaceAdjustment.NONE)
        document.pages.accept(text_absorber)
        # Remove hidden text
        for fragment in text_absorber.text_fragments:
            if fragment.text_state.invisible:
                fragment.text = ""
        # Save PDF document
        document.save(outfile)
```
