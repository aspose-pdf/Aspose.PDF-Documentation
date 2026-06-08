---
title: 填写列表框
type: docs
weight: 40
url: /zh/python-net/fill-list-box/
description: 本示例演示了如何使用 Aspose.PDF for Python via .NET 以编程方式填充 PDF 表单中的列表框和多选字段。它展示了如何绑定 PDF 文档、在基于列表的表单字段中选择值，并保存更新后的文件。
lastmod: "2026-06-08"
---

列表框和多选字段允许用户从预定义的选项集合中选择一个或多个值。在本示例中， [Form](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/form/) facade 来自 [aspose.pdf.facades](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/) 用于访问 PDF 表单并将选定的值分配给 favorite_colors 字段。选择所需的选项后，更新的文档将被保存。

1. 初始化 'pdf_facades.Form()' 以管理和更新表单字段。
1. 调用 'bind_pdf()' 以附加包含列表框或多选字段的源 PDF。
1. 使用 'fill_field()' 从可用选项中选择一个值。
1. 保存已更新的 Document。

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Fill List Box / Multi-Select Fields
def fill_list_box_fields(infile, outfile):
    """Fill list box and multi-select fields in PDF form."""
    # Create Form object
    pdf_form = pdf_facades.Form()

    # Bind PDF document
    pdf_form.bind_pdf(infile)

    # Fill list box / multi-select fields by name
    pdf_form.fill_field("favorite_colors", "Red")

    # Save updated PDF
    pdf_form.save(outfile)
```
