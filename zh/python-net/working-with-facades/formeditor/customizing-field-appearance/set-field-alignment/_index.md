---
title: 设置字段对齐
type: docs
weight: 30
url: /zh/python-net/set-field-alignment/
description: 本示例演示了如何使用 Aspose.PDF for Python 在 PDF 文档中设置表单字段的文本对齐方式。
lastmod: "2026-06-08"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 使用 Python 设置 PDF 表单字段的文本对齐
Abstract: 本文说明了如何打开 PDF 文档，使用 FormEditor 类设置特定字段的对齐方式，并保存更新后的 PDF。示例将名为 "First Name" 的字段的文本对齐方式设置为居中。
---

PDF 表单字段常常需要自定义文本对齐以保持一致且专业的布局。使用 Aspose.PDF for Python，开发者可以以编程方式设置表单字段文本内容的对齐方式。

这 [FormEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/formeditor/) 类，结合 [FormFieldFacade](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/formfieldfacade/) constants，允许开发者以编程方式修改现有表单字段的对齐方式。

1. 打开现有的 PDF 文档。
1. 创建一个 FormEditor 对象。
1. 将名为 "First Name" 的字段对齐方式设置为居中。
1. 保存修改后的文档。

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pydrawing as ap_pydrawing
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def set_field_alignment(infile, outfile):
    # Open document
    doc = ap.Document(infile)

    # Create FormEditor object
    form_editor = pdf_facades.FormEditor(doc)

    # Set field alignment to center
    if form_editor.set_field_alignment(
        "First Name", pdf_facades.FormFieldFacade.ALIGN_CENTER
    ):
        # Save updated document
        form_editor.save(outfile)
    else:
        raise Exception(
            "Failed to set field alignment. Field may not support alignment."
        )
```
