---
title: تعيين حد الحقل
linktitle: تعيين حد الحقل
type: docs
weight: 80
url: /ar/python-net/set-field-limit/
description: يوضح هذا المثال كيفية تعيين حد أقصى لعدد الأحرف لحقل نموذج في مستند PDF باستخدام Aspose.PDF لـ Python.
lastmod: "2026-06-11"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: تعيين الحد الأقصى لعدد الأحرف لحقول نموذج PDF باستخدام Python
Abstract: يوضح هذا المثال تعيين حد الأحرف لحقل يسمى «الاسم الأخير» إلى 10 أحرف، مما يضمن عدم تمكن المستخدمين من إدخال أكثر من الحد المحدد.
---

قد تتطلب حقول النموذج في مستندات PDF قيود الإدخال للحفاظ على التنسيق الصحيح. باستخدام Aspose.PDF لـ Python، يمكن للمطورين تعيين الحد الأقصى لعدد الأحرف للحقل برمجيًا.

ال [المحرر السابق](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/formeditor/) توفر الفئة طريقة «set_field_limit» لتحديد الحد الأقصى لطول الإدخال للحقل.

1. افتح نموذج PDF موجود.
1. قم بإنشاء كائن ForMeditor.
1. قم بتعيين الحد الأقصى لعدد الأحرف في حقل «الاسم الأخير».
1. احفظ ملف PDF المحدث.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pydrawing as ap_pydrawing
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def set_field_limit(infile, outfile):
    # Open document
    doc = ap.Document(infile)

    # Create FormEditor object
    form_editor = pdf_facades.FormEditor(doc)

    # Set field limit to 10
    if not form_editor.set_field_limit("Last Name", 10):
        raise Exception(
            "Failed to set field limit. Field may not support specified limit."
        )

    # Save updated document
    form_editor.save(outfile)
```
