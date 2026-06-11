---
title: استيراد بيانات FDF
linktitle: استيراد بيانات FDF
type: docs
weight: 10
url: /ar/python-net/import-fdf-data/
description: يوضح هذا المثال كيفية استيراد بيانات النموذج من ملف FDF إلى نموذج PDF باستخدام Aspose.PDF لـ Python عبر .NET. يوضح كيفية ربط مستند PDF، وقراءة قيم حقول النموذج من دفق FDF، وتعبئة الحقول المقابلة تلقائيًا.
lastmod: "2026-06-11"
---

FDF (تنسيق بيانات النماذج) هو تنسيق خفيف يستخدم لتخزين ونقل قيم حقول نموذج PDF دون تضمين المستند بأكمله. في هذا المثال، [نموذج](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/form/) واجهة من [واجهات أسبوز.pdf](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/) يستخدم لتحميل نموذج PDF واستيراد بيانات الحقل من ملف FDF خارجي. بعد عملية الاستيراد، يتم حفظ ملف PDF المحدث كملف جديد.

1. قم بتهيئة PDF_facades.form () للعمل مع حقول نموذج PDF التفاعلية.
1. اتصل بـ «bind_pdf ()» لإرفاق قالب نموذج PDF.
1. استخدم 'open () 'لقراءة ملف FDF في الوضع الثنائي.
1. اتصل بـ «import_fdf ()» لملء حقول PDF ببيانات من ملف FDF.
1. احفظ ملف PDF المحدث.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Import Data from FDF
def import_fdf_to_pdf_form(infile, datafile, outfile):
    """Import form data from FDF file into PDF form fields."""
    # Create Form object
    pdf_form = pdf_facades.Form()

    # Bind PDF document
    pdf_form.bind_pdf(infile)

    # Open FDF file as stream
    with open(datafile, "rb") as fdf_input_stream:
        pdf_form.import_fdf(fdf_input_stream)

    # Save updated PDF
    pdf_form.save(outfile)
```
