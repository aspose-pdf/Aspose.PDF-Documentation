---
title: 替换 XFA 数据
type: docs
weight: 50
url: /zh/python-net/replace-xfa-data/
description: 本例演示如何使用 Aspose.PDF for Python via .NET 在 PDF 中替换现有的 XFA 表单数据。它展示了如何绑定基于 XFA 的 PDF 文档、从外部 XFA 文件加载新数据，并以编程方式更新表单内容。
lastmod: "2026-06-08"
---

XFA（XML Forms Architecture）表单将其数据以 XML 格式存储在 PDF 结构中。在本例中， [Form](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/form/) 来自 [aspose.pdf.facades](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/) 模块用于绑定 PDF 并使用外部 XML 流替换其现有的 XFA 数据集。应用新数据后，更新后的 PDF 将另存为一个单独的文件。

1. 初始化 pdf_facades.Form() 以管理 XFA 表单数据。
1. 调用 'bind_pdf()' 以附加包含 XFA 表单的 PDF。
1. 使用 'FileIO()' 读取 XFA XML 文件。
1. 调用 'set_xfa_data()' 以新 XFA 内容更新 PDF。
1. 保存已更新的 Document。

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Replace from XFA data
def replace_xfa_data(infile, datafile, outfile):
    """Import form data from XFA file into PDF form fields."""
    # Create Form object
    form = pdf_facades.Form()

    # Bind PDF document
    form.bind_pdf(infile)

    # Open XFA file as stream
    with FileIO(datafile, "r") as xfa_stream:
        # Import data from XFA into PDF form fields
        form.set_xfa_data(xfa_stream)

    # Save updated PDF
    form.save(outfile)
```
