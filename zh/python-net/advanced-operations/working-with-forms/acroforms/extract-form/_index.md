---
title: 提取 AcroForm - 在 Python 中提取 PDF 表单数据
linktitle: 提取 AcroForm
type: docs
weight: 30
url: /zh/python-net/extract-form/
description: 通过使用 Aspose.PDF for Python via .NET，从 PDF 文档的 AcroForm 字段中提取值。
lastmod: "2026-06-08"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 如何使用 Python 从 PDF 获取表单数据
Abstract: 本文展示了如何通过使用 Aspose.PDF for Python via .NET，从 PDF 文档的 AcroForm 字段中提取数据。示例遍历表单字段名称，使用 Form 门面读取值，并返回一个字典以供后续处理。此工作流对于报告、验证以及与外部系统的集成非常有用。
---

## 提取表单数据

### 获取 PDF 文档中所有字段的值

要读取 PDF 文档中所有字段的值，遍历表单字段名称并从中检索每个值 [Form](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/form/) 外观。

使用以下步骤：

1. 将输入 PDF 绑定到 a `Form` 对象。
1. 遍历 `field_names`.
1. 使用以下方式读取每个值 `get_field()`.
1. 将值存储在字典中。
1. 返回或处理提取的值。

下面的 Python 代码片段展示了此方法。

```python
import aspose.pdf as ap


def get_values_from_all_fields(input_file_name):
    form = ap.facades.Form(input_file_name)

    form_values = {}
    for field_name in form.field_names:
        form_values[field_name] = form.get_field(field_name)

    print(form_values)
    return form_values
```

## 相关主题

- [创建 AcroForm](/pdf/zh/python-net/create-form/)
- [填写 AcroForm](/pdf/zh/python-net/fill-form/)
- [导入和导出表单数据](/pdf/zh/python-net/import-export-form-data/)
- [修改 AcroForm](/pdf/zh/python-net/modifying-form/)