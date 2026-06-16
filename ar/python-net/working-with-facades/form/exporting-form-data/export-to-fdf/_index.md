---
title: تصدير إلى FDF
linktitle: تصدير إلى FDF
type: docs
weight: 10
url: /ar/python-net/export-to-fdf/
description: يوضح هذا المثال كيفية تصدير بيانات حقل نموذج PDF إلى ملف FDF (تنسيق بيانات النماذج) باستخدام Aspose.PDF لـ Python عبر .NET. يوضح كيفية الوصول إلى بيانات النموذج التفاعلي من خلال واجهة النموذج، وربط مستند PDF المصدر، وحفظ القيم المستخرجة في دفق FDF.
lastmod: "2026-06-11"
---

FDF هو تنسيق خفيف مصمم خصيصًا لتخزين ونقل بيانات نموذج PDF دون تضمين المستند بأكمله. في هذا المثال، [نموذج](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/form/) تمت تهيئة الكائن من [واجهات أسبوز.pdf](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/) الوحدة، مما يسمح للمطورين بالتفاعل مع حقول AcroForm وتصدير قيمهم.

1. قم بإنشاء مثيل من PDF_facades.form () للعمل مع حقول نموذج PDF.
1. اتصل بـ «bind_pdf ()» لإرفاق مستند PDF الذي يحتوي على النموذج.
1. استخدم 'open (')' لإنشاء دفق ثنائي قابل للكتابة لملف FDF.
1. تصدير بيانات النموذج. اتصل بـ «export_fdf ()» لاستخراج جميع قيم حقول النموذج وحفظها.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Export Data to FDF
def export_form_data_to_fdf(infile, outfile):
    """Export PDF form data to FDF file."""
    # Create Form object
    pdf_form = pdf_facades.Form()

    # Bind PDF document
    pdf_form.bind_pdf(infile)

    # Create FDF file stream
    with open(outfile, "wb") as fdf_output_stream:
        # Export form data to FDF file
        pdf_form.export_fdf(fdf_output_stream)
```
