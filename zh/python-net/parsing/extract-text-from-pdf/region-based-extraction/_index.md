---
title: 使用 Python 的基于区域的提取
linktitle: 基于区域的提取
type: docs
weight: 20
url: /zh/python-net/region-based-extraction/
description: 本节包含使用 Aspose.PDF 在 Python 中对 PDF 文档进行基于区域提取的文章。
lastmod: "2025-11-05"
sitemap: 
    changefreq: "weekly"
    priority: 0.7
---

## 从页面的特定区域提取文本

使用 Aspose.PDF for Python 在 PDF 的特定页面上从定义的矩形区域提取文本。通过指定坐标，您可以将提取焦点放在特定区域——例如表格单元格、段落块或表单字段区域。

适用于基于区域的文本提取，例如从页眉、页脚、发票或固定布局报告中提取数据，这些文本出现在可预测的位置。

1. 打开 PDF 文档。
1. 创建 'TextAbsorber'。
1. 配置 'text_search_options' 以限制到矩形区域。
1. 在特定页面上接受吸收器。
1. 写入提取的文本。

```python

import os
import aspose.pdf as ap

def extract_text_from_region(infile, page_number, rect_coords, outfile):
    """
    Extract text from a specified rectangular region on a given page.
    Args:
        infile (str): Path to input PDF file.
        page_number (int): 1-based index of the page.
        rect_coords (tuple): (llx, lly, urx, ury) coordinates of the rectangle.
        outfile (str): Output text file path.
    """
    document = ap.Document(infile)
    try:
        absorber = ap.text.TextAbsorber()
        # Set options to restrict search to the rectangle
        absorber.text_search_options.limit_to_page_bounds = True
        llx, lly, urx, ury = rect_coords
        absorber.text_search_options.rectangle = ap.Rectangle(llx, lly, urx, ury, True)
        # Accept on the specific page
        document.pages[page_number].accept(absorber)
        extracted_text = absorber.text
        with open(outfile, "w", encoding="utf-8") as tw:
            tw.write(extracted_text)
    finally:
        document.close()
```

## 通过遍历提取段落

我们可以通过在单页或整个文档中搜索特定文本（使用“纯文本”或“正则表达式”），或获取单页、页码范围或完整文档的全部文本来获取 PDF 文档中的文本。然而，在某些情况下，您需要从 PDF 文档中提取段落或以段落形式的文本。我们实现了在 PDF 文档页面文本中搜索章节和段落的功能。我们引入了 ParagraphAbsorber 类（类似于 TextFragmentAbsorber 和 TextAbsorber），可用于从 PDF 文档中提取段落。

Aspose.PDF 库允许您读取 PDF 文件并使用 'ParagraphAbsorber' 提取每页的所有段落文本。它按页、章节和段落组织输出，并将提取的内容写入纯文本文件。这对于文本分析、归档或将结构化 PDF 内容转换为可读格式非常有用。

1. 打开 PDF 文档。
1. 实例化一个 'ParagraphAbsorber'。
1. 调用 'absorber.visit(document)' 来扫描所有页面的段落。
1. 遍历吸收器的 'page_markups' 集合。
1. 对于每个 page‑markup，遍历其 'sections'，然后遍历该章节中的每个 'paragraph'。
1. 在每个段落内，遍历 'lines'，然后遍历行中的每个 'fragment'，累加 'fragment.text'。
1. 将每个段落（包括页/章节/段落索引）写入输出文件。
1. 完成后关闭文档。

```python

import os
import aspose.pdf as ap

def extract_paragraphs_from_pdf(infile, outfile):
    """
    Extract all paragraphs from a PDF document, and write each paragraph’s text into an output file.
    Args:
        infile (str): Path to input PDF file.
        outfile (str): Path to output text file.
    """
    document = ap.Document(infile)
    try:
        absorber = ap.text.ParagraphAbsorber()
        absorber.visit(document)

        with open(outfile, "w", encoding="utf‑8") as tw:
            for page_markup in absorber.page_markups:
                for sec_idx, section in enumerate(page_markup.sections, start=1):
                    for para_idx, paragraph in enumerate(section.paragraphs, start=1):
                        # Concatenate all fragments/lines in the paragraph
                        parts = []
                        for line in paragraph.lines:
                            for fragment in line:
                                parts.append(fragment.text)
                            parts.append("\r\n")
                        paragraph_text = "".join(parts)
                        tw.write(f"Page {page_markup.number}, Section {sec_idx}, Paragraph {para_idx}:\n")
                        tw.write(paragraph_text + "\n")
    finally:
        document.close()
```

## 提取带有边界多边形渲染的段落

此代码片段从 PDF 的特定页面提取段落级别的文本和布局信息。它捕获每个段落的边界矩形和多边形坐标以及实际文本内容，并将结果写入文本文件。这对于分析文档结构、布局映射，或为可访问性和内容提取任务准备数据非常有帮助。

1. 打开 PDF 并加载文档。
1. 实例化 'ParagraphAbsorber'。
1. 调用 'absorber.visit(page)' 以处理所需的特定页面。
1. 从 'absorber.page_markups' 中获取第一个 'page_markup'。
1. 对该标记中的每个章节：
- 获取其 'rectangle'（矩形）。
1. 对章节中的每个段落：
- 获取其 'points'（多边形）。
- 通过遍历 'paragraph.lines' 并获取 'fragment.text' 来提取文本。
1. 将几何信息和文本信息写入输出文件。
1. 关闭文档。

```python

import os
import aspose.pdf as ap

def extract_paragraphs_with_geometry(infile, outfile):
    """
    Extract paragraphs and record geometry info (rectangle / polygon) for each paragraph in a PDF.
    Args:
        infile (str): Path to input PDF file.
        outfile (str): Path to output text file.
    """
    document = ap.Document(infile)
    try:
        absorber = ap.text.ParagraphAbsorber()
        absorber.visit(document.pages[1])  # Visit page 2 (pages are 1-indexed)

        page_markup = absorber.page_markups[0]
        with open(outfile, "w", encoding="utf‑8") as tw:
            for sec_idx, section in enumerate(page_markup.sections, start=1):
                tw.write(f"Section {sec_idx}: rectangle = {section.rectangle}\n")
                for para_idx, paragraph in enumerate(section.paragraphs, start=1):
                    tw.write(f"  Paragraph {para_idx}: polygon = {paragraph.points}\n")
                    # Concatenate paragraph text
                    parts = []
                    for line in paragraph.lines:
                        for fragment in line:
                            parts.append(fragment.text)
                        parts.append("\r\n")
                    tw.write("    Text: " + "".join(parts) + "\n\n")
    finally:
        document.close()
```

