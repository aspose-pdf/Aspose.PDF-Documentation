---
title: 填写单选按钮字段
type: docs
weight: 30
url: /zh/python-net/fill-radio-button-fields/
description: 本示例演示了如何使用 Aspose.PDF for Python via .NET 以编程方式填写 PDF 表单中的单选按钮字段。它展示了如何绑定 PDF 文档、按索引选择单选按钮选项，并保存更新后的文件。
lastmod: "2026-06-08"
---

单选按钮允许用户从预定义的组中选择单个选项，例如性别或偏好字段。在本示例中， [Form](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/form/) 来自 [aspose.pdf.facades](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/) 模块用于绑定源 PDF 并通过其索引值分配选定的选项。选择所需选项后，修改后的文档将被保存。

1. 初始化 pdf_facades.Form() 以管理 PDF 表单字段。
1. 调用 'bind_pdf()' 以附加包含单选按钮字段的 PDF。
1. 使用 'fill_field()' 选择第一个选项（索引 0）。
1. 保存更新后的 PDF。

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Fill Radio Button Fields
def fill_radio_button_fields(infile, outfile):
    """Fill radio button fields in PDF form."""
    # Create Form object
    pdf_form = pdf_facades.Form()

    # Bind PDF document
    pdf_form.bind_pdf(infile)

    # Fill radio button fields by name
    pdf_form.fill_field("gender", 0)  # Select male option (index 0)
    # pdf_form.fill_field("gender", 1) # Select female option (index 1)

    # Save updated PDF
    pdf_form.save(outfile)
```
