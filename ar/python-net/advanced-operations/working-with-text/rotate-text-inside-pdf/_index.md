---
title: تدوير نص PDF في بايثون
linktitle: تدوير النص داخل PDF
type: docs
weight: 50
url: /ar/python-net/rotate-text-inside-pdf/
description: تعرف على كيفية تدوير أجزاء النص والفقرات داخل مستندات PDF في Python.
lastmod: "2026-06-11"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: قم بتدوير أجزاء النص والفقرات في مستندات PDF باستخدام Python
Abstract: تشرح هذه المقالة كيفية تدوير النص في مستندات PDF باستخدام Aspose.PDF لـ Python عبر .NET. يوضح كيفية تعيين خاصية «التدوير» على `textFragment`، وإنشاء محتوى مستدير باستخدام `TextBuilder` و `TextParagraph`، وإضافة نص مستدير مباشرة إلى فقرات الصفحة لسيناريوهات تخطيط مختلفة.
---

قم بتدوير أجزاء النص في مستند PDF باستخدام Aspose.PDF لبيثون عبر.NET. تعرض هذه الصفحة كيفية التحكم في موضع النص وتدويره باستخدام `TextFragment`, `TextState`، و `TextBuilder`. من خلال ضبط زوايا التدوير، يمكنك إنشاء تخطيطات مثل الرؤوس القطرية والتسميات الرأسية والتعليقات التوضيحية المستديرة.

## تدوير أجزاء النص باستخدام TextBuilder في PDF

يقوم بإنشاء ملف PDF باسم `rotated_fragments.pdf` تحتوي على ثلاثة أجزاء نصية محاذاة أفقيًا:

- النص الأول غير مستدير
- يتم تدوير الثانية بزاوية 45 درجة
- يتم تدوير الثالث بزاوية 90 درجة

1. قم بإنشاء مستند PDF جديد.
1. قم بإدراج صفحة جديدة لاستضافة النص الذي تم تدويره.
1. قم بإنشاء جزء النص الأول (بدون تدوير).
1. قم بإنشاء جزء النص الثاني (دوران 45 درجة).
1. قم بإنشاء جزء النص الثالث (دوران 90 درجة).
1. إضافة أجزاء نصية باستخدام `TextBuilder`.
1. احفظ المستند.

```python
import aspose.pdf as ap

def rotate_text_inside_pdf_1(outfile):
    # Create PDF document
    with ap.Document() as document:
        # Get particular page
        page = document.pages.add()
        # Create text fragment
        text_fragment_1 = ap.text.TextFragment("main text")
        text_fragment_1.position = ap.text.Position(100, 600)
        # Set text properties
        text_fragment_1.text_state.font_size = 12
        text_fragment_1.text_state.font = ap.text.FontRepository.find_font(
            "TimesNewRoman"
        )
        # Create rotated text fragment
        text_fragment_2 = ap.text.TextFragment("rotated text")
        text_fragment_2.position = ap.text.Position(200, 600)
        # Set text properties
        text_fragment_2.text_state.font_size = 12
        text_fragment_2.text_state.font = ap.text.FontRepository.find_font(
            "TimesNewRoman"
        )
        text_fragment_2.text_state.rotation = 45
        # Create rotated text fragment
        text_fragment_3 = ap.text.TextFragment("rotated text")
        text_fragment_3.position = ap.text.Position(300, 600)
        # Set text properties
        text_fragment_3.text_state.font_size = 12
        text_fragment_3.text_state.font = ap.text.FontRepository.find_font(
            "TimesNewRoman"
        )
        text_fragment_3.text_state.rotation = 90
        # create TextBuilder object
        builder = ap.text.TextBuilder(page)
        # Append the text fragment to the PDF page
        builder.append_text(text_fragment_1)
        builder.append_text(text_fragment_2)
        builder.append_text(text_fragment_3)

        # Save the document
        document.save(outfile)
```

## قم بتدوير أجزاء النص الفردية داخل فقرة في PDF

قم بتدوير أجزاء النص الفردية داخل فقرة. يوضح كيفية إنشاء فقرة متعددة الأسطر (TextParagrapage) تحتوي على أجزاء متعددة (TextFragment)، ولكل منها زاوية دوران خاصة بها. هذه التقنية مفيدة لإنشاء مستندات غنية بصريًا تجمع بين النص الموجه أفقيًا وقطريًا - على سبيل المثال، الرؤوس المنمقة أو الرسوم التخطيطية أو التسميات المشروحة.

يقوم بإنشاء ملف PDF باسم `rotated_paragraph_fragments.pdf` تحتوي على فقرة تحتوي على ثلاثة أسطر من النص، يتم تدوير كل سطر بشكل مختلف:

