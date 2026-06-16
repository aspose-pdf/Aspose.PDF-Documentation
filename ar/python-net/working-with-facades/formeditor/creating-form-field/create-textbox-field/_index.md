---
title: إنشاء حقل مربع نص
linktitle: إنشاء حقل مربع نص
type: docs
weight: 60
url: /ar/python-net/create-textbox-field/
description: تعرف على كيفية إضافة حقول TextBox برمجيًا إلى مستند PDF باستخدام Aspose.PDF لـ Python. يوضح هذا البرنامج التعليمي كيفية إدراج حقول نصية متعددة وتعيين القيم الافتراضية وحفظ مستند PDF المحدث.
lastmod: "2026-06-11"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: إنشاء حقول مربع نص في PDF باستخدام Aspose.PDF لبيثون
Abstract: تسمح حقول TextBox في نماذج PDF للمستخدمين بإدخال النص وتحريره، مما يجعل المستندات تفاعلية وسهلة الاستخدام. في هذا البرنامج التعليمي، ستتعلم كيفية إنشاء حقول نموذج TextBox في ملف PDF باستخدام فئة ForMeditor في Aspose.PDF لـ Python. يوضح المثال إضافة حقول متعددة وتحديد القيم الافتراضية وحفظ PDF المعدل.
---

غالبًا ما تتطلب نماذج PDF إدخال نص من المستخدمين، مثل الأسماء أو العناوين أو التعليقات. تعمل حقول TextBox على تمكين هذه الوظيفة من خلال توفير حقول قابلة للتحرير مباشرة داخل مستند PDF.

ال [المحرر السابق](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/formeditor/) يسمح الفصل بإضافة حقول نصية ومربعات الاختيار وأزرار الاختيار ومربعات القوائم ومربعات المجموعات والأزرار، مما يجعل من السهل إنشاء ملفات PDF تفاعلية.

1. قم بتحميل مستند PDF موجود.
1. أضف حقول TextBox متعددة لإدخال المستخدم.
1. قم بتعيين القيم الافتراضية لكل حقل.
1. احفظ مستند PDF المحدث.

```python
import sys
from os import path
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def create_textbox_field(infile, outfile):
    """Create TextBox field in PDF document."""
    pdf_form_editor = pdf_facades.FormEditor()
    pdf_form_editor.bind_pdf(infile)

    # Add TextBox field to PDF form
    pdf_form_editor.add_field(
        pdf_facades.FieldType.TEXT, "first_name", "Alexander", 1, 50, 570, 150, 590
    )
    pdf_form_editor.add_field(
        pdf_facades.FieldType.TEXT, "last_name", "Smith", 1, 235, 570, 330, 590
    )

    # Save updated PDF document with form fields
    pdf_form_editor.save(outfile)
```
