---
title: تعيين عنوان URL للإرسال
linktitle: تعيين عنوان URL للإرسال
type: docs
weight: 40
url: /ar/python-net/set-submit-url/
description: يوضح هذا المثال كيفية تكوين إجراء إرسال لحقل زر في نموذج PDF باستخدام Aspose.PDF لـ Python.
lastmod: "2026-06-11"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: قم بتعيين عنوان URL لإرسال زر نموذج PDF باستخدام Python
Abstract: تشرح هذه المقالة كيفية فتح نموذج PDF موجود، وتحديد عنوان URL للإرسال لحقل الزر باستخدام فئة ForMeditor، والتحقق من نجاح العملية، وحفظ مستند PDF المحدث.
---

يمكن تصميم نماذج PDF لإرسال بياناتها إلى خادم الويب عندما ينقر المستخدم على زر الإرسال. باستخدام Aspose.PDF لـ Python، يمكن للمطورين تكوين إجراء إرسال لحقول النموذج برمجيًا.
من خلال تعيين عنوان URL للإرسال، يمكن للنموذج إرسال البيانات التي أدخلها المستخدم إلى الخادم عند النقر فوق الزر. هذه الوظيفة مفيدة لعمليات سير العمل حيث يجب أن ترسل نماذج PDF المعلومات إلى تطبيقات الويب أو قواعد البيانات أو خدمات المعالجة.

استخدام [المحرر السابق](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/formeditor/) فئة من [واجهات أسبوز.pdf](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/) الوحدة، يمكن للمطورين تعيين عنوان URL للإرسال برمجيًا إلى حقل زر في نموذج PDF موجود.

1. افتح نموذج PDF موجود.
1. حدد موقع حقل الزر المسمى Script_Demo_Button.
1. قم بتعيين عنوان URL حيث سيتم إرسال بيانات النموذج.
1. تحقق من تطبيق الإجراء بنجاح.
1. احفظ مستند PDF المحدث.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def set_submit_url(input_file_name, output_file_name):
    # Create FormEditor object
    form_editor = pdf_facades.FormEditor()

    # Set license
    set_license()

    # Open input PDF file
    form_editor.bind_pdf(input_file_name)

    # Set submit URL for the button
    if not form_editor.set_submit_url(
        "Script_Demo_Button", "http://www.example.com/submit"
    ):
        raise Exception("Failed to set submit URL")

    # Save output PDF file
    form_editor.save(output_file_name)
```
