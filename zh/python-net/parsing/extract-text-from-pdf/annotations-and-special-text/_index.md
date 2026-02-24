---
title: 使用 Python 的注释和特殊文本
linktitle: 注释和特殊文本
type: docs
weight: 40
url: /zh/python-net/annotation-and-special-text/
description: 本节包含使用 Python 中的 Aspose.PDF 对 PDF 文档进行注释和特殊文本提取的文章。
lastmod: "2025-11-05"
sitemap: 
    changefreq: "weekly"
    priority: 0.7
---

## 从印章注释中提取文本

Aspose.PDF for Python 库允许您从 PDF 页面上的印章注释（具体为 StampAnnotation）中提取文本。

1. 打开文档。
1. 从页面的注释集合中访问印章注释。
1. 获取印章的外观流（XForm）。
1. 使用 'TextAbsorber' 从该外观中提取嵌入的文本。

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

## 提取高亮文本

PDF 标准提供了在文档中高亮文本片段的功能。要提取这些高亮内容，请按照以下步骤操作：

1. 导入 `aspose.pdf as ap` 以及您使用的任何辅助函数（`is_assignable`、`cast`）。
2. 调用 `ap.Document(infile)` 打开 PDF。
3. 使用 `document.pages` 选择所需的页面（页面集合从 1 开始计数）。
4. 循环遍历 `page.annotations` 以检查该页面上的每个注释。
5. 过滤注释，仅处理高亮注释。
6. 将注释转换为 `HighlightAnnotation` 并调用 `get_marked_text()` 读取高亮文本。
7. 打印或以其他方式处理返回的文本。

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

**下标和上标** 最常用于公式、数学表达式以及化学化合物的规格说明。当同一段文字中出现大量下标或上标时，编辑它们非常困难。
在最新的某个版本中，**Aspose.PDF for Python via .NET** 库新增了从 PDF 中提取上标和下标文本的功能。使用 'TextFragmentAbsorber' 从 PDF 文档的特定页面提取所有文本（包括上标和下标）。

1. 加载 PDF 文档。
1. 实例化一个 'TextFragmentAbsorber()'，该对象支持根据版本功能检测上标/下标文本。
1. 调用 'document.pages[page_number].accept(absorber)' 仅扫描指定页面。
1. 通过 'absorber.text' 获取提取的文本。
1. 使用标准文件 I/O 将文本写入输出文件。
1. 关闭文档以释放资源。

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
        with open(outfile, "w", encoding="utf‑8") as f:
            f.write(extracted_text)
    finally:
        document.close()
```

## 迭代 TextFragments 检测上标/下标

遍历页面中的每个文本片段，检查它是上标还是下标，并相应处理。

1. 加载 PDF 文档。
1. 创建 'TextFragmentAbsorber()' 并在选定页面上接受它。
1. 访问 'absorber.text_fragments'，它返回该页面上找到的片段集合。
1. 对于每个片段：
- 获取 'fragment.text'。
- 检查 'fragment.text_state.superscript' 和 'fragment.text_state.subscript'。
- 将片段文本和标志写入输出文件的一行。
1. 关闭文件和文档。

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

        with open(outfile, "w", encoding="utf‑8") as f:
            for fragment in absorber.text_fragments:
                text = fragment.text
                is_sup = fragment.text_state.superscript  # True if superscript
                is_sub = fragment.text_state.subscript    # True if subscript
                f.write(f"Text: '{text}' | Superscript: {is_sup} | Subscript: {is_sub}\n")
    finally:
        document.close()
```
