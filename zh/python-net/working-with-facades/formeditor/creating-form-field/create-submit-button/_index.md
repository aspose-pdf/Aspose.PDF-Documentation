---
title: 创建提交按钮
type: docs
weight: 50
url: /zh/python-net/create-submit-button/
description: 了解如何使用 Aspose.PDF for Python 以编程方式向 PDF 文档添加提交按钮。本教程演示如何创建一个将表单数据提交到指定 URL 并保存更新后 PDF 的按钮。
lastmod: "2026-06-08"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 使用 Aspose.PDF for Python 在 PDF 中创建提交按钮
Abstract: PDF 表单中的提交按钮允许用户将表单数据直接发送到服务器或端点。在本指南中，您将学习如何使用 Aspose.PDF for Python 中的 FormEditor 类向 PDF 添加提交按钮字段。示例展示了如何配置按钮的名称、标签、目标 URL 和位置，随后保存更新后的 PDF 文档。
---

交互式 PDF 表单通常需要用户提交其输入以进行处理，例如发送调查结果、申请表或反馈数据。提交按钮字段通过将按钮链接到网络端点来提供此功能。

这 [FormEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/formeditor/) 类允许添加按钮、复选框、单选按钮、文本字段和其他表单控件。

1. 加载现有的 PDF 文档。
1. 在特定页面添加一个提交按钮字段。
1. 设置按钮标签和目标提交 URL。
1. 保存包含新按钮的更新后 PDF。

```python
import sys
from os import path
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def create_submit_button(infile, outfile):
    """Create Submit Button in PDF document."""
    pdf_form_editor = pdf_facades.FormEditor()
    pdf_form_editor.bind_pdf(infile)

    # Add Submit Button to PDF form
    pdf_form_editor.add_submit_btn(
        "submitbtn1",
        1,
        "Submit Button",
        "http://example.com/submit",
        100,
        450,
        200,
        470,
    )

    # Save updated PDF document with form fields
    pdf_form_editor.save(outfile)
```
