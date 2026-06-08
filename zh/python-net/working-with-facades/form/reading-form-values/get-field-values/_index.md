---
title: 获取字段值
type: docs
weight: 50
url: /zh/python-net/get-field-values/
description: 使用 Form 类的 Aspose.PDF Facades 从 PDF 表单检索字段值。
lastmod: "2026-06-08"
---

此代码片段展示了如何使用 Aspose.PDF Facades API 从 PDF 文档中检索表单字段的当前值。The [get_field()](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/form/#methods) 该方法允许您以编程方式访问输入到文本字段、复选框、单选按钮以及其他 AcroForm 元素中的数据。

1. 将 PDF 绑定到 Form 对象。
1. 指定您想读取的字段名称。
1. 使用 get_field() 检索每个字段的值。

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