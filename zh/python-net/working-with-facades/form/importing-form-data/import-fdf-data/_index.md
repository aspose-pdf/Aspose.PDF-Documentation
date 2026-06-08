---
title: 导入 FDF 数据
type: docs
weight: 10
url: /zh/python-net/import-fdf-data/
description: 本示例演示如何使用 Aspose.PDF for Python via .NET 将表单数据从 FDF 文件导入 PDF 表单。它展示了如何绑定 PDF 文档、从 FDF 流读取表单字段值，并自动填充相应的字段。
lastmod: "2026-06-08"
---

FDF（Forms Data Format）是一种轻量级格式，用于存储和传输 PDF 表单字段值，而不包含整个文档。在本示例中， [Form](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/form/) facade 来自 [aspose.pdf.facades](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/) 用于加载 PDF 表单并从外部 FDF 文件导入字段数据。导入过程完成后，更新后的 PDF 将另存为新文件。

1. 初始化 pdf_facades.Form() 以处理交互式 PDF 表单字段。
1. 调用 ‘bind_pdf()’ 以附加 PDF 表单模板。
1. 使用 ‘open()’ 以二进制模式读取 FDF 文件。
1. 调用 'import_fdf()' 将 PDF 字段填充来自 FDF 文件的数据。
1. 保存更新后的 PDF。

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Import Data from FDF
def import_fdf_to_pdf_form(infile, datafile, outfile):
    """Import form data from FDF file into PDF form fields."""
    # Create Form object
    pdf_form = pdf_facades.Form()

    # Bind PDF document
    pdf_form.bind_pdf(infile)

    # Open FDF file as stream
    with open(datafile, "rb") as fdf_input_stream:
        pdf_form.import_fdf(fdf_input_stream)

    # Save updated PDF
    pdf_form.save(outfile)
```
