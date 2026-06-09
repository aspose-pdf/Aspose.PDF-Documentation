---
title: 解析完整字段名称
type: docs
weight: 60
url: /zh/python-net/resolve-full-field-names/
description: 本示例演示如何使用 Aspose.PDF Facades API 检索 PDF 文档中表单字段的完全限定名称。
lastmod: "2026-06-08"
---

在 PDF 表单中，字段可以按层次结构组织，尤其是使用子表单时。每个字段都有一个短名称和一个完全限定名称。完全限定名称表示字段在表单层次结构中的完整路径，许多用于操作或读取表单数据的 API 方法都需要此名称。

1. 创建 Form 对象。
1. 绑定 PDF 文档。
1. 访问所有表单字段名称。
1. 每个字段的完全限定名称使用 get_full_field_name() 解析。

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Resolve full field names
def resolve_full_field_names(infile):
    """Resolve full field names in a PDF document."""
    # Create Form object
    pdf_form = pdf_facades.Form()

    # Bind PDF document
    pdf_form.bind_pdf(infile)

    # Resolve full field names
    for field in pdf_form.field_names:
        name = pdf_form.get_full_field_name(field)
        print(f"Full field name: {name}")
```
