---
title: 导入和导出表单数据
type: docs
weight: 80
url: /zh/python-net/import-export-form-data/
description: 本节解释如何导入和导出表单数据。
lastmod: "2025-08-05"
TechArticle: true
AlternativeHeadline: 使用 Aspose.PDF for Python via .NET 的导入和导出技术。
Abstract: 本汇编提供了使用 Aspose.PDF for Python via .NET 的表单数据导入和导出技术的完整套件。它涵盖了将 PDF 表单与包括 XML、FDF、XFDF 和 JSON 在内的外部数据格式集成的工作流。用户可以通过将结构化数据导入交互式字段来实现批量表单填写自动化，或导出字段值用于分析、备份或与其他系统集成。示例演示了如何绑定 PDF 表单、在不同格式之间转移数据并保存更新的文档，从而在各种应用中实现可扩展且一致的文档处理。
---

## 从 XML 文件导入表单数据

下面的示例演示了如何使用 Aspose.PDF for Python 将 XML 文件中的表单数据导入到现有的 PDF 表单中。通过绑定 PDF 表单、加载 XML 数据并保存更新后的文件，您可以快速填充交互式表单字段，而无需手动编辑每一页。该方法非常适合自动化批量表单填写、处理大型数据集以及确保多个文档之间的数据一致性。

使用以下步骤：

1. 使用 Aspose.PDF 创建 Form 对象。
1. 绑定 PDF 表单。
1. 加载 XML 数据。
1. 将 XML 导入 PDF。
1. 保存更新的 PDF。

```python

    from io import FileIO, StringIO
    import json
    from os import path
    import aspose.pdf as ap

    # Define the working directory path
    workdir_path = "/path/to/working/directory"

    # Construct full file paths using the working directory
    path_infile = path.join(workdir_path, infile)
    path_datafile = path.join(workdir_path, datafile)
    path_outfile = path.join(workdir_path, outfile)

    # Create a Form object from Aspose.PDF
    form = ap.facades.Form()

    # Bind the input PDF form
    form.bind_pdf(path_infile)

    # Import XML data into the form
    with FileIO(path_datafile, "r") as f:
        form.import_xml(f)

    # Save the form with imported data to a new PDF file
    form.save(path_outfile)
```

## 将 PDF 文档的表单字段数据导出为 XML 文件

Python 库演示了如何使用 Aspose.PDF for Python 将 PDF 文档的表单字段数据导出为 XML 文件。通过绑定 PDF 表单并以 XML 格式保存其字段值，您可以轻松地存储、处理或在其他应用或工作流中重用表单数据。此方法非常适合数据备份、分析以及与外部系统的集成。

使用以下步骤：

1. 使用 Aspose.PDF 创建 Form 对象。
1. 绑定 PDF 表单
1. 导出表单数据
1. 将字段值保存为 XML

```python

    from io import FileIO, StringIO
    import json
    from os import path
    import aspose.pdf as ap

    # Combine the working directory path with the input PDF file name
    path_infile = path.join(self.workdir_path, infile)

    # Combine the working directory path with the output XML file name
    path_outfile = path.join(self.workdir_path, datafile)

    # Create a Form object to work with PDF form fields
    form = ap.facades.Form()

    # Bind the PDF document containing the form
    form.bind_pdf(path_infile)

    # Open the XML file in write mode to store exported form data
    with FileIO(path_outfile, "w") as f:
        # Export form field data from the PDF to the XML file
        form.export_xml(f)
```

## 从 FDF 导入表单字段数据

‘import_data_from_fdf’ 方法将 FDF（表单数据格式）文件中的表单字段数据导入到现有的 PDF 表单并保存更新后的文档。此方法可用于在不修改文档结构的情况下，以编程方式预填充或更新 PDF 表单。

使用以下步骤：

1. 使用 Aspose.PDF 创建 Form 对象。
1. 绑定输入 PDF。
1. 使用 import_fdf() 导入表单数据。
1. 将包含导入数据的 PDF 保存到指定的输出文件路径。

```python

    from io import FileIO, StringIO
    import json
    from os import path
    import aspose.pdf as ap

    path_infile = path.join(self.workdir_path, infile)
    path_datafile = path.join(self.workdir_path, datafile)
    path_outfile = path.join(self.workdir_path, outfile)

    form = ap.facades.Form()
    form.bind_pdf(path_infile)

    with FileIO(path_datafile, "r") as f:
        form.import_fdf(f)
        form.save(path_outfile)
```

## 导出表单字段数据到 FDF

本示例演示了如何使用 Aspose.PDF for Python via .NET 将 PDF 文档的表单数据导出为 FDF（表单数据格式）文件。

1. 使用 Aspose.PDF 创建 Form 对象。
1. 绑定 PDF 文档。
1. 使用 export_fdf() 导出表单数据。

