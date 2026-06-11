---
title: إنشاء AcroForm - إنشاء ملف PDF قابل للتعبئة في Python
linktitle: إنشاء نموذج أكروفورم
type: docs
weight: 10
url: /ar/python-net/create-form/
description: قم بإنشاء حقول AcroForm من البداية في مستندات PDF باستخدام Aspose.PDF لبيثون عبر .NET.
lastmod: "2026-06-11"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: كيفية إنشاء أكروفورم في PDF باستخدام بايثون
Abstract: تشرح هذه المقالة كيفية إنشاء حقول AcroForm في مستندات PDF باستخدام Aspose.PDF لـ Python عبر .NET. ويغطي إنشاء الحقول الأساسية باستخدام TextBoxField، وتخصيص مظهر مربع النص متعدد الأدوات، وأنواع الحقول الإضافية مثل أزرار الاختيار، ومربعات التحرير، ومربعات الاختيار، ومربعات القوائم، وحقول التوقيع، وحقول الباركود. تساعدك هذه الأمثلة على إنشاء نماذج PDF تفاعلية لجمع البيانات وسير عمل التشغيل الآلي للمستندات.
---

## إنشاء نموذج من الصفر

### إضافة حقل نموذج في مستند PDF

ال [مستند](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) يوفر الفصل مجموعة مسماة [نموذج](https://reference.aspose.com/pdf/python-net/aspose.pdf.forms/form/) مما يساعدك على إدارة حقول النموذج في مستند PDF.

لإضافة حقل نموذج:

1. قم بإنشاء حقل النموذج الذي تريد إضافته.
1. اتصل بمجموعة النماذج [اضاف](https://reference.aspose.com/pdf/python-net/aspose.pdf.forms/form/#methods) طريقة.

### إضافة حقل مربع النص

يوضح المثال التالي كيفية إضافة ملف [حقل مربع النص](https://reference.aspose.com/pdf/python-net/aspose.pdf.forms/textboxfield/).

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

### حقل مربع نص متعدد الأدوات في PDF

قم بإنشاء حقل نموذج مربع نص مع ظهور عناصر واجهة مستخدم متعددة في PDF باستخدام Python و Aspose.PDF. يضع العديد من مناطق إدخال النص على الصفحة، ويطبق خطوطًا وألوانًا مختلفة على كل عنصر واجهة مستخدم، ويخصص الحدود، ويعين تصميم الخلفية لنموذج PDF تفاعلي.

1. قم بإنشاء مستند PDF جديد.
1. حدد مواضع حقول النص.
1. قم بإنشاء مظاهر افتراضية مختلفة.
1. إنشاء حقل مربع نص.
1. قم بتطبيق المظهر على كل عنصر واجهة مستخدم.
1. تخصيص نمط الحدود.
1. إضافة حقل إلى النموذج.
1. احفظ ملف PDF.

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

## إضافة حقول نموذج أخرى

توضح مقتطفات التعليمات البرمجية التالية كيفية إضافة أنواع حقول مختلفة، مثل أزرار الاختيار ومربعات التحرير ومربعات الاختيار ومربعات القوائم وحقول التوقيع وحقول الباركود. تقوم كل وظيفة بإنشاء مستند PDF جديد وإضافة حقل هدف بخيارات محددة وحفظ الملف المحدث.

1. إضافة حقل زر الراديو
1. إضافة حقل كومبو بوكس
1. إضافة حقل مربع الاختيار
1. إضافة حقل مربع قائمة
1. إضافة حقل توقيع
1. إضافة حقل باركود

### إضافة حقل زر الراديو

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

### إضافة حقل كومبو بوكس

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

### إضافة حقل مربع الاختيار

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

### إضافة حقل مربع قائمة

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

### إضافة حقل توقيع

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

### إضافة حقل باركود

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

## موضوعات ذات صلة

- [املأ نموذج أكروفورم](/pdf/ar/python-net/fill-form/)
- [استخراج أكروفورم](/pdf/ar/python-net/extract-form/)
- [تعديل أكروفورم](/pdf/ar/python-net/modifying-form/)
- [استيراد وتصدير بيانات النموذج](/pdf/ar/python-net/import-export-form-data/)
