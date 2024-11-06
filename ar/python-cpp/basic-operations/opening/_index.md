---
title: فتح مستند PDF برمجيًا
linktitle: فتح PDF
type: docs
weight: 20
url: ar/python-cpp/open-pdf-document/
description: تعلم كيفية فتح ملف PDF في Python باستخدام مكتبة Aspose.PDF لـ Python عبر C++. يمكنك فتح ملف PDF موجود، أو مستند من تدفق، أو مستند PDF مشفر.
lastmod: "2022-12-22"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## فتح مستند PDF موجود

هناك عدة طرق لفتح مستند. الأسهل هو تحديد اسم الملف.

```python

    import AsposePDFPythonWrappers as ap
    # فتح المستند
    document = ap.Document("sample.pdf")
    count = document.pages.count()
    print("الصفحات: " + str(count))
```

## فتح مستند PDF مشفر

```python

    import AsposePDFPythonWrappers as ap
    # فتح المستند
    document = ap.Document("sample.pdf","password")
    count = document.pages.count()
    print("الصفحات: " + str(count))
```