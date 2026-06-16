---
title: 使用 Python 的基本文本提取
linktitle: 基本文本提取
type: docs
weight: 10
url: /zh/python-net/basic-text-extraction/
description: 了解如何使用 Aspose.PDF for Python 提取 PDF 文档的文本 — 一次性从所有页面提取或从特定页面提取。
lastmod: "2026-06-08"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## 提取 PDF 文档所有页面的文本

使用 [TextAbsorber](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textabsorber) 捕获 PDF 文档每一页的全部文本并将其写入文本文件。此方法非常适合将 PDF 转换为可搜索的文本、进行内容分析，或为索引和后续处理准备文本。

1. 使用以下方法打开 PDF 文档 [文档](https://reference.aspose.com/pdf/python-net/aspose.pdf/document).
1. 创建一个 `TextAbsorber` 实例。
1. 调用 `document.pages.accept(text_absorber)` 扫描所有页面。
1. 检索提取的文本来自 `text_absorber.text`.
1. 将结果写入输出文本文件。

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
    # Create a TextAbsorber to extract text
    text_absorber = ap.text.TextAbsorber()
    # Accept the absorber for all pages
    document.pages.accept(text_absorber)
    # Get extracted text
    extracted_text = text_absorber.text
    # Write the text to an output file
    with open(outfile, "w", encoding="utf-8") as tw:
        tw.write(extracted_text)
```

## 从特定页面提取文本

应用 [TextAbsorber](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textabsorber) 对单个页面进行操作，以隔离并保存多页文档中该部分的文本。这在您只需要单页内容时非常有用——例如，发票、报告章节或表单摘要。

1. 使用以下方法打开 PDF 文档 [文档](https://reference.aspose.com/pdf/python-net/aspose.pdf/document).
1. 创建一个 `TextAbsorber` 实例。
1. 调用 `accept` 在目标页面上： `document.pages[page_number].accept(text_absorber)`.
1. 检索提取的文本并将其写入文件。

```python
import os
import aspose.pdf as ap


def extract_text_from_page(infile, outfile, page_number):
    """
    Extract text from a specific page number of the PDF.
    Args:
        infile (str): Path to input PDF file.
        outfile (str): Path to output text file.
        page_number (int): 1-based page index to extract.
    """
    document = ap.Document(infile)
    text_absorber = ap.text.TextAbsorber()
    # Accept the absorber on only the specified page
    document.pages[page_number].accept(text_absorber)
    extracted_text = text_absorber.text
    with open(outfile, "w", encoding="utf-8") as tw:
        tw.write(extracted_text)
```
