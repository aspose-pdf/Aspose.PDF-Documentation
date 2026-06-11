---
title: إنشاء حقل مربع الاختيار
linktitle: إنشاء حقل مربع الاختيار
type: docs
weight: 10
url: /ar/python-net/create-checkbox-field/
description: تعرف على كيفية إضافة حقل نموذج مربع الاختيار برمجيًا إلى مستند PDF باستخدام Aspose.PDF لـ Python. يوضح هذا الدليل كيفية استخدام فئة ForMeditor لإدراج مربع اختيار تفاعلي في ملف PDF موجود وحفظ المستند المحدث.
lastmod: "2026-06-11"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: قم بإنشاء حقل مربع الاختيار في ملف PDF باستخدام Aspose.PDF لبيثون
Abstract: تسمح حقول النماذج التفاعلية للمستخدمين بملء مستندات PDF والتفاعل معها رقميًا. في هذا البرنامج التعليمي، ستتعلم كيفية إضافة حقل مربع اختيار إلى PDF باستخدام Aspose.PDF Python API. يوضح المثال كيفية ربط مستند PDF موجود، وإنشاء حقل نموذج مربع الاختيار في الإحداثيات المحددة، وحفظ الملف المعدل.
---

تُستخدم نماذج PDF على نطاق واسع لجمع مدخلات المستخدم في المستندات مثل التطبيقات والاستطلاعات والاتفاقيات. يتيح حقل مربع الاختيار للمستخدمين تحديد خيار أو إلغاء تحديده داخل النموذج.

باستخدام Aspose.PDF لـ Python، يمكن للمطورين معالجة نماذج PDF برمجيًا. ال [المحرر السابق](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/formeditor/) يوفر الفصل طرقًا لإضافة حقول النموذج وتحريرها وإدارتها داخل مستند PDF.

1. قم بتحميل ملف PDF موجود.
1. قم باستدعاء طريقة 'add_field () 'باستخدام المعلمة «fieldType.check_box» لإنشاء مربع الاختيار وتحديد موضعه.
1. حدد اسم الحقل والتسمية التوضيحية والموضع.
1. احفظ مستند PDF المحدث.

```python
import sys
from os import path
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def create_checkbox_field(infile, outfile):
    """Create CheckBox field in PDF document."""
    pdf_form_editor = pdf_facades.FormEditor()
    pdf_form_editor.bind_pdf(infile)

    # Add CheckBox field to PDF form
    pdf_form_editor.add_field(
        pdf_facades.FieldType.CHECK_BOX,
        "checkbox1",
        "Check Box 1",
        1,
        240,
        498,
        256,
        514,
    )

    # Save updated PDF document with form fields
    pdf_form_editor.save(outfile)
```
