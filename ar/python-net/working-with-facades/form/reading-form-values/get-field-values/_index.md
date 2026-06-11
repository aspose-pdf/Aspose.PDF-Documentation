---
title: احصل على قيم الحقول
linktitle: احصل على قيم الحقول
type: docs
weight: 50
url: /ar/python-net/get-field-values/
description: استرداد قيم الحقول من نموذج PDF مع واجهات Aspose.PDF باستخدام فئة النموذج.
lastmod: "2026-06-11"
---

يوضح مقتطف الشفرة هذا كيفية استرداد القيم الحالية لحقول النموذج من مستند PDF باستخدام Aspose.PDF Facaces API. ال [get_field ()](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/form/#methods) تسمح لك الطريقة بالوصول برمجيًا إلى البيانات التي تم إدخالها في حقول النص ومربعات الاختيار وأزرار الاختيار وعناصر AcroForm الأخرى.

1. قم بربط PDF بكائن نموذج.
1. حدد أسماء الحقول التي تريد قراءتها.
1. استرجع قيمة كل حقل باستخدام get_field ().

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