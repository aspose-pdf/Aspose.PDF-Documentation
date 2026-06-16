---
title: حقل التزيين
linktitle: حقل التزيين
type: docs
weight: 10
url: /ar/python-net/decorate-field/
description: يوضح هذا المثال كيفية تخصيص مظهر حقل النموذج في مستند PDF باستخدام Aspose.PDF لـ Python.
lastmod: "2026-06-11"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: تزيين حقول نموذج PDF بألوان مخصصة ومحاذاة باستخدام Python
Abstract: توضح هذه المقالة كيفية فتح مستند PDF وتكوين خيارات التصميم باستخدام فئة FormFieldFacade وتطبيق هذه الإعدادات على حقل النموذج وحفظ PDF المحدث. يوضح المثال كيفية تزيين حقل باسم «الاسم الأول» بألوان مخصصة ومحاذاة نصية مركزية.
---

غالبًا ما تتطلب نماذج PDF تخصيصًا مرئيًا لتحسين قابلية الاستخدام وإنشاء تصميم متسق. باستخدام Aspose.PDF لـ Python، يمكن للمطورين تزيين حقول النموذج برمجيًا عن طريق تعيين خصائص مثل الألوان والحدود ومحاذاة النص.

استخدام [المحرر السابق](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/formeditor/) و [واجهة فورمفيلد](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/formfieldfacade/) يمكن لمطوري الفصول تعديل مظهر حقول النموذج بسهولة لتحسين قابلية القراءة أو تمييز الحقول المطلوبة أو مطابقة متطلبات العلامة التجارية.

1. افتح مستند PDF موجود.
1. قم بإنشاء كائن ForMeditor لمعالجة حقول النموذج.
1. تعريف التصميم المرئي باستخدام واجهة FormFieldFacade.
1. قم بتطبيق التصميم على حقل نموذج معين.
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


def decorate_field(infile, outfile):
    # Open document
    doc = ap.Document(infile)

    # Create FormEditor object
    form_editor = pdf_facades.FormEditor(doc)
    form_editor.facade = pdf_facades.FormFieldFacade()
    form_editor.facade.background_color = ap_pydrawing.Color.red
    form_editor.facade.text_color = ap_pydrawing.Color.blue
    form_editor.facade.border_color = ap_pydrawing.Color.green
    form_editor.facade.alignment = pdf_facades.FormFieldFacade.ALIGN_CENTER
    form_editor.decorate_field("First Name")

    # Save updated document
    form_editor.save(outfile)
```

