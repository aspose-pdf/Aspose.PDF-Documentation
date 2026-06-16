---
title: إنشاء حقل مربع القائمة
linktitle: إنشاء حقل مربع القائمة
type: docs
weight: 30
url: /ar/python-net/create-listbox-field/
description: تعرف على كيفية إضافة حقل نموذج ListBox برمجيًا إلى مستند PDF باستخدام Aspose.PDF لـ Python. يوضح هذا الدليل كيفية إدراج حقل ListBox وتحديد العناصر القابلة للتحديد وحفظ ملف PDF المحدث.
lastmod: "2026-06-11"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: قم بإنشاء حقل ListBox في ملف PDF باستخدام Aspose.PDF لبيثون
Abstract: تسمح نماذج PDF للمستخدمين بالتفاعل مع المستندات عن طريق تحديد الخيارات وإدخال البيانات وإرسال المعلومات رقميًا. يتيح حقل ListBox للمستخدمين اختيار قيمة واحدة أو عدة قيم من قائمة الخيارات المرئية. في هذا البرنامج التعليمي، ستتعلم كيفية إنشاء حقل ListBox في ملف PDF باستخدام فئة ForMeditor في Aspose.PDF لـ Python وتعبئته بعناصر محددة مسبقًا.
---

تُستخدم نماذج PDF بشكل شائع للتطبيقات والاستطلاعات ووثائق التسجيل. يعرض حقل ListBox خيارات متعددة في وقت واحد، مما يسهل على المستخدمين مراجعة العناصر وتحديدها من القائمة.

ال [المحرر السابق](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/formeditor/) توفر الفئة وظائف لإضافة أنواع مختلفة من الحقول التفاعلية، بما في ذلك عناصر ListBox.

1. قم بتحميل مستند PDF موجود.
1. حدد قائمة بالخيارات القابلة للتحديد.
1. أضف حقل ListBox إلى صفحة محددة.
1. قم بتعيين قيمة افتراضية محددة.
1. احفظ مستند PDF المحدث.

```python
import sys
from os import path
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def create_listbox_field(infile, outfile):
    """Create ListBox field in PDF document."""
    pdf_form_editor = pdf_facades.FormEditor()
    pdf_form_editor.bind_pdf(infile)

    # Add ListBox field to PDF form
    pdf_form_editor.items = ["Australia", "New Zealand", "Malaysia"]
    pdf_form_editor.add_field(
        pdf_facades.FieldType.LIST_BOX, "listbox1", "Australia", 1, 230, 398, 350, 514
    )

    # Save updated PDF document with form fields
    pdf_form_editor.save(outfile)
```
