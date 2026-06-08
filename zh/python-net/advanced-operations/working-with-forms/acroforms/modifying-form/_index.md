---
title: 修改 AcroForm
linktitle: 修改 AcroForm
type: docs
weight: 45
url: /zh/python-net/modifying-form/
description: 使用 Aspose.PDF for Python via .NET 修改 PDF 文档中的 AcroForm 字段，包括清除文本、设置限制、设置字段样式以及删除字段。
lastmod: "2026-06-08"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 管理和自定义 PDF 表单字段
Abstract: 本文提供了使用 Aspose.PDF for Python via .NET 修改 AcroForm 字段的实际示例。内容涵盖清除打字机表单内容中的文本、设置和读取文本字段的字符限制、应用自定义字体外观以及按名称删除字段。这些工作流支持在自动化 PDF 处理流水线中进行常见的表单维护任务。
---

## 在表单中清除文本

此示例演示了如何使用 Aspose.PDF for Python via .NET 清除 PDF 中 Typewriter 表单字段的文本。它会扫描 PDF 的首页，识别 Typewriter 表单，删除其内容，并保存更新后的文档。此方法对于在重新分发 PDF 之前重置或清理表单字段非常有用。

1. 加载输入的 PDF 文档。
1. 访问第一页上的表单。
1. 遍历每个表单并检查它是否为 `Typewriter` 表单。
1. 使用 TextFragmentAbsorber 在表单中查找文本片段。
1. 清除每个片段的文本。
1. 将修改后的 PDF 保存到输出文件。

```python
import aspose.pdf as ap


def clear_text_in_form(input_file_name, output_file_name):
    document = ap.Document(input_file_name)

    forms = document.pages[1].resources.forms

    for form in forms:
        if form.it == "Typewriter" and form.subtype == "Form":
            absorber = ap.text.TextFragmentAbsorber()
            absorber.visit(form)

            for fragment in absorber.text_fragments:
                fragment.text = ""

    document.save(output_file_name)
```

## 设置字段限制

使用 `set_field_limit(field, limit)` 从 `FormEditor` 定义文本字段允许的最大字符数。

1. 创建一个 `FormEditor` 对象。
1. 绑定输入 PDF。
1. 为目标字段设置字段限制。
1. 保存更新后的 PDF。

```python
import aspose.pdf as ap


def set_field_limit(input_file_name, output_file_name):
    form = ap.facades.FormEditor()
    form.bind_pdf(input_file_name)
    form.set_field_limit("First Name", 15)
    form.save(output_file_name)
```

## 获取字段限制

您也可以从文本字段读取字符限制。

1. 加载 PDF 文档。
1. 访问目标表单字段。
1. 确保该字段是 `TextBoxField`.
1. 读取并打印 `max_len`.

```python
import aspose.pdf as ap
from aspose.pycore import cast, is_assignable


def get_field_limit(input_file_name):
    document = ap.Document(input_file_name)
    if is_assignable(document.form[1], ap.forms.TextBoxField):
        text_box_field = cast(ap.forms.TextBoxField, document.form[1])
        print(f"Limit: {text_box_field.max_len}")
```

## 为表单字段设置自定义字体

此示例为文本框字段设置自定义默认外观，包括字体、大小和颜色。

1. 加载 PDF 文档。
1. 访问目标字段并验证其类型。
1. 在...中查找字体 `FontRepository`.
1. 应用新的 `DefaultAppearance`.
1. 保存更新后的 PDF。

```python
import aspose.pdf as ap
from aspose.pycore import cast, is_assignable


def set_form_field_font(input_file_name, output_file_name):
    document = ap.Document(input_file_name)
    if is_assignable(document.form[1], ap.forms.TextBoxField):
        text_box_field = cast(ap.forms.TextBoxField, document.form[1])
        font = ap.text.FontRepository.find_font("Calibri")
        text_box_field.default_appearance = ap.annotations.DefaultAppearance(
            font, 10, ap.Color.black.to_rgb()
        )

    document.save(output_file_name)
```

## 删除现有表单中的字段

此代码通过名称从 PDF 文档中删除特定的表单字段，并使用 Aspose.PDF for Python via .NET 保存更新后的文件。

1. 加载 PDF 文档。
1. 按名称删除表单字段。
1. 保存更新后的 PDF。

```python
import aspose.pdf as ap


def delete_form_field(input_file_name, output_file_name):
    document = ap.Document(input_file_name)
    document.form.delete("First Name")
    document.save(output_file_name)
```

## 相关主题

- [创建 AcroForm](/pdf/zh/python-net/create-form/)
- [填写 AcroForm](/pdf/zh/python-net/fill-form/)
- [提取 AcroForm](/pdf/zh/python-net/extract-form/)
- [导入和导出表单数据](/pdf/zh/python-net/import-export-form-data/)
