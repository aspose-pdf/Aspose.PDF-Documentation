---
title: 导入 JSON 数据
type: docs
weight: 30
url: /zh/python-net/import-json-data/
description: 本例演示了如何使用 Aspose.PDF for Python via .NET 将表单字段数据从 JSON 文件导入 PDF 表单。它展示了如何绑定 PDF 文档、通过文件流读取结构化 JSON 数据，并自动填充匹配的表单字段。
lastmod: "2026-06-08"
---

JSON 被广泛用于在系统之间存储和传输结构化数据。在本例中， [Form](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/form/) 来自 [aspose.pdf.facades](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/) 模块用于绑定 PDF 表单并从外部 JSON 文件导入字段值。导入过程完成后，更新后的文档被保存为新的 PDF。

1. 初始化 pdf_facades.Form() 以操作 PDF 表单字段。
1. 调用 ‘bind_pdf()’ 以附加 PDF 表单模板。
1. 使用 \u0027FileIO()\u0027 读取包含表单值的 JSON 文件。
1. 调用 \u0027import_json()\u0027 使用 JSON 键–值对填充 PDF 字段。
1. 保存更新后的 PDF。

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Import from JSON
def import_json_to_pdf_form(infile, datafile, outfile):
    """Import form data from JSON file into PDF form fields."""
    # Create Form object
    form = pdf_facades.Form()

    # Bind PDF document
    form.bind_pdf(infile)

    # Open JSON file as stream
    with FileIO(datafile, "r") as json_stream:
        # Import data from JSON into PDF form fields
        form.import_json(json_stream)

    # Save updated PDF
    form.save(outfile)
```
