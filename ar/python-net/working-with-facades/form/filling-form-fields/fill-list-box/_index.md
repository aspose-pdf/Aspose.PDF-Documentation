---
title: مربع قائمة التعبئة
linktitle: مربع قائمة التعبئة
type: docs
weight: 40
url: /ar/python-net/fill-list-box/
description: يوضح هذا المثال كيفية ملء مربع القائمة والحقول متعددة التحديد برمجيًا في نموذج PDF باستخدام Aspose.PDF لـ Python عبر .NET. يوضح كيفية ربط مستند PDF وتحديد القيم داخل حقل النموذج المستند إلى القائمة وحفظ الملف المحدث.
lastmod: "2026-06-11"
---

يسمح مربع القائمة وحقول التحديد المتعدد للمستخدمين باختيار قيمة واحدة أو عدة قيم من مجموعة خيارات محددة مسبقًا. في هذا المثال، [نموذج](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/form/) واجهة من [واجهات أسبوز.pdf](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/) يُستخدم للوصول إلى نموذج PDF وتعيين قيمة محددة لحقل favorite_colors. بمجرد تحديد الخيار المطلوب، يتم حفظ المستند المحدث.

1. قم بتهيئة 'PDF_facades.form () 'لإدارة حقول النموذج وتحديثها.
1. اتصل بـ «bind_pdf ()» لإرفاق ملف PDF المصدر الذي يحتوي على مربع القائمة أو الحقول متعددة التحديد.
1. استخدم 'fill_field () 'لتحديد قيمة من الخيارات المتاحة.
1. احفظ المستند المحدث.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Fill List Box / Multi-Select Fields
def fill_list_box_fields(infile, outfile):
    """Fill list box and multi-select fields in PDF form."""
    # Create Form object
    pdf_form = pdf_facades.Form()

    # Bind PDF document
    pdf_form.bind_pdf(infile)

    # Fill list box / multi-select fields by name
    pdf_form.fill_field("favorite_colors", "Red")

    # Save updated PDF
    pdf_form.save(outfile)
```
