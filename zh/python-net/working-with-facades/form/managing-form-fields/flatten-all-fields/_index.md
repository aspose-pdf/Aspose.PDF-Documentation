---
title: 扁平化所有字段
type: docs
weight: 10
url: /zh/python-net/flatten-all-fields/
description: 本示例演示如何使用 Aspose.PDF for Python via .NET 将 PDF 中的所有表单字段扁平化。它展示了如何绑定 PDF 文档、将每个交互式表单元素转换为静态页面内容，并保存最终文件。
lastmod: "2026-06-08"
---

扁平化通过将字段值直接合并到文档布局中，去除 PDF 表单的交互性。在本示例中， [Form](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/form/) facade 来自 [aspose.pdf.facades](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/) 用于绑定源 PDF 并应用 flatten_all_fields() 方法，该方法将所有字段转换为不可编辑的内容。

1. 初始化 pdf_facades.Form() 以操作 PDF 表单字段。
1. 调用 'bind_pdf()' 以附加源文档。
1. 调用 'flatten_all_fields()' 将所有交互式字段转换为静态内容。
1. 保存已更新的 Document。

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Flatten all fields
def flatten_all_fields(infile, outfile):
    """Flatten all fields in a PDF document."""
    # Create Form object
    pdf_form = pdf_facades.Form()

    # Bind PDF document
    pdf_form.bind_pdf(infile)

    # Flatten all fields in the PDF document
    pdf_form.flatten_all_fields()

    # Save updated PDF
    pdf_form.save(outfile)
```
