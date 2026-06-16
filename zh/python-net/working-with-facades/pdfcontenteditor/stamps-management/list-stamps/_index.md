---
title: 列出印章
type: docs
weight: 70
url: /zh/python-net/list-stamps/
description: 本示例加载 PDF，检索第 1 页的所有印章，打印它们，并在未找到印章时显示提示信息。
lastmod: "2026-06-08"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 使用 PdfContentEditor 在 Python 中列出 PDF 的橡胶印章注释
Abstract: 本示例演示如何使用 Aspose.PDF for Python via the Facades API 检索并列出 PDF 文档中的橡胶印章注释。它展示了如何访问特定页面上的印章并显示其详细信息。
---

在处理带有注释的 PDF 时，您可能需要在修改或删除之前检查现有的橡胶印章。'get_stamps()' 方法允许您检索特定页面上放置的所有印章。随后您可以遍历结果并以编程方式处理它们。

1. 创建一个 [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/) 实例。
1. 绑定输入的 PDF 文档。
1. 检索第 1 页的所有印章。
1. 遍历印章集合。
1. 打印每个印章。
1. 如果不存在印章，显示一条消息。

```python
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as apd
from io import BytesIO
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def list_stamps(infile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)
    # List all stamps on page 1
    stamps = content_editor.get_stamps(1)

    count = 0
    for stamp in stamps:
        count += 1
        print(f"Stamp {count}: {stamp}")

    if count == 0:
        print("No stamps found")
```
