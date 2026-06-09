---
title: 添加橡胶印章
type: docs
weight: 10
url: /zh/python-net/add-rubber-stamp/
description: 此示例绑定一个输入 PDF，在前四页添加一个绿色的“已批准”橡胶印章，并保存修改后的文档。
lastmod: "2026-06-08"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 使用 Python 中的 PdfContentEditor 向 PDF 添加橡胶印章注释
Abstract: 此示例演示如何使用 Aspose.PDF for Python 通过 Facades API 向 PDF 文档添加橡胶印章注释。橡胶印章允许您在页面上直观地标记批准、审阅或自定义标签。
---

橡胶印章注释通常用于 PDF 中，以指示批准、审阅状态或其他备注。使用 [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/)，您可以为印章定义矩形，设置其文本和注释，选择颜色，并将其应用于文档的多个页面。

1. 创建一个 PdfContentEditor 实例。
1. 绑定输入的 PDF 文档。
1. 循环遍历第 1–4 页。
1. 添加带有自定义文本、注释和颜色的橡胶印章注释。
1. 保存更新后的 PDF 文档。

```python
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as apd
from io import BytesIO
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def add_rubber_stamp(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)

    for i in range(1, 5):
        content_editor.create_rubber_stamp(
            i,
            apd.Rectangle(120, 450, 180, 60),
            "Approved",
            "Approved by reviewer",
            apd.Color.green,
        )
    # Save updated document
    content_editor.save(outfile)
```
