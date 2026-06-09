---
title: 获取字段Facade
type: docs
weight: 10
url: /zh/python-net/get-field-facades/
description: 本示例演示如何使用 Aspose.PDF Facades API 从 PDF 文档中读取特定表单字段的值。
lastmod: "2026-06-08"
---

PDF 表单包含用户可以输入数据的字段，例如文本框、复选框或单选按钮。为了以编程方式处理这些表单，通常需要检索这些字段的当前值。

1. 创建一个 Form 对象。
1. 将 PDF 文档绑定到表单对象。
1. 检索字段值。

```python

    from io import FileIO
    import sys
    from os import path
    import aspose.pdf as ap
    import aspose.pdf.facades as pdf_facades

    sys.path.append(path.join(path.dirname(__file__), ".."))

    from config import set_license, initialize_data_dir


    # Get field values
    def get_field_values(infile):
        """Get field values from a PDF document."""
        # Create Form object
        pdf_form = pdf_facades.Form()

        # Bind PDF document
        pdf_form.bind_pdf(infile)

        # Get field values by their names
        field_names = ["First Name", "Last Name"]
        for field_name in field_names:
            value = pdf_form.get_field(field_name)
            print(f"Value of '{field_name}': {value}")
```