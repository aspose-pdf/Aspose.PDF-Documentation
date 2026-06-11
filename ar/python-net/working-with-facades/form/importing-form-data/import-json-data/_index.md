---
title: استيراد بيانات JSON
linktitle: استيراد بيانات JSON
type: docs
weight: 30
url: /ar/python-net/import-json-data/
description: يوضح هذا المثال كيفية استيراد بيانات حقل النموذج من ملف JSON إلى نموذج PDF باستخدام Aspose.PDF لـ Python عبر .NET. يوضح كيفية ربط مستند PDF، وقراءة بيانات JSON المنظمة من خلال دفق الملفات، وتعبئة حقول النموذج المطابقة تلقائيًا.
lastmod: "2026-06-11"
---

يتم استخدام JSON على نطاق واسع لتخزين البيانات المنظمة ونقلها بين الأنظمة. في هذا المثال، [نموذج](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/form/) واجهة من [واجهات أسبوز.pdf](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/) يتم استخدام الوحدة لربط نموذج PDF واستيراد قيم الحقول من ملف JSON خارجي. بعد عملية الاستيراد، يتم حفظ المستند المحدث كملف PDF جديد.

1. قم بتهيئة PDF_facades.form () للتفاعل مع حقول نموذج PDF.
1. اتصل بـ «bind_pdf ()» لإرفاق قالب نموذج PDF.
1. استخدم 'FileIO () 'لقراءة ملف JSON الذي يحتوي على قيم النموذج.
1. اتصل بـ «import_json ()» لملء حقول PDF باستخدام أزواج قيم ومفتاح JSON.
1. احفظ ملف PDF المحدث.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Import from JSON
def import_json_to_pdf_form(infile, datafile, outfile):
    """Import form data from JSON file into PDF form fields."""
    # Create Form object
    form = pdf_facades.Form()

    # Bind PDF document
    form.bind_pdf(infile)

    # Open JSON file as stream
    with FileIO(datafile, "r") as json_stream:
        # Import data from JSON into PDF form fields
        form.import_json(json_stream)

    # Save updated PDF
    form.save(outfile)
```
