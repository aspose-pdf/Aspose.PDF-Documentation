---
title: تعيين المظهر الميداني
linktitle: تعيين المظهر الميداني
type: docs
weight: 50
url: /ar/python-net/set-field-appearance/
description: يوضح هذا المثال كيفية تغيير المظهر المرئي لحقل نموذج PDF باستخدام Aspose.PDF لـ Python.
lastmod: "2026-06-11"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: تعيين مظهر حقل نموذج PDF باستخدام Python
Abstract: توضح هذه المقالة كيفية فتح PDF وتعيين مظهر حقل النموذج باستخدام فئة ForMeditor وحفظ المستند المحدث. يقوم المثال بتعيين مظهر الحقل المسمى «الاسم الأول» إلى غير مرئي باستخدام علامة AnnotationFlags.invisible.
---

تدعم حقول نموذج PDF علامات المظهر التي تتحكم في الرؤية وقابلية الطباعة والتفاعل. باستخدام Aspose.PDF لـ Python، يمكن للمطورين تعديل هذه العلامات برمجيًا لحقول نموذج محددة.

استخدام [المحرر السابق](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/formeditor/) الفئة، يمكن للمطورين تعديل هذه العلامات لإخفاء أو إظهار أو تخصيص سلوك حقول النموذج في ملف PDF تفاعلي.

1. افتح مستند PDF موجود.
1. قم بإنشاء كائن ForMeditor.
1. قم بتعيين مظهر الحقل المسمى «الاسم الأول» إلى غير مرئي.
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


def set_field_appearance(infile, outfile):
    # Open document
    doc = ap.Document(infile)

    # Create FormEditor object
    form_editor = pdf_facades.FormEditor(doc)

    # Set field appearance to invisible
    if not form_editor.set_field_appearance(
        "First Name", ap.annotations.AnnotationFlags.INVISIBLE
    ):
        raise Exception(
            "Failed to set field appearance. Field may not support appearance flags."
        )

    # Save updated document
    form_editor.save(outfile)
```
