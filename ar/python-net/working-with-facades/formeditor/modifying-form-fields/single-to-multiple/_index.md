---
title: حقل أحادي الخط إلى حقل متعدد الأسطر
linktitle: حقل أحادي الخط إلى حقل متعدد الأسطر
type: docs
weight: 80
url: /ar/python-net/single-to-multiple/
description: قم بتحويل حقل نصي أحادي السطر إلى حقل متعدد الأسطر في مستند PDF باستخدام Aspose.PDF لـ Python.
lastmod: "2026-06-11"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: تحويل حقل نصي أحادي السطر إلى حقل متعدد الأسطر في PDF باستخدام Python
Abstract: يوضح هذا المثال كيفية تحويل حقل نصي أحادي السطر إلى حقل متعدد الأسطر في مستند PDF باستخدام Aspose.PDF لـ Python. يقوم الكود بتحميل نموذج PDF موجود، وتعديل الحقل المحدد للسماح بخطوط نصية متعددة، وحفظ المستند المحدث.
---

تحتوي نماذج PDF أحيانًا على حقول نصية مصممة لإدخال سطر واحد، والتي قد لا تكون كافية لأنواع معينة من البيانات. باستخدام Aspose.PDF لـ Python، يمكن للمطورين تحويل هذه الحقول بسهولة إلى حقول نصية متعددة الأسطر دون إعادة إنشائها.

استخدام [المحرر السابق](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/formeditor/) الفئة، يمكن للمطورين تعديل حقول النص الموجودة دون التأثير على موضعها أو خصائصها الأخرى.

1. قم بتحميل وثيقة PDF الموجودة.
1. قم بإنشاء مثيل ForMeditor.
1. قم بربط وثيقة PDF بالمحرر.
1. قم بتحويل الحقل المحدد إلى متعدد الأسطر.
1. احفظ المستند المحدث.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def single2multiple(infile, outfile):
    # Create FormEditor object
    form_editor = pdf_facades.FormEditor()
    # Bind document to FormEditor
    form_editor.bind_pdf(infile)
    # Change a single-lined text field to a multiple-lined one
    form_editor.single_2_multiple("City")
    # Save updated document
    form_editor.save(outfile)
```

