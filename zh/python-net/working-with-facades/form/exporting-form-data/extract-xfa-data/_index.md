---
title: 提取 XFA 数据
type: docs
weight: 50
url: /zh/python-net/extract-xfa-data/
description: 本示例说明如何使用 Aspose.PDF for Python via .NET 从 PDF 文件中提取 XFA 表单数据。它演示了如何将基于 XFA 的 PDF 文档绑定到 Form 门面并将其内部数据结构导出到文件流中。
lastmod: "2026-06-08"
---

XFA（XML Forms Architecture）表单不同于传统的 AcroForm，因为它们的数据存储在 PDF 内部的 XML 中。在本示例中， [Form](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/form/) 对象来自于 [aspose.pdf.facades](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/) 模块用于绑定 PDF 并将其 XFA 数据直接提取到文件中。

1. 创建 pdf_facades.Form() 的实例以管理表单数据。
1. 调用 'bind_pdf()' 以附加包含 XFA 表单的源 PDF。
1. 使用 'FileIO()' 创建可写文件流。
1. 调用 'extract_xfa_data()' 导出嵌入的 XFA XML 数据。

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Extract XFA Data
def export_xfa_data(infile, outfile):
    """Export XFA form data."""
    # Create Form object
    form = pdf_facades.Form()

    # Bind PDF document
    form.bind_pdf(infile)

    with FileIO(outfile, "w") as stream:
        # Export embedded XFA XML data to the output stream
        form.extract_xfa_data(stream)
```
