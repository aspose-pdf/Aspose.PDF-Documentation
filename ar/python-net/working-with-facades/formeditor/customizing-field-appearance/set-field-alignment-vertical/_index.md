---
title: تعيين محاذاة الحقل عموديًا
linktitle: تعيين محاذاة الحقل عموديًا
type: docs
weight: 40
url: /ar/python-net/set-field-alignment-vertical/
description: يوضح هذا المثال كيفية تعيين المحاذاة الرأسية لحقل النموذج في مستند PDF باستخدام Aspose.PDF لـ Python.
lastmod: "2026-06-11"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: تعيين المحاذاة الرأسية لحقول نموذج PDF باستخدام Python
Abstract: تشرح هذه المقالة كيفية فتح PDF وتعيين المحاذاة الرأسية للحقل باستخدام فئة ForMeditor وحفظ ملف PDF المحدث. يقوم المثال بتعيين المحاذاة الرأسية لحقل يسمى «الاسم الأول» إلى أسفل منطقة الحقل.
---

يمكن أن تحتوي حقول نموذج PDF على نص يحتاج إلى محاذاة رأسية مناسبة للحصول على مظهر متسق واحترافي. باستخدام Aspose.PDF لـ Python، يمكن للمطورين تعديل المحاذاة الرأسية لحقول النموذج برمجيًا.
تسمح المحاذاة الرأسية للمطورين بالتحكم فيما إذا كان نص الحقل يظهر في أعلى أو وسط أو أسفل المربع المحيط بالحقل، مما يحسن تخطيط بيانات النموذج وقابليتها للقراءة.

استخدام [المحرر السابق](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/formeditor/) الفئة و [واجهة فورمفيلد](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/formfieldfacade/) الثوابت، يمكن للمطورين ضبط المحاذاة الرأسية برمجيًا لتحقيق تخطيط نموذج متسق:

1. افتح مستند PDF موجود.
1. قم بإنشاء كائن ForMeditor.
1. قم بتعيين المحاذاة الرأسية للحقل المسمى «الاسم الأول» إلى الأسفل.
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


def set_field_alignment_vertical(infile, outfile):
    # Open document
    doc = ap.Document(infile)

    # Create FormEditor object
    form_editor = pdf_facades.FormEditor(doc)

    # Attempt to set vertical alignment of the "First Name" field to bottom
    if form_editor.set_field_alignment_v(
        "First Name", pdf_facades.FormFieldFacade.ALIGN_BOTTOM
    ):
        # Save updated document
        form_editor.save(outfile)
    else:
        raise Exception(
            "Failed to set field vertical alignment. Field may not support vertical alignment."
        )
```
