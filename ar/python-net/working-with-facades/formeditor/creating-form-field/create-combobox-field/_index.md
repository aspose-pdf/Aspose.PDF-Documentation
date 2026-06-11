---
title: إنشاء حقل كومبوبوكس
linktitle: إنشاء حقل كومبوبوكس
type: docs
weight: 20
url: /ar/python-net/create-combobox-field/
description: تحقق من كيفية إضافة حقل ComboBox (القائمة المنسدلة) برمجيًا إلى مستند PDF باستخدام Aspose.PDF لـ Python. يوضح هذا المثال كيفية إدراج حقل نموذج ComboBox وإضافة عناصر قابلة للتحديد وحفظ ملف PDF المحدث.
lastmod: "2026-06-11"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: قم بإنشاء حقل ComboBox في ملف PDF باستخدام Aspose.PDF لبيثون
Abstract: تعمل حقول النماذج التفاعلية على جعل ملفات PDF أكثر ديناميكية وسهولة في الاستخدام. يسمح حقل ComboBox للمستخدمين بتحديد خيار من قائمة منسدلة محددة مسبقًا. في هذا البرنامج التعليمي، ستتعلم كيفية إنشاء ComboBox في ملف PDF باستخدام فئة ForMeditor في Aspose.PDF لـ Python، وتعبئته بالخيارات، وحفظ المستند المعدل.
---

تُستخدم نماذج PDF على نطاق واسع لجمع المعلومات المنظمة في المستندات الرقمية مثل التطبيقات والاستطلاعات ونماذج التسجيل. يوفر حقل ComboBox طريقة ملائمة للمستخدمين للاختيار من قائمة القيم المحددة مسبقًا مع الحفاظ على النموذج مضغوطًا ومنظمًا.

ال [المحرر السابق](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/formeditor/) يتيح لك الفصل إنشاء وإدارة أنواع مختلفة من الحقول، بما في ذلك مربعات النص ومربعات الاختيار وأزرار الاختيار والقوائم المنسدلة.

1. قم بتحميل مستند PDF موجود.
1. أضف حقل كومبوبوكس باستخدام طريقة «add_field ()» ومعلمة «fieldType.combo_box».
1. استخدم طريقة 'add_list_item () 'لإدراج خيارات قابلة للتحديد في القائمة المنسدلة.
1. احفظ مستند PDF المحدث.

```python
import sys
from os import path
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def create_combobox_field(infile, outfile):
    """Create ComboBox field in PDF document."""
    pdf_form_editor = pdf_facades.FormEditor()
    pdf_form_editor.bind_pdf(infile)

    # Add ComboBox field to PDF form
    pdf_form_editor.add_field(
        pdf_facades.FieldType.COMBO_BOX, "combobox1", "Australia", 1, 230, 498, 350, 514
    )
    pdf_form_editor.add_list_item("combobox1", ["Australia", "Australia"])
    pdf_form_editor.add_list_item("combobox1", ["New Zealand", "New Zealand"])

    # Save updated PDF document with form fields
    pdf_form_editor.save(outfile)
```
