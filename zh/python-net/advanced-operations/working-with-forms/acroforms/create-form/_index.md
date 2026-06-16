---
title: 创建 AcroForm - 在 Python 中创建可填充 PDF
linktitle: 创建 AcroForm
type: docs
weight: 10
url: /zh/python-net/create-form/
description: 使用 Aspose.PDF for Python via .NET 从头创建 PDF 文档中的 AcroForm 字段。
lastmod: "2026-06-08"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 如何使用 Python 在 PDF 中创建 AcroForm
Abstract: 本文介绍了如何使用 Aspose.PDF for Python via .NET 在 PDF 文档中创建 AcroForm 字段。它涵盖了使用 TextBoxField 的基本字段创建、多部件文本框外观自定义，以及诸如单选按钮、组合框、复选框、列表框、签名字段和条形码字段等其他字段类型。这些示例帮助您构建交互式 PDF 表单，以进行数据收集和文档自动化工作流。
---

## 从头创建表单

### 在 PDF 文档中添加表单字段

这 [文档](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 类提供一个名为的集合 [Form](https://reference.aspose.com/pdf/python-net/aspose.pdf.forms/form/) 它帮助您管理 PDF 文档中的表单字段。

要添加表单字段：

1. 创建您想要添加的表单字段。
1. 调用 Form 集合的 [添加](https://reference.aspose.com/pdf/python-net/aspose.pdf.forms/form/#methods) 方法。

### 添加 TextBoxField

以下示例展示了如何添加一个 [文本框字段](https://reference.aspose.com/pdf/python-net/aspose.pdf.forms/textboxfield/).

```python
import aspose.pdf as ap
import aspose.pydrawing as drawing

def add_text_box_field(output_file_name):
    document = ap.Document()
    page = document.pages.add()

    rectangle = ap.Rectangle(10, 600, 110, 620, True)
    text_box_field = ap.forms.TextBoxField(page, rectangle)
    text_box_field.partial_name = "textbox1"
    text_box_field.value = "Text Box"

    text_box_field.default_appearance = ap.annotations.DefaultAppearance(
        "Arial", 10, drawing.Color.dark_blue
    )

    border = ap.annotations.Border(text_box_field)
    border.width = 1
    border.style = ap.annotations.BorderStyle.DASHED
    border.dash = ap.annotations.Dash(3, 3)
    text_box_field.border = border

    text_box_field.characteristics.border = ap.Color.red.to_rgb()
    text_box_field.characteristics.background = ap.Color.yellow.to_rgb()

    document.form.add(text_box_field, 1)
    document.save(output_file_name)
```

### PDF 中的多部件文本框字段

使用 Python 和 Aspose.PDF 在 PDF 中创建具有多个小部件外观的文本框表单字段。它在页面上放置多个文本输入区域，为每个小部件应用不同的字体和颜色，定制边框，并为交互式 PDF 表单设置背景样式。

1. 创建新 PDF 文档。
1. 定义文本字段位置。
1. 创建不同的默认外观。
1. 创建文本框字段。
1. 为每个小部件应用外观。
1. 自定义边框样式。
1. 向表单添加字段。
1. 保存 PDF 文件。

```python
import aspose.pdf as ap
import aspose.pydrawing as drawing

def add_text_box_field_nt(output_file_name):
    document = ap.Document()
    page = document.pages.add()

    rects = [
        ap.Rectangle(10, 600, 110, 620, normalize_coordinates=True),
        ap.Rectangle(10, 630, 110, 650, normalize_coordinates=True),
        ap.Rectangle(10, 660, 110, 680, normalize_coordinates=True),
    ]

    default_appearances = [
        ap.annotations.DefaultAppearance("Arial", 10, drawing.Color.dark_blue),
        ap.annotations.DefaultAppearance("Helvetica", 12, drawing.Color.dark_green),
        ap.annotations.DefaultAppearance(
            ap.text.FontRepository.find_font("Calibri"), 14, drawing.Color.dark_magenta
        ),
    ]

    text_box_field = ap.forms.TextBoxField(page, rects)
    text_box_field.partial_name = "textbox1"
    text_box_field.value = "Some text"

    for i, widget in enumerate(text_box_field):
        widget.default_appearance = default_appearances[i]

    border = ap.annotations.Border(text_box_field)
    border.width = 1
    border.style = ap.annotations.BorderStyle.DASHED
    border.dash = ap.annotations.Dash(3, 3)
    text_box_field.border = border

    text_box_field.characteristics.border = ap.Color.red.to_rgb()
    text_box_field.characteristics.background = ap.Color.yellow.to_rgb()

    document.form.add(text_box_field)
    document.save(output_file_name)
```

## 添加其他表单字段

下面的代码片段展示了如何添加各种字段类型，例如单选按钮、下拉框、复选框、列表框、签名字段和条形码字段。每个函数都会创建一个新的 PDF 文档，添加带有所选选项的目标字段，并保存更新后的文件。

1. 添加单选按钮字段
1. 添加组合框字段
1. 添加复选框字段
1. 添加列表框字段
1. 添加签名字段
1. 添加条形码字段

### 添加单选按钮字段

```python
import aspose.pdf as ap
import aspose.pydrawing as drawing

def add_radio_button(output_file_name):
    document = ap.Document()
    document.pages.add()

    radio = ap.forms.RadioButtonField(document.pages[1])
    radio.add_option(
        "Option 1", ap.Rectangle(100, 640, 120, 680, normalize_coordinates=True)
    )
    radio.add_option(
        "Option 2", ap.Rectangle(140, 640, 160, 680, normalize_coordinates=True)
    )

    document.form.add(radio)
    document.save(output_file_name)
```

### 添加组合框字段

```python
import aspose.pdf as ap
import aspose.pydrawing as drawing

def add_combo_box(output_file_name):
    document = ap.Document()
    page = document.pages.add()

    combo = ap.forms.ComboBoxField(
        page, ap.Rectangle(100, 640, 150, 656, normalize_coordinates=True)
    )
    combo.add_option("Red")
    combo.add_option("Yellow")
    combo.add_option("Green")
    combo.add_option("Blue")
    combo.selected = 3

    document.form.add(combo)
    document.save(output_file_name)
```

### 添加复选框字段

```python
import aspose.pdf as ap
import aspose.pydrawing as drawing

def add_checkbox_field_to_pdf(output_file_name):
    document = ap.Document()
    page = document.pages.add()

    checkbox = ap.forms.CheckboxField(
        page, ap.Rectangle(50, 620, 100, 650, normalize_coordinates=True)
    )
    checkbox.characteristics.background = ap.Color.aqua.to_rgb()
    checkbox.style = ap.forms.BoxStyle.CIRCLE

    document.form.add(checkbox)
    document.save(output_file_name)
```

### 添加列表框字段

```python
import aspose.pdf as ap
import aspose.pydrawing as drawing

def add_list_box_field_to_pdf(output_file_name):
    document = ap.Document()
    page = document.pages.add()

    list_box = ap.forms.ListBoxField(
        page, ap.Rectangle(50, 650, 100, 700, normalize_coordinates=True)
    )
    list_box.partial_name = "list"
    list_box.add_option("Red")
    list_box.add_option("Green")
    list_box.add_option("Blue")

    document.form.add(list_box)
    document.save(output_file_name)
```

### 添加签名字段

```python
import aspose.pdf as ap
import aspose.pydrawing as drawing

def add_signature_field(output_file_name):
    document = ap.Document()
    page = document.pages.add()

    signature_field = ap.forms.SignatureField(
        page, ap.Rectangle(100, 700, 200, 800, True)
    )
    signature_field.partial_name = "Signature1"
    document.form.add(signature_field)
    document.save(output_file_name)
```

### 添加条形码字段

```python
import aspose.pdf as ap
import aspose.pydrawing as drawing

def add_barcode_field(output_file_name):
    document = ap.Document()
    page = document.pages.add()

    barcode = ap.forms.BarcodeField(page, ap.Rectangle(100, 700, 200, 740, True))
    barcode.partial_name = "Barcode1"
    barcode.add_barcode("1234567890")
    document.form.add(barcode)
    document.save(output_file_name)
```

## 相关主题

- [填写 AcroForm](/pdf/zh/python-net/fill-form/)
- [提取 AcroForm](/pdf/zh/python-net/extract-form/)
- [修改 AcroForm](/pdf/zh/python-net/modifying-form/)
- [导入和导出表单数据](/pdf/zh/python-net/import-export-form-data/)
