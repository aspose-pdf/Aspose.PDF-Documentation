---
title: تحويل PDF إلى PowerPoint في Python
linktitle: تحويل PDF إلى PowerPoint
type: docs
weight: 30
url: /ar/python-net/convert-pdf-to-powerpoint/
description: تعلم كيفية تحويل PDF إلى PowerPoint في Python، بما في ذلك التحويل من PDF إلى PPTX، الشرائح كصور، وتحديد دقة الصورة المخصصة باستخدام Aspose.PDF.
lastmod: "2026-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: تحويل PDF إلى شرائح PowerPoint بصيغة PPTX في Python
Abstract: توضح هذه المقالة كيفية تحويل ملفات PDF إلى عروض PowerPoint باستخدام Aspose.PDF for Python via .NET. وتغطي تحويل PDF إلى PPTX، وتحويل الشرائح إلى صور، وتعيين دقة الصورة لمخرجات العرض.
---

## تحويل PDF إلى PowerPoint في Python

**Aspose.PDF for Python via .NET** يتيح لك تحويل ملفات PDF إلى عروض PowerPoint PPTX من شفرة Python.

استخدم هذا التدفق العملي عندما تحتاج إلى إعادة استخدام تقارير PDF أو عرائض الشرائح أو الكتيبات أو النشرات كملفات PowerPoint. أثناء التحويل، يتم تحويل صفحات PDF الفردية إلى شرائح منفصلة في ملف PPTX.

أثناء تحويل PDF إلى PPTX، يمكن عرض النص كنص قابل للتحديد يمكنك تحديثه في PowerPoint. لتحويل ملفات PDF إلى تنسيق PPTX، يوفر Aspose.PDF الـ [PptxSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/pptxsaveoptions/) فئة. مرر a `PptxSaveOptions` الكائن كوسيط ثانٍ إلى [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) طريقة.

## تحويل PDF إلى PPTX في Python

لتحويل PDF إلى PPTX، استخدم خطوات الشيفرة التالية.

خطوات: تحويل PDF إلى PowerPoint في Python

1. إنشاء مثيل من [مستند](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) فئة.
1. إنشاء مثيل من [PptxSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/pptxsaveoptions/) فئة.
1. استدعِ [document.save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) طريقة.

```python
import aspose.pdf as ap
from os import path
import sys

def convert_PDF_to_PPTX(infile, outfile):
    document = ap.Document(infile)
    save_options = ap.PptxSaveOptions()
    document.save(outfile, save_options)
```

## تحويل PDF إلى PPTX مع الشرائح كصور

{{% alert color="success" %}}
**جرب تحويل PDF إلى PowerPoint عبر الإنترنت**

Aspose.PDF يوفر خدمة عبر الإنترنت ["PDF إلى PPTX"](https://products.aspose.app/pdf/conversion/pdf-to-pptx) تطبيق يمكنك من اختبار جودة التحويل.


[![Aspose.PDF تحويل PDF إلى PPTX مع التطبيق](pdf_to_pptx.png)](https://products.aspose.app/pdf/conversion/pdf-to-pptx)
{{% /alert %}}

في حال كنت بحاجة إلى تحويل PDF قابل للبحث إلى PPTX كصور بدلاً من نص قابل للتحديد، توفر Aspose.PDF هذه الميزة عبر [PptxSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/pptxsaveoptions/) الفئة. لتحقيق ذلك، قم بتعيين الخاصية [slides_as_images](https://reference.aspose.com/pdf/python-net/aspose.pdf/pptxsaveoptions/#properties) من [PptxSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/pptxsaveoptions/) class إلى 'true' كما هو موضح في عينة الشيفرة التالية.

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

## تحويل PDF إلى PPTX مع دقة صورة مخصصة

هذه الطريقة تقوم بتحويل مستند PDF إلى ملف PowerPoint (PPTX) مع ضبط دقة صورة مخصصة (300 DPI) لتحسين الجودة.

1. حمّل ملف PDF إلى كائن 'ap.Document'.
1. أنشئ مثيلًا من 'PptxSaveOptions'.
1. عيّن الخاصية 'image_resolution' إلى 300 DPI للحصول على عرض عالي الجودة.
1. احفظ ملف PDF كملف PPTX باستخدام خيارات الحفظ المحددة.

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

- [تحويل PDF إلى Word](/pdf/ar/python-net/convert-pdf-to-word/) لإنتاج مستند قابل للتحرير بدلاً من الشرائح.
- [تحويل PDF إلى Excel](/pdf/ar/python-net/convert-pdf-to-excel/) عندما يحتوي PDF المصدر على بيانات تجارية غنية بالجداول.
- [تحويل PDF إلى HTML](/pdf/ar/python-net/convert-pdf-to-html/) لسير عمل النشر الجاهز للمتصفح.
