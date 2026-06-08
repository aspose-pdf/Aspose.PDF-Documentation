---
title: 从 PDF 中提取页面
type: docs
weight: 30
url: /zh/python-net/extract-pages-from-pdf/
description: 使用 Aspose.PDF for Python 从 PDF 文档中提取选定的页面。
lastmod: "2026-06-08"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 在 Python 中从 PDF 文档中提取特定页面
Abstract: 了解如何使用 Aspose.PDF for Python 从 PDF 文档中提取选定的页面。此示例演示如何创建仅包含所需页面的新 PDF，从而实现自定义文档创建和页级操作。
---

当您需要创建文档的子集、仅共享特定内容或为演示、报告或打印重新组织 PDF 时，提取 PDF 页面非常有用。使用 Aspose.PDF for Python，开发人员可以以编程方式从 PDF 文件中提取页面并将其保存为新文档。

了解如何使用 extract 方法 [PdfFileEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffileeditor/) 类。通过指定要提取的页面列表，您可以生成仅包含所选页面的新 PDF，同时保留原始内容和格式。

1. 创建一个 PdfFileEditor 对象。
1. 定义要提取的页面。
1. 提取页面。

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))
from config import set_license, initialize_data_dir


# Extract Pages from PDF
def extract_pages_from_pdf(infile, outfile):
    # Create a PdfFileEditor object
    pdf_editor = pdf_facades.PdfFileEditor()

    # Define the page numbers to be extracted (1-based index)
    pages_to_extract = [1, 4, 3]

    # Extract the specified pages from the PDF document and save to a new PDF document
    pdf_editor.extract(infile, pages_to_extract, outfile)
```
