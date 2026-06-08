---
title: 获取必填字段名称
type: docs
weight: 30
url: /zh/python-net/get-required-field-names/
description: 本示例演示如何使用 Aspose.PDF Facades API 在 PDF 文档中识别并检索必填表单字段的名称。
lastmod: "2026-06-08"
---

PDF 表单可能包含用户在提交前必须填写的强制性字段。这些字段通常在表单属性中标记为必填。

1. 创建 Form 对象。
1. 绑定 PDF 文档。
1. 使用 'pdf_form.field_names' 访问所有字段名称。

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Get required field names
def get_required_field_names(infile):
    """Get required field names from a PDF document."""
    # Create Form object
    pdf_form = pdf_facades.Form()

    # Bind PDF document
    pdf_form.bind_pdf(infile)

    # Get required field names
    for field in pdf_form.field_names:
        if pdf_form.is_required_field(field):
            print(f"Required field: {field}")
```
