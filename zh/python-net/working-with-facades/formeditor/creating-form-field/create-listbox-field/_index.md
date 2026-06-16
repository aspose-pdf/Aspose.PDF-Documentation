---
title: 创建 ListBox 字段
type: docs
weight: 30
url: /zh/python-net/create-listbox-field/
description: 了解如何使用 Aspose.PDF for Python 以编程方式向 PDF 文档添加 ListBox 表单字段。本指南展示了如何插入 ListBox 字段、定义可选项，并保存更新后的 PDF 文件。
lastmod: "2026-06-08"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 使用 Aspose.PDF for Python 在 PDF 中创建 ListBox 字段
Abstract: PDF 表单允许用户通过选择选项、输入数据以及数字方式提交信息来与文档交互。ListBox 字段让用户能够从可见的选项列表中选择一个或多个值。在本教程中，您将学习如何使用 Aspose.PDF for Python 的 FormEditor 类在 PDF 中创建 ListBox 字段，并使用预定义的项目进行填充。
---

PDF 表单常用于申请表、调查问卷和注册文件。ListBox 字段可同时显示多个选项，便于用户浏览并从列表中选择项目。

这 [FormEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/formeditor/) 类提供了添加不同类型交互字段的功能，包括 ListBox 元素。

1. 加载现有的 PDF 文档。
1. 定义一个可选择的选项列表。
1. 向特定页面添加 ListBox 字段。
1. 设置默认选定值。
1. 保存更新后的 PDF 文档。

```python
import sys
from os import path
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def create_listbox_field(infile, outfile):
    """Create ListBox field in PDF document."""
    pdf_form_editor = pdf_facades.FormEditor()
    pdf_form_editor.bind_pdf(infile)

    # Add ListBox field to PDF form
    pdf_form_editor.items = ["Australia", "New Zealand", "Malaysia"]
    pdf_form_editor.add_field(
        pdf_facades.FieldType.LIST_BOX, "listbox1", "Australia", 1, 230, 398, 350, 514
    )

    # Save updated PDF document with form fields
    pdf_form_editor.save(outfile)
```
