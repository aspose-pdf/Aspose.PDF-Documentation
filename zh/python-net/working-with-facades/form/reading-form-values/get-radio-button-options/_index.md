---
title: 获取单选按钮选项
type: docs
weight: 20
url: /zh/python-net/get-radio-button-options/
description: 本文演示如何使用 Aspose.PDF Facades API 检索 PDF 文档中单选按钮字段的当前选定值。
lastmod: "2026-06-08"
---

PDF 表单中的单选按钮字段是分组控件，一次只能选择一个选项。每个组都有字段名称，每个选项都有相应的值。

1. 创建 Form 对象。
1. 绑定 PDF 文档。
1. 检索已选的单选按钮选项。

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Get radio button options
def get_radio_button_options(infile):
    """Get radio button options from a PDF document."""
    # Create Form object
    pdf_form = pdf_facades.Form()

    # Bind PDF document
    pdf_form.bind_pdf(infile)

    # Get radio button options by their names
    field_names = ["WorkType"]
    for field_name in field_names:
        options = pdf_form.get_button_option_current_value(field_name)
        print(f"Options for '{field_name}': {options}")
```
