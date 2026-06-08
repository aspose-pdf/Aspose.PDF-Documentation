---
title: 设置提交 Url
type: docs
weight: 40
url: /zh/python-net/set-submit-url/
description: 此示例演示如何使用 Aspose.PDF for Python 在 PDF 表单中为按钮字段配置提交操作。
lastmod: "2026-06-08"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 使用 Python 为 PDF 表单按钮设置提交 Url
Abstract: 本文说明了如何打开现有的 PDF 表单，使用 FormEditor 类为按钮字段定义提交 Url，验证操作是否成功，并保存更新后的 PDF 文档。
---

PDF 表单可以设计为在用户点击提交按钮时将数据提交到 Web 服务器。使用 Aspose.PDF for Python，开发人员可以以编程方式为表单字段配置提交操作。
通过设置提交 Url，表单可以在按钮被点击时将用户输入的数据发送到服务器。此功能在 PDF 表单必须向 Web 应用程序、数据库或处理服务提交信息的工作流中非常有用。

使用 [FormEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/formeditor/) 类来自 [aspose.pdf.facades](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/) 模块中，开发者可以以编程方式为现有 PDF 表单中的按钮字段分配提交 URL。

1. 打开现有的 PDF 表单。
1. 定位名为 Script_Demo_Button 的按钮字段。
1. 分配一个将提交表单数据的 URL。
1. 验证该操作已成功应用。
1. 保存更新后的 PDF 文档。

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def set_submit_url(input_file_name, output_file_name):
    # Create FormEditor object
    form_editor = pdf_facades.FormEditor()

    # Set license
    set_license()

    # Open input PDF file
    form_editor.bind_pdf(input_file_name)

    # Set submit URL for the button
    if not form_editor.set_submit_url(
        "Script_Demo_Button", "http://www.example.com/submit"
    ):
        raise Exception("Failed to set submit URL")

    # Save output PDF file
    form_editor.save(output_file_name)
```
