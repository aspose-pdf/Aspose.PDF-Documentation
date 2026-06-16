---
title: 创建单选按钮字段
type: docs
weight: 40
url: /zh/python-net/create-radiobutton-field/
description: 了解如何使用 Aspose.PDF for Python 以编程方式向 PDF 文档添加单选按钮表单字段。此示例演示如何创建单选按钮组、定义可选项并保存更新后的 PDF 文件。
lastmod: "2026-06-08"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 使用 Aspose.PDF for Python 在 PDF 中创建单选按钮字段
Abstract: 单选按钮通常用于 PDF 表单中，以便用户从预定义的选项组中选择一个选项。在本教程中，您将学习如何使用 Aspose.PDF for Python 中的 FormEditor 类在 PDF 中创建单选按钮字段。示例展示了如何定义单选按钮项、设置默认选择以及保存更新后的文档。
---

交互式 PDF 表单使用户能够直接在文档中提供结构化输入。当用户必须从多个选项中仅选择一个时，例如选择国家、性别或偏好，单选按钮字段非常有用。

这 [FormEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/formeditor/) 类提供了创建不同类型字段的方法，包括文本框、复选框、组合框、列表框和单选按钮。

1. 加载现有的 PDF 文档。
1. 定义单选按钮选项列表。
1. 在特定页面添加单选按钮字段。
1. 设置默认选定值。
1. 保存修改后的 PDF 文档。

```python
import sys
from os import path
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def create_radiobutton_field(infile, outfile):
    """Create RadioButton field in PDF document."""
    pdf_form_editor = pdf_facades.FormEditor()
    pdf_form_editor.bind_pdf(infile)

    # Add RadioButton field to PDF form
    pdf_form_editor.items = ["Australia", "New Zealand", "Malaysia"]
    pdf_form_editor.add_field(
        pdf_facades.FieldType.RADIO, "radiobutton1", "Malaysia", 1, 240, 498, 256, 514
    )

    # Save updated PDF document with form fields
    pdf_form_editor.save(outfile)
```
