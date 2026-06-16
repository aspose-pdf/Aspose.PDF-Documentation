---
title: احصل على قيم نصية غنية
linktitle: احصل على قيم نصية غنية
type: docs
weight: 40
url: /ar/python-net/get-rich-text-values/
description: يشرح هذا القسم كيفية استرداد محتوى النص المنسق لحقل نموذج في مستند PDF باستخدام واجهة برمجة تطبيقات Aspose.PDF للواجهات. على عكس حقول النص العادي، يمكن أن تحتوي حقول النص المنسق على محتوى منسق مثل النص الغامق والخطوط المختلفة والألوان ونمط الفقرة.
lastmod: "2026-06-11"
---

قد تتضمن نماذج PDF حقول نصية تدعم تنسيق النص الغني. يمكن لهذه الحقول تخزين المحتوى بسمات التصميم بالإضافة إلى قيم النص العادي.

1. قم بإنشاء كائن نموذج.
1. قم بربط وثيقة PDF.
1. استرجع قيم النص الغني.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Get rich text values
def get_rich_text_values(infile):
    """Get rich text values from a PDF document."""
    # Create Form object
    pdf_form = pdf_facades.Form()

    # Bind PDF document
    pdf_form.bind_pdf(infile)

    # Get rich text values by their names
    field_names = ["Summary"]
    for field_name in field_names:
        rich_text_value = pdf_form.get_rich_text(field_name)
        print(f"Rich text value of '{field_name}': {rich_text_value}")
```