- يتم تدوير السطر الأول بزاوية 45 درجة
- يظل الخط الثاني أفقيًا (0 درجة)
- يتم تدوير الخط الثالث -45 درجة

1. قم بإنشاء مستند PDF جديد.
1. أضف صفحة فارغة حيث سيظهر النص الذي تم تدويره.
1. قم بإنشاء `TextParagraph`.
1. قم بإنشاء وتكوين جزء النص الأول (دوران +45 درجة).
1. قم بإنشاء جزء النص الثاني (بدون تدوير).
1. قم بإنشاء جزء النص الثالث (دوران -45 درجة).
1. قم بإلحاق أجزاء النص بالفقرة.
1. أضف الفقرة إلى الصفحة باستخدام `TextBuilder`.
1. احفظ المستند.

```python
import aspose.pdf as ap

def rotate_text_inside_pdf_2(outfile):
    # Create PDF document
    with ap.Document() as document:
        # Get particular page
        page = document.pages.add()
        paragraph = ap.text.TextParagraph()
        paragraph.position = ap.text.Position(200, 600)
        # Create text fragment
        text_fragment_1 = ap.text.TextFragment("rotated text")
        # Set text properties
        text_fragment_1.text_state.font_size = 12
        text_fragment_1.text_state.font = ap.text.FontRepository.find_font(
            "TimesNewRoman"
        )
        # Set rotation
        text_fragment_1.text_state.rotation = 45
        # Create text fragment
        text_fragment_2 = ap.text.TextFragment("main text")
        # Set text properties
        text_fragment_2.text_state.font_size = 12
        text_fragment_2.text_state.font = ap.text.FontRepository.find_font(
            "TimesNewRoman"
        )
        # Create text fragment
        text_fragment_3 = ap.text.TextFragment("another rotated text")
        # Set text properties
        text_fragment_3.text_state.font_size = 12
        text_fragment_3.text_state.font = ap.text.FontRepository.find_font(
            "TimesNewRoman"
        )
        # Set rotation
        text_fragment_3.text_state.rotation = -45
        # Append the text fragments to the paragraph
        paragraph.append_line(text_fragment_1)
        paragraph.append_line(text_fragment_2)
        paragraph.append_line(text_fragment_3)
        # Create TextBuilder object
        text_builder = ap.text.TextBuilder(page)
        # Append the text paragraph to the PDF page
        text_builder.append_paragraph(paragraph)

        # Save the document
        document.save(outfile)
```

## تدوير النص باستخدام فقرات الصفحة في PDF

يوضح هذا القسم طريقة مبسطة لتدوير النص داخل PDF باستخدام Aspose.PDF لـ Python عبر .NET.
على عكس مناهج المستوى الأدنى مع `TextBuilder` أو `TextParagraph`، تضيف هذه الطريقة أجزاء النص المستديرة مباشرة إلى مجموعة فقرات الصفحة (`page.paragraphs`). إنه مثالي عندما تحتاج إلى تدوير النص الأساسي ولكن لا يتطلب تحديد المواقع بدقة أو هيكلة الفقرة.

يقوم بإنشاء ملف باسم `simple_rotated_text.pdf` تحتوي على:

- جزء النص الأفقي الرئيسي (دوران 0 درجة)
- جزء مستدير بزاوية 315 درجة
- جزء مستدير بزاوية 270 درجة

1. قم بتهيئة مستند PDF جديد.
1. قم بإنشاء صفحة حيث سيتم وضع النص الذي تم تدويره.
1. قم بإنشاء جزء النص الأول (بدون تدوير).
1. قم بإنشاء جزء النص الثاني (دوران 315 درجة).
1. قم بإنشاء جزء النص الثالث (دوران 270 درجة).
1. أضف أجزاء نصية مباشرة إلى فقرات الصفحة.
1. احفظ مستند PDF.

```python
import aspose.pdf as ap

def rotate_text_inside_pdf_3(outfile):
    # Create PDF document
    with ap.Document() as document:
        # Get particular page
        page = document.pages.add()
        # Create text fragment
        text_fragment_1 = ap.text.TextFragment("main text")
        # Set text properties
        text_fragment_1.text_state.font_size = 12
        text_fragment_1.text_state.font = ap.text.FontRepository.find_font(
            "TimesNewRoman"
        )
        # Create text fragment
        text_fragment_2 = ap.text.TextFragment("rotated text")
        # Set text properties
        text_fragment_2.text_state.font_size = 12
        text_fragment_2.text_state.font = ap.text.FontRepository.find_font(
            "TimesNewRoman"
        )
        # Set rotation
        text_fragment_2.text_state.rotation = 315
        # Create text fragment
        text_fragment_3 = ap.text.TextFragment("rotated text")
        # Set text properties
        text_fragment_3.text_state.font_size = 12
        text_fragment_3.text_state.font = ap.text.FontRepository.find_font(
            "TimesNewRoman"
        )
        # Set rotation
        text_fragment_3.text_state.rotation = 270
        page.paragraphs.add(text_fragment_1)
        page.paragraphs.add(text_fragment_2)
        page.paragraphs.add(text_fragment_3)

        # Save the document
        document.save(outfile)
```

