---
title: تعبئة حقول الباركود
linktitle: تعبئة حقول الباركود
type: docs
weight: 50
url: /ar/python-net/fill-barcode-fields/
description: يوضح هذا المثال كيفية ملء حقول الباركود برمجيًا في نموذج PDF باستخدام Aspose.PDF لـ Python عبر .NET. يوضح كيفية ربط مستند PDF وتعيين قيمة لحقل الباركود وحفظ الملف المحدث.
lastmod: "2026-06-11"
---

تسمح حقول الباركود في نماذج PDF بتخزين المعلومات المشفرة وعرضها بصريًا كرموز شريطية. في هذا المثال، [نموذج](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/form/) واجهة من [واجهات أسبوز.pdf](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/) يتم استخدام الوحدة للوصول إلى حقول النموذج وتعيين قيمة الباركود. بمجرد ملء البيانات، يتم حفظ ملف PDF بمحتوى الباركود المحدث.

1. قم بتهيئة 'PDF_facades.form () 'لإدارة تفاعلات نموذج PDF.
1. اتصل بـ «bind_pdf ()» لإرفاق ملف PDF الذي يحتوي على حقول الباركود.
1. استخدم 'fill_field () 'لتعيين قيمة الباركود.
1. احفظ المستند المحدث.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Fill Barcode Fields
def fill_barcode_fields(infile, outfile):
    """Fill barcode fields in PDF form."""
    # Create Form object
    pdf_form = pdf_facades.Form()

    # Bind PDF document
    pdf_form.bind_pdf(infile)

    # Fill barcode fields by name
    pdf_form.fill_field("product_barcode", "123456789012")

    # Save updated PDF
    pdf_form.save(outfile)
```
