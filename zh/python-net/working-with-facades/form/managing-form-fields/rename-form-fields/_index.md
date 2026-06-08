---
title: 重命名表单字段
type: docs
weight: 30
url: /zh/python-net/rename-form-fields/
description: 本示例演示了如何使用 Aspose.PDF for Python via .NET 在 PDF 文档中重命名表单字段。它展示了如何绑定 PDF 表单、以编程方式更新现有字段名称并保存修改后的文件。重命名字段有助于统一表单结构、改进数据映射，并简化与自动化工作流或外部系统的集成。
lastmod: "2026-06-08"
---

在将 PDF 表单与内部命名规范对齐或为结构化数据处理准备文档时，重命名表单字段非常有用。在本示例中， [Form](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/form/) 来自 [aspose.pdf.facades](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/) 模块用于绑定源 PDF 并应用映射，将旧字段名称替换为新名称。更新字段标识符后，文档会以应用了更改的方式保存。

1. 初始化 pdf_facades.Form() 以操作 PDF 表单字段。
1. 调用 'bind_pdf()' 以附加 PDF 文档。
1. 创建一个包含旧字段名称及其对应新名称的元组列表。
1. 遍历映射并对每个条目调用 'rename_field()'。
1. 保存已更新的 Document。

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Rename form fields
def rename_form_fields(infile, outfile):
    """Rename form fields in a PDF document."""
    # Create Form object
    pdf_form = pdf_facades.Form()

    # Bind PDF document
    pdf_form.bind_pdf(infile)

    # Rename form fields by providing a mapping of old names to new names
    field_renaming_map = [("First Name", "NewFirstName"), ("Last Name", "NewLastName")]
    for old_name, new_name in field_renaming_map:
        pdf_form.rename_field(old_name, new_name)

    # Save updated PDF
    pdf_form.save(outfile)
```
