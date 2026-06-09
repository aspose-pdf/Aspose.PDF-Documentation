---
title: 设置字段脚本
type: docs
weight: 30
url: /zh/python-net/set-field-script/
description: 此代码片段演示了如何使用 Aspose.PDF for Python 将 JavaScript 操作分配给 PDF 文档中的表单字段。
lastmod: "2026-06-08"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 使用 Python 为 PDF 表单字段设置 JavaScript 操作
Abstract: 本文说明了如何打开 PDF 文档、将 JavaScript 代码分配给表单字段、使用 FormEditor 类更新脚本并保存修改后的文件。示例演示了如何覆盖已有脚本以修改表单字段的行为。
---

交互式 PDF 表单通常依赖 JavaScript 来执行诸如显示警报、验证输入或触发动态表单行为等任务。使用 Aspose.PDF for Python，开发者可以以编程方式管理这些脚本。

示例首先向字段添加一个 JavaScript 操作，然后使用 \u0027set_field_script\u0027 方法将其替换为另一个脚本。此方法允许开发者控制或更新 PDF 表单元素（如按钮或输入字段）的交互行为。

这个示例中使用的表单字段名为 'Script_Demo_Button'，通常表示一个在触发时执行指定脚本的按钮。

使用 [FormEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/formeditor/) 类来自 [aspose.pdf.facades](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/) 模块，开发人员可以以编程方式管理与表单字段关联的 JavaScript 动作：

1. 打开现有的 PDF 表单文档。
1. 向表单字段添加 JavaScript 动作。
1. 设置（替换）JavaScript 动作为新脚本。
1. 保存修改后的 PDF 文档。

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def set_field_script(input_file_name, output_file_name):
    # Create FormEditor object
    form_editor = pdf_facades.FormEditor()

    # Open input PDF file
    form_editor.bind_pdf(input_file_name)

    # Add JavaScript action to the field
    form_editor.add_field_script(
        "Script_Demo_Button", "app.alert('Script 1 has been executed');"
    )

    # Set JavaScript action for the field
    form_editor.set_field_script(
        "Script_Demo_Button", "app.alert('Script 2 has been executed');"
    )

    # Save output PDF file
    form_editor.save(output_file_name)
```
