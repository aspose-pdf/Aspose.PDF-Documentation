---
title: 导出为 JSON
type: docs
weight: 30
url: /zh/python-net/export-to-json/
description: 本示例演示如何使用 Aspose.PDF for Python via .NET 将 PDF 表单字段值导出到 JSON 文件。它解释了如何加载 PDF 表单，通过 Form 门面访问其字段，并将提取的数据保存为结构化的 JSON 格式。
lastmod: "2026-06-08"
---

JSON 是一种广泛使用的数据格式，能够实现应用程序和服务之间的无缝交换。在本示例中， [Form](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/form/) 对象来自于 [aspose.pdf.facades](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/) 模块用于绑定 PDF 文件并将其表单字段值导出为可读的 JSON 结构。

1. 初始化 pdf_facades.Form() 以处理表单字段。
1. 使用 'bind_pdf()' 将源 PDF 文档附加。
1. 使用 'FileIO()' 创建可写流。
1. 调用 'export_json()' 提取表单字段值并将其保存为格式化的 JSON。

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Export Data to JSON
def export_form_to_json(infile, outfile):
    """Export PDF form field values to JSON file."""
    # Create Form object
    form = pdf_facades.Form()

    # Bind PDF document
    form.bind_pdf(infile)

    # Create JSON file stream
    with FileIO(outfile, "w") as json_stream:
        # Export form field values to JSON
        form.export_json(json_stream, indented=True)
```
