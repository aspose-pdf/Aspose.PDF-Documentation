---
title: 创建 TextBox 字段
type: docs
weight: 60
url: /zh/python-net/create-textbox-field/
description: 了解如何使用 Aspose.PDF for Python 以编程方式向 PDF 文档添加 TextBox 字段。本教程展示了如何插入多个文本字段、设置默认值以及保存更新后的 PDF 文档。
lastmod: "2026-06-08"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 使用 Aspose.PDF for Python 在 PDF 中创建 TextBox 字段
Abstract: PDF 表单中的 TextBox 字段允许用户输入和编辑文本，使文档具备交互性且友好易用。在本教程中，您将学习如何使用 Aspose.PDF for Python 中的 FormEditor 类在 PDF 中创建 TextBox 表单字段。示例演示了添加多个字段、指定默认值以及保存已修改的 PDF。
---

PDF 表单通常需要用户输入文本，例如姓名、地址或评论。TextBox 字段通过在 PDF 文档中直接提供可编辑字段实现此功能。

这 [FormEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/formeditor/) 该类允许添加文本字段、复选框、单选按钮、列表框、组合框和按钮，使构建交互式 PDF 变得简便。

1. 加载现有的 PDF 文档。
1. 添加多个 TextBox 字段供用户输入。
1. 为每个字段设置默认值。
1. 保存更新后的 PDF 文档。

```python
import sys
from os import path
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def create_textbox_field(infile, outfile):
    """Create TextBox field in PDF document."""
    pdf_form_editor = pdf_facades.FormEditor()
    pdf_form_editor.bind_pdf(infile)

    # Add TextBox field to PDF form
    pdf_form_editor.add_field(
        pdf_facades.FieldType.TEXT, "first_name", "Alexander", 1, 50, 570, 150, 590
    )
    pdf_form_editor.add_field(
        pdf_facades.FieldType.TEXT, "last_name", "Smith", 1, 235, 570, 330, 590
    )

    # Save updated PDF document with form fields
    pdf_form_editor.save(outfile)
```
