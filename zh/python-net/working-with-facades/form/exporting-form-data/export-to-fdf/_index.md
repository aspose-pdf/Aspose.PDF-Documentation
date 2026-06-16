---
title: 导出为 FDF
type: docs
weight: 10
url: /zh/python-net/export-to-fdf/
description: 本示例解释了如何使用 Aspose.PDF for Python via .NET 将 PDF 表单字段数据导出到 FDF（Forms Data Format）文件。它演示了如何通过 Form 门面访问交互式表单数据，绑定源 PDF 文档，并将提取的数值保存到 FDF 流中。
lastmod: "2026-06-08"
---

FDF 是一种轻量级格式，专门用于存储和传输 PDF 表单数据，而无需嵌入整个文档。在本示例中， [Form](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/form/) 对象是从 [aspose.pdf.facades](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/) 模块中初始化的，允许开发者与 AcroForm 字段交互并导出它们的值。

1. 创建 pdf_facades.Form() 的实例以处理 PDF 表单字段。
1. 调用 'bind_pdf()' 以附加包含表单的 PDF 文档。
1. 使用 'open('')' 为 FDF 文件创建一个可写的二进制流。
1. 导出表单数据。调用 'export_fdf()' 提取并保存所有表单字段的值。

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Export Data to FDF
def export_form_data_to_fdf(infile, outfile):
    """Export PDF form data to FDF file."""
    # Create Form object
    pdf_form = pdf_facades.Form()

    # Bind PDF document
    pdf_form.bind_pdf(infile)

    # Create FDF file stream
    with open(outfile, "wb") as fdf_output_stream:
        # Export form data to FDF file
        pdf_form.export_fdf(fdf_output_stream)
```
