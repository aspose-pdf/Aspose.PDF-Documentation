---
title: إضافة طوابع نصية إلى PDF عبر بايثون
linktitle: طوابع نصية في ملف PDF
type: docs
weight: 20
url: /ar/python-net/text-stamps-in-the-pdf-file/
description: أضف طابعًا نصيًا إلى مستند PDF باستخدام فئة TextStamp مع مكتبة Aspose.PDF للغة بايثون.
lastmod: "2025-11-16"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: كيفية إضافة طوابع نصية إلى PDF باستخدام بايثون
Abstract: توفر هذه المقالة دليلًا شاملاً حول إضافة طوابع نصية إلى ملفات PDF باستخدام مكتبة Aspose.PDF للغة بايثون. توضح استخدام فئة `TextStamp` لإنشاء طوابع نصية قابلة للتخصيص بخصائص مثل حجم الخط، والنمط، واللون، والمحاذاة. تشمل المقالة مقتطفات شفرة توضح كيفية إضافة طابع نصي بسيط، وتكوين محاذاة النص، وتطبيق أوضاع عرض متقدمة مثل نص ملء وضربة. يشرح القسم الأول إنشاء كائن `Document` و `TextStamp`، وضبط خصائص النص، وإضافة الطابع إلى صفحة محددة. يقدم القسم الثاني خاصية `text_alignment` لمحاذاة النص أفقياً وعمودياً، مع مثال شفرة لتوسيط النص على صفحة PDF. يناقش القسم النهائي أوضاع العرض، موضحًا كيفية إضافة نص ملء وضربة باستخدام كائن `TextState` لتعيين لون الضربة وضعية العرض قبل ربطه بطابع. يرافق كل قسم أمثلة عملية لتسهيل الفهم والتنفيذ.
---

## إضافة طابع نصي باستخدام بايثون

يمكنك استخدام فئة [TextStamp](https://reference.aspose.com/pdf/python-net/aspose.pdf/textstamp/) لإضافة طابع نصي في ملف PDF. توفر فئة [TextStamp](https://reference.aspose.com/pdf/python-net/aspose.pdf/textstamp/) الخصائص اللازمة لإنشاء طابع قائم على النص مثل حجم الخط، نمط الخط، ولون الخط وغيرها. لإضافة طابع نصي، تحتاج إلى إنشاء كائن Document وكائن TextStamp باستخدام الخصائص المطلوبة. بعد ذلك، يمكنك استدعاء طريقة [add_stamp()](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/#methods) الخاصة بالصفحة لإضافة الطابع إلى PDF. يوضح مقتطف الشفرة التالي كيفية إضافة طابع نصي في ملف PDF. هذا مفيد لإضافة تعليقات توضيحية أو علامات مائية أو تسميات إلى صفحات PDF.

1. افتح مستند PDF.
1. أنشئ كائن TextStamp.
1. عيّن سلوك خلفية الطابع.
1. ضع الطابع على الصفحة.
1. دوّر الطابع إذا لزم الأمر.
1. عيّن خصائص النص.
1. أضف الطابع إلى صفحة.
1. احفظ مستند PDF المعدل.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def add_text_stamp(input_file_name, output_file_name):
    document = ap.Document(input_file_name)

    # Create text stamp
    text_stamp = ap.TextStamp("Sample Stamp")
    # Set whether stamp is background
    text_stamp.background = True
    # Set origin
    text_stamp.x_indent = 100
    text_stamp.y_indent = 100
    # Rotate stamp
    text_stamp.rotate = ap.Rotation.ON90
    # Set text properties
    text_stamp.text_state.font = ap.text.FontRepository.find_font("Arial")
    text_stamp.text_state.font_size = 14.0
    text_stamp.text_state.font_style = ap.text.FontStyles.BOLD
    text_stamp.text_state.font_style = ap.text.FontStyles.ITALIC
    text_stamp.text_state.foreground_color = ap.Color.dark_green
    # Add stamp to particular page
    document.pages[1].add_stamp(text_stamp)

    document.save(output_file_name)
```

