---
title: إضافة طوابع نصية إلى PDF في Python
linktitle: طوابع نصية في ملف PDF
type: docs
weight: 20
url: /ar/python-net/text-stamps-in-the-pdf-file/
description: تعرف على كيفية إضافة طوابع نصية إلى مستندات PDF في Python.
lastmod: "2026-06-11"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: كيفية إضافة طوابع نصية في PDF باستخدام Python
Abstract: توفر هذه المقالة دليلًا شاملاً حول إضافة طوابع نصية إلى ملفات PDF باستخدام مكتبة Aspose.PDF لـ Python. ويحدد استخدام فئة `TextStamp` لإنشاء طوابع نصية قابلة للتخصيص بخصائص مثل حجم الخط والنمط واللون والمحاذاة. تتضمن المقالة مقتطفات التعليمات البرمجية التي توضح كيفية إضافة طابع نصي بسيط وتكوين محاذاة النص وتطبيق أوضاع العرض المتقدمة مثل نص حد التعبئة. يشرح القسم الأول إنشاء كائن «Document» و «TextStamp»، وتعيين خصائص النص، وإضافة الطابع إلى صفحة معينة. يقدم القسم الثاني خاصية `text_alignment` لمحاذاة النص أفقيًا وعموديًا، مع تقديم مثال برمجي لتوسيط النص على صفحة PDF. يناقش القسم الأخير أوضاع العرض، ويوضح كيفية إضافة نص حد التعبئة باستخدام كائن `textState` لتعيين لون الحد ووضع العرض قبل الربط بالطابع. يرافق كل قسم أمثلة عملية لتسهيل الفهم والتنفيذ.
---

## إضافة طابع نصي باستخدام Python

يمكنك استخدام [ختم نصي](https://reference.aspose.com/pdf/python-net/aspose.pdf/textstamp/) فئة لإضافة طابع نصي في ملف PDF. [ختم نصي](https://reference.aspose.com/pdf/python-net/aspose.pdf/textstamp/) توفر الفئة الخصائص اللازمة لإنشاء طابع يستند إلى النص مثل حجم الخط ونمط الخط ولون الخط وما إلى ذلك لإضافة طابع نصي، تحتاج إلى إنشاء كائن مستند وكائن TextStamp باستخدام الخصائص المطلوبة. بعد ذلك، يمكنك الاتصال [إضافة طابع ()](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/#methods) طريقة الصفحة لإضافة الطابع في PDF. يوضح لك مقتطف الشفرة التالي كيفية إضافة طابع نصي في ملف PDF. هذا مفيد لإضافة التعليقات التوضيحية أو العلامات المائية أو التسميات إلى صفحات PDF.

1. افتح وثيقة PDF.
1. قم بإنشاء كائن تكستستامب.
1. قم بتعيين سلوك خلفية الطوابع.
1. ضع الختم على الصفحة.
1. قم بتدوير الختم إذا لزم الأمر.
1. قم بتعيين خصائص النص.
1. أضف الطابع إلى صفحة.
1. احفظ وثيقة PDF المعدلة.

```python
import sys
import aspose.pdf as ap
from os import path

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
    text_stamp.text_state.font_style = (
        ap.text.FontStyles.BOLD | ap.text.FontStyles.ITALIC
    )
    text_stamp.text_state.foreground_color = ap.Color.dark_green
    # Add stamp to particular page
    document.pages[1].add_stamp(text_stamp)

    document.save(output_file_name)
```

## موضوعات الختم ذات الصلة

- [ختم صفحات PDF في بايثون](/pdf/ar/python-net/stamping/)
- [أضف طوابع الصفحة إلى PDF في Python](/pdf/ar/python-net/page-stamps-in-the-pdf-file/)
- [أضف طوابع صور إلى PDF في Python](/pdf/ar/python-net/image-stamps-in-pdf-page/)
- [إضافة أرقام الصفحات إلى PDF في Python](/pdf/ar/python-net/add-page-number/)