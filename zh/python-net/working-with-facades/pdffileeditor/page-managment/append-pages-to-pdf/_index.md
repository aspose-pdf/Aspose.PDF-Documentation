---
title: 将页面追加到 PDF
type: docs
weight: 10
url: /zh/python-net/append-pages-to-pdf/
description: 使用 Aspose.PDF for Python 将一个 PDF 文档的页面追加到另一个 PDF 文档中。
lastmod: "2026-06-08"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 在 Python 中将页面从一个 PDF 追加到另一个 PDF
Abstract: 了解如何使用 Aspose.PDF for Python 将一个 PDF 文档的页面追加到另一个文档中。本示例演示如何使用 PdfFileEditor 类合并多个 PDF 的页面并创建单个输出文档。
---

在文档处理工作流中，合并来自不同 PDF 文档的页面是常见需求。使用 Aspose.PDF for Python，开发人员可以轻松地将一个或多个 PDF 文件的页面追加到现有文档中。

此代码片段展示了如何使用 append 方法 [PdfFileEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffileeditor/) 类，用于将另一个 PDF 文件的选定页面添加到源 PDF 的末尾。通过指定页码范围，开发人员可以精确控制最终文档中包含哪些页面。

1. 创建一个 PdfFileEditor 对象。
1. 从另一个 PDF 追加页面。

从二级 PDF 文档中指定的页面被追加到原始 PDF 的末尾，生成一个合并后的输出文件。

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))
from config import set_license, initialize_data_dir


# Append Pages to PDF
def append_pages_to_pdf(infile, sample_file, outfile):
    # Create a PdfFileEditor object
    pdf_editor = pdf_facades.PdfFileEditor()
    # Append pages from the specified PDF document to the end of the source PDF document
    pdf_editor.append(infile, [sample_file], 1, 2, outfile)
```
