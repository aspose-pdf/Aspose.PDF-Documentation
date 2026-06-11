---
title: احصل على أسماء الحقول المطلوبة
linktitle: احصل على أسماء الحقول المطلوبة
type: docs
weight: 30
url: /ar/python-net/get-required-field-names/
description: يوضح هذا المثال كيفية تحديد واسترجاع أسماء حقول النموذج المطلوبة في مستند PDF باستخدام واجهة برمجة تطبيقات Aspose.PDF للواجهات.
lastmod: "2026-06-11"
---

قد تحتوي نماذج PDF على حقول إلزامية يجب على المستخدمين إكمالها قبل الإرسال. عادةً ما يتم وضع علامة على هذه الحقول على أنها مطلوبة في خصائص النموذج.

1. قم بإنشاء كائن نموذج.
1. قم بربط وثيقة PDF.
1. قم بالوصول إلى جميع أسماء الحقول باستخدام 'pdf_form.field_names'.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Get required field names
def get_required_field_names(infile):
    """Get required field names from a PDF document."""
    # Create Form object
    pdf_form = pdf_facades.Form()

    # Bind PDF document
    pdf_form.bind_pdf(infile)

    # Get required field names
    for field in pdf_form.field_names:
        if pdf_form.is_required_field(field):
            print(f"Required field: {field}")
```
