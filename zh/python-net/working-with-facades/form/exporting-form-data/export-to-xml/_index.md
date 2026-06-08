---
title: 导出为 XML
type: docs
weight: 40
url: /zh/python-net/export-to-xml/
description: 这个示例演示如何使用 Aspose.PDF for Python via .NET 将 PDF 表单数据导出为 XML 文件。它展示了如何加载 PDF 文档，通过 Form facade 访问其表单字段，并使用 Form Class 将提取的数据保存为结构化 XML。
lastmod: "2026-06-08"
---

导出表单数据使开发者能够在无需手动复制字段值的情况下重复使用存储在 PDF AcroForms 中的信息。在本示例中，a [Form](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/form/) 对象是从 aspose.pdf 创建的。在 facades 模块中，源 PDF 与其绑定，表单数据被写入 XML 流。

1. 创建一个 Form 对象。初始化 pdf_facades.Form() 以访问和管理表单字段。
1. 使用 'bind_pdf()' 将源 PDF 文档附加到 Form 实例。
1. 使用 'FileIO()' 创建可写文件流。
1. 调用 'export_xml()' 以提取所有表单字段值并将其写入 XML 文件。

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Export Data to XML
def export_pdf_form_data_to_xml(infile, datafile):
    """Export PDF form data to XML file."""
    # Create Form object
    pdf_form = pdf_facades.Form()

    # Bind PDF document
    pdf_form.bind_pdf(infile)

    # Open XML file as stream
    with FileIO(datafile, "w") as xml_output_stream:
        # Export data from PDF form fields to XML
        pdf_form.export_xml(xml_output_stream)
```
