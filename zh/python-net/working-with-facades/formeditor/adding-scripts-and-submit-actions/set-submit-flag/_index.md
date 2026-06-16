---
title: 设置提交标志
type: docs
weight: 50
url: /zh/python-net/set-submit-flag/
description: 了解如何使用 Aspose.PDF for Python 以编程方式为 PDF 表单按钮设置提交标志。这样当用户点击按钮时，可将表单数据以特定格式（例如 XFDF）提交。
lastmod: "2026-06-08"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 使用 Aspose.PDF for Python 为 PDF 表单按钮设置提交标志
Abstract: PDF 表单可以配置为以不同格式将表单数据提交到服务器或端点。通过在按钮字段上设置提交标志，开发者可以定义数据的发送方式。本教程演示如何使用 FormEditor 类为 PDF 文档中现有的提交按钮设置提交标志并保存更新后的文件。
---

PDF 表单通常包含提交按钮，用于将用户输入发送到服务器。提交标志决定发送的数据格式（例如 XFDF、FDF、HTML）。

1. 绑定 PDF 文档。
1. 访问现有的提交按钮。
1. 为所需的格式设置提交标志。
1. 保存更新后的 PDF 文档。

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def set_submit_flag(input_file_name, output_file_name):
    # Create FormEditor object
    form_editor = pdf_facades.FormEditor()

    # Open input PDF file
    form_editor.bind_pdf(input_file_name)

    # Set submit flag for the form
    form_editor.set_submit_flag("Script_Demo_Button", ap.facades.SubmitFormFlag.XFDF)

    # Save output PDF file
    form_editor.save(output_file_name)
```
