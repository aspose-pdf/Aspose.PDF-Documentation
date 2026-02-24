---
title: تدوير النص داخل PDF باستخدام بايثون
linktitle: تدوير النص داخل PDF
type: docs
weight: 50
url: /ar/python-net/rotate-text-inside-pdf/
description: استكشف كيفية تدوير النص داخل مستند PDF باستخدام بايثون لتنسيق المستندات بمرونة مع Aspose.PDF للبايثون.
lastmod: "2025-11-13"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: كيفية تدوير النص في PDF باستخدام بايثون
Abstract: توفر المقالة دليلًا مفصلاً حول كيفية تدوير النص داخل مستند PDF باستخدام مكتبة Aspose.PDF للبايثون عبر .NET. تصف استخدام خاصية `Rotation` في فئة `TextFragment` لتحقيق تدوير النص بزاويا مختلفة، وهو مفيد في سيناريوهات إنشاء المستندات المتعددة. توضح إنشاء شظايا النص مع زوايا تدوير محددة وإضافتها إلى صفحة PDF باستخدام `TextBuilder'. توضح كيفية إلحاق شظايا النص المدورة إلى `TextParagraph` ثم إضافة الفقرة إلى صفحة PDF. تظهر كيفية إضافة شظايا النص المدورة مباشرة إلى مجموعة فقرات الصفحة. تشرح تدوير فقرة كاملة تحتوي على شظايا نص متعددة.
---

تدوير شظايا النص في مستند PDF باستخدام Aspose.PDF للبايثون عبر .NET. يوضح كيفية التحكم بدقة في موضع وتدوير عناصر النص الفردية من خلال الجمع بين فئات 'TextFragment' و 'TextState' و 'TextBuilder'. عن طريق تعديل زاوية التدوير لكل شظية نص، يمكنك إنشاء تخطيطات بصرية ديناميكية، مثل رؤوس مائلة، تسميات عمودية، أو تعليقات تدوير.

## تدوير شظايا النص باستخدام TextBuilder في PDF

إنشاء ملف PDF باسم rotated_fragments.pdf يحتوي على ثلاث شظايا نصية مصفوفة أفقياً:

- النص الأول غير مدور
- الثاني مدور بزاوية 45°
- الثالث مدور بزاوية 90°

1. إنشاء مستند PDF جديد.
1. إدراج صفحة جديدة لاستضافة النص المدور.
1. إنشاء شظية النص الأولى - بدون تدوير.
1. إنشاء شظية النص الثانية - تدوير 45°.
1. إنشاء شظية النص الثالثة - تدوير 90°.
1. إضافة شظايا النص باستخدام TextBuilder.
1. حفظ المستند.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def rotate_text_inside_pdf_1(outfile):
    """
    Implement text rotation using TextFragment and TextBuilder.

    Demonstrates basic text rotation techniques by creating multiple text
    fragments with different rotation angles. Shows how to position and
    rotate individual text elements using TextBuilder for precise control.

    Args:
        outfile (str): Path where the PDF with rotated text will be saved.

    Returns:
        None: The function creates and saves a PDF file with rotated text fragments.

    Note:
        - Creates three text fragments with 0°, 45°, and 90° rotations
        - Uses Position class for precise text placement
        - Applies TimesNewRoman font with 12pt size
        - TextBuilder provides low-level control over text placement
        - Demonstrates individual fragment rotation capabilities

    Example:
        >>> rotate_text_inside_pdf_1("rotated_fragments.pdf")
        # Creates a PDF with text fragments at different rotation angles
    """

    # Create PDF document
    with ap.Document() as document:
        # Get particular page
        page = document.pages.add()
        # Create text fragment
        text_fragment_1 = ap.text.TextFragment("main text")
        text_fragment_1.position = ap.text.Position(100, 600)
        # Set text properties
        text_fragment_1.text_state.font_size = 12
        text_fragment_1.text_state.font = ap.text.FontRepository.find_font("TimesNewRoman")
        # Create rotated text fragment
        text_fragment_2 = ap.text.TextFragment("rotated text")
        text_fragment_2.position = ap.text.Position(200, 600)
        # Set text properties
        text_fragment_2.text_state.font_size = 12
        text_fragment_2.text_state.font = ap.text.FontRepository.find_font("TimesNewRoman")
        text_fragment_2.text_state.rotation = 45
        # Create rotated text fragment
        text_fragment_3 = ap.text.TextFragment("rotated text")
        text_fragment_3.position = ap.text.Position(300, 600)
        # Set text properties
        text_fragment_3.text_state.font_size = 12
        text_fragment_3.text_state.font = ap.text.FontRepository.find_font("TimesNewRoman")
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

## تدوير شظايا النص الفردية داخل فقرة في PDF

تدوير شظايا النص الفردية داخل فقرة. يوضح كيفية بناء فقرة متعددة الأسطر (TextParagraph) تحتوي على عدة شظايا (TextFragment)، كل منها بزاوية تدوير خاصة به. هذه التقنية مفيدة لإنشاء مستندات بصرية غنية تجمع بين النص الأفقي والمائل — على سبيل المثال، رؤوس مزيّنة، مخططات، أو تسميات مع شروح.

إنشاء ملف PDF باسم rotated_paragraph_fragments.pdf يحتوي على فقرة بثلاث أسطر نصية، كل سطر مدور بزاوية مختلفة:

- السطر الأول مدور بزاوية 45°
- السطر الثاني يبقى أفقياً (0°)
- السطر الثالث مدور بزاوية -45°

1. إنشاء مستند PDF جديد.
1. إضافة صفحة فارغة حيث سيظهر النص المدور.
1. إنشاء TextParagraph.
1. إنشاء وتكوين شظية النص الأولى - تدوير 45°.
1. إنشاء شظية النص الثانية - بدون تدوير.
1. إنشاء شظية النص الثالثة - تدوير 45°.
1. إلحاق شظايا النص بالفقرة.
1. إضافة الفقرة إلى الصفحة باستخدام TextBuilder.
1. حفظ المستند.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def rotate_text_inside_pdf_2(outfile):
    """
    Implement text rotation using TextParagraph and TextBuilder with rotated fragments.

    Demonstrates how to create multi-line paragraphs containing individually
    rotated text fragments. Shows the combination of paragraph structure
    with fragment-level rotation control.

    Args:
        outfile (str): Path where the PDF with rotated paragraph fragments will be saved.

    Returns:
        None: The function creates and saves a PDF file with a paragraph containing rotated fragments.

    Note:
        - Creates a TextParagraph containing multiple text fragments
        - Individual fragments have different rotations: 45°, 0°, and -45°
        - Uses append_line to structure fragments within the paragraph
        - Demonstrates mixed rotation within a single paragraph
        - TextBuilder handles paragraph-level placement and rendering

    Example:
        >>> rotate_text_inside_pdf_2("rotated_paragraph_fragments.pdf")
        # Creates a PDF with a paragraph containing individually rotated text fragments
    """

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
        text_fragment_1.text_state.font = ap.text.FontRepository.find_font("TimesNewRoman")
        # Set rotation
        text_fragment_1.text_state.rotation = 45
        # Create text fragment
        text_fragment_2 = ap.text.TextFragment("main text")
        # Set text properties
        text_fragment_2.text_state.font_size = 12
        text_fragment_2.text_state.font = ap.text.FontRepository.find_font("TimesNewRoman")
        # Create text fragment
        text_fragment_3 = ap.text.TextFragment("another rotated text")
        # Set text properties
        text_fragment_3.text_state.font_size = 12
        text_fragment_3.text_state.font = ap.text.FontRepository.find_font("TimesNewRoman")
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

طريقة مبسطة لتدوير النص داخل PDF باستخدام Aspose.PDF للبايثون عبر .NET.
على عكس الأساليب ذات المستوى الأدنى باستخدام TextBuilder أو TextParagraph، تضيف هذه الطريقة شظايا النص المدورة مباشرة إلى مجموعة فقرات الصفحة (page.paragraphs). إنها مثالية للحالات التي تحتاج فيها إلى تدوير نص بسيط دون الحاجة إلى تحديد موقع دقيق أو هيكلة الفقرات. يبسط هذا النهج إنشاء التخطيط، مع معالجة تلقائية لموضع النص على الصفحة مع الاستمرار في السماح بالتحكم في تدوير النص الفردي.

ينشئ ملفًا باسم 'simple_rotated_text.pdf' يحتوي على:

- شظية نصية أفقية رئيسية بتدوير 0°
- شظية مدورة بزاوية 315°
- شظية مدورة بزاوية 270°

1. تهيئة مستند PDF جديد.
1. إنشاء صفحة حيث سيتم وضع النص المدور.
1. إنشاء أول قطعة نصية - بدون تدوير.
1. إنشاء القطعة النصية الثانية - تدوير 315°.
1. إنشاء القطعة النصية الثالثة - تدوير 270°.
1. إضافة قطع النص مباشرة إلى فقرات الصفحة.
1. حفظ مستند PDF.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def rotate_text_inside_pdf_3(outfile):
    """
    Implement text rotation using TextFragment and Page.Paragraphs.

    Demonstrates a simplified approach to text rotation by adding rotated
    text fragments directly to the page's paragraph collection. Shows
    high-level text placement without TextBuilder complexity.

    Args:
        outfile (str): Path where the PDF with rotated text will be saved.

    Returns:
        None: The function creates and saves a PDF file with rotated text using page paragraphs.

    Note:
        - Uses Page.Paragraphs for direct text fragment addition
        - Creates fragments with 0°, 315°, and 270° rotations
        - Simpler approach compared to TextBuilder method
        - Demonstrates automatic layout with rotated text elements
        - Good for basic rotation without precise positioning needs

    Example:
        >>> rotate_text_inside_pdf_3("simple_rotated_text.pdf")
        # Creates a PDF with rotated text using the simplified page paragraphs approach
    """

    # Create PDF document
    with ap.Document() as document:
        # Get particular page
        page = document.pages.add()
        # Create text fragment
        text_fragment_1 = ap.text.TextFragment("main text")
        # Set text properties
        text_fragment_1.text_state.font_size = 12
        text_fragment_1.text_state.font = ap.text.FontRepository.find_font("TimesNewRoman")
        # Create text fragment
        text_fragment_2 = ap.text.TextFragment("rotated text")
        # Set text properties
        text_fragment_2.text_state.font_size = 12
        text_fragment_2.text_state.font = ap.text.FontRepository.find_font("TimesNewRoman")
        # Set rotation
        text_fragment_2.text_state.rotation = 315
        # Create text fragment
        text_fragment_3 = ap.text.TextFragment("rotated text")
        # Set text properties
        text_fragment_3.text_state.font_size = 12
        text_fragment_3.text_state.font = ap.text.FontRepository.find_font("TimesNewRoman")
        # Set rotation
        text_fragment_3.text_state.rotation = 270
        page.paragraphs.add(text_fragment_1)
        page.paragraphs.add(text_fragment_2)
        page.paragraphs.add(text_fragment_3)

        # Save the document
        document.save(outfile)
```

