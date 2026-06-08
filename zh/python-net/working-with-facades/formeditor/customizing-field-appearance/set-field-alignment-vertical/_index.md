---
title: 设置字段垂直对齐
type: docs
weight: 40
url: /zh/python-net/set-field-alignment-vertical/
description: 本示例演示如何使用 Aspose.PDF for Python 在 PDF 文档中设置表单字段的垂直对齐方式。
lastmod: "2026-06-08"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 使用 Python 设置 PDF 表单字段的垂直对齐
Abstract: 本文说明了如何打开 PDF，使用 FormEditor 类为字段设置垂直对齐，并保存更新后的 PDF。示例将名为 "First Name" 的字段的垂直对齐设置为字段区域的底部。
---

PDF 表单字段可能包含需要正确垂直对齐的文本，以实现一致且专业的外观。使用 Aspose.PDF for Python，开发人员可以以编程方式修改表单字段的垂直对齐。
垂直对齐使开发人员能够控制字段文本是显示在字段边界框的顶部、居中还是底部，从而提升表单数据的布局和可读性。

使用 [FormEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/formeditor/) 类和 [FormFieldFacade](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/formfieldfacade/) 常量，开发人员可以以编程方式调整垂直对齐，以实现一致的表单布局：

1. 打开现有的 PDF 文档。
1. 创建一个 FormEditor 对象。
1. 将名为 "First Name" 的字段的垂直对齐设置为底部。
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


def set_field_alignment_vertical(infile, outfile):
    # Open document
    doc = ap.Document(infile)

    # Create FormEditor object
    form_editor = pdf_facades.FormEditor(doc)

    # Attempt to set vertical alignment of the "First Name" field to bottom
    if form_editor.set_field_alignment_v(
        "First Name", pdf_facades.FormFieldFacade.ALIGN_BOTTOM
    ):
        # Save updated document
        form_editor.save(outfile)
    else:
        raise Exception(
            "Failed to set field vertical alignment. Field may not support vertical alignment."
        )
```
