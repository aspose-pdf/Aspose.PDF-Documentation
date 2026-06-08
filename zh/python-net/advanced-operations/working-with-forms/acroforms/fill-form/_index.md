---
title: 填写 AcroForm - 使用 Python 填写 PDF 表单
linktitle: 填写 AcroForm
type: docs
weight: 20
url: /zh/python-net/fill-form/
description: 使用 Aspose.PDF for Python via .NET 在 PDF 文档中填写 AcroForm 字段。
lastmod: "2026-06-08"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 如何使用 Python 填写 PDF 表单字段
Abstract: 本文解释了如何使用 Aspose.PDF for Python via .NET 在 PDF 文档中填写 AcroForm 字段。示例使用 Form 门面，将字段名称映射到字典中的新值，更新匹配的字段，并保存输出 PDF。此方法适用于自动化文档完成工作流和批量表单处理。
---

## 在 PDF 文档中填写 Form 字段

以下示例通过使用 the [Form](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/form/) 外观。

使用以下步骤：

1. 创建一个包含字段名称和值的字典。
1. 将输入 PDF 绑定到 Form 对象。
1. 遍历可用的表单字段。
1. 填充字典中存在的字段。
1. 保存更新后的 PDF。

```python
import aspose.pdf as ap

def fill_form(input_file_name, output_file_name):
    new_field_values = {
        "First Name": "Alexander_New",
        "Last Name": "Greenfield_New",
        "City": "Yellowtown_New",
        "Country": "Redland_New",
    }

    form = ap.facades.Form(input_file_name)

    for field_name in form.field_names:
        if field_name in new_field_values:
            form.fill_field(field_name, new_field_values[field_name])

    form.save(output_file_name)
```

## 相关主题

- [创建 AcroForm](/pdf/zh/python-net/create-form/)
- [提取 AcroForm](/pdf/zh/python-net/extract-form/)
- [导入和导出表单数据](/pdf/zh/python-net/import-export-form-data/)