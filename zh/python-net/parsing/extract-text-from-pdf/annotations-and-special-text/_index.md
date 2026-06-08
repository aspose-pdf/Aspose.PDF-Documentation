---
title: 使用 Python 的批注和特殊文本
linktitle: 批注和特殊文本
type: docs
weight: 40
url: /zh/python-net/annotation-and-special-text/
description: 了解如何使用 Aspose.PDF for Python 从 PDF 文档中的印章批注、突出显示的文本以及上标/下标内容中提取文本。
lastmod: "2026-06-08"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## 从印章批注中提取文本

使用 [TextAbsorber](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textabsorber) 提取嵌入的文本 [StampAnnotation](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/stampannotation) 外观流。当印章内容以表单 XObject 的形式渲染而不是以纯文本形式存储时，这非常有用。

1. 打开 [文档](https://reference.aspose.com/pdf/python-net/aspose.pdf/document).
1. 访问目标注释 `page.annotations`.
1. 验证它是一个 `StampAnnotation`，然后检索其正常外观 XForm。
1. 将 XForm 传递给 `TextAbsorber.visit()` 提取嵌入的文本。

```python
import os
import aspose.pdf as ap


def extract_text_from_stamp(infile, page_number, annotation_index, outfile):
    """
    Extracts text from a stamp annotation on a given page in a PDF document.
    Args:
        infile (str): Path to the input PDF file.
        page_number (int): 1-based index of the page containing the stamp.
        annotation_index (int): 1-based index of the annotation in that page.
        outfile (str): Path to the output text file where extracted text will be saved.
    """
    document = ap.Document(infile)
    try:
        page = document.pages[page_number]
        annot = page.annotations[annotation_index]
        # Ensure it's a StampAnnotation
        if isinstance(annot, ap.annotations.StampAnnotation):
            # Get normal appearance XForm of the stamp
            xform = annot.appearance["N"]
            absorber = ap.text.TextAbsorber()
            absorber.visit(xform)
            extracted = absorber.text
            with open(outfile, "w", encoding="utf-8") as f:
                f.write(extracted)
    finally:
        document.close()
```

## 提取突出显示的文本

遍历页面的注释并使用 [HighlightAnnotation.get_marked_text()](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/highlightannotation) 读取每个突出显示所覆盖的文本跨度。页面注释集合是从 1 开始的。

1. 打开 [文档](https://reference.aspose.com/pdf/python-net/aspose.pdf/document) 并选择目标页面。
1. 遍历 `page.annotations`.
1. 使用 `is_assignable` 用于筛选 [HighlightAnnotation](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/highlightannotation) 实例。
1. 将注释强制转换后调用 `get_marked_text()` 检索突出显示的内容。

```python
def extract_highlight_text(infile):
    """
    Extract text from highlight annotations.

    Args:
        infile (str): Input PDF filename

    Returns:
        None

    Example:
        extract_highlight_text("sample.pdf")

    Note:
        Prints marked text from each highlight annotation on first page.
    """
    document = ap.Document(infile)
    page = document.pages[1]

    for annotation in page.annotations:
        if is_assignable(annotation, ap.annotations.HighlightAnnotation):
            highlight_annotation = cast(ap.annotations.HighlightAnnotation, annotation)
            print(highlight_annotation.get_marked_text())
```

## 提取上标和下标文本

上标和下标在公式、数学表达式以及化学化合物名称中经常出现。Aspose.PDF for Python via .NET 支持提取这些内容。 [TextFragmentAbsorber](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragmentabsorber), 它检测字符级别的定位元数据。

1. 打开 [文档](https://reference.aspose.com/pdf/python-net/aspose.pdf/document).
1. 创建一个 `TextFragmentAbsorber` 实例。
1. 调用 `document.pages[page_number].accept(absorber)` 扫描目标页面。
1. 从中检索完整提取的文本 `absorber.text`.
1. 将结果写入文件并关闭文档。

```python
import os
import aspose.pdf as ap


def extract_super_sub_text(infile, outfile, page_number=1):
    """
    Extract text (including superscript/subscript) from a specified page of a PDF and write to a text file.
    Args:
        infile (str): Path to input PDF file.
        outfile (str): Path to output text file.
        page_number (int): 1‑based index of the page to extract.
    """
    document = ap.Document(infile)
    try:
        absorber = ap.text.TextFragmentAbsorber()
        # Accept only the specific page for extraction
        document.pages[page_number].accept(absorber)
        extracted_text = absorber.text
        with open(outfile, "w", encoding="utf-8") as f:
            f.write(extracted_text)
    finally:
        document.close()
```

## 遍历文本碎片以检测上标/下标

对于每个片段的检查，遍历 `absorber.text_fragments` 并阅读 `text_state.superscript` 和 `text_state.subscript` 每个的布尔标志 [TextFragment](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragment).

1. 打开 [文档](https://reference.aspose.com/pdf/python-net/aspose.pdf/document) 并创建一个 [TextFragmentAbsorber](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragmentabsorber).
1. 接受目标页上的吸收器以进行填充 `absorber.text_fragments`.
1. 对于每个片段，读取 `fragment.text`, `fragment.text_state.superscript`，和 `fragment.text_state.subscript`.
1. 将结果写入输出文件并关闭文档。

```python
import os
import aspose.pdf as ap


def extract_super_sub_details(infile, outfile, page_number=1):
    """
    Extract details of each text fragment on a page, identifying superscript and subscript items.
    Args:
        infile (str): Path to input PDF file.
        outfile (str): Path to output text file.
        page_number (int): 1‑based page index.
    """
    document = ap.Document(infile)
    try:
        absorber = ap.text.TextFragmentAbsorber()
        document.pages[page_number].accept(absorber)

        with open(outfile, "w", encoding="utf-8") as f:
            for fragment in absorber.text_fragments:
                text = fragment.text
                is_sup = fragment.text_state.superscript  # True if superscript
                is_sub = fragment.text_state.subscript  # True if subscript
                f.write(
                    f"Text: '{text}' | Superscript: {is_sup} | Subscript: {is_sub}\n"
                )
    finally:
        document.close()
```
