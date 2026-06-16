---
title: 创建复选框字段
type: docs
weight: 10
url: /zh/python-net/create-checkbox-field/
description: 了解如何使用 Aspose.PDF for Python 以编程方式向 PDF 文档添加复选框表单字段。本指南演示如何使用 FormEditor 类将交互式复选框插入现有 PDF 文件并保存更新后的文档。
lastmod: "2026-06-08"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 使用 Aspose.PDF for Python 在 PDF 中创建复选框字段
Abstract: 交互式表单字段允许用户在 PDF 文档中进行数字化填写和交互。在本教程中，您将学习如何使用 Aspose.PDF Python API 向 PDF 添加复选框字段。示例展示了如何绑定现有 PDF 文档、在指定坐标处创建复选框表单字段并保存修改后的文件。
---

PDF 表单广泛用于在申请、调查和协议等文档中收集用户输入。复选框字段让用户能够在表单中选择或取消选择一个选项。

使用 Aspose.PDF for Python，开发人员可以以编程方式操作 PDF 表单。 [FormEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/formeditor/) 类提供用于在 PDF 文档中添加、编辑和管理表单字段的方法。

1. 加载现有的 PDF 文件。
1. 调用 'add_field()' 方法并使用 'FieldType.CHECK_BOX' 参数来创建复选框并指定其位置。
1. 定义字段名称、标题和位置。
1. 保存更新后的 PDF 文档。

```python
import sys
from os import path
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def create_checkbox_field(infile, outfile):
    """Create CheckBox field in PDF document."""
    pdf_form_editor = pdf_facades.FormEditor()
    pdf_form_editor.bind_pdf(infile)

    # Add CheckBox field to PDF form
    pdf_form_editor.add_field(
        pdf_facades.FieldType.CHECK_BOX,
        "checkbox1",
        "Check Box 1",
        1,
        240,
        498,
        256,
        514,
    )

    # Save updated PDF document with form fields
    pdf_form_editor.save(outfile)
```
