---
title: فتح مستند PDF برمجيًا
linktitle: فتح PDF
type: docs
weight: 20
url: /ar/python-net/open-pdf-document/
description: تعلم كيفية فتح ملف PDF في مكتبة Aspose.PDF لـ Python عبر .NET. يمكنك فتح ملف PDF موجود، مستند من دفق، ومستند PDF مشفر.
lastmod: "2022-12-22"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## فتح مستند PDF موجود

هناك عدة طرق لفتح مستند. الأسهل هو تحديد اسم الملف.

```python

    import aspose.pdf as ap

    # فتح المستند
    document = ap.Document(input_pdf)
    print("الصفحات: " + str(len(document.pages)))
```

## فتح مستند PDF موجود من دفق

```python

    import aspose.pdf as ap

    input_pdf = DIR_INPUT + "sample.pdf"
    stream = io.FileIO(input_pdf, 'r')
    # فتح المستند
    document = ap.Document(stream)
    print("الصفحات: " + str(len(document.pages)))
```

## فتح مستند PDF مشفر

```python

    import aspose.pdf as ap

    # فتح المستند
    document = ap.Document(input_pdf, password)
    print("الصفحات: " + str(len(document.pages)))
```