---
title: 导入 XML 数据
type: docs
weight: 40
url: /zh/python-net/import-xml-data/
description: 本示例演示如何使用 Aspose.PDF for Python via .NET 将 XML 文件中的表单数据导入到 PDF 表单字段。它展示了如何绑定 PDF 文档，通过文件流读取结构化的 XML 数据，并自动填充相应的表单字段。
lastmod: "2026-06-08"
---

XML 通常用于存储结构化的表单数据，使其成为在系统之间传递值的实用格式。在本示例中，the [Form](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/form/) facade 来自 [aspose.pdf.facades](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/) 用于加载 PDF 表单并直接从 XML 文件应用字段值。导入数据后，更新后的 PDF 将保存为新文档。

1. 初始化 pdf_facades.Form() 以操作 PDF 表单字段。
1. 调用 ‘bind_pdf()’ 以附加 PDF 表单模板。
1. 使用 'FileIO()' 来访问包含表单数据的 XML 文件。
1. 调用 'import_xml()' 将 PDF 字段填充为来自 XML 文件的值。
1. 保存更新后的 PDF。

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Import data from XML
def import_xml_to_pdf_fields(infile, datafile, outfile):
    """Import form data from XML file into PDF form fields."""
    # Create Form object
    pdf_form = pdf_facades.Form()

    # Bind PDF document
    pdf_form.bind_pdf(infile)

    # Open XML file as stream
    with FileIO(datafile, "r") as xml_input_stream:
        # Import data from XML into PDF form fields
        pdf_form.import_xml(xml_input_stream)

    # Save updated PDF
    pdf_form.save(outfile)
```
