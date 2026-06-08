---
title: 导入 XFDF 数据
type: docs
weight: 20
url: /zh/python-net/import-xfdf-data/
description: 本示例演示如何使用 Aspose.PDF for Python via .NET 将 XFDF 文件中的表单数据导入到 PDF 表单中。它展示了如何绑定 PDF 文档，通过文件流读取基于 XML 的 XFDF 数据，并自动填充匹配的表单字段。导入 XFDF 数据可实现高效的表单数据交换，并支持依赖结构化 XML 格式的自动化文档工作流。
lastmod: "2026-06-08"
---

XFDF（XML Forms Data Format）是 PDF 表单数据的 XML 表示形式，旨在实现互操作性和数据交换。在本示例中， [Form](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/form/) 来自 [aspose.pdf.facades](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/) 模块用于绑定 PDF 表单并从外部 XFDF 文件导入字段值。导入数据后，更新后的 PDF 被另存为新文档。

1. 初始化 pdf_facades.Form() 以操作 PDF 表单字段。
1. 调用 ‘bind_pdf()’ 以附加 PDF 表单模板。
1. 使用 'open()' 读取 XFDF 文件。
1. 调用 'import_xfdf()' 以使用 XFDF 文件中的值填充 PDF 字段。
1. 保存已更新的 Document。

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Import Data from XFDF
def import_data_from_xfdf(infile, datafile, outfile):
    """Import form data from XFDF file into PDF form fields."""
    # Create Form object
    pdf_form = pdf_facades.Form()

    # Bind PDF document
    pdf_form.bind_pdf(infile)

    # Open XFDF file as stream
    with open(datafile, "rb") as xfdf_input_stream:
        # Import data from XFDF into PDF form fields
        pdf_form.import_xfdf(xfdf_input_stream)

    # Save updated PDF
    pdf_form.save(outfile)
```
