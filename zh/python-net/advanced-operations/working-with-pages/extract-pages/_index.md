---
title: 使用 Python 编程提取页面
linktitle: 提取 PDF 页面
type: docs
weight: 80
url: /zh/python-net/extract-pages/
description: 您可以使用 Aspose.PDF for Python via .NET 库提取 PDF 文件中的页面。
lastmod: "2025-11-16"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 如何使用 Python 提取 PDF 页面
Abstract: 本文演示了如何使用 Aspose.PDF for Python 库从 PDF 文档中提取页面。该技术涵盖单页提取和多页提取，使开发者能够创建仅包含所选页面的新 PDF 文件。示例说明了如何通过基于 1 的索引访问特定页面，将其复制到新 PDF 文档并保存结果，同时保持原始文档完整。这些方法对于拆分大型文档、共享选定章节或创建用于分发或分析的自定义 PDF 子集非常有用。
---

## 从 PDF 中提取单页

从 PDF 文档中提取特定页面并将其保存为新文件。使用 Aspose.PDF 库，脚本会将所需页面复制到新的 PDF 中，保持原始文档不变。这对于拆分 PDF 或隔离重要页面进行分发非常有用。

1. 使用 [`文档`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) API (`ap.Document()`) 加载源 PDF。
1. 创建一个新的 [`文档`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 以保存提取的页面。
1. 使用目标文档的 [`页面集合`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/) (`dst_document.pages.add(...)`) 将源文档中所需的 [`页面`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) 添加到新 PDF。
- 在本例中，提取第 2 页（基于 1 的索引）。
1. 将包含提取页面的新 [`文档`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 保存到指定的输出文件。

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def extract_page(input_file_name, output_file_name):
    """
    Extract a single page from a PDF document.

    Demonstrates how to extract a specific page from a PDF document using
    the Aspose.PDF library. This function extracts page 2 from the input
    document and saves it as a new file containing only that page.

    Args:
        input_file_name (str): Path to the input PDF file from which to extract a page.
        output_file_name (str): Path where the extracted page will be saved.

    Returns:
        None: The function creates a new PDF containing the extracted page and saves it to the output path.

    Note:
        - Extracts page 2 (1-based indexing) from the document
        - Page numbering is 1-based (page 2 is the second page)
        - The original document is not modified; a new file is created
        - If the document has fewer than 2 pages, this may raise an error

    Example:
        >>> extract_page("input.pdf", "output.pdf")
        # Extracts page 2 from input.pdf and saves result as output.pdf
    """
    # Open source PDF as Document
    src_document = ap.Document(input_file_name)
    # Create destination Document to hold extracted pages
    dst_document = ap.Document()
    # Add a Page from source to destination using PageCollection API
    dst_document.pages.add(src_document.pages[2])
    # Save destination Document
    dst_document.save(output_file_name)
```

## 从 PDF 中提取多页

从 PDF 文档中提取多个特定页面并将它们保存到新文件中。使用 Aspose.PDF 库，选定的页面会被复制到新 PDF，同时保持原始文档完整。这对于创建仅包含较大文档中相关部分的较小 PDF 非常有用。

1. 使用 [`文档`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) API (`ap.Document()`) 加载源 PDF。
1. 创建一个新的 [`文档`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 以保存提取的页面。
1. 选择要提取的页面（在本例中，使用基于 1 的索引提取第 2 页和第 3 页）。
1. 使用其 [`页面集合`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/) 将源文档中每个选定的 [`页面`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) 添加到新 PDF。
1. 将包含提取页面的新 [`文档`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 保存到指定的输出文件。

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def extract_bunch_pages(input_file_name, output_file_name):
    """
    Extract specific pages from a PDF document and save them to a new file.

    This function reads a PDF document, extracts pages 2 and 3 (1-indexed),
    and saves them to a new PDF file.

    Args:
        input_file_name (str): Path to the input PDF file to extract pages from.
        output_file_name (str): Path where the new PDF file with extracted pages will be saved.

    Returns:
        None

    Note:
        The function specifically extracts pages 2 and 3 from the source document.
        Page indexing appears to be 1-based in this implementation.
    """
    # Open source Document
    document = ap.Document(input_file_name)
    pages = [2,3]
    # Create destination Document
    another_document = ap.Document()
    # Copy selected Page objects via PageCollection API
    for page_index in pages:
        another_document.pages.add(document.pages[page_index])
    # Save destination Document
    another_document.save(output_file_name)
```
