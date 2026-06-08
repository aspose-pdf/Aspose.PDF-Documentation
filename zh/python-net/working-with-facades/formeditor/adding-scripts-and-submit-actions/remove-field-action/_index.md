---
title: 删除字段操作
type: docs
weight: 20
url: /zh/python-net/remove-field-action/
description: 从表单字段中删除 JavaScript 在修改交互式 PDF 表单、禁用先前分配的操作或清理包含不必要脚本的文档时可能有用。
lastmod: "2026-06-08"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 使用 Python 删除 PDF 表单字段中的 JavaScript 操作
Abstract: 使用 Aspose.PDF for Python，开发者可以以编程方式移除附加在表单字段上的 JavaScript 操作。本文说明了如何打开现有的 PDF 表单、使用 FormEditor 类删除特定字段关联的脚本、验证该操作并保存修改后的文档。
---

PDF 表单通常包含在用户与按钮或输入字段等表单元素交互时执行的 JavaScript 操作。在某些情况下，需要移除这些脚本以简化表单行为、提升安全性或更新表单逻辑。使用 Aspose.PDF for Python 从 PDF 文档的表单字段中删除 JavaScript 操作。代码打开现有的 PDF 表单，定位特定字段，移除其关联的 JavaScript 操作，并将更新后的文档保存为新的 PDF 文件。

使用 [FormEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/formeditor/) 类来自 [aspose.pdf.facades](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/)，您可以从现有的 PDF 表单中的特定字段删除 JavaScript 操作：

1. 打开现有的 PDF 表单。
1. 定位名为 'Script_Demo_Button' 的表单字段。
1. 删除与该字段关联的 JavaScript 操作。
1. 检查删除是否成功。
1. 保存更新后的 PDF 文档。

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def remove_field_script(input_file_name, output_file_name):
    # Create FormEditor object
    form_editor = pdf_facades.FormEditor()

    # Open input PDF file
    form_editor.bind_pdf(input_file_name)

    # Remove JavaScript action from the field
    if not form_editor.remove_field_action("Script_Demo_Button"):
        raise Exception("Failed to remove field script")

    # Save output PDF file
    form_editor.save(output_file_name)
```
