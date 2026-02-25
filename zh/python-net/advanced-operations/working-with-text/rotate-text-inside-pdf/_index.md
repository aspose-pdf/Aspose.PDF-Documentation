---
title: 使用 Python 在 PDF 中旋转文本
linktitle: 在 PDF 中旋转文本
type: docs
weight: 50
url: /zh/python-net/rotate-text-inside-pdf/
description: 探索如何在 Python 中旋转 PDF 文档中的文本，以实现使用 Aspose.PDF for Python 的灵活文档格式化。
lastmod: "2025-11-13"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 如何使用 Python 在 PDF 中旋转文本
Abstract: 本文提供了使用 Aspose.PDF for Python via .NET 在 PDF 文档中旋转文本的详细指南。文中描述了利用 `TextFragment` 类的 `Rotation` 属性在不同角度下实现文本旋转，这在多种文档生成场景中非常有用。演示了创建具有指定旋转角度的文本片段并使用 `TextBuilder` 将其添加到 PDF 页面。说明了如何将旋转的文本片段追加到 `TextParagraph` 中，然后将段落添加到 PDF 页面。展示了如何直接将旋转的文本片段添加到页面的段落集合。解释了对包含多个文本片段的完整段落进行旋转。
---

使用 Aspose.PDF for Python via .NET 在 PDF 文档中旋转文本片段。它展示了如何通过组合 'TextFragment'、'TextState' 和 'TextBuilder' 类来精确控制各个文本元素的位置和旋转。通过为每个文本片段调节旋转角度，您可以创建视觉上动态的布局，例如对角线标题、垂直标签或旋转的注释。

## 使用 TextBuilder 在 PDF 中旋转文本片段

创建一个名为 rotated_fragments.pdf 的 PDF 文件，其中包含水平对齐的三个文本片段：

- 第一个文本未旋转
- 第二个文本旋转 45°
- 第三个文本旋转 90°

1. 创建一个新的 PDF 文档。
1. 插入一个新页面以容纳旋转的文本。
1. 创建第一个文本片段 - 不旋转。
1. 创建第二个文本片段 - 旋转 45°。
1. 创建第三个文本片段 - 旋转 90°。
1. 使用 TextBuilder 添加文本片段。
1. 保存文档。

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def rotate_text_inside_pdf_1(outfile):
    """
    Implement text rotation using TextFragment and TextBuilder.

    Demonstrates basic text rotation techniques by creating multiple text
    fragments with different rotation angles. Shows how to position and
    rotate individual text elements using TextBuilder for precise control.

    Args:
        outfile (str): Path where the PDF with rotated text will be saved.

    Returns:
        None: The function creates and saves a PDF file with rotated text fragments.

    Note:
        - Creates three text fragments with 0°, 45°, and 90° rotations
        - Uses Position class for precise text placement
        - Applies TimesNewRoman font with 12pt size
        - TextBuilder provides low-level control over text placement
        - Demonstrates individual fragment rotation capabilities

    Example:
        >>> rotate_text_inside_pdf_1("rotated_fragments.pdf")
        # Creates a PDF with text fragments at different rotation angles
    """

    # Create PDF document
    with ap.Document() as document:
        # Get particular page
        page = document.pages.add()
        # Create text fragment
        text_fragment_1 = ap.text.TextFragment("main text")
        text_fragment_1.position = ap.text.Position(100, 600)
        # Set text properties
        text_fragment_1.text_state.font_size = 12
        text_fragment_1.text_state.font = ap.text.FontRepository.find_font("TimesNewRoman")
        # Create rotated text fragment
        text_fragment_2 = ap.text.TextFragment("rotated text")
        text_fragment_2.position = ap.text.Position(200, 600)
        # Set text properties
        text_fragment_2.text_state.font_size = 12
        text_fragment_2.text_state.font = ap.text.FontRepository.find_font("TimesNewRoman")
        text_fragment_2.text_state.rotation = 45
        # Create rotated text fragment
        text_fragment_3 = ap.text.TextFragment("rotated text")
        text_fragment_3.position = ap.text.Position(300, 600)
        # Set text properties
        text_fragment_3.text_state.font_size = 12
        text_fragment_3.text_state.font = ap.text.FontRepository.find_font("TimesNewRoman")
        text_fragment_3.text_state.rotation = 90
        # create TextBuilder object
        builder = ap.text.TextBuilder(page)
        # Append the text fragment to the PDF page
        builder.append_text(text_fragment_1)
        builder.append_text(text_fragment_2)
        builder.append_text(text_fragment_3)

        # Save the document
        document.save(outfile)
