---
title: إنشاء حقل زر الراديو
linktitle: إنشاء حقل زر الراديو
type: docs
weight: 40
url: /ar/python-net/create-radiobutton-field/
description: تعرف على كيفية إضافة حقل نموذج زر الاختيار برمجيًا إلى مستند PDF باستخدام Aspose.PDF لـ Python. يوضح هذا المثال كيفية إنشاء مجموعة أزرار الاختيار وتحديد الخيارات القابلة للتحديد وحفظ ملف PDF المحدث.
lastmod: "2026-06-11"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: قم بإنشاء حقل زر الراديو في ملف PDF باستخدام Aspose.PDF لبيثون
Abstract: تُستخدم أزرار الاختيار بشكل شائع في نماذج PDF للسماح للمستخدمين بتحديد خيار واحد من مجموعة اختيارات محددة مسبقًا. في هذا البرنامج التعليمي، ستتعلم كيفية إنشاء حقل زر الراديو في ملف PDF باستخدام فئة ForMeditor في Aspose.PDF لـ Python. يوضح المثال كيفية تعريف عناصر زر الاختيار وتعيين التحديد الافتراضي وحفظ المستند المحدث.
---

تتيح نماذج PDF التفاعلية للمستخدمين تقديم مدخلات منظمة مباشرة داخل المستند. يُعد حقل زر الاختيار مفيدًا عندما يتعين على المستخدمين اختيار خيار واحد فقط من خيارات متعددة، مثل تحديد بلد أو جنس أو تفضيل.

ال [المحرر السابق](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/formeditor/) يوفر الفصل طرقًا لإنشاء أنواع مختلفة من الحقول، بما في ذلك مربعات النص ومربعات الاختيار ومربعات التحرير ومربعات القوائم وأزرار الاختيار.

1. قم بتحميل مستند PDF موجود.
1. حدد قائمة خيارات زر الاختيار.
1. أضف حقل زر الاختيار إلى صفحة معينة.
1. قم بتعيين قيمة افتراضية محددة.
1. احفظ وثيقة PDF المعدلة.

```python
import sys
from os import path
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def create_radiobutton_field(infile, outfile):
    """Create RadioButton field in PDF document."""
    pdf_form_editor = pdf_facades.FormEditor()
    pdf_form_editor.bind_pdf(infile)

    # Add RadioButton field to PDF form
    pdf_form_editor.items = ["Australia", "New Zealand", "Malaysia"]
    pdf_form_editor.add_field(
        pdf_facades.FieldType.RADIO, "radiobutton1", "Malaysia", 1, 240, 498, 256, 514
    )

    # Save updated PDF document with form fields
    pdf_form_editor.save(outfile)
```
