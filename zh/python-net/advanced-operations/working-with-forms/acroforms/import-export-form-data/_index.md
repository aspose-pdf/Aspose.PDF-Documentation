---
title: 导入和导出表单数据
linktitle: 导入和导出表单数据
type: docs
weight: 80
url: /zh/python-net/import-export-form-data/
description: 使用 Aspose.PDF for Python via .NET 导入和导出 AcroForm 字段数据，支持 XML、FDF、XFDF 和 JSON 格式。
lastmod: "2026-06-08"
TechArticle: true
AlternativeHeadline: 使用 Aspose.PDF for Python via .NET 的导入和导出技术。
Abstract: 本汇编呈现了一套使用 Aspose.PDF for Python via .NET 的表单数据导入导出技术的完整方案。它涵盖了将 PDF 表单与包括 XML、FDF、XFDF 和 JSON 在内的外部数据格式集成的工作流。用户可以通过将结构化数据导入交互式字段来实现批量表单填充自动化，或提取字段值用于分析、备份或与其他系统的集成。示例展示了如何绑定 PDF 表单、在不同格式之间传输数据以及保存更新后的文档，从而在各种应用中实现可扩展且一致的文档处理。
---

此页面展示了使用 Aspose.PDF for Python via .NET 导入和导出 AcroForm 数据的常见工作流。所有操作使用 [Form](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/form/) 外观。

## 从 XML 导入表单字段数据

使用此方法从外部 XML 数据填充 PDF 表单。

1. 创建一个 `Form` 对象。
1. 绑定输入 PDF。
1. 打开 XML 数据文件。
1. 将 XML 数据导入表单。
1. 保存更新后的 PDF。

```python
from io import FileIO
import aspose.pdf as ap

def import_data_from_xml(input_file_name, data_file_name, output_file_name):
    form = ap.facades.Form()
    form.bind_pdf(input_file_name)

    with FileIO(data_file_name, "r") as f:
        form.import_xml(f)

    form.save(output_file_name)
```

## 将表单字段数据导出为 XML

此方法将 PDF 文档中的 FormField 值导出为 XML。

1. 创建一个 `Form` 对象。
1. 绑定输入 PDF。
1. 打开 XML 输出文件。
1. 将表单数据导出为 XML。

```python
from io import FileIO
import aspose.pdf as ap

def export_data_to_xml(input_file_name, output_file_name):
    form = ap.facades.Form()
    form.bind_pdf(input_file_name)
    with FileIO(output_file_name, "w") as f:
        form.export_xml(f)
```

## 从 FDF 导入表单字段数据

这 `import_data_from_fdf` 方法将表单字段数据从 FDF（Forms Data Format）文件导入到 PDF 表单中。

1. 创建一个 `Form` 对象。
1. 绑定输入 PDF。
1. 使用导入表单数据 `import_fdf()`.
1. 保存更新后的 PDF。

```python
from io import FileIO
import aspose.pdf as ap

def import_data_from_fdf(input_file_name, data_file_name, output_file_name):
    form = ap.facades.Form()
    form.bind_pdf(input_file_name)

    with FileIO(data_file_name, "r") as f:
        form.import_fdf(f)
        form.save(output_file_name)
```

## 导出表单字段数据到 FDF

此示例将 PDF 文档中的表单数据导出到 FDF 文件。

1. 创建一个 `Form` 对象。
1. 绑定 PDF 文档。
1. 导出表单数据使用 `export_fdf()`.

```python
from io import FileIO
import aspose.pdf as ap

def export_data_to_fdf(input_file_name, output_file_name):
    form = ap.facades.Form()
    form.bind_pdf(input_file_name)

    with FileIO(output_file_name, "w") as f:
        form.export_fdf(f)
```

## 从XFDF导入表单字段数据

使用此方法将表单字段数据从 XFDF（XML 表单数据格式）文件导入到 PDF 表单中。

1. 创建一个 `Form` 对象。
1. 绑定输入 PDF。
1. 从 XFDF 文件导入表单数据。
1. 保存更新后的 PDF。