## تدوير الفقرات بالكامل في PDF

تُظهر مكتبتنا تدوير النص على مستوى الفقرة المتقدم في PDF. على عكس تدوير المستوى الجزئي (حيث يتم تدوير كل قطعة نصية بشكل فردي)، هذه الطريقة تقوم بتدوير الفقرات بالكامل ككتل موحدة بزوايا مختلفة.
كل فقرة تحتوي على عدة قطع نصية منسقة، ويتم تدوير الفقرة كاملة بزاويات محددة — مما يتيح تحويلات تخطيطية معقدة ومتسقة.
هذا مثال مثالي للتصاميم الفنية، العلامات المائية، أو ملفات PDF ذات التصميم المكثف حيث تحتاج أقسام النص بالكامل إلى توجيه في اتجاهات مختلفة.

ينشئ 'rotated_paragraphs.pdf'، يحتوي على أربع فقرات منسقة ومدوّرة بالكامل:

- كل واحدة مدوّرة بزاوية فريدة (45°, 135°, 225°, و315°)
- كل فقرة تحتوي على ثلاثة أسطر نصية بخلفيات ملونة، وتسطير، وتنسيق متسق

1. إنشاء مستند PDF جديد.
1. إضافة صفحة فارغة لاحتواء الفقرات المدوّرة.
1. التكرار لإنشاء فقرات متعددة.
1. إنشاء الفقرة وتحديد موقعها.
1. إنشاء قطع النص مع التنسيق.
1. تطبيق تنسيق النص.
1. إضافة قطع النص إلى الفقرة.
1. إلحاق الفقرة بالصفحة باستخدام TextBuilder.
1. تكرار العملية لجميع الأربع تدويرات.
1. حفظ مستند PDF.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def rotate_text_inside_pdf_4(outfile):
    """
    Implement whole paragraph rotation using TextParagraph and TextBuilder.

    Demonstrates advanced text rotation by rotating entire paragraphs at
    different angles. Creates multiple styled paragraphs with comprehensive
    formatting and rotates each paragraph as a complete unit.

    Args:
        outfile (str): Path where the PDF with rotated paragraphs will be saved.

    Returns:
        None: The function creates and saves a PDF file with fully rotated paragraphs.

    Note:
        - Creates 4 paragraphs rotated at 45°, 135°, 225°, and 315°
        - Each paragraph contains multiple formatted text fragments
        - Applies comprehensive styling: colors, backgrounds, underlines
        - Demonstrates paragraph-level rotation vs. fragment-level rotation
        - Shows complex multi-line content with consistent rotation
        - Uses loop to create systematic rotation pattern

    Example:
        >>> rotate_text_inside_pdf_4("rotated_paragraphs.pdf")
        # Creates a PDF with complete paragraphs rotated at different angles
    """

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
            text_fragment_1.text_state.font = ap.text.FontRepository.find_font("TimesNewRoman")
            text_fragment_1.text_state.background_color = ap.Color.light_gray
            text_fragment_1.text_state.foreground_color = ap.Color.blue
            # Create text fragment
            text_fragment_2 = ap.text.TextFragment("Second line of text")
            # Set text properties
            text_fragment_2.text_state.font_size = 12
            text_fragment_2.text_state.font = ap.text.FontRepository.find_font("TimesNewRoman")
            text_fragment_2.text_state.background_color = ap.Color.light_gray
            text_fragment_2.text_state.foreground_color = ap.Color.blue
            # Create text fragment
            text_fragment_3 = ap.text.TextFragment("And some more text...")
            # Set text properties
            text_fragment_3.text_state.font_size = 12
            text_fragment_3.text_state.font = ap.text.FontRepository.find_font("TimesNewRoman")
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
