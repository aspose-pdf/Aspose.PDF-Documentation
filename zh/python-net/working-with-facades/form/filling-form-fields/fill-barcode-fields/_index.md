---
title: 填写条形码字段
type: docs
weight: 50
url: /zh/python-net/fill-barcode-fields/
description: 本示例演示了如何使用 Aspose.PDF for Python via .NET 以编程方式填充 PDF 表单中的条形码字段。它展示了如何绑定 PDF 文档、为条形码字段分配值，并保存更新后的文件。
lastmod: "2026-06-08"
---

PDF 表单中的条形码字段允许将编码信息存储并以条形码的形式可视化展示。在本示例中， [Form](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/form/) 来自 [aspose.pdf.facades](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/) 模块用于访问表单字段并分配条形码值。数据填充完成后，PDF 将以更新的条形码内容进行保存。

1. 初始化 'pdf_facades.Form()' 以管理 PDF 表单交互。
1. 调用 'bind_pdf()' 来附加包含条形码字段的 PDF。
1. 使用 'fill_field()' 来分配条形码值。
1. 保存已更新的 Document。

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Fill Barcode Fields
def fill_barcode_fields(infile, outfile):
    """Fill barcode fields in PDF form."""
    # Create Form object
    pdf_form = pdf_facades.Form()

    # Bind PDF document
    pdf_form.bind_pdf(infile)

    # Fill barcode fields by name
    pdf_form.fill_field("product_barcode", "123456789012")

    # Save updated PDF
    pdf_form.save(outfile)
```
