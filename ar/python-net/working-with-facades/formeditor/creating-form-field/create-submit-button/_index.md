---
title: زر إنشاء إرسال
linktitle: زر إنشاء إرسال
type: docs
weight: 50
url: /ar/python-net/create-submit-button/
description: تعرف على كيفية إضافة زر إرسال إلى مستند PDF برمجيًا باستخدام Aspose.PDF لـ Python. يوضح هذا البرنامج التعليمي كيفية إنشاء زر يرسل بيانات النموذج إلى عنوان URL محدد ويحفظ ملف PDF المحدث.
lastmod: "2026-06-11"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: قم بإنشاء زر إرسال في ملف PDF باستخدام Aspose.PDF لبيثون
Abstract: تسمح أزرار الإرسال في نماذج PDF للمستخدمين بإرسال بيانات النموذج مباشرة إلى الخادم أو نقطة النهاية. في هذا الدليل، ستتعلم كيفية إضافة حقل زر الإرسال إلى PDF باستخدام فئة ForMeditor في Aspose.PDF لـ Python. يوضح المثال كيفية تكوين اسم الزر والتسمية وعنوان URL المستهدف والموضع، ثم حفظ مستند PDF المحدث.
---

غالبًا ما تتطلب نماذج PDF التفاعلية من المستخدمين إرسال مدخلاتهم للمعالجة، مثل إرسال نتائج الاستطلاع أو نماذج الطلبات أو بيانات التعليقات. يوفر حقل زر الإرسال هذه الوظيفة من خلال ربط الزر بنقطة نهاية الويب.

ال [المحرر السابق](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/formeditor/) تسمح الفئة بإضافة الأزرار ومربعات الاختيار وأزرار الاختيار وحقول النص وعناصر التحكم الأخرى في النموذج.

1. قم بتحميل مستند PDF موجود.
1. أضف حقل زر الإرسال إلى صفحة محددة.
1. قم بتعيين تسمية الزر وعنوان URL للإرسال المستهدف.
1. احفظ ملف PDF المحدث بالزر الجديد.

```python
import sys
from os import path
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def create_submit_button(infile, outfile):
    """Create Submit Button in PDF document."""
    pdf_form_editor = pdf_facades.FormEditor()
    pdf_form_editor.bind_pdf(infile)

    # Add Submit Button to PDF form
    pdf_form_editor.add_submit_btn(
        "submitbtn1",
        1,
        "Submit Button",
        "http://example.com/submit",
        100,
        450,
        200,
        470,
    )

    # Save updated PDF document with form fields
    pdf_form_editor.save(outfile)
```
