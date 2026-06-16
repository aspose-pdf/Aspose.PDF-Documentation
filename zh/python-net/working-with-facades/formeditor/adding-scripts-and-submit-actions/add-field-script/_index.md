---
title: 添加字段脚本
type: docs
weight: 10
url: /zh/python-net/add-field-script/
description: 交互式 PDF 表单可以包含 JavaScript，以在用户与表单字段交互时自动执行操作。使用 Aspose.PDF for Python，开发者可以轻松地将脚本附加到表单元素，如按钮或文本字段。
lastmod: "2026-06-08"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 使用 Python 为 PDF 表单字段添加 JavaScript 操作
Abstract: 本文说明了如何打开 PDF 表单、将 JavaScript 代码分配给特定表单字段、追加其他脚本操作并保存更新后的文档。示例使用来自 Aspose.PDF Facades API 的 FormEditor 类，以编程方式操作表单行为。
---

## 使用 Python 为 PDF 表单字段添加 JavaScript 操作

此代码片段使您能够使用 Aspose.PDF for Python 库向现有 PDF 表单字段添加 JavaScript 操作。它打开一个 PDF 文档，将 JavaScript 操作分配给表单字段，并添加一个在字段触发时运行的脚本。最后，将更新后的 PDF 保存为新文件。
使用 [FormEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/formeditor/) 类来自 [aspose.pdf.facades](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/) 模块，您可以以编程方式将 JavaScript 附加到现有表单字段：

1. 打开现有的 PDF 表单。
1. 为特定字段设置 JavaScript 操作。
1. 向同一字段追加另一个 JavaScript 操作。
1. 保存修改后的 PDF 文档。

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def add_field_script(input_file_name, output_file_name):
    # Create FormEditor object
    form_editor = pdf_facades.FormEditor()

    # Open input PDF file
    form_editor.bind_pdf(input_file_name)

    # Set JavaScript action for the field
    form_editor.set_field_script(
        "Script_Demo_Button", "app.alert('Script 1 has been executed');"
    )

    # Add JavaScript action to the field
    form_editor.add_field_script(
        "Script_Demo_Button", "app.alert('Script 2 has been executed');"
    )

    # Save output PDF file
    form_editor.save(output_file_name)
```
