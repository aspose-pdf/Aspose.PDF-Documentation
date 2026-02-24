---
title: 使用 Python 的基本文本提取
linktitle: 基本文本提取
type: docs
weight: 10
url: /zh/python-net/basic-text-extraction/
description: 本节包含使用 Aspose.PDF 在 Python 中从 PDF 文档进行基本文本提取的文章。
lastmod: "2025-11-05"
sitemap: 
    changefreq: "weekly"
    priority: 0.7
---

## 从 PDF 文档的所有页面提取文本

Aspose.PDF for Python 教你如何从 PDF 文档的每一页提取文本。它使用 TextAbsorber 类捕获整篇文档的所有文本内容，并将其保存到单独的文本文件中。
非常适合将 PDF 转换为可搜索的文本、进行内容分析，或导出文本以用于索引和处理任务。

1. 加载 PDF 文件。
1. 创建一个 'TextAbsorber' 对象。
1. 调用 'document.pages.accept(text_absorber)' 以扫描所有页面。
1. 通过 'text_absorber.text' 获取完整文本。
1. 将结果写入文本文件。

```python

import os
import aspose.pdf as ap

def extract_text_from_all_pages(infile, outfile):
    """
    Extract all text from every page of the PDF and write to an output text file.
    Args:
        infile (str): Path to input PDF file.
        outfile (str): Path to output text file.
    """
    # Open the PDF document
    document = ap.Document(infile)
    try:
        # Create a TextAbsorber to extract text
        text_absorber = ap.text.TextAbsorber()
        # Accept the absorber for all pages
        document.pages.accept(text_absorber)
        # Get extracted text
        extracted_text = text_absorber.text
        # Write the text to an output file
        with open(outfile, "w", encoding="utf-8") as tw:
            tw.write(extracted_text)
    finally:
        document.close()
```

## 从特定页面提取文本

从 PDF 文档的单个页面提取文本。仅将 TextAbsorber 应用于指定页面，可隔离并保存多页 PDF 中特定部分的文本。

当您仅需要单页内容时很有用，例如，从发票页、报告章节或表单字段摘要中提取文本。

1. 打开 PDF。
1. 创建 TextAbsorber。
1. 仅接受指定页面 (pages[page_number])。
1. 提取文本并写入文件。

```python

import os
import aspose.pdf as ap

def extract_text_from_page(infile, page_number, outfile):
    """
    Extract text from a specific page number of the PDF.
    Args:
        infile (str): Path to input PDF file.
        page_number (int): 1-based page index to extract.
        outfile (str): Path to output text file.
    """
    document = ap.Document(infile)
    try:
        text_absorber = ap.text.TextAbsorber()
        # Accept the absorber on only the specified page
        document.pages[page_number].accept(text_absorber)
        extracted_text = text_absorber.text
        with open(outfile, "w", encoding="utf-8") as tw:
            tw.write(extracted_text)
    finally:
        document.close()
```

