---
title: 创建 PDF 小册子
type: docs
weight: 20
url: /zh/python-net/create-pdf-booklet/
description: 使用 Aspose.PDF for Python 从现有文档生成小册子式 PDF
lastmod: "2026-06-08"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 使用 Python 从现有 PDF 创建 PDF 小册子
Abstract: 了解如何使用 Aspose.PDF for Python 从现有文档生成小册子式 PDF。此示例演示如何使用 PdfFileEditor 类重新排列页面，以便它们可以打印并折叠成小册子。该方法会自动对页面进行排序，以生成正确的小册子布局。
---

在准备 PDF 打印时，创建小册子式文档是常见需求。在小册子布局中，页面会重新排列，以便打印并折叠后呈现正确的顺序。

使用 Aspose.PDF for Python，开发者可以轻松地将标准 PDF 转换为小册子，使用 [PdfFileEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffileeditor/) class. 'make_booklet' 方法会自动重新组织输入文档的页面，并生成一个针对小册子打印优化的新 PDF。

1. 打开现有的 PDF 文档。
1. 创建一个 PdfFileEditor 实例。
1. 使用 make_booklet 方法重新组织页面。
1. 将输出保存为小册子就绪的 PDF 文件。

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
from io import FileIO

import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Create PDF Booklet
def create_pdf_booklet(infile, outfile):
    # Create BookletMaker object
    booklet_maker = pdf_facades.PdfFileEditor()
    # Make booklet from input PDF file and save to output PDF file
    booklet_maker.make_booklet(FileIO(infile), FileIO(outfile, "w"))
```

此代码片段展示了如何使用 ‘try_make_booklet’ 方法 [PdfFileEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffileeditor/) 类来重新排列页面以进行小册子打印，在操作失败时不抛出异常。

小册子布局会重新排列页面，使得打印并折叠后文档能够按正确顺序阅读。自动化此过程可确保结果一致，并消除手动重新排列页面的需求。

‘try_make_booklet’ 方法的工作方式类似于 ‘make_booklet’，但有一个重要的区别：

- 'make_booklet' 如果操作失败会抛出异常。
- 'try_make_booklet' 返回 True 或 False，允许开发者更安全地管理错误。

1. 打开现有的 PDF 文档。
1. 创建一个 PdfFileEditor 实例。
1. 尝试创建小册子。
1. 处理结果。

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
from io import FileIO

import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def try_create_pdf_booklet(infile, outfile):
    # Create BookletMaker object
    booklet_maker = pdf_facades.PdfFileEditor()
    # Make booklet from input PDF file and save to output PDF file
    # The try_make_booklet method is like the make_booklet method,
    # except the try_make_booklet method does not throw an exception if the operation fails.
    if not booklet_maker.try_make_booklet(FileIO(infile), FileIO(outfile, "w")):
        print("Failed to create booklet.")
```
