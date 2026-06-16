---
title: تحويل PDF إلى بوربوينت في بايثون
linktitle: تحويل PDF إلى بوربوينت
type: docs
weight: 30
url: /ar/python-net/convert-pdf-to-powerpoint/
description: تعرف على كيفية تحويل PDF إلى PowerPoint في Python، بما في ذلك PDF إلى PPTX، والشرائح كصور، ودقة الصورة المخصصة باستخدام Aspose.PDF.
lastmod: "2026-06-11"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: تحويل PDF إلى شرائح بوربوينت PPTX في بايثون
Abstract: توضح هذه المقالة كيفية تحويل ملفات PDF إلى عروض PowerPoint التقديمية باستخدام Aspose.PDF لبيثون عبر .NET. ويغطي تحويل PDF إلى PPTX، وتحويل الشرائح كصور، وإعداد دقة الصورة لإخراج العرض التقديمي.
---

## تحويل PDF إلى بوربوينت في بايثون

**Aspose.pdf لبايثون عبر .NET** يتيح لك تحويل ملفات PDF إلى عروض بوربوينت PPTX من كود بايثون.

استخدم سير العمل هذا عندما تحتاج إلى إعادة توظيف تقارير PDF أو مجموعات الشرائح أو الكتيبات أو النشرات كملفات PowerPoint. أثناء التحويل، يتم تحويل صفحات PDF الفردية إلى شرائح منفصلة في ملف PPTX.

أثناء تحويل PDF إلى PPTX، يمكن عرض النص كنص قابل للتحديد يمكنك تحديثه في PowerPoint. لتحويل ملفات PDF إلى صيغة PPTX، يوفر Aspose.PDF [خيارات حفظ PPTX](https://reference.aspose.com/pdf/python-net/aspose.pdf/pptxsaveoptions/) فئة. قم بتمرير `PptxSaveOptions` الكائن باعتباره الحجة الثانية لـ [حفظ ()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) طريقة.

## تحويل PDF إلى PPTX بلغة بايثون

لتحويل PDF إلى PPTX، استخدم خطوات التعليمات البرمجية التالية.

الخطوات: تحويل PDF إلى بوربوينت في بايثون

1. قم بإنشاء مثيل لـ [مستند](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) فئة.
1. قم بإنشاء مثيل لـ [خيارات حفظ PPTX](https://reference.aspose.com/pdf/python-net/aspose.pdf/pptxsaveoptions/) فئة.
1. اتصل بـ [حفظ المستند ()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) طريقة.

```python
import aspose.pdf as ap
from os import path
import sys

def convert_PDF_to_PPTX(infile, outfile):
    document = ap.Document(infile)
    save_options = ap.PptxSaveOptions()
    document.save(outfile, save_options)
```

## تحويل PDF إلى PPTX باستخدام الشرائح كصور

{{% alert color="success" %}}
** حاول تحويل PDF إلى PowerPoint عبر الإنترنت**

يوفر Aspose.PDF خدمة الإنترنت [«PDF إلى PPTX»](https://products.aspose.app/pdf/conversion/pdf-to-pptx) تطبيق حيث يمكنك اختبار جودة التحويل.


[![Aspose.PDF - تحويل ملفات PDF إلى PPTX مع التطبيق](pdf_to_pptx.png)](https://products.aspose.app/pdf/conversion/pdf-to-pptx)
{{% /alert %}}

في حالة احتياجك لتحويل ملف PDF قابل للبحث إلى PPTX كصور بدلاً من نص قابل للتحديد، يوفر Aspose.PDF هذه الميزة عبر [خيارات حفظ PPTX](https://reference.aspose.com/pdf/python-net/aspose.pdf/pptxsaveoptions/) فئة. لتحقيق ذلك، قم بتعيين الخاصية [الشرائح كصور](https://reference.aspose.com/pdf/python-net/aspose.pdf/pptxsaveoptions/#properties) من [خيارات حفظ PPTX](https://reference.aspose.com/pdf/python-net/aspose.pdf/pptxsaveoptions/) class to 'true' كما هو موضح في نموذج التعليمات البرمجية التالي.

```python
import aspose.pdf as ap
from os import path
import sys

def convert_PDF_to_PPTX_slides_as_images(infile, outfile):

    document = ap.Document(infile)
    save_options = ap.PptxSaveOptions()
    save_options.slides_as_images = True

    document.save(outfile, save_options)
```

## تحويل PDF إلى PPTX مع دقة الصورة المخصصة

تقوم هذه الطريقة بتحويل مستند PDF إلى ملف PowerPoint (PPTX) أثناء تعيين دقة صورة مخصصة (300 نقطة في البوصة) لتحسين الجودة.

1. قم بتحميل ملف PDF إلى كائن «AP.Document».
1. قم بإنشاء مثيل «PPTxSaveOptions».
1. قم بتعيين خاصية «image_resolution» إلى 300 نقطة في البوصة للحصول على عرض عالي الجودة.
1. احفظ PDF كملف PPTX باستخدام خيارات الحفظ المحددة.

```python
import aspose.pdf as ap
from os import path
import sys

def convert_PDF_to_PPTX_image_resolution(infile, outfile):
    document = ap.Document(infile)
    save_options = ap.PptxSaveOptions()
    save_options.image_resolution = 300

    document.save(outfile, save_options)
```

## التحويلات ذات الصلة

- [تحويل ملفات PDF إلى وورد](/pdf/ar/python-net/convert-pdf-to-word/) لإخراج مستند قابل للتحرير بدلاً من الشرائح.
- [تحويل ملفات PDF إلى إكسيل](/pdf/ar/python-net/convert-pdf-to-excel/) عندما يحتوي ملف PDF المصدر على بيانات أعمال مليئة بالجدول.
- [تحويل ملفات PDF إلى HTML](/pdf/ar/python-net/convert-pdf-to-html/) لعمليات سير عمل النشر الجاهزة للمتصفح.
