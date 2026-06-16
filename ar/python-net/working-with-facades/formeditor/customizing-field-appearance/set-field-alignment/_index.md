---
title: تعيين محاذاة الحقول
linktitle: تعيين محاذاة الحقول
type: docs
weight: 30
url: /ar/python-net/set-field-alignment/
description: يوضح هذا المثال كيفية تعيين محاذاة النص لحقل نموذج في مستند PDF باستخدام Aspose.PDF لـ Python.
lastmod: "2026-06-11"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: تعيين محاذاة النص لحقول نموذج PDF باستخدام Python
Abstract: تشرح هذه المقالة كيفية فتح مستند PDF وتعيين محاذاة حقل معين باستخدام فئة ForMeditor وحفظ ملف PDF المحدث. يقوم المثال بتعيين محاذاة النص لحقل يسمى «الاسم الأول» إلى الوسط.
---

غالبًا ما تتطلب حقول نموذج PDF محاذاة نصية مخصصة للحفاظ على تخطيط متسق واحترافي. باستخدام Aspose.PDF لـ Python، يمكن للمطورين تعيين محاذاة محتوى نص حقل النموذج برمجيًا.

ال [المحرر السابق](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/formeditor/) الفئة، بالاشتراك مع [واجهة فورمفيلد](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/formfieldfacade/) الثوابت، تسمح للمطورين بتعديل محاذاة حقول النموذج الموجودة برمجيًا.

1. افتح مستند PDF موجود.
1. قم بإنشاء كائن ForMeditor.
1. قم بتعيين محاذاة الحقل المسمى «الاسم الأول» إلى المركز.
1. احفظ المستند المعدل.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pydrawing as ap_pydrawing
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def set_field_alignment(infile, outfile):
    # Open document
    doc = ap.Document(infile)

    # Create FormEditor object
    form_editor = pdf_facades.FormEditor(doc)

    # Set field alignment to center
    if form_editor.set_field_alignment(
        "First Name", pdf_facades.FormFieldFacade.ALIGN_CENTER
    ):
        # Save updated document
        form_editor.save(outfile)
    else:
        raise Exception(
            "Failed to set field alignment. Field may not support alignment."
        )
```
