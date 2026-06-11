---
title: إضافة برنامج نصي ميداني
linktitle: إضافة برنامج نصي ميداني
type: docs
weight: 10
url: /ar/python-net/add-field-script/
description: يمكن أن تتضمن نماذج PDF التفاعلية JavaScript لأتمتة الإجراءات عندما يتفاعل المستخدمون مع حقول النموذج. باستخدام Aspose.PDF لـ Python، يمكن للمطورين إرفاق البرامج النصية بسهولة لتشكيل عناصر مثل الأزرار أو الحقول النصية.
lastmod: "2026-06-11"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: إضافة إجراءات جافا سكريبت إلى حقول نموذج PDF باستخدام Python
Abstract: توضح هذه المقالة كيفية فتح نموذج PDF، وتعيين شفرة JavaScript لحقل نموذج معين، وإلحاق إجراءات البرنامج النصي الإضافية، وحفظ المستند المحدث. يستخدم المثال فئة ForMeditor من واجهة برمجة تطبيقات Aspose.PDF للواجهات لمعالجة سلوك النموذج برمجيًا.
---

## إضافة إجراءات جافا سكريبت إلى حقول نموذج PDF باستخدام Python

يمكّنك مقتطف الشفرة هذا من إضافة إجراءات JavaScript إلى حقل نموذج PDF موجود باستخدام مكتبة Aspose.PDF لـ Python. يفتح مستند PDF، ويعين إجراء JavaScript لحقل النموذج، ويضيف نصًا يتم تشغيله عند تشغيل الحقل. أخيرًا، يتم حفظ ملف PDF المحدث كملف جديد.
استخدام [المحرر السابق](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/formeditor/) فئة من [واجهات أسبوز.pdf](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/) الوحدة، يمكنك إرفاق JavaScript برمجيًا بحقول النموذج الموجودة:

1. افتح نموذج PDF موجود.
1. قم بتعيين إجراء JavaScript لحقل معين.
1. قم بإلحاق إجراء JavaScript آخر بنفس الحقل.
1. احفظ وثيقة PDF المعدلة.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def add_field_script(input_file_name, output_file_name):
    # Create FormEditor object
    form_editor = pdf_facades.FormEditor()

    # Open input PDF file
    form_editor.bind_pdf(input_file_name)

    # Set JavaScript action for the field
    form_editor.set_field_script(
        "Script_Demo_Button", "app.alert('Script 1 has been executed');"
    )

    # Add JavaScript action to the field
    form_editor.add_field_script(
        "Script_Demo_Button", "app.alert('Script 2 has been executed');"
    )

    # Save output PDF file
    form_editor.save(output_file_name)
```
