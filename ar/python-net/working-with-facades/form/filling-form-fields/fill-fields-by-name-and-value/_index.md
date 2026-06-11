---
title: تعبئة الحقول حسب الاسم والقيمة
linktitle: تعبئة الحقول حسب الاسم والقيمة
type: docs
weight: 60
url: /ar/python-net/fill-fields-by-name-and-value/
description: توضح هذه المقالة كيفية ملء حقول نماذج PDF المتعددة ديناميكيًا بالاسم والقيمة باستخدام Aspose.PDF لـ Python عبر .NET. بدلاً من تعيين كل حقل على حدة، فإنه يستخدم بنية القاموس لتعيين أسماء الحقول إلى القيم وتعبئتها في حلقة.
lastmod: "2026-06-11"
---

يتيح ملء حقول النموذج باستخدام مجموعة الاسم والقيمة للمطورين إنشاء حلول قابلة للتطوير ومرنة لأتمتة نماذج PDF. في هذا المثال، [نموذج](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/form/) واجهة من [واجهات أسبوز.pdf](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/) يستخدم لربط مستند PDF والتكرار من خلال قاموس البيانات الميدانية. يتم تطبيق كل إدخال باستخدام «طريقة fill_field»، مما يتيح إجراء تحديثات مجمعة فعالة لحقول النموذج.

1. قم بتهيئة 'PDF_facades.form () 'للعمل مع حقول النماذج التفاعلية.
1. استخدم «bind_pdf ()» لإرفاق مستند PDF المصدر.
1. قم بإنشاء قاموس يحتوي على أسماء الحقول والقيم التي تريد إدراجها.
1. قم بالتكرار من خلال القاموس واتصل بـ 'fill_field () 'لكل إدخال.
1. احفظ المستند المحدث.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Fill Fields by Name and Value
def fill_fields_by_name_and_value(infile, outfile):
    """Fill PDF form fields by name and value."""
    # Create Form object
    pdf_form = pdf_facades.Form()

    # Bind PDF document
    pdf_form.bind_pdf(infile)

    # Fill fields by name and value
    fields = {
        "name": "Jane Smith",
        "address": "456 Elm St, Othertown, USA",
        "email": "jane.smith@example.com",
    }
    for field_name, value in fields.items():
        pdf_form.fill_field(field_name, value)

    # Save updated PDF using outfile
    pdf_form.save(outfile)
```
