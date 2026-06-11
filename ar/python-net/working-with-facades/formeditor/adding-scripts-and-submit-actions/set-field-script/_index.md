---
title: تعيين البرنامج النصي الميداني
linktitle: تعيين البرنامج النصي الميداني
type: docs
weight: 30
url: /ar/python-net/set-field-script/
description: يوضح مقتطف الشفرة هذا كيفية تعيين إجراء JavaScript لحقل نموذج في مستند PDF باستخدام Aspose.PDF لـ Python.
lastmod: "2026-06-11"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: قم بتعيين إجراءات JavaScript لحقول نموذج PDF باستخدام Python
Abstract: توضح هذه المقالة كيفية فتح مستند PDF، وتعيين شفرة JavaScript لحقل النموذج، وتحديث البرنامج النصي باستخدام فئة ForMeditor، وحفظ الملف المعدل. يوضح المثال كيف يمكن تجاوز البرامج النصية الموجودة لتعديل سلوك حقول النموذج.
---

غالبًا ما تعتمد نماذج PDF التفاعلية على JavaScript لأداء مهام مثل عرض التنبيهات أو التحقق من صحة الإدخال أو تشغيل سلوك النموذج الديناميكي. باستخدام Aspose.PDF لـ Python، يمكن للمطورين إدارة هذه البرامج النصية برمجيًا.

يضيف المثال أولاً إجراء JavaScript إلى الحقل ثم يستبدله بنص برمجي آخر باستخدام طريقة 'set_field_script'. يسمح هذا الأسلوب للمطورين بالتحكم أو تحديث السلوك التفاعلي لعناصر نموذج PDF مثل الأزرار أو حقول الإدخال.

يُطلق على حقل النموذج المستخدم في هذا المثال اسم «Script_Demo_Button»، والذي يمثل عادةً زرًا يقوم بتنفيذ البرنامج النصي المعين عند تشغيله.

استخدام [المحرر السابق](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/formeditor/) فئة من [واجهات أسبوز.pdf](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/) الوحدة، يمكن للمطورين إدارة إجراءات JavaScript المرتبطة بحقول النموذج برمجيًا:

1. افتح مستند نموذج PDF موجود.
1. أضف إجراء JavaScript إلى حقل النموذج.
1. قم بتعيين (استبدال) إجراء JavaScript ببرنامج نصي جديد.
1. احفظ وثيقة PDF المعدلة.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def set_field_script(input_file_name, output_file_name):
    # Create FormEditor object
    form_editor = pdf_facades.FormEditor()

    # Open input PDF file
    form_editor.bind_pdf(input_file_name)

    # Add JavaScript action to the field
    form_editor.add_field_script(
        "Script_Demo_Button", "app.alert('Script 1 has been executed');"
    )

    # Set JavaScript action for the field
    form_editor.set_field_script(
        "Script_Demo_Button", "app.alert('Script 2 has been executed');"
    )

    # Save output PDF file
    form_editor.save(output_file_name)
```
