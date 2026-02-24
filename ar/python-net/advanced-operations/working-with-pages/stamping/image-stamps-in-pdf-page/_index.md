---
title: إضافة علامات الصورة في PDF باستخدام بايثون
linktitle: علامات الصورة في ملف PDF
type: docs
weight: 10
url: /ar/python-net/image-stamps-in-pdf-page/
description: أضف علامة الصورة في مستند PDF الخاص بك باستخدام فئة ImageStamp مع مكتبة Aspose.PDF للغة بايثون.
lastmod: "2025-11-16"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: كيفية إضافة علامات الصورة في PDF باستخدام بايثون
Abstract: توفر هذه المقالة دليلًا شاملاً حول إضافة علامات الصور إلى ملفات PDF باستخدام مكتبة Aspose.PDF للبايثون. تشرح استخدام فئة `ImageStamp` التي تسمح بتخصيص العلامات المستندة إلى الصور بما في ذلك الخصائص مثل الارتفاع، العرض، الشفافية، والدوران. تتضمن العملية إنشاء كائن `Document` وكائن `ImageStamp` بالخصائص المطلوبة، ثم إضافة العلامة إلى صفحة محددة من PDF باستخدام طريقة `add_stamp()`. تشمل المقالة مقتطفات شفرة بايثون توضح كيفية تطبيق علامة صورة على PDF والتحكم في جودتها باستخدام الخاصية `quality` التي تضبط جودة الصورة بالنسبة المئوية. بالإضافة إلى ذلك، تشرح المقالة كيفية استخدام علامات الصور كخلفيات في صناديق عائمة باستخدام فئة `FloatingBox`، وتقدم مثالًا آخر للشفرة لبيان كيفية تنفيذ ذلك. هذا الدليل يمثل مصدرًا مفيدًا للمطورين الذين يرغبون في تحسين ملفات PDF باستخدام علامات الصور عبر Aspose.PDF.
---

## إضافة علامة صورة في ملف PDF

يمكنك استخدام الفئة [ImageStamp](https://reference.aspose.com/pdf/python-net/aspose.pdf/imagestamp/) لإضافة علامة صورة إلى ملف PDF. توفر الفئة [ImageStamp](https://reference.aspose.com/pdf/python-net/aspose.pdf/imagestamp/) الخصائص اللازمة لإنشاء علامة مستندة إلى صورة، مثل الارتفاع والعرض والشفافية وغيرها. يمكن وضع العلامة، تغيير حجمها، تدويرها، وجعلها شفافة جزئياً، مما يسمح بإضافة علامة مائية أو علامة تجارية أو ملاحظات.

تظهر مقتطف الشفرة التالي كيفية إضافة علامة صورة في ملف PDF.

1. تحميل ملف PDF باستخدام 'ap.Document()'.
1. إنشاء علامة صورة باستخدام 'ImageStamp()'.
1. ضبط خصائص العلامة.
1. إضافة العلامة إلى الصفحة المستهدفة.
1. حفظ ملف PDF المعدل.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

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

## التحكم في جودة الصورة عند إضافة العلامة

عند إضافة صورة كعنصر علامة، يمكنك التحكم في جودة الصورة. تُستخدم خاصية [quality](https://reference.aspose.com/pdf/python-net/aspose.pdf/imagestamp/#properties) في فئة [ImageStamp](https://reference.aspose.com/pdf/python-net/aspose.pdf/imagestamp/) لهذا الغرض. تُشير إلى جودة الصورة بالنسبة المئوية (القيم الصالحة هي 0..100).
من خلال ضبط خاصية الجودة، يمكنك تقليل دقة الصورة لتحسين حجم PDF أو الحفاظ على وضوح أعلى.

1. فتح وثيقة PDF.
1. إنشاء علامة صورة.
1. ضبط جودة الصورة.
1. إضافة العلامة إلى الصفحة المستهدفة.
1. حفظ ملف PDF المعدل.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def add_image_stamp_image_control_image_quality(infile, input_image_file, outfile):
    document = ap.Document(infile)

    image_stamp = ap.ImageStamp(input_image_file)
    image_stamp.quality = 10

    document.pages[1].add_stamp(image_stamp)
    document.save(outfile)
```

## علامة الصورة كخلفية في الصندوق العائم

إنشاء [FloatingBox](https://reference.aspose.com/pdf/python-net/aspose.pdf/floatingbox/) في ملف PDF وتطبيق صورة كخلفيته. يوضح أيضاً كيفية إضافة نص، ضبط الحدود، لون الخلفية، وتحديد موقع الصندوق بدقة على الصفحة. هذا مفيد لإنشاء محتوى PDF غني بصرياً مثل الملاحظات التوضيحية، اللافتات، أو الأقسام المميزة بنص فوق الصور.

1. فتح أو إنشاء وثيقة PDF.
1. إنشاء كائن 'FloatingBox'.
1. إضافة محتوى نصي إلى الصندوق.
1. ضبط حدود الصندوق ولون الخلفية.
1. إضافة صورة خلفية.
1. إضافة الـ FloatingBox إلى الصفحة.
1. حفظ وثيقة PDF.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def add_image_as_background_in_floating_box(infile, input_image_file, outfile):

    document = ap.Document(infile)
    # Add page to PDF document
    page = document.pages.add()
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


