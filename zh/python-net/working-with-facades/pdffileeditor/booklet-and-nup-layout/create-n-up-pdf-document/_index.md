---
title: 创建 N-Up PDF 文档
type: docs
weight: 10
url: /zh/python-net/create-n-up-pdf-document/
description: 了解如何使用 Aspose.PDF for Python 在安全处理潜在错误的同时创建 N-Up PDF 文档。
lastmod: "2026-06-08"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 在 Python 中创建 N-Up PDF 布局
Abstract: 了解如何使用 Aspose.PDF for Python 生成 N-Up PDF 布局。本示例演示如何使用 PdfFileEditor 类的 'make_n_up' 或 'try_make_n_up' 方法将 PDF 文档的多页合并到单页上。
---

N-Up 布局将 PDF 文档的多页以网格形式放置在单页上。此布局常用于打印演示文稿、讲义或报告，以便一次查看多页内容。

使用 Aspose.PDF for Python，开发者可以通过指定行数和列数快速创建 N-Up 文档，这决定了每个输出页上显示多少原始页面。

在此代码片段中，‘make_n_up’方法的 [PdfFileEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffileeditor/) 类将输入 PDF 的页面排列成 2 × 2 的网格，这意味着四个原始页面会显示在输出文档的一页上。

在示例中，布局使用 2 行 2 列，每张纸产生四页：

1. 打开源 PDF 文件。
1. 创建一个 PdfFileEditor 实例。
1. 指定 N-Up 布局的行数和列数。
1. 生成一个合并页面的新 PDF。

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
from io import FileIO

import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Create N-Up PDF Document
def create_nup_pdf_document(infile, outfile):
    # Create NUpMaker object
    nup_maker = pdf_facades.PdfFileEditor()
    # Make N-Up layout from input PDF file and save to output PDF file
    nup_maker.make_n_up(
        FileIO(infile), FileIO(outfile, "w"), 2, 2
    )  # 2 rows and 2 columns for N-Up layout
```

Aspose.PDF for Python via .NET 允许您使用 PdfFileEditor 类生成 N-Up 布局。'try_make_n_up' 方法的工作方式类似于 make_n_up，但在操作失败时不会抛出异常，而是返回一个布尔值，指示该过程是否成功。

N-Up 布局使用由行和列定义的网格，将多个 PDF 页面安排在单个页面上。

'try_make_n_up' 方法提供了一种更安全的执行此操作的方式，因为：

- 如果布局成功创建，它返回 True。
- 如果操作失败，它返回 False。
- 它不会用异常中断程序执行。

在下面的示例中，文档使用 2 × 2 网格排列，将每个输出页放置四个原始页。

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
from io import FileIO

import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Create N-Up PDF Document
def try_create_nup_pdf_document(infile, outfile):
    # Create NUpMaker object
    nup_maker = pdf_facades.PdfFileEditor()
    # Make N-Up layout from input PDF file and save to output PDF file
    if not nup_maker.try_make_n_up(FileIO(infile), FileIO(outfile, "w"), 2, 2):
        print("Failed to create N-Up PDF document.")
```
