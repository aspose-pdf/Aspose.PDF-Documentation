---
title: احصل على واجهات ميدانية
linktitle: احصل على واجهات ميدانية
type: docs
weight: 10
url: /ar/python-net/get-field-facades/
description: يوضح هذا المثال كيفية قراءة قيم حقول النموذج المحددة من مستند PDF باستخدام Aspose.PDF Facaces API.
lastmod: "2026-06-11"
---

تحتوي نماذج PDF على حقول حيث يمكن للمستخدمين إدخال البيانات، مثل مربعات النص أو مربعات الاختيار أو أزرار الاختيار. لمعالجة هذه النماذج برمجيًا، غالبًا ما يكون من الضروري استرداد القيم الحالية لهذه الحقول.

1. قم بإنشاء كائن نموذج.
1. قم بربط وثيقة PDF بكائن النموذج.
1. استرجع قيم الحقول.

```python

    from io import FileIO
    import sys
    from os import path
    import aspose.pdf as ap
    import aspose.pdf.facades as pdf_facades

    sys.path.append(path.join(path.dirname(__file__), ".."))

    from config import set_license, initialize_data_dir


    # Get field values
    def get_field_values(infile):
        """Get field values from a PDF document."""
        # Create Form object
        pdf_form = pdf_facades.Form()

        # Bind PDF document
        pdf_form.bind_pdf(infile)

        # Get field values by their names
        field_names = ["First Name", "Last Name"]
        for field_name in field_names:
            value = pdf_form.get_field(field_name)
            print(f"Value of '{field_name}': {value}")
```