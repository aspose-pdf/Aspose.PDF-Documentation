---
title: 使用 Python 从 AcroForm 提取数据
linktitle: 从 AcroForm 提取数据
type: docs
weight: 50
url: /zh/python-net/extract-data-from-acroform/
description: Aspose.PDF 让从 PDF 文件中提取表单字段数据变得简单。了解如何从 AcroForms 提取数据并将其保存为 JSON、XML 或 FDF 格式。
lastmod: "2026-06-08"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 如何通过 Python 提取 AcroForm 数据
Abstract: 本文提供了使用 Aspose.PDF for Python 管理 PDF 文档中表单字段的综合指南。它详细说明了从 PDF 中提取、操作和导出表单数据的各种方法。文章首先演示如何提取表单字段值并将其存入字典，随后以 JSON 格式输出数据。进一步展示了将表单数据直接导出为 JSON 文件，以增强数据序列化能力。此外，本文还涵盖了将表单数据导出为 XML、FDF（Forms Data Format）和 XFDF 等其他格式，这些格式有助于数据交换和结构化数据存储。每个章节都包含 Python 代码片段，以帮助理解和实现。总体而言，本文是希望在 Python 应用中集成 PDF 表单处理的开发者的实用资源。
---

## 从 PDF 文档中提取表单字段

[Form](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/form) 来自 `aspose.pdf.facades` namespace 提供了一种直接的方法来读取 AcroForm 字段数据，而无需打开完整的文档对象模型。遍历 `form.field_names` 要获取表单中出现的每个字段名称，然后调用 `form.get_field(name)` 检索其当前值。

1. 构建一个 `Form` 通过传递输入文件路径来创建对象。
1. 遍历 `form.field_names` 枚举所有字段名称。
1. 调用 `form.get_field(name)` 对每个名称，将结果存储在字典中。

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

## 通过标题获取表单字段值

当您知道 PDF 表单中定义的确切字段名称（title）时，您可以直接使用 `form.get_field(name)` 无需遍历整个字段集合。当仅需要特定字段时，这是最快的方法。

1. 构建一个 [Form](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/form) 包含输入文件路径的对象。
1. 调用 `form.get_field("FieldName")` 使用 PDF 中出现的确切字段标题。
1. 在您的应用程序中根据需要使用返回的字符串值。

```python

    import aspose.pdf as apdf

    form = apdf.facades.Form(path_infile)

    # Retrieve a single field value by its name
    value = form.get_field("FirstName")
    print(value)
```

## 从 PDF 文档中提取表单字段为 JSON

有两种方法可以将 AcroForm 数据导出为 JSON。第一种使用内置的 `export_json` 方法 在 [Form](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/form), 将所有字段数据直接序列化到文件流中，一次调用完成。

1. 构建一个 `Form` 包含输入文件路径的对象。
1. 使用二进制流打开输出文件 `FileIO`.
1. 调用 `form.export_json(stream, True)` 编写 JSON 输出。

```python

    import aspose.pdf as apdf
    from io import FileIO
    from os import path

    path_infile = path.join(self.dataDir, infile)
    path_outfile = path.join(self.dataDir, outfile)

    form = apdf.facades.Form(path_infile)
    with FileIO(path_outfile, "w") as json_file:
        form.export_json(json_file, True)
```

第二种方法从...构建一个 Python 字典 `field_names` 和 `get_field`，然后使用它进行序列化 `json.dumps`. 在需要在写入之前转换或过滤数据时使用它。

1. 遍历 `form.field_names` 并用字段值填充字典。
1. 使用以下方式序列化字典 `json.dumps(form_data, indent=4)`.
1. 将结果 JSON 字符串写入输出文件。

```python

    import aspose.pdf as apdf
    from os import path
    import json

    path_infile = path.join(self.dataDir, infile)
    path_outfile = path.join(self.dataDir, outfile)

    form = apdf.facades.Form(path_infile)
    form_data = {}
    # Get values from all fields
    for formField in form.field_names:
        form_data[formField] = form.get_field(formField)

    # Serialize to JSON
    json_string = json.dumps(form_data, indent=4)
    print(json_string)

    with open(path_outfile, "w", encoding="utf-8") as json_file:
        json_file.write(json_string)
```

## 从 PDF 文件提取数据到 XML

XML 导出对于将 PDF 表单数据与使用结构化 XML 提要或模式的系统集成非常有用。该 [Form](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/form) 类提供 `export_xml` 一次完成转换。

1. 创建一个 `Form` 实例并将 PDF 与之绑定 `form.bind_pdf(path)`.
1. 以二进制流打开输出文件。
1. 调用 `form.export_xml(stream)` 将所有字段数据写入 XML。

```python

    import aspose.pdf as apdf
    from io import FileIO
    from os import path

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

## 从PDF文件导出数据到FDF

FDF（表单数据格式）是 AcroForm 数据的标准交换格式，广泛得到 PDF 查看器和处理工具的支持。使用 `export_fdf` 在 [Form](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/form) 用于生成可独立的 FDF 文件的类，该文件可以导入回原始 PDF 或其他兼容的表单。

1. 创建一个 `Form` 实例并将源 PDF 绑定到 `form.bind_pdf(path)`.
1. 以二进制流打开输出文件。
1. 调用 `form.export_fdf(stream)` 写入 FDF 数据。

```python

    import aspose.pdf as apdf
    from io import FileIO
    from os import path

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

## 从 PDF 文件导出数据到 XFDF

XFDF（XML Forms Data Format）是基于 XML 的 FDF 的后继者，更适合在 Web 服务和现代数据管道中使用。和 FDF 一样，XFDF 文件可以导入回兼容的 PDF 表单。使用 `export_xfdf` 在 [Form](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/form) 生成输出的类。

1. 创建一个 `Form` 实例并将源 PDF 绑定到 `form.bind_pdf(path)`.
1. 以二进制流打开输出文件。
1. 调用 `form.export_xfdf(stream)` 编写 XFDF 数据。

```python

    import aspose.pdf as apdf
    from io import FileIO
    from os import path

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
