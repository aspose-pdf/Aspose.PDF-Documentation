---
title: إضافة رقم الصفحة إلى PDF باستخدام Python
linktitle: إضافة رقم الصفحة
type: docs
weight: 30
url: /ar/python-net/add-page-number/
description: تتيح لك Aspose.PDF للـ Python عبر .NET إضافة ختم رقم الصفحة إلى ملف PDF الخاص بك باستخدام فئة PageNumber Stamp.
lastmod: "2025-11-16"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: كيفية إضافة رقم الصفحة إلى PDF باستخدام Python
Abstract: تناقش هذه المقالة أهمية إضافة أرقام الصفحات إلى المستندات لتسهيل التنقل وتُقدِّم مكتبة Aspose.PDF للـ Python عبر .NET كأداة لتحقيق ذلك في ملفات PDF. تستخدم المكتبة الفئة PageNumberStamp، التي تُوفر خصائص لتخصيص ختم رقم الصفحة، بما في ذلك التنسيق والهوامش والمحاذاة ورقم البداية. تشمل العملية إنشاء كائن Document وكائن PageNumberStamp، وضبط الخصائص المطلوبة، وتطبيق الختم على صفحات PDF باستخدام طريقة add_stamp(). تُقدم المقالة مثالًا على شفرة Python يُظهر كيفية إعداد وتطبيق أغطية أرقام الصفحات مع خصائص الخط القابلة للتخصيص.
---

يجب أن تحتوي جميع المستندات على أرقام صفحات. تجعل أرقام الصفحات القارئ يسهُل عليه العثور على أجزاء مختلفة من المستند.

**Aspose.PDF for Python via .NET** يسمح لك بإضافة أرقام الصفحات باستخدام [PageNumberStamp](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagenumberstamp/).

## إضافة ختم رقم الصفحة إلى PDF

أضف أغطية أرقام صفحات ديناميكية إلى PDF [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) باستخدام Aspose.PDF للـ Python. يسمح لك كائن [`PageNumberStamp`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagenumberstamp/) بعرض رقم الصفحة الحالي تلقائيًا مع إجمالي عدد الصفحات. يُظهر المثال كيفية إنشاء ختم رقم الصفحة، وتخصيص مظهره (الخط، الحجم، النمط، اللون، المحاذاة، والهوامش) باستخدام [`TextState`](https://reference.aspose.com/pdf/python-net/aspose.pdf/textstate/)، وتطبيقه على صفحة محددة [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) في PDF عبر طريقة [`Page.add_stamp()`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/#methods). قيم المحاذاة تأتي من تعداد [`HorizontalAlignment`](https://reference.aspose.com/pdf/python-net/aspose.pdf/horizontalalignment/) ، ويتوفر اللون/الخط/النمط عبر [`Color`](https://reference.aspose.com/pdf/python-net/aspose.pdf/color/) و[`FontStyles`](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/fontstyles/) (الخطوط المكتشفة عبر [`FontRepository.find_font()`](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/fontrepository/#methods)). هذه الوظيفة مفيدة لإنشاء مستندات احترافية مرقمة وتلقائيًا لإدارة الصفحات في سير عمل PDF.

1. افتح مستند PDF.
1. أنشئ ختم رقم الصفحة.
1. اضبط خصائص الختم.
1. خصص نمط النص.
1. طبّق الختم على صفحة.
1. احفظ ملف PDF المعدّل.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def add_page_num_stamp(input_file_name, output_file_name):
    # Open document
    document = ap.Document(input_file_name)

    # Create page number stamp
    page_number_stamp = ap.PageNumberStamp()
    # Whether the stamp is background
    page_number_stamp.background = False
    page_number_stamp.format = "Page # of " + str(len(document.pages))
    page_number_stamp.bottom_margin = 10
    page_number_stamp.horizontal_alignment = ap.HorizontalAlignment.CENTER
    page_number_stamp.starting_number = 1
    # Set text properties
    page_number_stamp.text_state.font = ap.text.FontRepository.find_font("Arial")
    page_number_stamp.text_state.font_size = 14.0
    page_number_stamp.text_state.font_style = ap.text.FontStyles.BOLD
    page_number_stamp.text_state.font_style = ap.text.FontStyles.ITALIC
    page_number_stamp.text_state.foreground_color = ap.Color.blue_violet

    # Add stamp to particular page
    document.pages[1].add_stamp(page_number_stamp)

    # Save output document
    document.save(output_file_name)
```

## إضافة أرقام صفحات بالأرقام الرومانية إلى PDF

أضف أرقام صفحات بالتنسيق الروماني إلى جميع صفحات مستند PDF. تُضاف أرقام الصفحات كأغطية باستخدام [`PageNumberStamp`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagenumberstamp/)، مع إمكانية تخصيص الخط والحجم والنمط واللون والمحاذاة. استخدم تعداد [`NumberingStyle`](https://reference.aspose.com/pdf/python-net/aspose.pdf/numberingstyle/) لاختيار الأرقام الرومانية أو أنظمة ترقيم أخرى. يمكن أيضًا أن يبدأ الترقيم من أي قيمة محددة.

1. افتح مستند PDF.
1. أنشئ ختم رقم الصفحة.
1. اضبط خصائص الختم.
1. عيّن مظهر النص.
1. طبّق الختم على جميع الصفحات.
1. احفظ ملف PDF المعدّل.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def add_page_num_stamp_roman(input_file_name, output_file_name):
    # Open document
    document = ap.Document(input_file_name)

    # Create page number stamp
    page_number_stamp = ap.PageNumberStamp()
    # Whether the stamp is background
    page_number_stamp.background = False
    page_number_stamp.bottom_margin = 10
    page_number_stamp.horizontal_alignment = ap.HorizontalAlignment.CENTER
    page_number_stamp.starting_number = 42
    page_number_stamp.numbering_style = ap.NumberingStyle.NUMERALS_ROMAN_UPPERCASE

    # Set text properties
    page_number_stamp.text_state.font = ap.text.FontRepository.find_font("Arial")
    page_number_stamp.text_state.font_size = 14.0
    page_number_stamp.text_state.font_style = ap.text.FontStyles.BOLD
    page_number_stamp.text_state.foreground_color = ap.Color.blue_violet

    # Add stamp to particular page
    for page in document.pages:
        page.add_stamp(page_number_stamp)

    # Save output document
    document.save(output_file_name)
```

## مثال مباشر

[إضافة أرقام صفحات PDF](https://products.aspose.app/pdf/page-number) هو تطبيق ويب مجاني عبر الإنترنت يتيح لك استكشاف كيفية عمل وظيفة إضافة أرقام الصفحات.

[![كيفية إضافة رقم الصفحة في PDF باستخدام Python](page_number.png)](https://products.aspose.app/pdf/page-number)


