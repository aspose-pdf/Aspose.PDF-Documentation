---
title: حل أسماء الحقول الكاملة
linktitle: حل أسماء الحقول الكاملة
type: docs
weight: 60
url: /ar/python-net/resolve-full-field-names/
description: يوضح هذا المثال كيفية استرداد الأسماء المؤهلة بالكامل لحقول النموذج في مستند PDF باستخدام Aspose.PDF Facaces API.
lastmod: "2026-06-11"
---

في نماذج PDF، يمكن تنظيم الحقول بشكل هرمي، خاصة عند استخدام النماذج الفرعية. يحتوي كل حقل على اسم قصير واسم مؤهل بالكامل. يمثل الاسم المؤهل بالكامل المسار الكامل للحقل داخل التسلسل الهرمي للنموذج وهو مطلوب من قبل العديد من طرق API التي تعالج بيانات النموذج أو تقرأها.

1. قم بإنشاء كائن نموذج.
1. قم بربط وثيقة PDF.
1. قم بالوصول إلى جميع أسماء حقول النموذج.
1. يتم حل الاسم المؤهل بالكامل لكل حقل باستخدام get_full_field_name ().

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Resolve full field names
def resolve_full_field_names(infile):
    """Resolve full field names in a PDF document."""
    # Create Form object
    pdf_form = pdf_facades.Form()

    # Bind PDF document
    pdf_form.bind_pdf(infile)

    # Resolve full field names
    for field in pdf_form.field_names:
        name = pdf_form.get_full_field_name(field)
        print(f"Full field name: {name}")
```
