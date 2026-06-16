---
title: إضافة أرقام الصفحات إلى PDF في Python
linktitle: إضافة رقم الصفحة
type: docs
weight: 30
url: /ar/python-net/add-page-number/
description: تعرف على كيفية إضافة طوابع أرقام الصفحات إلى مستندات PDF في Python.
lastmod: "2026-06-11"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: كيفية إضافة رقم الصفحة إلى PDF باستخدام Python
Abstract: تتناول هذه المقالة أهمية إضافة أرقام الصفحات إلى المستندات لتسهيل التنقل وتقدم Aspose.PDF لـ Python عبر مكتبة.NET كأداة لتحقيق ذلك في ملفات PDF. تستخدم المكتبة فئة PageNumberStamp، التي توفر خصائص لتخصيص طابع رقم الصفحة، بما في ذلك التنسيق والهوامش والمحاذاة ورقم البداية. تتضمن العملية إنشاء كائن مستند وكائن PageNumberStamp، وتكوين الخصائص المطلوبة، وتطبيق الطابع على صفحات PDF باستخدام طريقة add_stamp (). تقدم المقالة مثالاً على رمز Python يوضح كيفية إعداد وتطبيق طوابع أرقام الصفحات بسمات الخط القابلة للتخصيص.
---

يجب أن تحتوي جميع المستندات على أرقام صفحات فيها. يسهّل رقم الصفحة على القارئ تحديد أجزاء مختلفة من المستند.

**Aspose.pdf لبيثون عبر .NET** يسمح لك بإضافة أرقام الصفحات باستخدام [ختم رقم الصفحة](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagenumberstamp/).

## إضافة ختم رقم الصفحة إلى PDF

إضافة طوابع أرقام الصفحات الديناميكية إلى PDF [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) باستخدام Aspose.PDF لبيثون. ال [`PageNumberStamp`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagenumberstamp/) يسمح لك الكائن بعرض رقم الصفحة الحالية تلقائيًا مع إجمالي عدد الصفحات. يوضح المثال كيفية إنشاء طابع رقم الصفحة وتخصيص مظهره (الخط والحجم والنمط واللون والمحاذاة والهوامش) باستخدام [`TextState`](https://reference.aspose.com/pdf/python-net/aspose.pdf/textstate/)، وتطبيقه على مادة محددة [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) في ملف PDF عبر [`Page.add_stamp()`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/#methods) طريقة. تأتي قيم المحاذاة من [`HorizontalAlignment`](https://reference.aspose.com/pdf/python-net/aspose.pdf/horizontalalignment/) يتوفر التعداد واللون/الخط/النمط من خلال [`Color`](https://reference.aspose.com/pdf/python-net/aspose.pdf/color/) و [`FontStyles`](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/fontstyles/) (تم اكتشاف الخطوط عبر [`FontRepository.find_font()`](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/fontrepository/#methods)). هذه الوظيفة مفيدة لإنشاء مستندات احترافية مرقمة وأتمتة ترقيم الصفحات في عمليات سير عمل PDF.

1. افتح وثيقة PDF.
1. قم بإنشاء طابع رقم الصفحة.
1. قم بتعيين خصائص الطوابع.
1. تخصيص نمط النص.
1. قم بتطبيق الطابع على الصفحة.
1. احفظ ملف PDF المعدل.

```python
import sys
import aspose.pdf as ap
from os import path

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
    page_number_stamp.text_state.font_style = (
        ap.text.FontStyles.BOLD | ap.text.FontStyles.ITALIC
    )
    page_number_stamp.text_state.foreground_color = ap.Color.blue_violet

    # Add stamp to particular page
    document.pages[1].add_stamp(page_number_stamp)

    # Save output document
    document.save(output_file_name)
```

## إضافة أرقام الصفحات الرومانية إلى PDF

أضف أرقام الصفحات بصيغة الأرقام الرومانية إلى جميع صفحات وثيقة PDF. تتم إضافة أرقام الصفحات كطوابع باستخدام [`PageNumberStamp`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagenumberstamp/)، مع تخصيص الخط والحجم والنمط واللون والمحاذاة. استخدم [`NumberingStyle`](https://reference.aspose.com/pdf/python-net/aspose.pdf/numberingstyle/) التعداد لاختيار الأرقام الرومانية أو أنظمة الترقيم الأخرى. يمكن أن يبدأ الترقيم أيضًا من أي قيمة محددة.

1. افتح وثيقة PDF.
1. قم بإنشاء طابع رقم الصفحة.
1. قم بتكوين خصائص الطوابع.
1. تعيين مظهر النص.
1. قم بتطبيق الطابع على جميع الصفحات.
1. احفظ ملف PDF المعدل.

```python
import sys
import aspose.pdf as ap
from os import path

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

[إضافة أرقام صفحات PDF](https://products.aspose.app/pdf/page-number) هو تطبيق ويب مجاني عبر الإنترنت يسمح لك بالتحقيق في كيفية عمل وظيفة إضافة أرقام الصفحات.

[![كيفية إضافة رقم الصفحة في pdf باستخدام Python](page_number.png)](https://products.aspose.app/pdf/page-number)

## موضوعات الختم ذات الصلة

- [ختم صفحات PDF في بايثون](/pdf/ar/python-net/stamping/)
- [أضف طوابع الصفحة إلى PDF في Python](/pdf/ar/python-net/page-stamps-in-the-pdf-file/)
- [أضف طوابع صور إلى PDF في Python](/pdf/ar/python-net/image-stamps-in-pdf-page/)
- [أضف طوابع نصية إلى PDF في Python](/pdf/ar/python-net/text-stamps-in-the-pdf-file/)