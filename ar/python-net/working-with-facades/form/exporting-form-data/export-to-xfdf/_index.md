---
title: التصدير إلى XFDF
linktitle: التصدير إلى XFDF
type: docs
weight: 20
url: /ar/python-net/export-to-xfdf/
description: يوضح هذا المثال كيفية تصدير بيانات حقل نموذج PDF إلى ملف XFDF (تنسيق بيانات نماذج XML) باستخدام Aspose.PDF لـ Python عبر .NET. يوضح كيفية تحميل نموذج PDF والوصول إلى حقوله من خلال واجهة النموذج وحفظ القيم المستخرجة في دفق XFDF.
lastmod: "2026-06-11"
---

XFDF هو تمثيل XML لبيانات نموذج PDF الذي يسمح للمطورين بنقل قيم حقول النموذج بشكل مستقل عن المستند الأصلي. في هذا المثال، [نموذج](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/form/) كائن من [واجهات أسبوز.pdf](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/) يستخدم لربط PDF المصدر وتصدير بياناته إلى ملف XFDF منظم.

1. قم بتهيئة PDF_facades.form () لإدارة بيانات نموذج PDF.
1. اتصل بـ «bind_pdf ()» لإرفاق مستند PDF المصدر.
1. استخدم 'open () 'لإنشاء دفق ثنائي قابل للكتابة.
1. تصدير بيانات النموذج. اتصل بـ «export_xfdf ()» لاستخراج قيم حقول النموذج وحفظها بتنسيق XFDF.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Export Data to XFDF
def export_pdf_form_to_xfdf(infile, outfile):
    """Export PDF form data to XFDF file."""
    # Create Form object
    pdf_form = pdf_facades.Form()

    # Bind PDF document
    pdf_form.bind_pdf(infile)

    # Create XFDF file stream
    with open(outfile, "wb") as xfdf_output_stream:
        # Export form data to XFDF file
        pdf_form.export_xfdf(xfdf_output_stream)
```
