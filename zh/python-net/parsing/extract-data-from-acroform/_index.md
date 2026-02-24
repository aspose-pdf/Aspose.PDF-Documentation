---
title: 使用 Python 从 AcroForm 提取数据
linktitle: 从 AcroForm 提取数据
type: docs
weight: 50
url: /zh/python-net/extract-data-from-acroform/
description: Aspose.PDF 使从 PDF 文件中提取表单字段数据变得轻松。了解如何从 AcroForm 中提取数据并将其保存为 JSON、XML 或 FDF 格式。
lastmod: "2025-03-13"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 如何使用 Python 从 AcroForm 提取数据
Abstract: 本文提供了使用 Aspose.PDF for Python 管理 PDF 文档中表单字段的综合指南。它详细说明了从 PDF 中提取、操作和导出表单数据的多种方法。文章首先演示如何提取表单字段值并将其存储在字典中，随后以 JSON 格式输出数据。进一步说明了直接将表单数据导出为 JSON 文件，以增强数据序列化能力。此外，本文还涵盖了将表单数据导出为其他格式，如 XML、FDF（表单数据格式）和 XFDF，这对于数据交换和结构化数据存储非常有用。每个章节均包含 Python 代码片段，以帮助理解和实现。总体而言，本文是开发者在 Python 应用程序中集成 PDF 表单处理的实用资源。
---

## 从 PDF 文档中提取表单字段

除了让您生成和填写表单字段之外，Aspose.PDF for Python 还能轻松从 PDF 文件中提取表单字段数据或字段信息。

代码片段创建了一个字典，用于存储 PDF 表单中所有字段的值。它遍历表单的字段名称，获取其值，并用这些数据填充字典。最后，打印收集到的表单值。

```python

    import aspose.pdf as apdf
    from io import FileIO
    from os import path
    import json
    from aspose.pycore import cast, is_assignable

    path_infile = self.dataDir + infile
    form = apdf.facades.Form(path_infile)

    form_values = {}
    # Get values from all fields
    for formField in form.field_names:
        # Analyze names and values if needed
        form_values[formField] = form.get_field(formField)

    print(form_values)
```

## 按标题检索表单字段值

## 将 PDF 文档中的表单字段提取为 JSON

```python

    import aspose.pdf as apdf
    from io import FileIO
    from os import path
    import json
    from aspose.pycore import cast, is_assignable

    path_infile = path.join(self.dataDir, infile)
    path_outfile = path.join(self.dataDir, outfile)

    form = apdf.facades.Form(path_infile)
    with FileIO(path_outfile, "w") as json_file:
        form.export_json(json_file, True)
```

提供的 Python 代码片段提取其字段的值并将这些数据序列化为 JSON 格式。它导入必要的模块，构建输入和输出文件路径，从 PDF 表单中检索字段名称和值，并将序列化的 JSON 字符串写入指定的输出文件。

```python

    import aspose.pdf as apdf
    from io import FileIO
    from os import path
    import json
    from aspose.pycore import cast, is_assignable

    path_infile = path.join(self.dataDir, infile)
    path_outfile = path.join(self.dataDir, outfile)

    form = apdf.facades.Form(path_infile)
    form_data = {}
    # Get values from all fields
    for formField in form.field_names:
        # Analyze names and values if need
        form_data[formField] = form.get_field(formField)

    # Serialize to JSON
    json_string = json.dumps(form_data, indent=4)

    # Output the JSON string
    print(json_string)

    with open(path_outfile, "w", encoding="utf-8") as json_file:
        json_file.write(json_string)
```

## 从 PDF 文件提取数据为 XML

下面的 Python 代码片段创建一个表单对象，将 PDF 文档绑定到该对象，并将表单数据导出为 XML 文件。该代码自动从 PDF 表单中提取数据并以结构化的 XML 格式保存。

```python

    import aspose.pdf as apdf
    from io import FileIO
    from os import path
    import json
    from aspose.pycore import cast, is_assignable

    path_infile = path.join(self.dataDir, infile)
    path_outfile = path.join(self.dataDir, outfile)

    # Create Form object
    form = apdf.facades.Form()

    # Bind PDF document
    form.bind_pdf(path_infile)

    # Export data to XML file
    with FileIO(path_outfile, "w") as f:
        form.export_xml(f)
```

## 从 PDF 文件导出数据为 FDF

以下代码片段创建一个表单对象，将 PDF 文档绑定到该表单，然后将表单数据导出为 FDF（表单数据格式）文件。FDF 文件是一种用于存储 PDF 文档表单数据的格式，便于数据交换。

```python

    import aspose.pdf as apdf
    from io import FileIO
    from os import path
    import json
    from aspose.pycore import cast, is_assignable

    path_infile = path.join(self.dataDir, infile)
    path_outfile = path.join(self.dataDir, outfile)

    # Create Form object
    form = apdf.facades.Form()

    # Bind PDF document
    form.bind_pdf(path_infile)

    # Export form data to an FDF file
    with FileIO(path_outfile, "w") as f:
        form.export_fdf(f)
```

## 从 PDF 文件导出数据为 XFDF

```python

    import aspose.pdf as apdf
    from io import FileIO
    from os import path
    import json
    from aspose.pycore import cast, is_assignable

    path_infile = path.join(self.dataDir, infile)
    path_outfile = path.join(self.dataDir, outfile)

    # Create Form object
    form = apdf.facades.Form()

    # Bind PDF document
    form.bind_pdf(path_infile)

    # Export form data to an XFDF file
    with FileIO(path_outfile, "w") as f:
        form.export_xfdf(f)
```

