---
title: استيراد بيانات XFDF
linktitle: استيراد بيانات XFDF
type: docs
weight: 20
url: /ar/python-net/import-xfdf-data/
description: يوضح هذا المثال كيفية استيراد بيانات النموذج من ملف XFDF إلى نموذج PDF باستخدام Aspose.PDF لـ Python عبر .NET. يوضح كيفية ربط مستند PDF، وقراءة بيانات XFDF المستندة إلى XML من خلال دفق الملفات، وتعبئة حقول النموذج المطابقة تلقائيًا. يتيح استيراد بيانات XFDF تبادل بيانات النموذج بكفاءة ويدعم عمليات سير العمل الآلية للمستندات التي تعتمد على تنسيقات XML المهيكلة.
lastmod: "2026-06-11"
---

XFDF (تنسيق بيانات نماذج XML) هو تمثيل XML لبيانات نموذج PDF المصممة للتشغيل البيني وتبادل البيانات. في هذا المثال، [نموذج](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/form/) واجهة من [واجهات أسبوز.pdf](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/) يتم استخدام الوحدة لربط نموذج PDF واستيراد قيم الحقول من ملف XFDF خارجي. بعد استيراد البيانات، يتم حفظ ملف PDF المحدث كمستند جديد.

1. قم بتهيئة PDF_facades.form () للتفاعل مع حقول نموذج PDF.
1. اتصل بـ «bind_pdf ()» لإرفاق قالب نموذج PDF.
1. استخدم 'open () 'لقراءة ملف XFDF.
1. اتصل بـ «import_xfdf ()» لملء حقول PDF بقيم من ملف XFDF.
1. احفظ المستند المحدث.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Import Data from XFDF
def import_data_from_xfdf(infile, datafile, outfile):
    """Import form data from XFDF file into PDF form fields."""
    # Create Form object
    pdf_form = pdf_facades.Form()

    # Bind PDF document
    pdf_form.bind_pdf(infile)

    # Open XFDF file as stream
    with open(datafile, "rb") as xfdf_input_stream:
        # Import data from XFDF into PDF form fields
        pdf_form.import_xfdf(xfdf_input_stream)

    # Save updated PDF
    pdf_form.save(outfile)
```
