---
title: استبدال بيانات XFA
linktitle: استبدال بيانات XFA
type: docs
weight: 50
url: /ar/python-net/replace-xfa-data/
description: يوضح هذا المثال كيفية استبدال بيانات نموذج XFA الموجودة في PDF باستخدام Aspose.PDF لـ Python عبر .NET. يوضح كيفية ربط مستند PDF يستند إلى XFA، وتحميل بيانات جديدة من ملف XFA خارجي، وتحديث محتوى النموذج برمجيًا.
lastmod: "2026-06-11"
---

تقوم نماذج XFA (بنية نماذج XML) بتخزين بياناتها بتنسيق XML داخل بنية PDF. في هذا المثال، [نموذج](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/form/) واجهة من [واجهات أسبوز.pdf](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/) يتم استخدام الوحدة لربط PDF واستبدال مجموعة بيانات XFA الحالية باستخدام دفق XML خارجي. بعد تطبيق البيانات الجديدة، يتم حفظ ملف PDF المحدث كملف منفصل.

1. قم بتهيئة PDF_facades.form () لإدارة بيانات نموذج XFA.
1. اتصل بـ «bind_pdf ()» لإرفاق ملف PDF الذي يحتوي على نماذج XFA.
1. استخدم 'FileIO () 'لقراءة ملف XFA XML.
1. اتصل بـ 'set_xfa_data () 'لتحديث ملف PDF بمحتوى XFA الجديد.
1. احفظ المستند المحدث.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Replace from XFA data
def replace_xfa_data(infile, datafile, outfile):
    """Import form data from XFA file into PDF form fields."""
    # Create Form object
    form = pdf_facades.Form()

    # Bind PDF document
    form.bind_pdf(infile)

    # Open XFA file as stream
    with FileIO(datafile, "r") as xfa_stream:
        # Import data from XFA into PDF form fields
        form.set_xfa_data(xfa_stream)

    # Save updated PDF
    form.save(outfile)
```
