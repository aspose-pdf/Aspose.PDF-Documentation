---
title: 使用 Python 的基于区域的提取
linktitle: 基于区域的提取
type: docs
weight: 20
url: /zh/python-net/region-based-extraction/
description: 了解如何使用 Aspose.PDF for Python 从 PDF 文档中的特定页面区域或段落结构提取文本。
lastmod: "2026-06-08"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## 从页面的特定区域提取文本

使用 [TextAbsorber](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textabsorber/) 与 a [矩形](https://reference.aspose.com/pdf/python-net/aspose.pdf/rectangle/) 将提取限制在页面的特定区域。此方法对于从页眉、页脚、表格单元格、表单字段、发票或其他已预先知晓文本位置的固定布局区域进行基于区块的提取非常有用。

1. 打开源 PDF 作为 [文档](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. 创建一个 `TextAbsorber` 实例。
1. 配置 `text_search_options` 将提取限制在矩形内。
1. 在目标页面接受吸收器。
1. 将提取的文本写入输出文件。

```python
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

## 通过遍历它们来提取段落

使用 [ParagraphAbsorber](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/paragraphabsorber/) 当您需要段落感知的提取而不是普通的页面文本时。不同于 [TextAbsorber](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textabsorber/) 或 [TextFragmentAbsorber](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragmentabsorber/), 此 API 按页面、章节和段落组织输出，这对于文本分析、结构化导出以及布局敏感的处理非常有用。

1. 打开源 PDF 作为 [文档](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. 创建一个 `ParagraphAbsorber` 实例。
1. 调用 `absorber.visit(document)` 分析所有页面。
1. 遍历 `page_markups`，然后遍历每个章节和段落。
1. 从每个段落读取文本片段，并将结果写入文件。

```python
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

        with open(outfile, "w", encoding="utf-8") as tw:
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
                        tw.write(
                            f"Page {page_markup.number}, Section {sec_idx}, Paragraph {para_idx}:\n"
                        )
                        tw.write(paragraph_text + "\n")
    finally:
        document.close()
```

## 提取段落并呈现其边界多边形

您也可以使用 [ParagraphAbsorber](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/paragraphabsorber/) 以检查段落几何形状。除了提取文本之外，此方法还记录每个章节矩形和段落多边形，这对于布局映射、文档分析、可访问性工具或基于区域的后处理非常有用。

1. 打开源 PDF 作为 [文档](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. 创建一个 `ParagraphAbsorber` 实例。
1. 访问目标页面。
1. 读取页面标记来自 `absorber.page_markups`.
1. 遍历章节和段落以捕获几何信息和文本。
1. 将矩形、多边形和文本数据写入输出文件。

```python
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
        with open(outfile, "w", encoding="utf-8") as tw:
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
