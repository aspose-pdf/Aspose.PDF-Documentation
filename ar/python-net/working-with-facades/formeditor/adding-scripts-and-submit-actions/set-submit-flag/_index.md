---
title: تعيين علامة الإرسال
linktitle: تعيين علامة الإرسال
type: docs
weight: 50
url: /ar/python-net/set-submit-flag/
description: تعرف على كيفية تعيين علامة إرسال لزر نموذج PDF برمجيًا باستخدام Aspose.PDF لـ Python. يسمح هذا للزر بإرسال بيانات النموذج بتنسيق معين، مثل XFDF، عند النقر عليه من قبل المستخدم.
lastmod: "2026-06-11"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: تعيين علامة الإرسال لزر نموذج PDF باستخدام Aspose.PDF لبيثون
Abstract: يمكن تكوين نماذج PDF لإرسال بيانات النموذج إلى خادم أو نقطة نهاية بتنسيقات مختلفة. من خلال تعيين علامة إرسال على حقل الزر، يمكن للمطورين تحديد كيفية إرسال البيانات. يوضح هذا البرنامج التعليمي كيفية استخدام فئة ForMeditor لتعيين علامة إرسال لزر إرسال موجود في مستند PDF وحفظ الملف المحدث.
---

غالبًا ما تتضمن نماذج PDF أزرار الإرسال لإرسال مدخلات المستخدم إلى الخادم. تحدد علامة الإرسال تنسيق البيانات المرسلة (على سبيل المثال، XFDF، FDF، HTML).

1. قم بربط مستند PDF.
1. قم بالوصول إلى زر إرسال موجود.
1. قم بتعيين علامة الإرسال للتنسيق المطلوب.
1. احفظ مستند PDF المحدث.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def set_submit_flag(input_file_name, output_file_name):
    # Create FormEditor object
    form_editor = pdf_facades.FormEditor()

    # Open input PDF file
    form_editor.bind_pdf(input_file_name)

    # Set submit flag for the form
    form_editor.set_submit_flag("Script_Demo_Button", ap.facades.SubmitFormFlag.XFDF)

    # Save output PDF file
    form_editor.save(output_file_name)
```