## قم بتدوير فقرات كاملة في PDF

يوضح هذا المثال التدوير المتقدم للنص على مستوى الفقرة في PDF. على عكس التدوير على مستوى الجزء (حيث يتم تدوير كل قطعة نصية بشكل فردي)، تقوم هذه الطريقة بتدوير الفقرات بأكملها ككتل موحدة بزوايا مختلفة.
تحتوي كل فقرة على أجزاء نصية متعددة الأنماط، ويتم تدوير الفقرة الكاملة بزوايا محددة - مما يسمح بإجراء تحويلات تخطيطية معقدة ومتسقة.
يعد هذا مثاليًا للتخطيطات الفنية أو العلامات المائية أو ملفات PDF ذات التصميم الثقيل حيث يجب توجيه أقسام النص بأكملها في اتجاهات مختلفة.

يخلق `rotated_paragraphs.pdf`، تحتوي على أربع فقرات مصممة بشكل كامل ومستديرة:

- تدور كل منها بزاوية فريدة (45 درجة، 135 درجة، 225 درجة، 315 درجة)
- تحتوي كل فقرة على ثلاثة أسطر من النص بخلفيات ملونة وتسطير وتصميم متسق

1. قم بإنشاء مستند PDF جديد.
1. أضف صفحة فارغة للاحتفاظ بالفقرات المستديرة.
1. كرر لإنشاء فقرات متعددة.
1. قم بإنشاء الفقرة ووضعها.
1. قم بإنشاء أجزاء نصية بالتنسيق.
1. قم بتطبيق تنسيق النص.
1. أضف أجزاء نصية إلى الفقرة.
1. قم بإلحاق الفقرة بالصفحة باستخدام `TextBuilder`.
1. كرر ذلك لجميع الدورات الأربع.
1. احفظ مستند PDF.

```python
import aspose.pdf as ap

def rotate_text_inside_pdf_4(outfile):
    # Create PDF document
    with ap.Document() as document:
        # Get particular page
        page = document.pages.add()
        for i in range(4):
            paragraph = ap.text.TextParagraph()
            paragraph.position = ap.text.Position(200, 600)
            # Specify rotation
            paragraph.rotation = i * 90 + 45
            # Create text fragment
            text_fragment_1 = ap.text.TextFragment("Paragraph Text")
            # Create text fragment
            text_fragment_1.text_state.font_size = 12
            text_fragment_1.text_state.font = ap.text.FontRepository.find_font(
                "TimesNewRoman"
            )
            text_fragment_1.text_state.background_color = ap.Color.light_gray
            text_fragment_1.text_state.foreground_color = ap.Color.blue
            # Create text fragment
            text_fragment_2 = ap.text.TextFragment("Second line of text")
            # Set text properties
            text_fragment_2.text_state.font_size = 12
            text_fragment_2.text_state.font = ap.text.FontRepository.find_font(
                "TimesNewRoman"
            )
            text_fragment_2.text_state.background_color = ap.Color.light_gray
            text_fragment_2.text_state.foreground_color = ap.Color.blue
            # Create text fragment
            text_fragment_3 = ap.text.TextFragment("And some more text...")
            # Set text properties
            text_fragment_3.text_state.font_size = 12
            text_fragment_3.text_state.font = ap.text.FontRepository.find_font(
                "TimesNewRoman"
            )
            text_fragment_3.text_state.background_color = ap.Color.light_gray
            text_fragment_3.text_state.foreground_color = ap.Color.blue
            text_fragment_3.text_state.underline = True
            paragraph.append_line(text_fragment_1)
            paragraph.append_line(text_fragment_2)
            paragraph.append_line(text_fragment_3)
            # Create TextBuilder object
            builder = ap.text.TextBuilder(page)
            # Append the text fragment to the PDF page
            builder.append_paragraph(paragraph)

        # Save the document
        document.save(outfile)
```

## موضوعات نصية ذات صلة

- [العمل مع النص في PDF باستخدام Python](/pdf/ar/python-net/working-with-text/)
- [إضافة نص إلى PDF](/pdf/ar/python-net/add-text-to-pdf-file/)
- [تنسيق نص PDF في بايثون](/pdf/ar/python-net/text-formatting-inside-pdf/)
- [استبدل النص في PDF باستخدام Python](/pdf/ar/python-net/replace-text-in-pdf/)