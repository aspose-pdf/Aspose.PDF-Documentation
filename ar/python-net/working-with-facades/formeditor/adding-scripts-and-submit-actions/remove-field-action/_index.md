---
title: إزالة الإجراء الميداني
linktitle: إزالة الإجراء الميداني
type: docs
weight: 20
url: /ar/python-net/remove-field-action/
description: يمكن أن تكون إزالة JavaScript من حقول النموذج مفيدة عند تعديل نماذج PDF التفاعلية أو تعطيل الإجراءات المعينة مسبقًا أو تنظيف المستندات التي تحتوي على نصوص غير ضرورية.
lastmod: "2026-06-11"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: قم بإزالة إجراءات JavaScript من حقول نموذج PDF باستخدام Python
Abstract: باستخدام Aspose.PDF لـ Python، يمكن للمطورين إزالة إجراءات JavaScript المرفقة بحقول النموذج برمجيًا. توضح هذه المقالة كيفية فتح نموذج PDF موجود، وإزالة البرنامج النصي المرتبط بحقل معين باستخدام فئة ForMeditor، والتحقق من العملية، وحفظ المستند المعدل.
---

غالبًا ما تحتوي نماذج PDF على إجراءات JavaScript التي يتم تنفيذها عندما يتفاعل المستخدمون مع عناصر النموذج مثل الأزرار أو حقول الإدخال. في بعض الحالات، يجب إزالة هذه البرامج النصية لتبسيط سلوك النموذج أو تحسين الأمان أو تحديث منطق النموذج. قم بإزالة إجراء JavaScript من حقل نموذج في مستند PDF باستخدام Aspose.PDF لـ Python. يفتح الكود نموذج PDF موجود، ويحدد موقع حقل معين، ويزيل إجراء JavaScript المرتبط به، ويحفظ المستند المحدث كملف PDF جديد.

استخدام [المحرر السابق](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/formeditor/) فئة من [واجهات أسبوز.pdf](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/)، يمكنك إزالة إجراءات JavaScript من حقول محددة في نموذج PDF موجود:

1. افتح نموذج PDF موجود.
1. حدد موقع حقل النموذج المسمى «Script_Demo_Button».
1. قم بإزالة إجراء JavaScript المرتبط بهذا الحقل.
1. تحقق مما إذا كانت الإزالة ناجحة.
1. احفظ مستند PDF المحدث.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def remove_field_script(input_file_name, output_file_name):
    # Create FormEditor object
    form_editor = pdf_facades.FormEditor()

    # Open input PDF file
    form_editor.bind_pdf(input_file_name)

    # Remove JavaScript action from the field
    if not form_editor.remove_field_action("Script_Demo_Button"):
        raise Exception("Failed to remove field script")

    # Save output PDF file
    form_editor.save(output_file_name)
```
