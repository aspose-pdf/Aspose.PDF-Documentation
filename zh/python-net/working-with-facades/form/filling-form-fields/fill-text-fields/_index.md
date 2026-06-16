---
title: 填写文本字段
type: docs
weight: 10
url: /zh/python-net/fill-text-fields/
description: 此示例演示如何使用 Aspose.PDF for Python via .NET 自动填充 PDF 表单中的文本字段。它展示了如何加载 PDF 文档、按名称填充特定的表单字段并保存更新后的文件。
lastmod: "2026-06-08"
---

通过编程方式填充文本字段使应用程序能够重复使用 PDF 模板并插入动态内容，而无需手动编辑。在本示例中， [Form](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/form/) facade 来自 [aspose.pdf.facades](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/) 用于绑定 PDF 表单并更新多个字段，如姓名、地址和电子邮件。赋值后，修改后的 PDF 被保存为新文档。

1. 初始化 \u0027pdf_facades.Form()\u0027 以管理表单字段操作。
1. 使用 \u0027bind_pdf()\u0027 附加包含文本字段的输入 PDF。
1. 调用 'fill_field()' 将数据插入到诸如 name、address 和 email 等字段。
1. 保存更新后的 PDF。

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Fill Text Fields
def fill_text_fields(infile, outfile):
    """Fill text fields in PDF form."""
    # Create Form object
    pdf_form = pdf_facades.Form()

    # Bind PDF document
    pdf_form.bind_pdf(infile)

    # Fill text fields by name
    pdf_form.fill_field("name", "John Doe")
    pdf_form.fill_field("address", "123 Main St, Anytown, USA")
    pdf_form.fill_field("email", "john.doe@example.com")

    # Save updated PDF
    pdf_form.save(outfile)
```
