---
title: تصدير إلى JSON
linktitle: تصدير إلى JSON
type: docs
weight: 30
url: /ar/python-net/export-to-json/
description: يوضح هذا المثال كيفية تصدير قيم حقول نموذج PDF إلى ملف JSON باستخدام Aspose.PDF لـ Python عبر .NET. يشرح كيفية تحميل نموذج PDF والوصول إلى حقوله من خلال واجهة النموذج وحفظ البيانات المستخرجة بتنسيق JSON منظم
lastmod: "2026-06-11"
---

JSON هو تنسيق بيانات مستخدم على نطاق واسع يتيح التبادل السلس بين التطبيقات والخدمات. في هذا المثال، [نموذج](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/form/) كائن من [واجهات أسبوز.pdf](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/) يتم استخدام الوحدة لربط ملف PDF وتصدير قيم حقول النموذج الخاصة به إلى بنية JSON قابلة للقراءة.

1. قم بتهيئة PDF_facades.form () للعمل مع حقول النموذج.
1. استخدم «bind_pdf ()» لإرفاق مستند PDF المصدر.
1. قم بإنشاء دفق قابل للكتابة باستخدام 'FileIO () '.
1. اتصل بـ «export_json ()» لاستخراج قيم حقول النموذج وحفظها في JSON المنسق.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Export Data to JSON
def export_form_to_json(infile, outfile):
    """Export PDF form field values to JSON file."""
    # Create Form object
    form = pdf_facades.Form()

    # Bind PDF document
    form.bind_pdf(infile)

    # Create JSON file stream
    with FileIO(outfile, "w") as json_stream:
        # Export form field values to JSON
        form.export_json(json_stream, indented=True)
```
