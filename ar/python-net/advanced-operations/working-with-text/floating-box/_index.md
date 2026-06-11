---
title: استخدم FloatingBox لتخطيط PDF في بايثون
linktitle: استخدام الصندوق العائم
type: docs
weight: 30
url: /ar/python-net/floating-box/
description: تعرف على كيفية استخدام FloatingBox لتخطيط النص والمحتوى متعدد الأعمدة والموضع الدقيق في مستندات PDF باستخدام Python.
lastmod: "2026-06-11"
sitemap:
    changefreq: "monthly"
    priority: 0.5
TechArticle: true
AlternativeHeadline: قم بإنشاء ووضع حاويات FloatingBox ذات النمط في PDF باستخدام Python
Abstract: تشرح هذه المقالة كيفية استخدام FloatingBox في Aspose.PDF لبيثون عبر .NET. تعرف على كيفية وضع النص والمحتوى الآخر في حاويات عائمة ذات نمط، والتحكم في التخطيط، والحدود، والمحاذاة، والقص، وإنشاء تصميمات أكثر تنظيمًا لصفحات PDF في Python.
---

## الاستخدام الأساسي للصندوق العائم

ال [`FloatingBox`](https://reference.aspose.com/pdf/python-net/aspose.pdf/floatingbox/) الفئة عبارة عن حاوية لوضع النص والمحتويات الأخرى على صفحة PDF. يمنحك تحكمًا أقوى في التخطيط والحدود والتصميم مقارنة بالفقرات النصية العادية. إذا تجاوز المحتوى حجم المربع، يتم التحكم في سلوك القطع من خلال إعدادات الصندوق.

استخدم هذه الصفحة عندما تحتاج إلى حاويات نصية منظمة وتخطيطات متعددة الأعمدة وتحديد المواقع بدقة في مستندات PDF باستخدام Aspose.PDF لـ Python عبر .NET.

1. قم بإنشاء ملف جديد [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. إضافة [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) إلى المستند.
1. قم بإنشاء [`FloatingBox`](https://reference.aspose.com/pdf/python-net/aspose.pdf/floatingbox/).
1. قم بتعيين حدود الصندوق باستخدام [`BorderInfo`](https://reference.aspose.com/pdf/python-net/aspose.pdf/borderinfo/) و [`BorderSide`](https://reference.aspose.com/pdf/python-net/aspose.pdf/borderside/).
1. تكرار مربع التحكم مع [`is_need_repeating`](https://reference.aspose.com/pdf/python-net/aspose.pdf/floatingbox/#properties) الملكية.
1. إضافة محتوى نصي باستخدام [`TextFragment`](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragment/).
1. أضف `FloatingBox` إلى [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/).
1. احفظ مستند PDF النهائي باستخدام [`Document.save()`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods).

```python
import aspose.pdf as ap

def create_and_add_floating_box(outfile):
    # Create PDF document
    with ap.Document() as document:
        # Add page to pages collection of PDF
        page = document.pages.add()
        # Create and fill box
        box = ap.FloatingBox(400, 30)
        box.border = ap.BorderInfo(ap.BorderSide.ALL, 1.5, ap.Color.dark_green)
        box.is_need_repeating = False
        phrase = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce quam odio, sollicitudin ac mauris vel, suscipit pellentesque nisi."
        box.paragraphs.add(ap.text.TextFragment(phrase))
        # Add box
        page.paragraphs.add(box)
        document.save(outfile)
```

في المثال أعلاه، `FloatingBox` تم إنشاؤه بعرض 400 نقطة وارتفاع 30 نقطة.
يتجاوز النص الارتفاع المتاح عن قصد، لذلك يتم قص جزء منه.

![صورة 1](image01.png)

ال [`is_need_repeating`](https://reference.aspose.com/pdf/python-net/aspose.pdf/floatingbox/#properties) عقار بقيمة `False` يحد من عرض النص إلى صفحة واحدة.

إذا قمت بتعيين هذه الخاصية إلى `True`، يعاد تدفق النص إلى الصفحات اللاحقة في نفس الموضع.

![الصورة 2](image02.png)

## ميزات الصندوق العائم المتقدمة

### دعم متعدد الأعمدة

#### تخطيط متعدد الأعمدة (حالة بسيطة)

`FloatingBox` يدعم تخطيط متعدد الأعمدة. لإنشاء مثل هذا التخطيط، يجب تحديد قيم [`ColumnInfo`](https://reference.aspose.com/pdf/python-net/aspose.pdf/columninfo/) خصائص.

* `column_widths` هي سلسلة تحدد عرض كل عمود بالنقاط.
* `column_spacing` هي سلسلة تحدد عرض الفجوة بين الأعمدة.
* `column_count` هو عدد الأعمدة.

```python
import sys
import aspose.pdf as ap
from os import path

def multi_column_layout(outfile):
    # Create PDF document
    with ap.Document() as document:
        # Add page to pages collection of PDF
        page = document.pages.add()
        # Set margin settings
        page.page_info.margin = ap.MarginInfo(36, 18, 36, 18)
        column_count = 3
        spacing = 10
        width = (
            page.page_info.width
            - page.page_info.margin.left
            - page.page_info.margin.right
            - (column_count - 1) * spacing
        )
        column_width = width / 3
        # Create FloatingBox
        box = ap.FloatingBox()
        box.is_need_repeating = True
        box.column_info.column_widths = f"{column_width} {column_width} {column_width}"
        box.column_info.column_spacing = f"{spacing}"
        box.column_info.column_count = 3
        phrase = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce quam odio, sollicitudin ac mauris vel, suscipit pellentesque nisi."
        paragraphs = [
            phrase,
            phrase,
            phrase,
            phrase,
            phrase,
            phrase,
            phrase,
            phrase,
            phrase,
            phrase,
        ]
        for paragraph in paragraphs:
            box.paragraphs.add(ap.text.TextFragment(paragraph))
        # Add a box to a page
        page.paragraphs.add(box)
        # Save PDF document
        document.save(outfile)
```

يقوم المثال بإنشاء عينة من الفقرات ووضعها عبر ثلاثة أعمدة. يستمر المحتوى في الصفحات الإضافية حتى يتم عرض جميع الفقرات.

#### تخطيط متعدد الأعمدة مع بدء العمود القسري

يستخدم هذا المثال نفس الإعداد متعدد الأعمدة، ولكنه يفرض على كل فقرة مضافة أن تبدأ في عمود جديد. للقيام بذلك، قم بتعيين `is_first_paragraph_in_column = True` على كل `TextFragment` قبل إضافته إلى `FloatingBox`.

```python
import sys
import aspose.pdf as ap
from os import path

def multi_column_layout_2(outfile):
    # Create PDF document
    with ap.Document() as document:
        # Add page to pages collection of PDF
        page = document.pages.add()
        # Set margin settings
        page.page_info.margin = ap.MarginInfo(36, 18, 36, 18)
        column_count = 3
        spacing = 10
        width = (
            page.page_info.width
            - page.page_info.margin.left
            - page.page_info.margin.right
            - (column_count - 1) * spacing
        )
        column_width = width / 3
        # Create FloatingBox
        box = ap.FloatingBox()
        box.is_need_repeating = True
        box.column_info.column_widths = f"{column_width} {column_width} {column_width}"
        box.column_info.column_spacing = f"{spacing}"
        box.column_info.column_count = 3
        phrase = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce quam odio, sollicitudin ac mauris vel, suscipit pellentesque nisi."
        paragraphs = [
            phrase,
            phrase,
            phrase,
            phrase,
            phrase,
            phrase,
            phrase,
            phrase,
            phrase,
            phrase,
        ]
        for paragraph in paragraphs:
            text = ap.text.TextFragment(paragraph)
            text.is_first_paragraph_in_column = True
            box.paragraphs.add(text)
        # Add a box to a page
        page.paragraphs.add(box)
        # Save PDF document
        document.save(outfile)
```

### دعم الخلفية

قم بتطبيق لون الخلفية على `FloatingBox` في وثيقة PDF باستخدام Aspose.PDF لبيثون عبر.NET.
من خلال تعيين [`Color`](https://reference.aspose.com/pdf/python-net/aspose.pdf/color/) إلى `background_color`، يمكنك تمييز المحتوى الخاص بالعناوين أو وسائل الشرح أو الأقسام ذات الأنماط.

يوضح مقتطف الشفرة هذا كيفية إنشاء مربع نص بسيط باللون الأخضر الفاتح مع نموذج للمحتوى.

```python
import sys
import aspose.pdf as ap
from os import path

def background_support(outfile):
    # Create PDF document
    with ap.Document() as document:
        # Add page to pages collection of PDF
        page = document.pages.add()
        # Create and fill box
        box = ap.FloatingBox(400, 30)
        box.background_color = ap.Color.light_green
        box.is_need_repeating = False
        box.paragraphs.add(ap.text.TextFragment("text example"))
        # Add box
        page.paragraphs.add(box)
        # Save PDF document
        document.save(outfile)
```

### دعم تحديد المواقع

موقف أ `FloatingBox` على الصفحة يتم التحكم فيها بواسطة `positioning_mode`, `left`، و `top`.
عندما `positioning_mode` هو:

* [`ParagraphPositioningMode.DEFAULT`](https://reference.aspose.com/pdf/python-net/aspose.pdf/paragraphpositioningmode/) (افتراضي)

يعتمد الموقع على العناصر المضافة مسبقًا. تؤثر إضافة فقرة جديدة على تدفق العناصر اللاحقة. إذا [`left`](https://reference.aspose.com/pdf/python-net/aspose.pdf/floatingbox/#properties) أو [`top`](https://reference.aspose.com/pdf/python-net/aspose.pdf/floatingbox/#properties) ليست صفرية، ويتم تطبيقها أيضًا.

* [`ParagraphPositioningMode.ABSOLUTE`](https://reference.aspose.com/pdf/python-net/aspose.pdf/paragraphpositioningmode/)

تم إصلاح الموقع بواسطة `left` و `top`؛ لا يعتمد على العناصر السابقة ولا يؤثر على تدفق العناصر اللاحقة.

```python
import sys
import aspose.pdf as ap
from os import path

def offset_support(outfile):
    # Create PDF document
    with ap.Document() as document:
        # Add page to pages collection of PDF
        page = document.pages.add()
        # Create and fill box
        box = ap.FloatingBox(400, 30)
        box.top = 45
        box.left = 15
        box.positioning_mode = ap.ParagraphPositioningMode.ABSOLUTE
        box.border = ap.BorderInfo(ap.BorderSide.ALL, 1.5, ap.Color.dark_green)
        box.paragraphs.add(ap.text.TextFragment("text example 1"))
        page.paragraphs.add(ap.text.TextFragment("text example 2"))
        # Add the box to the page
        page.paragraphs.add(box)
        page.paragraphs.add(ap.text.TextFragment("text example 3"))
        document.save(outfile)
```

### قم بمحاذاة المربعات العائمة مع المحاذاة الرأسية والأفقية في PDF

محاذاة `FloatingBox` عناصر على صفحة PDF باستخدام [`VerticalAlignment`](https://reference.aspose.com/pdf/python-net/aspose.pdf/verticalalignment/) و [`HorizontalAlignment`](https://reference.aspose.com/pdf/python-net/aspose.pdf/horizontalalignment/) في Aspose.PDF لبيثون عبر.NET. يساعدك هذا في وضع الحاويات العائمة في المواضع العلوية أو الوسطى أو السفلية لتخطيطات الصفحات أو كتل الرأس/التذييل أو الملاحظات الجانبية.

1. قم بإنشاء مستند PDF جديد.
1. أضف صفحة إلى المستند.
1. أضف الأول `FloatingBox` مع المحاذاة السفلية اليمنى.
1. أضف الثانية `FloatingBox` مع محاذاة وسط اليمين.
1. أضف الثالث `FloatingBox` مع المحاذاة العلوية اليمنى.
1. احفظ المستند.

```python
import sys
import aspose.pdf as ap
from os import path

def align_text_to_float(outfile):
    # Create PDF document
    with ap.Document() as document:
        # Add page to pages collection of PDF
        page = document.pages.add()

        # Create float box
        float_box = ap.FloatingBox(100, 100)
        # Set settings to float box
        float_box.vertical_alignment = ap.VerticalAlignment.BOTTOM
        float_box.horizontal_alignment = ap.HorizontalAlignment.RIGHT
        float_box.paragraphs.add(ap.text.TextFragment("FloatingBox_bottom"))
        float_box.border = ap.BorderInfo(ap.BorderSide.ALL, ap.Color.blue)
        # Add float box
        page.paragraphs.add(float_box)

        # Create float box
        float_box_2 = ap.FloatingBox(100, 100)
        # Set settings to float box
        float_box_2.vertical_alignment = ap.VerticalAlignment.CENTER
        float_box_2.horizontal_alignment = ap.HorizontalAlignment.RIGHT
        float_box_2.paragraphs.add(ap.text.TextFragment("FloatingBox_center"))
        float_box_2.border = ap.BorderInfo(ap.BorderSide.ALL, ap.Color.blue)
        # Add float box
        page.paragraphs.add(float_box_2)

        # Create float box
        float_box_3 = ap.FloatingBox(100, 100)
        # Set settings to float box
        float_box_3.vertical_alignment = ap.VerticalAlignment.TOP
        float_box_3.horizontal_alignment = ap.HorizontalAlignment.RIGHT
        float_box_3.paragraphs.add(ap.text.TextFragment("FloatingBox_top"))
        float_box_3.border = ap.BorderInfo(ap.BorderSide.ALL, ap.Color.blue)
        # Add float box
        page.paragraphs.add(float_box_3)

        # Save the document
        document.save(outfile)
```

## موضوعات نصية ذات صلة

* [العمل مع النص في PDF باستخدام Python](/pdf/ar/python-net/working-with-text/)
* [إضافة نص إلى PDF](/pdf/ar/python-net/add-text-to-pdf-file/)
* [تنسيق نص PDF في بايثون](/pdf/ar/python-net/text-formatting-inside-pdf/)
* [إضافة تلميحات الأدوات إلى نص PDF في Python](/pdf/ar/python-net/pdf-tooltip/)
