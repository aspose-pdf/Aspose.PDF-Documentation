---
title: املأ حقول زر الراديو
linktitle: املأ حقول زر الراديو
type: docs
weight: 30
url: /ar/python-net/fill-radio-button-fields/
description: يوضح هذا المثال كيفية ملء حقول أزرار الاختيار برمجيًا في نموذج PDF باستخدام Aspose.PDF لـ Python عبر .NET. يوضح كيفية ربط مستند PDF وتحديد خيار زر الاختيار حسب الفهرس وحفظ الملف المحدث.
lastmod: "2026-06-11"
---

تسمح أزرار الاختيار للمستخدمين بتحديد خيار واحد من مجموعة محددة مسبقًا، مثل حقول الجنس أو التفضيلات. في هذا المثال، [نموذج](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/form/) واجهة من [واجهات أسبوز.pdf](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/) يتم استخدام الوحدة لربط PDF المصدر وتعيين خيار محدد بقيمة الفهرس الخاصة به. بمجرد اختيار الخيار المطلوب، يتم حفظ المستند المعدل.

1. قم بتهيئة PDF_facades.form () لإدارة حقول نموذج PDF.
1. اتصل بـ «bind_pdf ()» لإرفاق ملف PDF الذي يحتوي على حقول أزرار الاختيار.
1. استخدم 'fill_field () 'لتحديد الخيار الأول (index 0).
1. احفظ ملف PDF المحدث.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Fill Radio Button Fields
def fill_radio_button_fields(infile, outfile):
    """Fill radio button fields in PDF form."""
    # Create Form object
    pdf_form = pdf_facades.Form()

    # Bind PDF document
    pdf_form.bind_pdf(infile)

    # Fill radio button fields by name
    pdf_form.fill_field("gender", 0)  # Select male option (index 0)
    # pdf_form.fill_field("gender", 1) # Select female option (index 1)

    # Save updated PDF
    pdf_form.save(outfile)
```
