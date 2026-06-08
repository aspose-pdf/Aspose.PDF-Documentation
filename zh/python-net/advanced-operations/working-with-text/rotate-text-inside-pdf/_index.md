---
title: 在 Python 中旋转 PDF 文本
linktitle: 旋转 PDF 内的文本
type: docs
weight: 50
url: /zh/python-net/rotate-text-inside-pdf/
description: 了解如何在 Python 中旋转 PDF 文档内的文本片段和段落。
lastmod: "2026-06-08"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 使用 Python 旋转 PDF 文档中的文本片段和段落
Abstract: 本文解释了如何使用 Aspose.PDF for Python via .NET 在 PDF 文档中旋转文本。它展示了如何在 `TextFragment` 上设置 `rotation` 属性，使用 `TextBuilder` 和 `TextParagraph` 构建旋转内容，并将旋转文本直接添加到页面段落中以适应不同的布局场景。
---

使用 Aspose.PDF for Python via .NET 在 PDF 文档中旋转文本片段。本页展示了如何通过使用来控制文本的位置和旋转。 `TextFragment`, `TextState`，和 `TextBuilder`. 通过调整旋转角度，您可以创建诸如对角线标题、垂直标签和旋转注释等布局。

## 使用 TextBuilder 在 PDF 中旋转文本片段

创建一个名为…的 PDF 文件 `rotated_fragments.pdf` 包含三个水平对齐的文本片段：

- 第一段文本未旋转
- 第二段已旋转45°
- 第三段已旋转90°

1. 创建一个新的 PDF 文档。
1. 插入一个新页面来容纳旋转的文本。
1. 创建第一个文本片段（无旋转）。
1. 创建第二个文本片段（旋转 45°）。
1. 创建第三个文本片段（旋转 90°）。
1. 使用添加文本片段 `TextBuilder`.
1. 保存文档。

```python
import aspose.pdf as ap

def rotate_text_inside_pdf_1(outfile):
    # Create PDF document
    with ap.Document() as document:
        # Get particular page
        page = document.pages.add()
        # Create text fragment
        text_fragment_1 = ap.text.TextFragment("main text")
        text_fragment_1.position = ap.text.Position(100, 600)
        # Set text properties
        text_fragment_1.text_state.font_size = 12
        text_fragment_1.text_state.font = ap.text.FontRepository.find_font(
            "TimesNewRoman"
        )
        # Create rotated text fragment
        text_fragment_2 = ap.text.TextFragment("rotated text")
        text_fragment_2.position = ap.text.Position(200, 600)
        # Set text properties
        text_fragment_2.text_state.font_size = 12
        text_fragment_2.text_state.font = ap.text.FontRepository.find_font(
            "TimesNewRoman"
        )
        text_fragment_2.text_state.rotation = 45
        # Create rotated text fragment
        text_fragment_3 = ap.text.TextFragment("rotated text")
        text_fragment_3.position = ap.text.Position(300, 600)
        # Set text properties
        text_fragment_3.text_state.font_size = 12
        text_fragment_3.text_state.font = ap.text.FontRepository.find_font(
            "TimesNewRoman"
        )
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

## 在 PDF 中旋转段落内的单个文本片段

在段落中旋转单个文本片段。它展示了如何构建包含多个片段（TextParagraph）的多行段落（TextFragment），每个片段都有自己的旋转角度。此技术可用于创建视觉丰富的文档，结合水平和对角线方向的文本——例如，样式化标题、图表或带注释的标签。

创建一个名为的 PDF `rotated_paragraph_fragments.pdf` 包含一个段落，其中有三行文本，每行的旋转角度不同：

- 第一行旋转45°
- 第二行保持水平 (0°)
- 第三行旋转-45°

1. 创建一个新的 PDF 文档。
1. 在旋转文本出现的地方添加一个空白页。
1. 创建一个 `TextParagraph`.
1. 创建并配置第一个文本片段（+45° 旋转）。
1. 创建第二个文本片段（无旋转）。
1. 创建第三个文本片段（-45° 旋转）。
1. 将文本片段附加到段落。
1. 使用以下方法将段落添加到页面 `TextBuilder`.
1. 保存文档。

```python
import aspose.pdf as ap

def rotate_text_inside_pdf_2(outfile):
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
        text_fragment_1.text_state.font = ap.text.FontRepository.find_font(
            "TimesNewRoman"
        )
        # Set rotation
        text_fragment_1.text_state.rotation = 45
        # Create text fragment
        text_fragment_2 = ap.text.TextFragment("main text")
        # Set text properties
        text_fragment_2.text_state.font_size = 12
        text_fragment_2.text_state.font = ap.text.FontRepository.find_font(
            "TimesNewRoman"
        )
        # Create text fragment
        text_fragment_3 = ap.text.TextFragment("another rotated text")
        # Set text properties
        text_fragment_3.text_state.font_size = 12
        text_fragment_3.text_state.font = ap.text.FontRepository.find_font(
            "TimesNewRoman"
        )
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

