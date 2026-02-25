---
title: فتح مستند PDF برمجياً
linktitle: فتح PDF
type: docs
weight: 20
url: /ar/python-net/open-pdf-document/
description: تعلم كيفية فتح ملف PDF في بايثون باستخدام مكتبة Aspose.PDF لبايثون عبر .NET. يمكنك فتح PDF موجود، أو مستند من تدفق، ومستند PDF مشفر.
lastmod: "2025-02-27"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: فتح مستندات PDF باستخدام مكتبة Aspose.PDF في بايثون
Abstract: توفر هذه المقالة دليلًا لفتح مستندات PDF الموجودة باستخدام مكتبة Aspose.PDF في بايثون. توضح ثلاث طرق لتحقيق ذلك - فتح PDF بتحديد اسم الملف، فتح PDF من تدفق، وفتح PDF مشفر بتوفير كلمة مرور. يتضمن كل طريقة مقطع شفرة يوضح كيفية استخدام مكتبة Aspose.PDF للوصول إلى PDF وطباعة عدد الصفحات التي يحتويها. توضح هذه الأمثلة مرونة ووظائف Aspose.PDF للتعامل مع سيناريوهات مختلفة للوصول إلى ملفات PDF.
---

## فتح مستند PDF موجود

هناك عدة طرق لفتح مستند. أسهلها هو تحديد اسم الملف.

```python

    import aspose.pdf as ap

    # Open document
    document = ap.Document(input_pdf)
    print("Pages: " + str(len(document.pages)))
```

## فتح مستند PDF موجود من تدفق

```python

    import aspose.pdf as ap

    input_pdf = DIR_INPUT + "sample.pdf"
    stream = io.FileIO(input_pdf, 'r')
    # Open document
    document = ap.Document(stream)
    print("Pages: " + str(len(document.pages)))
```

## فتح مستند PDF مشفر

```python

    import aspose.pdf as ap

    # Open document
    document = ap.Document(input_pdf, password)
    print("Pages: " + str(len(document.pages)))
```

