---
title: استيراد وتصدير بيانات النموذج
linktitle: استيراد وتصدير بيانات النموذج
type: docs
weight: 80
url: /ar/python-net/import-export-form-data/
description: قم باستيراد وتصدير بيانات حقل AcroForm بتنسيقات XML و FDF و XFDF و JSON باستخدام Aspose.PDF لبيثون عبر .NET.
lastmod: "2026-06-11"
TechArticle: true
AlternativeHeadline: تقنيات الاستيراد والتصدير باستخدام Aspose.PDF لبيثون عبر.NET.
Abstract: يقدم هذا التجميع مجموعة شاملة من تقنيات استيراد وتصدير بيانات النموذج باستخدام Aspose.PDF لـ Python عبر .NET. ويغطي عمليات سير العمل لدمج نماذج PDF مع تنسيقات البيانات الخارجية بما في ذلك XML و FDF و XFDF و JSON. يمكن للمستخدمين أتمتة تعبئة النماذج المجمعة عن طريق استيراد البيانات المهيكلة إلى الحقول التفاعلية، أو استخراج قيم الحقول للتحليل أو النسخ الاحتياطي أو التكامل مع الأنظمة الأخرى. توضح الأمثلة كيفية ربط نماذج PDF ونقل البيانات بين التنسيقات وحفظ المستندات المحدثة، مما يتيح معالجة المستندات القابلة للتطوير والمتسقة عبر تطبيقات متنوعة.
---

تعرض هذه الصفحة عمليات سير العمل الشائعة لاستيراد وتصدير بيانات AcroForm باستخدام Aspose.PDF لـ Python عبر .NET. تستخدم جميع العمليات [نموذج](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/form/) واجهة.

## استيراد بيانات حقل النموذج من XML

استخدم هذا الأسلوب لتعبئة نموذج PDF من بيانات XML الخارجية.

1. قم بإنشاء `Form` كائن.
1. قم بربط ملف PDF المدخل.
1. افتح ملف بيانات XML.
1. قم باستيراد بيانات XML إلى النموذج.
1. احفظ ملف PDF المحدث.

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

## تصدير بيانات حقل النموذج إلى XML

تقوم هذه الطريقة بتصدير قيم حقول النموذج من وثيقة PDF إلى XML.

1. قم بإنشاء `Form` كائن.
1. قم بربط ملف PDF المدخل.
1. افتح ملف إخراج XML.
1. تصدير بيانات النموذج إلى XML.

```python
from io import FileIO
import aspose.pdf as ap

def export_data_to_xml(input_file_name, output_file_name):
    form = ap.facades.Form()
    form.bind_pdf(input_file_name)
    with FileIO(output_file_name, "w") as f:
        form.export_xml(f)
```

## استيراد بيانات حقل النموذج من FDF

ال `import_data_from_fdf` تقوم الطريقة باستيراد بيانات حقل النموذج من ملف FDF (تنسيق بيانات النماذج) إلى نموذج PDF.

1. قم بإنشاء `Form` كائن.
1. قم بربط ملف PDF المدخل.
1. قم باستيراد بيانات النموذج باستخدام `import_fdf()`.
1. احفظ ملف PDF المحدث.

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

## تصدير بيانات حقل النموذج إلى FDF

يقوم هذا المثال بتصدير بيانات النموذج من وثيقة PDF إلى ملف FDF.

1. قم بإنشاء `Form` كائن.
1. قم بربط وثيقة PDF.
1. تصدير بيانات النموذج باستخدام `export_fdf()`.

```python
from io import FileIO
import aspose.pdf as ap

def export_data_to_fdf(input_file_name, output_file_name):
    form = ap.facades.Form()
    form.bind_pdf(input_file_name)

    with FileIO(output_file_name, "w") as f:
        form.export_fdf(f)
```

## استيراد بيانات حقل النموذج من XFDF

استخدم هذه الطريقة لاستيراد بيانات حقل النموذج من ملف XFDF (تنسيق بيانات نماذج XML) إلى نموذج PDF.

1. قم بإنشاء `Form` كائن.
1. قم بربط ملف PDF المدخل.
1. استيراد بيانات النموذج من ملف XFDF.
1. احفظ ملف PDF المحدث.

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

## تصدير بيانات حقل النموذج إلى XFDF

يقوم هذا الرمز بتصدير بيانات حقل النموذج من مستند PDF إلى ملف XFDF.

1. قم بإنشاء `Form` كائن.
1. قم بربط ملف PDF المدخل.
1. تصدير بيانات النموذج إلى XFDF.

```python
from io import FileIO
import aspose.pdf as ap

def export_data_to_xfdf(input_file_name, output_file_name):
    form = ap.facades.Form()
    form.bind_pdf(input_file_name)

    with FileIO(output_file_name, "w") as f:
        form.export_xfdf(f)
```

## استيراد البيانات من PDF آخر

ينقل هذا المثال بيانات حقل النموذج من PDF المصدر إلى PDF الوجهة عن طريق تصدير XFDF إلى دفق داخل الذاكرة واستيراده إلى النموذج الهدف.

1. إنشاء المصدر والوجهة `Form` الكائنات.
1. قم بربط ملفات PDF المصدر والوجهة.
1. تصدير بيانات النموذج من مصدر PDF.
1. قم باستيراد بيانات النموذج إلى PDF الوجهة.
1. احفظ ملف PDF الوجهة المحدّث.

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

## استخراج حقول النموذج إلى JSON

تقوم هذه الطريقة بتصدير حقول النموذج إلى ملف JSON باستخدام `export_json()`.

1. قم بإنشاء `Form` كائن.
1. افتح ملف إخراج JSON.
1. تصدير حقول النموذج باستخدام `export_json()`.

```python
from io import FileIO
import aspose.pdf as ap

def extract_form_fields_to_json(input_file_name, output_file_name):
    form = ap.facades.Form(input_file_name)
    with FileIO(output_file_name, "w") as json_file:
        form.export_json(json_file, True)
```

## استخراج حقول النموذج إلى مستند JSON

يقوم هذا المثال بإنشاء مستند JSON مخصص من أسماء حقول النموذج والقيم.

1. قم بإنشاء كائن نموذج من ملف الإدخال.
1. قم بتهيئة قاموس فارغ لتخزين بيانات حقل النموذج.
1. قم بالتكرار في جميع حقول النموذج واستخرج قيمها.
1. قم بتسلسل قاموس بيانات النموذج إلى سلسلة JSON ذات المسافة البادئة المكونة من 4 مسافات.
1. اكتب سلسلة JSON إلى ملف الإخراج بترميز UTF-8.

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

## موضوعات ذات صلة (نهج الواجهات)

- [استيراد بيانات XML](/pdf/ar/python-net/import-xml-data/)
- [استيراد بيانات FDF](/pdf/ar/python-net/import-fdf-data/)
- [استيراد بيانات XFDF](/pdf/ar/python-net/import-xfdf-data/)
- [استيراد بيانات JSON](/pdf/ar/python-net/import-json-data/)
- [تصدير إلى XML](/pdf/ar/python-net/export-to-xml/)
- [تصدير إلى FDF](/pdf/ar/python-net/export-to-fdf/)
- [التصدير إلى XFDF](/pdf/ar/python-net/export-to-xfdf/)
- [تصدير إلى JSON](/pdf/ar/python-net/export-to-json/)
