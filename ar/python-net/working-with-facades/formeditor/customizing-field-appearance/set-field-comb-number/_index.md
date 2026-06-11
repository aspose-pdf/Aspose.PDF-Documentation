---
title: تعيين رقم المشط الميداني
linktitle: تعيين رقم المشط الميداني
type: docs
weight: 70
url: /ar/python-net/set-field-comb-number/
description: يوضح هذا المثال كيفية تعيين رقم مشط لحقل نموذج PDF باستخدام Aspose.PDF لـ Python.
lastmod: "2026-06-11"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: تعيين رقم المشط لحقول نموذج PDF باستخدام Python
Abstract: باستخدام Aspose.PDF لـ Python، يمكن للمطورين تعيين عدد المربعات (رقم المشط) برمجيًا لحقل النموذج لفرض إدخال بطول ثابت. توضح هذه المقالة تعيين رقم المشط لحقل يسمى «PIN».
---

يحدد رقم المشط كيفية تقسيم محتوى الحقل إلى مربعات متساوية المسافات، وغالبًا ما تستخدم لرموز PIN أو الأرقام التسلسلية أو حقول الإدخال الأخرى ذات الطول الثابت. يفتح الكود ملف PDF موجود، ويضبط رقم المشط للحقل، ويحفظ المستند المعدل.

ال [المحرر السابق](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/formeditor/) توفر الفئة طريقة «set_field_comb_number» لتحديد عدد المربعات (الأحرف) في حقل النموذج.

1. افتح نموذج PDF موجود.
1. يقوم بإنشاء كائن ForMeditor.
1. قم بتعيين رقم مشط الحقل المسمى «PIN» إلى 5.
1. احفظ المستند المحدث.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pydrawing as ap_pydrawing
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def set_field_comb_number(infile, outfile):
    # Open document
    doc = ap.Document(infile)

    # Create FormEditor object
    form_editor = pdf_facades.FormEditor(doc)

    # Set field comb number to 5
    form_editor.set_field_comb_number("PIN", 5)

    # Save updated document
    form_editor.save(outfile)
```
