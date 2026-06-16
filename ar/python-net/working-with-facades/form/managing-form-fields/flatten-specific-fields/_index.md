---
title: تسطيح حقول محددة
linktitle: تسطيح حقول محددة
type: docs
weight: 20
url: /ar/python-net/flatten-specific-fields/
description: يوضح هذا القسم كيفية إدارة وتعديل حقول نموذج PDF باستخدام Aspose.PDF لـ Python عبر .NET. ويغطي أمثلة عملية لتسوية حقول محددة، وتسوية جميع حقول النموذج، وإعادة تسمية الحقول الموجودة برمجيًا.
lastmod: "2026-06-11"
---

تعد إدارة حقول النموذج جزءًا مهمًا من عمليات سير عمل معالجة PDF. تؤدي تسوية الحقول إلى إزالة التفاعل عن طريق تحويل عناصر النموذج إلى محتوى صفحة عادي، بينما تساعد إعادة تسمية الحقول على توحيد اصطلاحات التسمية لتسهيل معالجة البيانات.

1. قم بتهيئة PDF_facades.form () للوصول إلى حقول نموذج PDF وإدارتها.
1. استخدم 'bind_pdf () 'لإرفاق مستند الإدخال.
1. قم بتوفير أسماء الحقول واستدعاء 'flatt_field () 'لتحويل الحقول المحددة إلى محتوى ثابت.
1. قم باستدعاء 'flatt_all_fields () 'لإزالة التفاعل من كل حقل نموذج.
1. حدد أسماء الحقول القديمة والجديدة وقم بتطبيق 'rename_field () '.
1. احفظ ملف PDF المحدث.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Flatten specific fields
def flatten_specific_fields(infile, outfile):
    """Flatten specific fields in a PDF document."""
    # Create Form object
    pdf_form = pdf_facades.Form()

    # Bind PDF document
    pdf_form.bind_pdf(infile)

    # Flatten specific fields by their names
    fields_to_flatten = ["First Name", "Last Name"]
    for field_name in fields_to_flatten:
        pdf_form.flatten_field(field_name)

    # Save updated PDF
    pdf_form.save(outfile)
```
