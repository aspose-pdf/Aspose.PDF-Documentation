---
title: 导出为 XFDF
type: docs
weight: 20
url: /zh/python-net/export-to-xfdf/
description: 本示例展示了如何使用 Aspose.PDF for Python via .NET 将 PDF 表单字段数据导出为 XFDF（XML Forms Data Format）文件。它演示了如何加载 PDF 表单，通过 Form 外观访问其字段，并将提取的值保存到 XFDF 流中。
lastmod: "2026-06-08"
---

XFDF 是 PDF 表单数据的 XML 表示形式，允许开发人员独立于原始文档传输表单字段值。在本示例中，the [Form](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/form/) 对象 来自 [aspose.pdf.facades](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/) 用于绑定源 PDF 并将其数据导出为结构化的 XFDF 文件。

1. 初始化 pdf_facades.Form() 以管理 PDF 表单数据。
1. 调用 'bind_pdf()' 以附加源 PDF 文档。
1. 使用 'open()' 创建可写的二进制流。
1. 导出表单数据。调用 'export_xfdf()' 提取并保存表单字段值为 XFDF 格式。

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Export Data to XFDF
def export_pdf_form_to_xfdf(infile, outfile):
    """Export PDF form data to XFDF file."""
    # Create Form object
    pdf_form = pdf_facades.Form()

    # Bind PDF document
    pdf_form.bind_pdf(infile)

    # Create XFDF file stream
    with open(outfile, "wb") as xfdf_output_stream:
        # Export form data to XFDF file
        pdf_form.export_xfdf(xfdf_output_stream)
```