```

## 在 PDF 段落中旋转单个文本片段

在段落内旋转单个文本片段。它展示了如何构建包含多个片段（TextFragment）的多行段落（TextParagraph），每个片段都有各自的旋转角度。此技术对于创建视觉丰富的文档非常有用，可将水平和对角线方向的文本结合起来——例如，样式化标题、图表或带注释的标签。

创建一个名为 rotated_paragraph_fragments.pdf 的 PDF，包含一个段落，三行文本分别以不同角度旋转：

- 第一行旋转 45°
- 第二行保持水平 (0°)
- 第三行旋转 -45°

1. 创建一个新的 PDF 文档。
1. 添加一个空白页面，放置旋转的文本。
1. 创建一个 TextParagraph。
1. 创建并配置第一个文本片段 - 旋转 45°。
1. 创建第二个文本片段 - 不旋转。
1. 创建第三个文本片段 - 旋转 45°。
1. 将文本片段追加到段落中。
1. 使用 TextBuilder 将段落添加到页面。
1. 保存文档。

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def rotate_text_inside_pdf_2(outfile):
    """
    Implement text rotation using TextParagraph and TextBuilder with rotated fragments.

    Demonstrates how to create multi-line paragraphs containing individually
    rotated text fragments. Shows the combination of paragraph structure
    with fragment-level rotation control.

    Args:
        outfile (str): Path where the PDF with rotated paragraph fragments will be saved.

    Returns:
        None: The function creates and saves a PDF file with a paragraph containing rotated fragments.

    Note:
        - Creates a TextParagraph containing multiple text fragments
        - Individual fragments have different rotations: 45°, 0°, and -45°
        - Uses append_line to structure fragments within the paragraph
        - Demonstrates mixed rotation within a single paragraph
        - TextBuilder handles paragraph-level placement and rendering

    Example:
        >>> rotate_text_inside_pdf_2("rotated_paragraph_fragments.pdf")
        # Creates a PDF with a paragraph containing individually rotated text fragments
    """

    # Create PDF document
    with ap.Document() as document:
        # Get particular page
        page = document.pages.add()
        paragraph = ap.text.TextParagraph()
        paragraph.position = ap.text.Position(200, 600)
        # Create text fragment
        text_fragment_1 = ap.text.TextFragment("rotated text")
        # Set text properties
        text_fragment_1.text_state.font_size = 12
        text_fragment_1.text_state.font = ap.text.FontRepository.find_font("TimesNewRoman")
        # Set rotation
        text_fragment_1.text_state.rotation = 45
        # Create text fragment
        text_fragment_2 = ap.text.TextFragment("main text")
        # Set text properties
        text_fragment_2.text_state.font_size = 12
        text_fragment_2.text_state.font = ap.text.FontRepository.find_font("TimesNewRoman")
        # Create text fragment
        text_fragment_3 = ap.text.TextFragment("another rotated text")
        # Set text properties
        text_fragment_3.text_state.font_size = 12
        text_fragment_3.text_state.font = ap.text.FontRepository.find_font("TimesNewRoman")
        # Set rotation
        text_fragment_3.text_state.rotation = -45
        # Append the text fragments to the paragraph
        paragraph.append_line(text_fragment_1)
        paragraph.append_line(text_fragment_2)
        paragraph.append_line(text_fragment_3)
        # Create TextBuilder object
        text_builder = ap.text.TextBuilder(page)
        # Append the text paragraph to the PDF page
        text_builder.append_paragraph(paragraph)

        # Save the document
        document.save(outfile)
```

## 使用页面段落在 PDF 中旋转文本

使用 Aspose.PDF for Python via .NET 在 PDF 中旋转文本的简化方法。
不同于使用 TextBuilder 或 TextParagraph 的底层方法，此方法将旋转的文本片段直接添加到页面的段落集合 (page.paragraphs) 中。它适用于只需基本文本旋转且不需要精确定位或段落结构的情况。此方式简化了布局创建，自动处理页面上的文本放置，同时仍然可以对单个文本进行旋转控制。

生成一个名为 'simple_rotated_text.pdf' 的文件，包含：

- 一个主水平文本片段，旋转 0°
- 旋转 315° 的片段
- 旋转 270° 的片段

1. 初始化一个新的 PDF 文档。
1. 创建一个页面，用于放置旋转的文本。
1. 创建第一个文本片段 - 无旋转。
1. 创建第二个文本片段 - 315° 旋转。
1. 创建第三个文本片段 - 270° 旋转。
1. 将文本片段直接添加到页面段落中。
1. 保存 PDF 文档。

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def rotate_text_inside_pdf_3(outfile):
    """
    Implement text rotation using TextFragment and Page.Paragraphs.

    Demonstrates a simplified approach to text rotation by adding rotated
    text fragments directly to the page's paragraph collection. Shows
    high-level text placement without TextBuilder complexity.

    Args:
        outfile (str): Path where the PDF with rotated text will be saved.

    Returns:
        None: The function creates and saves a PDF file with rotated text using page paragraphs.

    Note:
        - Uses Page.Paragraphs for direct text fragment addition
        - Creates fragments with 0°, 315°, and 270° rotations
        - Simpler approach compared to TextBuilder method
        - Demonstrates automatic layout with rotated text elements
        - Good for basic rotation without precise positioning needs

    Example:
        >>> rotate_text_inside_pdf_3("simple_rotated_text.pdf")
        # Creates a PDF with rotated text using the simplified page paragraphs approach
    """

    # Create PDF document
    with ap.Document() as document:
        # Get particular page
        page = document.pages.add()
        # Create text fragment
        text_fragment_1 = ap.text.TextFragment("main text")
        # Set text properties
        text_fragment_1.text_state.font_size = 12
        text_fragment_1.text_state.font = ap.text.FontRepository.find_font("TimesNewRoman")
        # Create text fragment
        text_fragment_2 = ap.text.TextFragment("rotated text")
        # Set text properties
        text_fragment_2.text_state.font_size = 12
        text_fragment_2.text_state.font = ap.text.FontRepository.find_font("TimesNewRoman")
        # Set rotation
        text_fragment_2.text_state.rotation = 315
        # Create text fragment
        text_fragment_3 = ap.text.TextFragment("rotated text")
        # Set text properties
        text_fragment_3.text_state.font_size = 12
        text_fragment_3.text_state.font = ap.text.FontRepository.find_font("TimesNewRoman")
        # Set rotation
        text_fragment_3.text_state.rotation = 270
        page.paragraphs.add(text_fragment_1)
        page.paragraphs.add(text_fragment_2)
        page.paragraphs.add(text_fragment_3)

        # Save the document
        document.save(outfile)
