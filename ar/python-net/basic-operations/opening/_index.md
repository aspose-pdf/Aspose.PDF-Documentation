---
title: افتح مستند PDF برمجيًا
linktitle: افتح ملف PDF
type: docs
weight: 20
url: /ar/python-net/open-pdf-document/
description: تعلم كيفية فتح ملف PDF في بايثون Aspose.PDF لبيثون عبر مكتبة.NET. يمكنك فتح ملف PDF الحالي والمستند من البث ومستند PDF المشفر.
lastmod: "2026-06-11"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: فتح مستندات PDF باستخدام مكتبة Aspose.PDF في بايثون
Abstract: توفر هذه المقالة دليلًا حول فتح مستندات PDF الحالية باستخدام مكتبة Aspose.PDF في Python. وهي تحدد ثلاث طرق لتحقيق ذلك - فتح ملف PDF عن طريق تحديد اسم الملف، وفتح PDF من البث، وفتح ملف PDF مشفر من خلال توفير كلمة مرور. تتضمن كل طريقة مقتطف شفرة يوضح كيفية استخدام مكتبة Aspose.PDF للوصول إلى PDF وطباعة عدد الصفحات التي تحتوي عليها. توضح هذه الأمثلة مرونة ووظائف Aspose.PDF للتعامل مع سيناريوهات الوصول إلى ملفات PDF المختلفة.
---

## افتح مستند PDF الحالي

هناك عدة طرق لفتح مستند. الأسهل هو تحديد اسم ملف.

```python
import aspose.pdf as ap

def open_document_from_file(infile):

    # Open document
    document = ap.Document(infile)
    print("Pages: " + str(len(document.pages)))
```

## افتح مستند PDF الحالي من البث

```python
import aspose.pdf as ap
import io

def open_document_from_stream(infile):
    with io.FileIO(infile, "r") as stream:
        # Open document
        document = ap.Document(stream)
        print("Pages: " + str(len(document.pages)))
```

## افتح مستند PDF مشفر

```python
import aspose.pdf as ap

def open_document_encrypted(infile):
    password = "P@ssw0rd"
    # Open document
    document = ap.Document(infile, password)
    print("Pages: " + str(len(document.pages)))
```
