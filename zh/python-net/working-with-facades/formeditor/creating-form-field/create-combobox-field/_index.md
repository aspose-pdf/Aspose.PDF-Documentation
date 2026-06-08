---
title: 创建 ComboBox 字段
type: docs
weight: 20
url: /zh/python-net/create-combobox-field/
description: 了解如何使用 Aspose.PDF for Python 以编程方式向 PDF 文档添加 ComboBox（下拉列表）字段。本示例演示如何插入 ComboBox 表单字段、添加可选择项，并保存更新后的 PDF 文件。
lastmod: "2026-06-08"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 使用 Aspose.PDF for Python 在 PDF 中创建 ComboBox 字段
Abstract: 交互式表单字段使 PDF 更加动态且用户友好。ComboBox 字段允许用户从预定义的下拉列表中选择一个选项。在本教程中，您将学习如何使用 Aspose.PDF for Python 中的 FormEditor 类在 PDF 中创建 ComboBox，填充选项，并保存修改后的文档。
---

PDF 表单广泛用于在数字文档（如申请表、调查问卷和注册表）中收集结构化信息。ComboBox 字段提供了一种方便的方式，让用户从预定义值列表中选择，同时保持表单紧凑有序。

这 [FormEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/formeditor/) 该类允许您创建和管理不同类型的字段，包括文本框、复选框、单选按钮和下拉列表。

1. 加载现有的 PDF 文档。
1. 使用 'add_field()' 方法和 'FieldType.COMBO_BOX' 参数添加 ComboBox 字段。
1. 使用 'add_list_item()' 方法向下拉列表中插入可选择的选项。
1. 保存更新后的 PDF 文档。

```python
import sys
from os import path
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def create_combobox_field(infile, outfile):
    """Create ComboBox field in PDF document."""
    pdf_form_editor = pdf_facades.FormEditor()
    pdf_form_editor.bind_pdf(infile)

    # Add ComboBox field to PDF form
    pdf_form_editor.add_field(
        pdf_facades.FieldType.COMBO_BOX, "combobox1", "Australia", 1, 230, 498, 350, 514
    )
    pdf_form_editor.add_list_item("combobox1", ["Australia", "Australia"])
    pdf_form_editor.add_list_item("combobox1", ["New Zealand", "New Zealand"])

    # Save updated PDF document with form fields
    pdf_form_editor.save(outfile)
```