```

## 在 PDF 中旋转整个段落

我们的库展示了 PDF 中的高级段落级文本旋转。不同于片段级旋转（每个文本片段单独旋转），此方法将整个段落作为统一块以不同角度旋转。
每个段落包含多个样式化的文本片段，整个段落会在特定角度旋转——实现复杂且一致的布局转换。
这非常适用于艺术布局、水印或设计密集型 PDF，其中需要将整个文本章节定向到不同方向。

创建 'rotated_paragraphs.pdf'，其中包含四个完整样式且已旋转的段落：

- 每个段落以独特角度旋转（45°、135°、225° 和 315°）
- 每个段落有三行带彩色背景、下划线和统一样式的文本

1. 创建新的 PDF 文档。
1. 添加一个空白页以容纳旋转的段落。
1. 迭代创建多个段落。
1. 创建并定位段落。
1. 创建带格式的文本片段。
1. 应用文本格式。
1. 将文本片段添加到段落中。
1. 使用 TextBuilder 将段落追加到页面。
1. 对所有四个旋转重复上述步骤。
1. 保存 PDF 文档。

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def rotate_text_inside_pdf_4(outfile):
    """
    Implement whole paragraph rotation using TextParagraph and TextBuilder.

    Demonstrates advanced text rotation by rotating entire paragraphs at
    different angles. Creates multiple styled paragraphs with comprehensive
    formatting and rotates each paragraph as a complete unit.

    Args:
        outfile (str): Path where the PDF with rotated paragraphs will be saved.

    Returns:
        None: The function creates and saves a PDF file with fully rotated paragraphs.

    Note:
        - Creates 4 paragraphs rotated at 45°, 135°, 225°, and 315°
        - Each paragraph contains multiple formatted text fragments
        - Applies comprehensive styling: colors, backgrounds, underlines
        - Demonstrates paragraph-level rotation vs. fragment-level rotation
        - Shows complex multi-line content with consistent rotation
        - Uses loop to create systematic rotation pattern

    Example:
        >>> rotate_text_inside_pdf_4("rotated_paragraphs.pdf")
        # Creates a PDF with complete paragraphs rotated at different angles
    """

    # Create PDF document
    with ap.Document() as document:
        # Get particular page
        page = document.pages.add()
        for i in range(4):
            paragraph = ap.text.TextParagraph()
            paragraph.position = ap.text.Position(200, 600)
            # Specify rotation
            paragraph.rotation = i * 90 + 45
            # Create text fragment
            text_fragment_1 = ap.text.TextFragment("Paragraph Text")
            # Create text fragment
            text_fragment_1.text_state.font_size = 12
            text_fragment_1.text_state.font = ap.text.FontRepository.find_font("TimesNewRoman")
            text_fragment_1.text_state.background_color = ap.Color.light_gray
            text_fragment_1.text_state.foreground_color = ap.Color.blue
            # Create text fragment
            text_fragment_2 = ap.text.TextFragment("Second line of text")
            # Set text properties
            text_fragment_2.text_state.font_size = 12
            text_fragment_2.text_state.font = ap.text.FontRepository.find_font("TimesNewRoman")
            text_fragment_2.text_state.background_color = ap.Color.light_gray
            text_fragment_2.text_state.foreground_color = ap.Color.blue
            # Create text fragment
            text_fragment_3 = ap.text.TextFragment("And some more text...")
            # Set text properties
            text_fragment_3.text_state.font_size = 12
            text_fragment_3.text_state.font = ap.text.FontRepository.find_font("TimesNewRoman")
            text_fragment_3.text_state.background_color = ap.Color.light_gray
            text_fragment_3.text_state.foreground_color = ap.Color.blue
            text_fragment_3.text_state.underline = True
            paragraph.append_line(text_fragment_1)
            paragraph.append_line(text_fragment_2)
            paragraph.append_line(text_fragment_3)
            # Create TextBuilder object
            builder = ap.text.TextBuilder(page)
            # Append the text fragment to the PDF page
            builder.append_paragraph(paragraph)

        # Save the document
        document.save(outfile)
```
