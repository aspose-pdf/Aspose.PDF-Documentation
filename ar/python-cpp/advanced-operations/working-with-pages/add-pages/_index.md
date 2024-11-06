---
title: إضافة صفحات في PDF باستخدام بايثون عبر C++
linktitle: إضافة صفحات
type: docs
weight: 10
url: ar/python-cpp/add-pages/
description: تعلمك هذه المقالة كيفية إدراج (إضافة) صفحة في الموقع المطلوب في ملف PDF باستخدام بايثون عبر C++.
lastmod: "2024-04-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## إدراج صفحة فارغة في ملف PDF في الموقع المطلوب

تفتح قطعة الشيفرة مستند PDF، تضيف صفحة فارغة إليه، وتحفظ المستند المعدل كملف PDF جديد.

لإدراج صفحة فارغة في ملف PDF:

1. افتح مستند الـ PDF
1. أضف صفحة فارغة جديدة إلى المستند
1. احفظ المستند المعدل في ملف الإخراج باستخدام طريقة 'document.save'

توضح قطعة الشيفرة التالية كيفية إدراج صفحة في ملف PDF:

```python

    import AsposePDFPythonWrappers as apw
    import AsposePDFPython as apCore
    import os
    import os.path

    # تعيين مسار الدليل حيث توجد ملفات PDF النموذجية
    dataDir = os.path.join(os.getcwd(), "samples")

    # تعيين مسار ملف الإدخال
    input_file = os.path.join(dataDir, "sample0.pdf")

    # تعيين مسار ملف الإخراج
    output_file = os.path.join(dataDir, "results", "blank_pdf_document.pdf")

    # فتح مستند الـ PDF
    document = apw.Document(input_file)

    # إضافة صفحة فارغة جديدة إلى المستند
    document.pages.add()

    # حفظ المستند المعدل في ملف الإخراج
    document.save(output_file)
```