```python
from io import FileIO
import aspose.pdf as ap

def import_data_from_xfdf(input_file_name, data_file_name, output_file_name):
    form = ap.facades.Form()
    form.bind_pdf(input_file_name)

    with FileIO(data_file_name, "r") as f:
        form.import_xfdf(f)
        form.save(output_file_name)
```

## 导出表单字段数据到 XFDF

此代码将 PDF 文档中的表单字段数据导出到 XFDF 文件。

1. 创建一个 `Form` 对象。
1. 绑定输入 PDF。
1. 将表单数据导出为 XFDF。

```python
from io import FileIO
import aspose.pdf as ap

def export_data_to_xfdf(input_file_name, output_file_name):
    form = ap.facades.Form()
    form.bind_pdf(input_file_name)

    with FileIO(output_file_name, "w") as f:
        form.export_xfdf(f)
```

## 从另一个 PDF 导入数据

此示例通过将 XFDF 导出到内存流并将其导入目标表单，将表单字段数据从源 PDF 传输到目标 PDF。

1. 创建源和目标 `Form` 对象。
1. 绑定源 PDF 和目标 PDF。
1. 从源 PDF 导出表单数据。
1. 将表单数据导入目标 PDF。
1. 保存已更新的目标 PDF。

```python
from io import StringIO
import aspose.pdf as ap

def import_data_from_another_pdf(source_pdf_name, destination_pdf_name, output_file_name):
    form_source = ap.facades.Form()
    form_dest = ap.facades.Form()

    form_source.bind_pdf(source_pdf_name)
    form_dest.bind_pdf(destination_pdf_name)

    with StringIO() as xfdf_stream:
        form_source.export_xfdf(xfdf_stream)
        xfdf_stream.seek(0)
        form_dest.import_xfdf(xfdf_stream)

    form_dest.save(output_file_name)
```

## 提取表单字段为 JSON

此方法通过使用将表单字段导出为JSON文件。 `export_json()`.

1. 创建一个 `Form` 对象。
1. 打开 JSON 输出文件。
1. 通过使用导出表单字段 `export_json()`.

```python
from io import FileIO
import aspose.pdf as ap

def extract_form_fields_to_json(input_file_name, output_file_name):
    form = ap.facades.Form(input_file_name)
    with FileIO(output_file_name, "w") as json_file:
        form.export_json(json_file, True)
```

## 提取表单字段为 JSON 文档

此示例从表单字段名称和值创建自定义 JSON 文档。

1. 从输入文件创建 Form 对象。
1. 初始化一个空字典以存储表单字段数据。
1. 遍历所有表单字段并提取它们的值。
1. 将表单数据字典序列化为带有 4 空格缩进的 JSON 字符串。
1. 将 JSON 字符串以 UTF-8 编码写入输出文件。

```python
import json
import aspose.pdf as ap

def extract_form_fields_to_json_doc(input_file_name, output_file_name):
    form = ap.facades.Form(input_file_name)
    form_data = {}
    for field_name in form.field_names:
        form_data[field_name] = form.get_field(field_name)

    json_string = json.dumps(form_data, indent=4)

    with open(output_file_name, "w", encoding="utf-8") as json_file:
        json_file.write(json_string)
```

## 相关主题（外观方法）

- [导入 XML 数据](/pdf/zh/python-net/import-xml-data/)
- [导入 FDF 数据](/pdf/zh/python-net/import-fdf-data/)
- [导入 XFDF 数据](/pdf/zh/python-net/import-xfdf-data/)
- [导入 JSON 数据](/pdf/zh/python-net/import-json-data/)
- [导出为 XML](/pdf/zh/python-net/export-to-xml/)
- [导出为 FDF](/pdf/zh/python-net/export-to-fdf/)
- [导出为 XFDF](/pdf/zh/python-net/export-to-xfdf/)
- [导出为 JSON](/pdf/zh/python-net/export-to-json/)
