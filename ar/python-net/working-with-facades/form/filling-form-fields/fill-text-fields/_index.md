---
title: تعبئة الحقول النصية
linktitle: تعبئة الحقول النصية
type: docs
weight: 10
url: /ar/python-net/fill-text-fields/
description: يوضح هذا المثال كيفية ملء الحقول النصية تلقائيًا في نموذج PDF باستخدام Aspose.PDF لـ Python عبر .NET. يوضح كيفية تحميل مستند PDF وتعبئة حقول نموذج محددة بالاسم وحفظ الملف المحدث.
lastmod: "2026-06-11"
---

يسمح ملء الحقول النصية برمجيًا للتطبيقات بإعادة استخدام قوالب PDF وإدراج محتوى ديناميكي دون تحرير يدوي. في هذا المثال، [نموذج](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/form/) واجهة من [واجهات أسبوز.pdf](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/) يستخدم لربط نموذج PDF وتحديث حقول متعددة مثل الاسم والعنوان والبريد الإلكتروني. بعد تعيين القيم، يتم حفظ PDF المعدل كمستند جديد.

1. قم بتهيئة 'PDF_facades.form () 'لإدارة عمليات حقل النموذج.
1. استخدم 'bind_pdf () 'لإرفاق ملف PDF المدخل الذي يحتوي على حقول نصية.
1. اتصل بـ 'fill_field () 'لإدراج البيانات في حقول مثل الاسم والعنوان والبريد الإلكتروني.
1. احفظ ملف PDF المحدث.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Fill Text Fields
def fill_text_fields(infile, outfile):
    """Fill text fields in PDF form."""
    # Create Form object
    pdf_form = pdf_facades.Form()

    # Bind PDF document
    pdf_form.bind_pdf(infile)

    # Fill text fields by name
    pdf_form.fill_field("name", "John Doe")
    pdf_form.fill_field("address", "123 Main St, Anytown, USA")
    pdf_form.fill_field("email", "john.doe@example.com")

    # Save updated PDF
    pdf_form.save(outfile)
```
