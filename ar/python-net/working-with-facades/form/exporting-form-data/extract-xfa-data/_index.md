---
title: استخراج بيانات XFA
linktitle: استخراج بيانات XFA
type: docs
weight: 50
url: /ar/python-net/extract-xfa-data/
description: يوضح هذا المثال كيفية استخراج بيانات نموذج XFA من ملف PDF باستخدام Aspose.PDF لـ Python عبر .NET. يوضح كيفية ربط مستند PDF المستند إلى XFA بواجهة النموذج وتصدير بنية البيانات الداخلية الخاصة به إلى دفق الملفات.
lastmod: "2026-06-11"
---

تختلف نماذج XFA (بنية نماذج XML) عن AcroForms التقليدية لأن بياناتها يتم تخزينها كملف XML داخل PDF. في هذا المثال، [نموذج](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/form/) كائن من [واجهات أسبوز.pdf](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/) يتم استخدام الوحدة لربط ملف PDF واستخراج بيانات XFA الخاصة به مباشرة في ملف.

1. قم بإنشاء مثيل PDF_facades.form () لإدارة بيانات النموذج.
1. اتصل بـ «bind_pdf ()» لإرفاق ملف PDF المصدر الذي يحتوي على نماذج XFA.
1. استخدم 'FileIO () 'لإنشاء دفق ملفات قابل للكتابة.
1. قم باستدعاء 'extract_xfa_data () 'لتصدير بيانات XFA XML المضمنة.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Extract XFA Data
def export_xfa_data(infile, outfile):
    """Export XFA form data."""
    # Create Form object
    form = pdf_facades.Form()

    # Bind PDF document
    form.bind_pdf(infile)

    with FileIO(outfile, "w") as stream:
        # Export embedded XFA XML data to the output stream
        form.extract_xfa_data(stream)
```