## 在 PDF 中使用页面段落旋转文本

本节演示了一种使用 Aspose.PDF for Python via .NET 在 PDF 中旋转文本的简化方法。
不同于采用低层次方法的 `TextBuilder` 或 `TextParagraph`，此方法直接将旋转的文本片段添加到页面的段落集合中（`page.paragraphs`). 当您需要基本文本旋转而不需要精确定位或段落结构时，它是理想的。

生成一个名为 `simple_rotated_text.pdf` 包含：

- 一个主要的水平文本片段，旋转角度为 0°
- 315° 旋转片段
- 270° 旋转片段

1. 初始化一个新的 PDF 文档。
1. 创建一个页面以放置旋转的文本。
1. 创建第一个文本片段（无旋转）。
1. 创建第二个文本片段（315° 旋转）。
1. 创建第三个文本片段（270° 旋转）。
1. 直接将文本片段添加到页面段落。
1. 保存 PDF 文档。

```python
import aspose.pdf as ap

def rotate_text_inside_pdf_3(outfile):
    # Create PDF document
    with ap.Document() as document:
        # Get particular page
        page = document.pages.add()
        # Create text fragment
        text_fragment_1 = ap.text.TextFragment("main text")
        # Set text properties
        text_fragment_1.text_state.font_size = 12
        text_fragment_1.text_state.font = ap.text.FontRepository.find_font(
            "TimesNewRoman"
        )
        # Create text fragment
        text_fragment_2 = ap.text.TextFragment("rotated text")
        # Set text properties
        text_fragment_2.text_state.font_size = 12
        text_fragment_2.text_state.font = ap.text.FontRepository.find_font(
            "TimesNewRoman"
        )
        # Set rotation
        text_fragment_2.text_state.rotation = 315
        # Create text fragment
        text_fragment_3 = ap.text.TextFragment("rotated text")
        # Set text properties
        text_fragment_3.text_state.font_size = 12
        text_fragment_3.text_state.font = ap.text.FontRepository.find_font(
            "TimesNewRoman"
        )
        # Set rotation
        text_fragment_3.text_state.rotation = 270
        page.paragraphs.add(text_fragment_1)
        page.paragraphs.add(text_fragment_2)
        page.paragraphs.add(text_fragment_3)

        # Save the document
        document.save(outfile)
```

## 在 PDF 中旋转整个段落

此示例演示了在 PDF 中的高级段落级文本旋转。不同于片段级旋转（每个文本片段单独旋转），此方法将整个段落作为统一块以不同角度进行旋转。
每个段落包含多个样式化的文本片段，整个段落会以特定角度旋转——从而实现复杂且一致的布局转换。
这非常适用于艺术布局、水印或设计密集的 PDF，在这些情况下，需要将整段文本以不同方向进行排版。

创建 `rotated_paragraphs.pdf`，包含四个完整样式和旋转的段落:

- 每个都以唯一的角度旋转（45°、135°、225°和315°）
- 每段包含三行文字，具有彩色背景、下划线和一致的样式

1. 创建一个新的 PDF 文档。
1. 添加一个空白页以容纳旋转的段落。
1. 迭代以创建多个段落。
1. 创建并定位段落。
1. 创建具有格式的文本片段。
1. 应用文本格式化。
1. 向段落添加文本片段。
1. 使用将段落追加到页面 `TextBuilder`.
1. 对所有四个旋转重复此操作。
1. 保存 PDF 文档。

```python
import aspose.pdf as ap

def rotate_text_inside_pdf_4(outfile):
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
            text_fragment_1.text_state.font = ap.text.FontRepository.find_font(
                "TimesNewRoman"
            )
            text_fragment_1.text_state.background_color = ap.Color.light_gray
            text_fragment_1.text_state.foreground_color = ap.Color.blue
            # Create text fragment
            text_fragment_2 = ap.text.TextFragment("Second line of text")
            # Set text properties
            text_fragment_2.text_state.font_size = 12
            text_fragment_2.text_state.font = ap.text.FontRepository.find_font(
                "TimesNewRoman"
            )
            text_fragment_2.text_state.background_color = ap.Color.light_gray
            text_fragment_2.text_state.foreground_color = ap.Color.blue
            # Create text fragment
            text_fragment_3 = ap.text.TextFragment("And some more text...")
            # Set text properties
            text_fragment_3.text_state.font_size = 12
            text_fragment_3.text_state.font = ap.text.FontRepository.find_font(
                "TimesNewRoman"
            )
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

## 相关文本主题

- [使用 Python 在 PDF 中处理文本](/pdf/zh/python-net/working-with-text/)
- [向 PDF 添加文本](/pdf/zh/python-net/add-text-to-pdf-file/)
- [在 Python 中格式化 PDF 文本](/pdf/zh/python-net/text-formatting-inside-pdf/)
- [使用 Python 替换 PDF 中的文本](/pdf/zh/python-net/replace-text-in-pdf/)