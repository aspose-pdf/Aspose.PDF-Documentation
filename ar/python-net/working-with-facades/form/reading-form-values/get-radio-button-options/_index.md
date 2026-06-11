---
title: احصل على خيارات زر الراديو
linktitle: احصل على خيارات زر الراديو
type: docs
weight: 20
url: /ar/python-net/get-radio-button-options/
description: توضح هذه المقالة كيفية استرداد القيمة المحددة حاليًا لحقل زر الاختيار في مستند PDF باستخدام واجهة برمجة تطبيقات Aspose.PDF للواجهات.
lastmod: "2026-06-11"
---

حقول أزرار الراديو في نماذج PDF هي عناصر تحكم مجمعة حيث يمكن تحديد خيار واحد فقط في كل مرة. تحتوي كل مجموعة على اسم حقل، ولكل خيار قيمة مقابلة.

1. قم بإنشاء كائن نموذج.
1. قم بربط وثيقة PDF.
1. استرجع خيار زر الراديو المحدد.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Get radio button options
def get_radio_button_options(infile):
    """Get radio button options from a PDF document."""
    # Create Form object
    pdf_form = pdf_facades.Form()

    # Bind PDF document
    pdf_form.bind_pdf(infile)

    # Get radio button options by their names
    field_names = ["WorkType"]
    for field_name in field_names:
        options = pdf_form.get_button_option_current_value(field_name)
        print(f"Options for '{field_name}': {options}")
```
