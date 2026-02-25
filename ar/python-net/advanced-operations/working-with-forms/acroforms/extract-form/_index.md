---
title: استخراج AcroForm - استخراج بيانات النموذج من PDF باستخدام Python
linktitle: استخراج AcroForm
type: docs
weight: 30
url: /ar/python-net/extract-form/
description: استخراج النموذج من مستند PDF الخاص بك باستخدام مكتبة Aspose.PDF للغة Python. احصل على القيمة من حقل فردي في ملف PDF.
lastmod: "2025-02-27"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: كيفية الحصول على بيانات النموذج من PDF باستخدام Python
Abstract: توفر هذه المقالة دليلًا حول استخراج البيانات من حقول النموذج داخل مستند PDF باستخدام Python. تصف كيفية التنقل عبر جميع الحقول باستخدام مكتبة Aspose.PDF، تحديدًا عبر الوصول إلى مجموعة `Form` واستخدام نوع `Field` وخصائصه `value`. يتضمن مقطع شفرة Python مثالًا يوضح كيفية فتح مستند PDF، iterating عبر حقوله النموذجية، وطباعة اسم كل حقل وقيمته. هذه الطريقة مفيدة لاسترجاع بيانات النموذج برمجيًا من ملفات PDF.
---

## استخراج البيانات من النموذج

### الحصول على القيم من جميع حقول مستند PDF

للحصول على القيم من جميع الحقول في مستند PDF، تحتاج إلى التنقل عبر جميع حقول النموذج ثم الحصول على القيمة باستخدام خاصية Value. احصل على كل حقل من مجموعة Form، في النوع الأساسي للحقل المسمى [Field](https://reference.aspose.com/pdf/python-net/aspose.pdf.forms/field/) وادخل إلى خاصية [value](https://reference.aspose.com/pdf/python-net/aspose.pdf.forms/field/#properties) الخاصة به.

توضح مقتطفات الشفرة التالية بلغة Python كيفية الحصول على قيم جميع الحقول من مستند PDF.

```python

    import aspose.pdf as ap

    # Construct the full path to the input PDF file
    data_dir = "/path/to/your/pdf/files/"
    path_infile = os.path.join(work_dir, infile)

    # Create a Form object from the PDF file
    form = ap.facades.Form(path_infile)

    # Initialize an empty dictionary to store form values
    form_values = {}

    # Iterate through all form fields in the PDF
    for formField in form.field_names:
        # Retrieve the value for each form field and store in the dictionary
        form_values[formField] = form.get_field(formField)

    # Print and return the extracted form values
    print(form_values)
```

