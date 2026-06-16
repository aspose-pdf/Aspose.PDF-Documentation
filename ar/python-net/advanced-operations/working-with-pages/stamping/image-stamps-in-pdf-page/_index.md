---
title: إضافة طوابع صور إلى PDF في Python
linktitle: طوابع الصور في ملف PDF
type: docs
weight: 10
url: /ar/python-net/image-stamps-in-pdf-page/
description: تعرف على كيفية إضافة طوابع صور إلى صفحات PDF في Python.
lastmod: "2026-06-11"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: كيفية إضافة طوابع الصور في PDF باستخدام Python
Abstract: توفر هذه المقالة دليلًا شاملاً حول إضافة طوابع صور إلى ملفات PDF باستخدام مكتبة Aspose.PDF لـ Python. ويوضح بالتفصيل استخدام فئة `ImageStamp`، التي تسمح بتخصيص الطوابع القائمة على الصور بما في ذلك الخصائص مثل الارتفاع والعرض والعتامة والدوران. تتضمن العملية إنشاء كائن «Document» وكائن «ImageStamp» بالخصائص المرغوبة، ثم إضافة الطابع إلى صفحة معينة من PDF باستخدام طريقة `add_stamp () `. تتضمن المقالة مقتطفات شفرة Python توضح كيفية تطبيق ختم صورة على ملف PDF والتحكم في جودته باستخدام خاصية «الجودة»، التي تضبط جودة الصورة من حيث النسبة المئوية. بالإضافة إلى ذلك، توضح المقالة كيفية استخدام طوابع الصور كخلفيات في مربعات عائمة مع فئة `FloatingBox`، مع تقديم مثال رمز آخر لإظهار كيفية تنفيذ ذلك. يعمل هذا الدليل كمورد مفيد للمطورين الذين يتطلعون إلى تحسين ملفات PDF باستخدام طوابع الصور باستخدام Aspose.PDF.
---

## إضافة ختم صورة في ملف PDF

يمكنك استخدام [ختم الصورة](https://reference.aspose.com/pdf/python-net/aspose.pdf/imagestamp/) فئة لإضافة طابع صورة إلى ملف PDF. ال [ختم الصورة](https://reference.aspose.com/pdf/python-net/aspose.pdf/imagestamp/) توفر الفئة الخصائص اللازمة لإنشاء طابع قائم على الصورة، مثل الارتفاع والعرض والعتامة وما إلى ذلك. يمكن وضع الختم وتغيير حجمه وتدويره وجعله شفافًا جزئيًا، مما يسمح بوضع علامة مائية أو علامة تجارية أو تعليقات توضيحية.

يوضح مقتطف الشفرة التالي كيفية إضافة طابع صورة في ملف PDF.

1. قم بتحميل ملف PDF باستخدام «AP.document ()».
1. قم بإنشاء طابع صورة باستخدام «ImageStamp ()».
1. قم بتكوين خصائص الطوابع.
1. أضف الطابع إلى الصفحة المستهدفة.
1. احفظ ملف PDF المعدل.

```python
import sys
import aspose.pdf as ap
from os import path

def add_image_stamp(infile, input_image_file, outfile):
    document = ap.Document(infile)
    image_stamp = ap.ImageStamp(input_image_file)
    image_stamp.background = True
    image_stamp.x_indent = 100
    image_stamp.y_indent = 100
    image_stamp.height = 300
    image_stamp.width = 300
    image_stamp.rotate = ap.Rotation.ON270
    image_stamp.opacity = 0.5

    document.pages[1].add_stamp(image_stamp)
    document.save(outfile)
```

## التحكم في جودة الصورة عند إضافة الطابع

عند إضافة صورة ككائن ختم، يمكنك التحكم في جودة الصورة. ال [نوعية](https://reference.aspose.com/pdf/python-net/aspose.pdf/imagestamp/#properties) الملكية الخاصة بـ [ختم الصورة](https://reference.aspose.com/pdf/python-net/aspose.pdf/imagestamp/) يتم استخدام الفصل لهذا الغرض. يشير إلى جودة الصورة بالنسب المئوية (القيم الصحيحة هي 0.. 100).
من خلال تعيين خاصية الجودة، يمكنك تقليل دقة الصورة لتحسين حجم PDF أو الحفاظ على دقة أعلى للوضوح.

1. افتح وثيقة PDF.
1. قم بإنشاء طابع صورة.
1. ضبط جودة الصورة.
1. أضف الطابع إلى الصفحة المستهدفة.
1. احفظ ملف PDF المعدل.

```python
import sys
import aspose.pdf as ap
from os import path

def add_image_stamp_with_quality_control(infile, input_image_file, outfile):
    document = ap.Document(infile)

    image_stamp = ap.ImageStamp(input_image_file)
    image_stamp.quality = 10

    document.pages[1].add_stamp(image_stamp)
    document.save(outfile)
```

## ختم الصورة كخلفية في المربع العائم

قم بإنشاء [صندوق عائم](https://reference.aspose.com/pdf/python-net/aspose.pdf/floatingbox/) في ملف PDF وتطبيق صورة كخلفية لها. كما يوضح كيفية إضافة نص وتعيين الحدود ولون الخلفية ووضع المربع بدقة على الصفحة. هذا مفيد لإنشاء محتوى PDF غني بصريًا مثل وسائل الشرح أو اللافتات أو الأقسام المميزة بنص فوق الصور.

1. افتح مستند PDF أو قم بإنشائه.
1. قم بإنشاء كائن «FloatingBox».
1. أضف محتوى نصي إلى المربع.
1. قم بتعيين حدود الصندوق ولون الخلفية.
1. أضف صورة خلفية.
1. قم بإضافة FloatingBox إلى الصفحة.
1. احفظ مستند PDF.

```python
import sys
import aspose.pdf as ap
from os import path

def add_image_as_background_in_floating_box(infile, input_image_file, outfile):
    document = ap.Document(infile)
    page = document.pages[1]
    # Create FloatingBox object
    box = ap.FloatingBox(200.0, 100.0)
    # Set left position for FloatingBox
    box.left = 40
    # Set Top position for FloatingBox
    box.top = 80
    # Set the Horizontal alignment for FloatingBox
    box.horizontal_alignment = ap.HorizontalAlignment.CENTER
    # Add text fragment to paragraphs collection of FloatingBox
    box.paragraphs.add(ap.text.TextFragment("Text in Floating Box"))
    # Set border for FloatingBox
    box.border = ap.BorderInfo(ap.BorderSide.ALL, ap.Color.red)

    img = ap.Image()
    img.file = input_image_file
    # Add background image
    box.background_image = img
    # Set background color for FloatingBox
    box.background_color = ap.Color.yellow
    # Add FloatingBox to paragraphs collection of page object
    page.paragraphs.add(box)
    # Save the PDF document
    document.save(outfile)
```

## موضوعات الختم ذات الصلة

- [ختم صفحات PDF في بايثون](/pdf/ar/python-net/stamping/)
- [أضف طوابع الصفحة إلى PDF في Python](/pdf/ar/python-net/page-stamps-in-the-pdf-file/)
- [أضف طوابع نصية إلى PDF في Python](/pdf/ar/python-net/text-stamps-in-the-pdf-file/)
- [إضافة أرقام الصفحات إلى PDF في Python](/pdf/ar/python-net/add-page-number/)