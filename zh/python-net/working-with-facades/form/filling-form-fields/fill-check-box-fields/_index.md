---
title: 填写复选框字段
type: docs
weight: 20
url: /zh/python-net/fill-check-box-fields/
description: 本示例演示了如何使用 Aspose.PDF for Python via .NET 以编程方式填写 PDF 表单中的复选框字段。它展示了如何绑定 PDF 文档、按字段名称更新复选框的值，并保存修改后的文件。
lastmod: "2026-06-08"
---

复选框通常在 PDF 表单中用于表示二元选择，例如订阅或协议确认。在本示例中， [Form](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/form/) facade 来自 [aspose.pdf.facades](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/) 用于访问表单字段并将其值设置为选中状态。更新复选框后，填写的 PDF 将另存为新文档。

1. 初始化 'pdf_facades.Form()' 以管理表单字段交互。
1. 使用 'bind_pdf()' 将包含复选框字段的源 PDF 附加上。
1. 调用 'fill_field()' 将诸如 'subscribe_newsletter' 和 'accept_terms' 等字段标记为已选中。
1. 保存已更新的 Document。

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Fill Check Box Fields
def fill_check_box_fields(infile, outfile):
    """Fill check box fields in PDF form."""
    # Create Form object
    pdf_form = pdf_facades.Form()

    # Bind PDF document
    pdf_form.bind_pdf(infile)

    # Fill check box fields by name
    pdf_form.fill_field("subscribe_newsletter", "Yes")
    pdf_form.fill_field("accept_terms", "Yes")

    # Save updated PDF
    pdf_form.save(outfile)
```
