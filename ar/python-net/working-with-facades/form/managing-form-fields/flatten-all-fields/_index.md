---
title: تسطيح جميع الحقول
linktitle: تسطيح جميع الحقول
type: docs
weight: 10
url: /ar/python-net/flatten-all-fields/
description: يوضح هذا المثال كيفية تسوية جميع حقول النموذج في PDF باستخدام Aspose.PDF لـ Python عبر .NET. يوضح كيفية ربط مستند PDF وتحويل كل عنصر نموذج تفاعلي إلى محتوى صفحة ثابت وحفظ الملف النهائي.
lastmod: "2026-06-11"
---

التسوية تزيل التفاعل من نماذج PDF عن طريق دمج قيم الحقول مباشرة في تخطيط المستند. في هذا المثال، [نموذج](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/form/) واجهة من [واجهات أسبوز.pdf](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/) يستخدم لربط ملف PDF المصدر وتطبيق طريقة flatten_all_fields ()، والتي تحول جميع الحقول إلى محتوى غير قابل للتحرير.

1. قم بتهيئة PDF_facades.form () للتفاعل مع حقول نموذج PDF.
1. اتصل بـ «bind_pdf ()» لإرفاق المستند المصدر.
1. اتصل بـ «flatten_all_fields ()» لتحويل جميع الحقول التفاعلية إلى محتوى ثابت.
1. احفظ المستند المحدث.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Flatten all fields
def flatten_all_fields(infile, outfile):
    """Flatten all fields in a PDF document."""
    # Create Form object
    pdf_form = pdf_facades.Form()

    # Bind PDF document
    pdf_form.bind_pdf(infile)

    # Flatten all fields in the PDF document
    pdf_form.flatten_all_fields()

    # Save updated PDF
    pdf_form.save(outfile)
```
