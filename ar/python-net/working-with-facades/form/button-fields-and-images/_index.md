---
title: حقول الأزرار والصور
linktitle: حقول الأزرار والصور
type: docs
weight: 40
url: /ar/python-net/button-fields-and-images/
description: يوضح هذا المثال كيفية إدارة حقول الأزرار في نموذج PDF باستخدام واجهة برمجة تطبيقات Aspose.PDF للواجهات.
lastmod: "2026-06-11"
TechArticle: true
AlternativeHeadline: إضافة مظهر الصورة إلى حقول الأزرار وقراءة علامات الإرسال
Abstract: غالبًا ما تتضمن نماذج PDF أزرارًا تفاعلية تقوم إما بتشغيل إجراءات JavaScript أو إرسال بيانات النموذج. يمكنك تحسين حقول الأزرار بصريًا عن طريق إضافة الصور كمظهر وفحص سلوك الإرسال الخاص بها برمجيًا.
---

## إضافة مظهر الصورة إلى حقول الأزرار

يشرح مقتطف الشفرة هذا كيفية إضافة مظهر صورة إلى حقل زر موجود في نموذج PDF. تعمل العملية على تحسين العرض المرئي لزر PDF عن طريق استبدال مظهره الافتراضي بصورة مخصصة.

1. قم بإنشاء كائن نموذج.
1. قم بربط ملف PDF بكائن النموذج.
1. إضافة صورة إلى حقل الزر.

    - تحديد المسار إلى ملف الصورة المرتبط بـ PDF
    - افتح الصورة في الوضع الثنائي باسم image_stream.
    - اتصل بـ fill_image_field () باستخدام اسم حقل الزر المؤهل بالكامل.

1. احفظ ملف PDF المحدث.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Add image appearance to button fields
def add_image_appearance_to_button_fields(infile, outfile):
    """Add image appearance to button fields in a PDF document."""
    # Create Form object
    pdf_form = pdf_facades.Form()

    # Bind PDF document
    pdf_form.bind_pdf(infile)

    # Add image appearance to button fields by providing the field name and image stream
    image_path = infile.replace(".pdf", ".jpg")
    with open(image_path, "rb") as image_stream:
        pdf_form.fill_image_field("Image1_af_image", image_stream)

    # Save updated PDF
    pdf_form.save(outfile)
```

## احصل على علامات الإرسال

تساعدك مكتبة Python على استرداد علامات الإرسال الخاصة بزر الإرسال في نموذج PDF باستخدام واجهة برمجة تطبيقات Aspose.PDF Facades. تحدد علامات الإرسال سلوك زر الإرسال، مثل ما إذا كان يرسل النموذج بأكمله، أو يتضمن التعليقات التوضيحية، أو يرسل بتنسيق FDF أو XFDF أو PDF أو HTML.

1. قم بإنشاء كائن نموذج.
1. اتصل بـ get_submit_flags () على كائن النموذج باستخدام اسم زر الإرسال المؤهل بالكامل.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def get_submit_flags(infile, outfile):
    # Create Form object
    pdf_form = pdf_facades.Form()

    # Bind PDF document
    pdf_form.bind_pdf(infile)
    flags = pdf_form.get_submit_flags("Submit1_af_submit")

    print(f"Submit flags: {flags}")
```
