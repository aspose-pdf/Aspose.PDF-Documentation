---
title: 添加插入符号注释
type: docs
weight: 10
url: /zh/python-net/add-caret-annotation/
description: 此示例加载现有的 PDF，在首页添加插入符号注释，并保存修改后的文档。该注释包含红色插入符号图案和描述性注释文字。
lastmod: "2026-06-08"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 使用 Python 向 PDF 添加插入符号注释
Abstract: 此示例演示如何使用 Aspose.PDF for Python via the Facades API 向 PDF 文档添加插入符号注释。示例展示了如何绑定 PDF 文件、使用矩形定义注释位置、配置插入符号属性以及保存更新后的文档。
---

插入符号注释通常用于指示文档中的文字插入或编辑性评论。使用 PdfContentEditor，您可以通过指定页码、注释边界、指示区、符号、备注文字和颜色，以编程方式添加插入符号注释。

1. 创建 [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/) 对象。
1. 绑定输入 PDF。
1. 定义插入符号注释参数：
  - 将添加注释的页码
  - 插入符号矩形（注释位置）
  - 呼出矩形（文本区域）
  - 符号（例如 "P"）
  - 批注文本
  - 批注颜色
1. 添加插入符号批注。
1. 保存已更新的 Document。

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as apd
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def add_caret_annotation(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)
    # Add caret annotation to page 1
    content_editor.create_caret(
        1,
        apd.Rectangle(350, 400, 10, 10),
        apd.Rectangle(300, 380, 115, 15),
        "P",
        "This is a caret annotation",
        apd.Color.red,
    )
    # Save updated document
    content_editor.save(outfile)
```
