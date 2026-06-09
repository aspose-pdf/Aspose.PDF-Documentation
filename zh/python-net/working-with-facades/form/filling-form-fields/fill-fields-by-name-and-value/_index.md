---
title: 按名称和值填写字段
type: docs
weight: 60
url: /zh/python-net/fill-fields-by-name-and-value/
description: 本文演示了如何使用 Aspose.PDF for Python via .NET 通过名称和值动态填充多个 PDF 表单字段。它不是逐个设置字段，而是使用字典结构将字段名称映射到对应值，并在循环中批量填充。
lastmod: "2026-06-08"
---

使用名称‑值集合填充表单字段可让开发者打造可伸缩且灵活的 PDF 表单自动化解决方案。在本示例中，the [Form](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/form/) facade 来自 [aspose.pdf.facades](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/) 用于绑定 PDF 文档并遍历字段数据字典。每个条目通过 ‘fill_field method’ 应用，实现对表单字段的高效批量更新。

1. 初始化 ‘pdf_facades.Form()’ 以处理交互式表单字段。
1. 使用 'bind_pdf()' 将源 PDF 文档附加。
1. 创建一个字典，包含字段名称以及您想插入的值。
1. 遍历字典并对每个条目调用 'fill_field()'。
1. 保存已更新的 Document。

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Fill Fields by Name and Value
def fill_fields_by_name_and_value(infile, outfile):
    """Fill PDF form fields by name and value."""
    # Create Form object
    pdf_form = pdf_facades.Form()

    # Bind PDF document
    pdf_form.bind_pdf(infile)

    # Fill fields by name and value
    fields = {
        "name": "Jane Smith",
        "address": "456 Elm St, Othertown, USA",
        "email": "jane.smith@example.com",
    }
    for field_name, value in fields.items():
        pdf_form.fill_field(field_name, value)

    # Save updated PDF using outfile
    pdf_form.save(outfile)
```