```python

    from io import FileIO, StringIO
    import json
    from os import path
    import aspose.pdf as ap

    path_infile = path.join(self.workdir_path, infile)
    path_outfile = path.join(self.workdir_path, outfile)

    # Create Form object
    form = ap.facades.Form()

    # Bind PDF document
    form.bind_pdf(path_infile)

    # Export form data to an FDF file
    with FileIO(path_outfile, "w") as f:
        form.export_fdf(f)
```

## 从 XFDF 导入表单字段数据

本示例将 PDF 文档的表单字段数据导出为 XFDF（XML 表单数据格式）文件，然后使用 Aspose.PDF for Python via .NET 保存更新的 PDF。

1. 使用 Aspose.PDF 创建 Form 对象。
1. 将 PDF 文档绑定到表单。
1. 将表单数据导出为 XFDF 文件。
1. 保存处理后的表单。

```python

    from io import FileIO, StringIO
    import json
    from os import path
    import aspose.pdf as ap

    path_infile = path.join(self.workdir_path, infile)
    path_datafile = path.join(self.workdir_path, datafile)
    path_outfile = path.join(self.workdir_path, outfile)

    # Create Form object
    form = ap.facades.Form()

    # Bind PDF document
    form.bind_pdf(path_infile)

    # Export form data to an XFDF file
    with FileIO(path_datafile, "w") as f:
        form.export_xfdf(f)
        form.save(path_outfile)
```

## 导出表单字段数据到 XFDF

此代码从 PDF 文档中提取表单字段数据，并使用 Aspose.PDF for Python 将其导出为 XFDF（XML 表单数据格式）文件。

1. 使用 Aspose.PDF 创建 Form 对象。
1. 将 PDF 文档绑定到表单。
1. 将表单数据导出为 FDF 文件。

```python

    from io import FileIO, StringIO
    import json
    from os import path
    import aspose.pdf as ap

    path_infile = path.join(self.workdir_path, infile)
    path_outfile = path.join(self.workdir_path, outfile)

    # Create Form object
    form = ap.facades.Form()

    # Bind PDF document
    form.bind_pdf(path_infile)

    # Export form data to an FDF file
    with FileIO(path_outfile, "w") as f:
        form.export_xfdf(f)
```

## 从另一个 PDF 导入数据

此代码片段演示了如何将表单字段数据从源 PDF 传输到目标 PDF。表单数据从源 PDF 导出为 XFDF 流，然后使用 Aspose.PDF for Python via .NET 导入到目标 PDF 中。

1. 使用 Aspose.PDF 创建 Form 对象。
1. 将 PDF 文档绑定到表单。
1. 从源 PDF 导出表单数据。
1. 将表单数据导入目标 PDF。
1. 保存已更新的目标 PDF。

```python

    from io import FileIO, StringIO
    import json
    from os import path
    import aspose.pdf as ap

    path_infile = path.join(self.workdir_path, infile)
    path_outfile = path.join(self.workdir_path, outfile)

    # Create Form object
    form_source = ap.facades.Form()
    form_dest = ap.facades.Form()

    # Bind PDF document
    form_source.bind_pdf(path_infile)
    form_dest.bind_pdf(path_outfile)

    # Export form data to an FDF file
    with StringIO() as f:
        form_source.export_xfdf(f)
        form_dest.import_xfdf(f)
        form_dest.save()
```

## 提取表单字段到 Json

此方法从输入文件中提取表单字段并将其导出到 JSON 文件。

1. 使用 Aspose.PDF 创建 Form 对象。
1. 使用 FileIO() 以写入模式打开输出文件。
1. 使用 form.export_json() 方法将表单字段导出到 JSON 文件。

```python

    from io import FileIO, StringIO
    import json
    from os import path
    import aspose.pdf as ap

    path_infile = path.join(self.workdir_path, infile)
    path_outfile = path.join(self.workdir_path, outfile)

    form = ap.facades.Form(path_infile)
    with FileIO(path_outfile, "w") as json_file:
        form.export_json(json_file, True)
```

## 提取表单字段到 JSON 文档

1. 从输入文件创建 Form 对象。
1. 初始化一个空字典以存储表单字段数据。
1. 遍历所有表单字段并提取其值。
1. 将表单数据字典序列化为具有 4 空格缩进的 JSON 字符串。
1. 使用 UTF-8 编码将 JSON 字符串写入输出文件。

```python

    from io import FileIO, StringIO
    import json
    from os import path
    import aspose.pdf as ap

    path_infile = path.join(self.workdir_path, infile)
    path_outfile = path.join(self.workdir_path, outfile)

    form = ap.facades.Form(path_infile)
    form_data = {}
    # Get values from all fields
    for formField in form.field_names:
        # Analyze names and values if needed
        form_data[formField] = form.get_field(formField)

    # Serialize to JSON
    json_string = json.dumps(form_data, indent=4)

    with open(path_outfile, "w", encoding="utf-8") as json_file:
        json_file.write(json_string)
```

