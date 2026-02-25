---
title: تنسيق النص داخل ملف PDF باستخدام بايثون
linktitle: تنسيق النص داخل PDF
type: docs
weight: 70
url: /ar/python-net/text-formatting-inside-pdf/
description: استكشف خيارات تنسيق النص داخل ملفات PDF في بايثون باستخدام Aspose.PDF لتخصيص نمط المستند.
lastmod: "2025-11-13"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: كيفية تحرير النص في ملف PDF باستخدام بايثون
Abstract: يقدم المقال دليلاً شاملاً حول مختلف تقنيات تنسيق النص في مستندات PDF باستخدام Aspose.PDF لبايثون عبر .NET. يغطي مجموعة من الوظائف بما في ذلك إضافة مسافات سطرية، إنشاء حدود للنص، وضع خط تحت النص، وإضافة نص مشطوب، وغيرها.
---

## المسافة بين السطور والأحرف

### استخدام مسافات السطر

#### كيفية تنسيق النص مع مسافات سطر مخصصة في بايثون - الحالة البسيطة

Aspose.PDF لبايثون يوضح نهجًا بسيطًا للتحكم في تخطيط النص وقابليته للقراءة من خلال تعديل مسافات السطر.

يُظهر مقتطف الكود الخاص بنا كيفية التحكم في مسافات السطر في مستند PDF. يقرأ النص من ملف (أو يستخدم رسالة احتياطية)، يطبق حجم خط مخصص ومسافة سطر، ويضيف النص المنسق إلى صفحة جديدة في PDF.

1. إنشاء مستند PDF جديد.
1. تحميل النص المصدر.
1. تهيئة كائن TextFragment وتعيين النص المحمَّل إليه.
1. ضبط خصائص الخط والمسافات للنص. تحدد هذه القيم مدى تقارب أو تباعد أسطر النص:
- حجم الخط: 12 نقطة
- مسافة السطر: 16 نقطة
1. إدراج جزء النص المنسق في مجموعة الفقرات للصفحة.
1. حفظ المستند.

```python

import aspose.pdf as ap
from aspose.pdf import Color
from aspose.pdf.drawing import Graph, Line
import os

# Global configuration
DATA_DIR = "your path here"

def specify_line_spacing_simple_case(outfile):
    """
    Specify custom line spacing for text in a PDF document.

    Creates a PDF document with text that has custom line spacing applied.
    Loads text content from an external file and applies 16-point line spacing
    to improve readability and text layout.

    Args:
        outfile (str): The file path where the generated PDF document will be saved.

    Returns:
        None: The function saves the document to the specified output file.

    Note:
        - Attempts to load text from "lorem.txt" file in DATA_DIR
        - Falls back to default message if file doesn't exist
        - Font size: 12 points
        - Line spacing: 16 points (increased from default for better readability)
        - Demonstrates basic line spacing control in PDF text formatting

    Example:
        >>> specify_line_spacing_simple_case("line_spacing.pdf")
        # Creates a PDF with custom 16-point line spacing
    """

    document = ap.Document()
    page = document.pages.add()

    lorem_path = os.path.join(DATA_DIR, "lorem.txt")
    text = (
        open(lorem_path, "r", encoding="utf-8").read()
        if os.path.exists(lorem_path)
        else "Lorem ipsum text not found."
    )

    text_fragment = ap.text.TextFragment(text)
    text_fragment.text_state.font_size = 12
    text_fragment.text_state.line_spacing = 16
    page.paragraphs.add(text_fragment)

    document.save(outfile)
```

#### كيفية تنسيق النص مع مسافات سطر مخصصة في بايثون - الحالة المحددة

دعونا نتحقق من كيفية تطبيق أوضاع مسافات سطر مختلفة في مستند PDF باستخدام خط TrueType مخصص (TTF).
يقوم بتحميل النص من ملف، يدمج خطًا معينًا، ويعرض نفس النص مرتين على صفحة PDF — كل مرة باستخدام وضع مسافة سطر مختلف:

- وضع FONT_SIZE: مسافة السطر تساوي حجم الخط.
- وضع FULL_SIZE: مسافة السطر تأخذ في الاعتبار الارتفاع الكامل للخط، بما في ذلك القواعد والأنصاف.

يظهر المثال كيف يمكن أن تختلف سلوك مسافة السطر اعتمادًا على الوضع المختار.

1. إنشاء مستند PDF جديد.
1. تحديد المسارات لكل من ملف الخط المخصص وملف مصدر النص.
1. تحميل محتوى النص.
1. فتح الخط المخصص.
1. إنشاء وتكوين أول TextFragment (وضع FONT_SIZE). ضبط line_spacing إلى 'TextFormattingOptions.LineSpacingMode.FONT_SIZE'، مما يعني أن مسافة السطر تساوي حجم الخط.
1. إنشاء وتكوين ثاني TextFragment (وضع FULL_SIZE). ضبط line_spacing إلى 'TextFormattingOptions.LineSpacingMode.FULL_SIZE'، الذي يستخدم الارتفاع الكامل للخط.
1. إلحاق كلا جزءَي النص إلى نفس صفحة PDF.
1. حفظ المستند النهائي إلى موقع الإخراج المحدد.

```python

import aspose.pdf as ap
from aspose.pdf import Color
from aspose.pdf.drawing import Graph, Line
import os

# Global configuration
DATA_DIR = "your path here"

def specify_line_spacing_specific_case(outfile):
    """
    Create a PDF document demonstrating different line spacing modes with custom font.
    This function creates a PDF with two text fragments using the same custom TTF font
    but different line spacing modes to demonstrate the visual differences between
    FONT_SIZE and FULL_SIZE line spacing options.
    Args:
        outfile (str): Path where the output PDF file will be saved.
    Notes:
        - Requires 'HPSimplified.ttf' font file in DATA_DIR
        - Requires 'lorem.txt' text file in DATA_DIR for content
        - Falls back to default text if lorem.txt is not found
        - First fragment uses FONT_SIZE line spacing mode
        - Second fragment uses FULL_SIZE line spacing mode
    Dependencies:
        - aspose.pdf (ap) library
        - os module for file path operations
        - DATA_DIR constant must be defined
    """

    document = ap.Document()
    page = document.pages.add()

    font_file = os.path.join(DATA_DIR, "HPSimplified.ttf")
    lorem_path = os.path.join(DATA_DIR, "lorem.txt")
    text = (
        open(lorem_path, "r", encoding="utf-8").read()
        if os.path.exists(lorem_path)
        else "Lorem ipsum text not found."
    )

    with open(font_file, "rb") as font_stream:
        font = ap.text.FontRepository.open_font(font_stream, ap.text.FontTypes.TTF)

        fragment1 = ap.text.TextFragment(text)
        fragment1.text_state.font = font
        fragment1.text_state.formatting_options = ap.text.TextFormattingOptions()
        fragment1.text_state.formatting_options.line_spacing = (
            ap.text.TextFormattingOptions.LineSpacingMode.FONT_SIZE
        )
        page.paragraphs.add(fragment1)

        fragment2 = ap.text.TextFragment(text)
        fragment2.text_state.font = font
        fragment2.text_state.formatting_options = ap.text.TextFormattingOptions()
        fragment2.text_state.formatting_options.line_spacing = (
            ap.text.TextFormattingOptions.LineSpacingMode.FULL_SIZE
        )
        page.paragraphs.add(fragment2)

    document.save(outfile)
```

![مستند PDF يعرض نصًا مع مسافة سطر مخصصة توضح تباعد 16 نقطة بين الأسطر لتحسين قابلية القراءة وتنسيق تخطيط النص](line_spacing.png)

### استخدام مسافة الأحرف

#### كيفية التحكم في مسافة الأحرف في نص PDF باستخدام فئة TextFragment

تحدد مسافة الأحرف المسافة بين الأحرف الفردية في سطر النص — مفيدة لضبط مظهر النص بدقة أو لتحقيق تأثيرات طباعية محددة.

1. تهيئة كائن Document جديد وإضافة صفحة فارغة لوضع النص.
1. تعريف مُولد القطع. ينفذ دالة مساعدة make_fragment(spacing):
- إنشاء TextFragment بالنص التجريبي.
- ضبط الخط.
1. إضافة أجزاء نصية بمقاييس مسافة مختلفة.
1. حفظ المستند.

```python

import aspose.pdf as ap
from aspose.pdf import Color
from aspose.pdf.drawing import Graph, Line
import os

# Global configuration
DATA_DIR = "your path here"

def character_spacing_using_text_fragment(outfile):
    """
    Demonstrate character spacing control using TextFragment objects.

    Creates a PDF document showing different character spacing values applied
    to text fragments. Each line demonstrates progressively increased character
    spacing to illustrate the visual effect on text appearance.

    Args:
        outfile (str): The file path where the generated PDF document will be saved.

    Returns:
        None: The function saves the document to the specified output file.

    Note:
        - Creates multiple TextFragment objects with varying character spacing
        - Character spacing values: 0, 1, 2, 3, and 4 points
        - Font: Times Roman, 12 points
        - Each fragment is positioned on a new line for comparison
        - Character spacing affects only horizontal letter spacing
        - Higher values create more space between individual characters

    Example:
        >>> character_spacing_using_text_fragment("char_spacing_fragment.pdf")
        # Creates a PDF showing progressive character spacing effects
    """
    document = ap.Document()
    page = document.pages.add()

    def make_fragment(spacing):
        fragment = ap.text.TextFragment("Sample Text with character spacing")
        fragment.text_state.font = ap.text.FontRepository.find_font("Arial")
        fragment.text_state.font_size = 14
        fragment.text_state.character_spacing = spacing
        return fragment

    page.paragraphs.add(make_fragment(2.0))
    page.paragraphs.add(make_fragment(1.0))
    page.paragraphs.add(make_fragment(0.75))

    document.save(outfile)
```

![مستند PDF يعرض ثلاث أسطر من النص المتطابق Sample Text مع تباعد الأحرف يوضح تباعد الأحرف المتزايد تدريجياً من الأعلى إلى الأسفل، حيث السطر الأول به مسافات أوسع بين الحروف، والسطر الأوسط به مسافات معتدلة، والسطر الأسفل به أقرب تباعد بين الأحرف، مما يوضح التأثير البصري لقيم تباعد الأحرف المختلفة في تنسيق نص PDF](character_spacing_simple.png)

#### كيفية التحكم في تباعد الأحرف في نص PDF باستخدام TextParagraph و TextBuilder

تتيح Aspose.PDF تطبيق تباعد أحرف مخصص عند إضافة نص إلى مستند PDF باستخدام TextParagraph و TextBuilder.
يحدد منطقة معينة على الصفحة، يضبط لف النص، ويعرض مقطع نصي مع تعديل التباعد بين الأحرف.

استخدام TextParagraph مثالي عندما تحتاج إلى تحكم دقيق في موضع النص وتخطيطه، مثل عند إنشاء كتل نصية منظمة أو متعددة الأعمدة.

1. إنشاء مستند PDF جديد.
1. تهيئة كائن TextBuilder للصفحة.
1. إنشاء وتكوين TextParagraph.
- ضبط وضع التفاف الكلمات إلى 'TextFormattingOptions.WordWrapMode.BY_WORDS'.
1. إنشاء TextFragment مع تباعد أحرف مخصص.
- إنشاء TextFragment جديد وتعيين نصه (مثال: "Sample Text with character spacing").
- تحديد خصائص الخط مثل Arial وحجم الخط 14 نقطة.
- تطبيق تباعد الأحرف = 2.0، الذي يزيد المسافة بين الأحرف.
1. إضافة TextFragment إلى TextParagraph.
1. إضافة TextParagraph إلى الصفحة.
1. حفظ مستند PDF.

```python

import aspose.pdf as ap
from aspose.pdf import Color
from aspose.pdf.drawing import Graph, Line
import os

# Global configuration
DATA_DIR = "your path here"

def character_spacing_using_text_paragraph(outfile):
    """
    Demonstrate character spacing control using TextParagraph objects.

    Creates a PDF document with text paragraph that has custom character spacing
    applied. Shows how to set character spacing at the paragraph level and
    demonstrates the visual effect on text layout.

    Args:
        outfile (str): The file path where the generated PDF document will be saved.

    Returns:
        None: The function saves the document to the specified output file.

    Note:
        - Uses TextParagraph for paragraph-level formatting
        - Character spacing: 2.0 points
        - Font: Times Roman, 12 points
        - Demonstrates paragraph-based character spacing control
        - Character spacing applies to all text within the paragraph
        - Alternative approach to fragment-based character spacing

    Example:
        >>> character_spacing_using_text_paragraph("char_spacing_paragraph.pdf")
        # Creates a PDF with paragraph-level character spacing
    """
    document = ap.Document()
    page = document.pages.add()

    builder = ap.text.TextBuilder(page)
    paragraph = ap.text.TextParagraph()
    paragraph.rectangle = ap.Rectangle(100, 700, 500, 750, True)
    paragraph.formatting_options.wrap_mode = (
        ap.text.TextFormattingOptions.WordWrapMode.BY_WORDS
    )

    fragment = ap.text.TextFragment("Sample Text with character spacing")
    fragment.text_state.font = ap.text.FontRepository.find_font("Arial")
    fragment.text_state.font_size = 14
    fragment.text_state.character_spacing = 2.0

    paragraph.append_line(fragment)
    builder.append_paragraph(paragraph)
    document.save(outfile)
```

## إنشاء القوائم

عند العمل مع ملفات PDF، قد تحتاج إلى عرض معلومات منظمة مثل القوائم — سواء كانت نقطية أو مرقمة أو مُنسقة باستخدام HTML أو LaTeX.
توفر Aspose.PDF for Python عبر .NET عدة طرق مرنة لإنشاء وتنسيق القوائم مباشرة داخل مستندات PDF الخاصة بك، مما يمنحك تحكمًا كاملاً في التخطيط، الخط، والأسلوب.

توضح هذه المقالة طرقًا متعددة لإنشاء القوائم في ملفات PDF، من تنسيق النص العادي إلى عرض HTML و LaTeX المتقدم. كل طريقة تخدم حالة استخدام معينة — سواء كنت تفضل التحكم البرمجي الدقيق أو تنسيق سهل يعتمد على العلامات.

بنهاية هذه المقالة، ستعرف كيفية:

- إنشاء قوائم نقطية ومرقمة مخصصة باستخدام TextParagraph و TextBuilder.

- استخدام مقاطع HTML (HtmlFragment) لتصميم قوائم '<ul>' و '<ol>' بسهولة في ملفات PDF.

- الاستفادة من مقاطع LaTeX (TeXFragment) لتنسيق القوائم الرياضية أو العلمية.

- التحكم في لف النص، أنماط الخط، وتحديد موقع التخطيط داخل الصفحة.

- فهم الفرق بين إنشاء القوائم يدويًا والنهج القائم على العلامات.

### إنشاء قائمة نقطية

إنشاء قائمة نقطية مخصصة في ملف PDF باستخدام TextParagraph و TextBuilder، دون الاعتماد على تنسيق HTML أو LaTeX.
كل عنصر في القائمة يسبق بحرف نقطي (•) ويُضاف كمقطع نصي منفصل.

1. تهيئة كائن Document وإضافة صفحة فارغة.
1. تعريف قائمة Python من السلاسل التي سيتم تحويلها إلى نقاط نقطية.
1. إنشاء TextBuilder و TextParagraph.
1. استخدام 'TextBuilder' لإضافة الفقرة المُكوَّنة إلى الصفحة.
1. حفظ مستند PDF.

```python

import aspose.pdf as ap
from aspose.pdf import Color
from aspose.pdf.drawing import Graph, Line
import os

# Global configuration
DATA_DIR = "your path here"

def create_bullet_list(outfile):
    """
    Create a PDF document with a bullet list using plain text formatting.
    This function generates a PDF document containing a bullet list with predefined items.
    The list is formatted with bullet points, uses Times New Roman font, and includes
    text wrapping behavior for longer items.
    Args:
        outfile (str): The file path where the PDF document will be saved.
    Returns:
        None: The function saves the document to the specified file path.
    Note:
        The bullet list is positioned within a rectangle at coordinates (80, 200, 400, 800)
        and uses word wrapping mode for text formatting.
    """

    document = ap.Document()
    page = document.pages.add()
    items = [
        "First item in the list",
        "Second item with more text to demonstrate wrapping behavior.",
        "Third item",
        "Fourth item",
    ]

    builder = ap.text.TextBuilder(page)
    paragraph = ap.text.TextParagraph()
    paragraph.rectangle = ap.Rectangle(80, 200, 400, 800, True)
    paragraph.formatting_options.wrap_mode = (
        ap.text.TextFormattingOptions.WordWrapMode.BY_WORDS
    )

    for item in items:
        fragment = ap.text.TextFragment("• " + item)
        fragment.text_state.font = ap.text.FontRepository.find_font("Times New Roman")
        fragment.text_state.font_size = 12
        paragraph.append_line(fragment)

    builder.append_paragraph(paragraph)
    document.save(outfile)
```

### إنشاء قائمة مرقمة

إنشاء قائمة مرقمة مخصصة (مرتبة) في ملف PDF باستخدام TextParagraph و TextBuilder، دون الاعتماد على تنسيق HTML أو LaTeX.
كل عنصر في القائمة يسبق برقمه (مثال: 1., 2.) ويُضاف كمقطع نصي منفصل.

1. تهيئة كائن Document وإضافة صفحة فارغة.
1. تعريف قائمة Python من السلاسل التي سيتم تحويلها إلى عناصر قائمة مرقمة.
1. إنشاء TextBuilder و TextParagraph.
1. إضافة كل عنصر كمقطع نصي (TextFragment) مع رقمه.
1. استخدام TextBuilder لإضافة الفقرة المُكوَّنة إلى الصفحة.
1. حفظ مستند PDF.

```python

import aspose.pdf as ap
from aspose.pdf import Color
from aspose.pdf.drawing import Graph, Line
import os

# Global configuration
DATA_DIR = "your path here"

def create_numbered_list(outfile):
    """
    Create a numbered list in a PDF document using plain text formatting.
    This function generates a PDF document containing a numbered list with predefined
    items. The list is formatted with Times New Roman font and includes text wrapping
    by words within a specified rectangular area on the page.
    Args:
        outfile (str): The file path where the generated PDF document will be saved.
    Returns:
        None: The function saves the document to the specified file path but does
              not return any value.
    Note:
        - Uses Aspose.PDF library (imported as 'ap')
        - List items are hardcoded within the function
        - Font: Times New Roman, size 12
        - Text wrapping: BY_WORDS mode
        - Rectangle bounds: (80, 200, 400, 800)
    """

    document = ap.Document()
    page = document.pages.add()
    items = [
        "First item in the list",
        "Second item with more text to demonstrate wrapping behavior.",
        "Third item",
        "Fourth item",
    ]

    builder = ap.text.TextBuilder(page)
    paragraph = ap.text.TextParagraph()
    paragraph.rectangle = ap.Rectangle(80, 200, 400, 800, True)
    paragraph.formatting_options.wrap_mode = (
        ap.text.TextFormattingOptions.WordWrapMode.BY_WORDS
    )

    for i, item in enumerate(items):
        fragment = ap.text.TextFragment(f"{i + 1}. {item}")
        fragment.text_state.font = ap.text.FontRepository.find_font("Times New Roman")
        fragment.text_state.font_size = 12
        paragraph.append_line(fragment)

    builder.append_paragraph(paragraph)
    document.save(outfile)
```

### إنشاء نسخة HTML من قائمة نقطية

تظهر مكتبتنا كيفية إنشاء قائمة نقطية (غير مرتبة) في مستند PDF باستخدام مقاطع HTML. فهي تحول قائمة Python من السلاسل إلى عنصر HTML `<ul>` وتدرجه في صفحة PDF كـ HtmlFragment. يسمح استخدام مقاطع HTML بالاستفادة من ميزات تنسيق HTML (مثل القوائم، العريض، المائل) مباشرةً في PDF.

1. إنشاء مستند PDF جديد وإضافة صفحة.
1. إعداد عناصر القائمة.
1. تحويل القائمة إلى قائمة HTML غير مرتبة.
- استخدام وسم `<ul>` لقائمة غير مرتبة (نقطية).
- تغليف كل عنصر بوسوم 'li' باستخدام تعبير القائمة.
1. إنشاء HtmlFragment. تحويل سلسلة HTML إلى كائن HtmlFragment يمكن إضافته إلى صفحة PDF.
1. إدراج HtmlFragment في مجموعة فقرات الصفحة.
1. حفظ مستند PDF.

```python

import aspose.pdf as ap
from aspose.pdf import Color
from aspose.pdf.drawing import Graph, Line
import os

# Global configuration
DATA_DIR = "your path here"

def create_bullet_list_html_version(outfile):
    """
    Create a bulleted list using HTML formatting in a PDF document.

    Generates a PDF with an unordered (bulleted) list created using HTML markup.
    Demonstrates how to use HtmlFragment to embed HTML list structures directly
    into PDF documents with proper formatting and styling.

    Args:
        outfile (str): The file path where the generated PDF document will be saved.

    Returns:
        None: The function saves the document to the specified output file.

    Note:
        - Uses HTML <ul> and <li> tags for list structure
        - Items are predefined with sample content
        - HtmlFragment automatically handles HTML rendering
        - Lists maintain proper bullet formatting and indentation
        - Simpler alternative to manual list creation with TextFragments
        - Supports nested lists and HTML styling if needed

    Example:
        >>> create_bullet_list_html_version("bullet_list_html.pdf")
        # Creates a PDF with HTML-formatted bulleted list
    """

    document = ap.Document()
    page = document.pages.add()
    items = [
        "First item in the list",
        "Second item with more text to demonstrate wrapping behavior.",
        "Third item",
        "Fourth item",
    ]
    html_list = "<ul>" + "".join([f"<li>{item}</li>" for item in items]) + "</ul>"
    html_fragment = ap.HtmlFragment(html_list)
    page.paragraphs.add(html_fragment)
    document.save(outfile)
```

![قائمة نقطية معروضة في مستند PDF تُظهر أربعة عناصر: العنصر الأول في القائمة، العنصر الثاني بنص إضافي لتوضيح سلوك الالتفاف، العنصر الثالث، والعنصر الرابع. كل عنصر يسبقه نقط قياسية ويظهر عرض قائمة بتنسيق HTML داخل بنية PDF مع مسافة وتباعد مناسبين](bullet_list_html.png)

### إنشاء قائمة مرقمة بإصدار HTML

إنشاء قائمة مرقمة (مرتبة) في مستند PDF باستخدام مقاطع HTML. يحول قائمة Python من السلاسل النصية إلى عنصر HTML `<ol>` ويُدرجها في صفحة PDF كـ HtmlFragment.

استخدام مقاطع HTML يتيح لك دمج ميزات التنسيق القائمة على HTML، مثل القوائم المرقمة، الغضّ، المائل، والمزيد، مباشرةً في ملف PDF الخاص بك.

1. إنشاء مستند PDF جديد وإضافة صفحة.
1. تحضير عناصر القائمة.
1. تحويل القائمة إلى قائمة HTML مرتبة.
- استخدم الوسم `<ol>` لإنشاء قائمة مرقمة.
- غلف كل عنصر بوسوم 'li' باستخدام تعبير تفصيلي (list comprehension).
1. تحويل سلسلة HTML إلى كائن HtmlFragment يمكن إضافته إلى صفحة PDF.
1. إدراج HtmlFragment في مجموعة فقرات الصفحة.
1. حفظ مستند PDF.

```python

import aspose.pdf as ap
from aspose.pdf import Color
from aspose.pdf.drawing import Graph, Line
import os

# Global configuration
DATA_DIR = "your path here"

def create_numbered_list_html_version(outfile):
    """
    Create a numbered list using HTML formatting in a PDF document.

    Generates a PDF with an ordered (numbered) list created using HTML markup.
    Demonstrates how to use HtmlFragment to embed HTML ordered list structures
    directly into PDF documents with automatic numbering and formatting.

    Args:
        outfile (str): The file path where the generated PDF document will be saved.

    Returns:
        None: The function saves the document to the specified output file.

    Note:
        - Uses HTML <ol> and <li> tags for ordered list structure
        - Items are predefined with sample content
        - HtmlFragment automatically handles HTML rendering and numbering
        - Lists maintain proper numeric formatting and indentation
        - Numbers are automatically generated (1, 2, 3, etc.)
        - Supports nested lists and custom numbering styles if needed

    Example:
        >>> create_numbered_list_html_version("numbered_list_html.pdf")
        # Creates a PDF with HTML-formatted numbered list
    """

    document = ap.Document()
    page = document.pages.add()
    items = [
        "First item in the list",
        "Second item with more text to demonstrate wrapping behavior.",
        "Third item",
        "Fourth item",
    ]
    html_list = "<ol>" + "".join([f"<li>{item}</li>" for item in items]) + "</ol>"
    html_fragment = ap.HtmlFragment(html_list)
    page.paragraphs.add(html_fragment)
    document.save(outfile)
```

![قائمة مرقمة معروضة في مستند PDF تُظهر أربعة عناصر مرقمة تلقائيًا: 1. العنصر الأول في القائمة، 2. العنصر الثاني بنص إضافي لتوضيح سلوك الالتفاف، 3. العنصر الثالث، و4. العنصر الرابع. توضح القائمة عرض قائمة مرتبة بتنسيق HTML داخل بنية PDF مع تسلسل رقمي صحيح، وتوسيط، وتباعد بين العناصر](numbered_list_html.png)

### إنشاء قائمة نقطية بإصدار LaTeX

إنشاء قائمة نقطية (غير مرتبة) في ملف PDF باستخدام مقاطع LaTeX (TeXFragment). يحول قائمة Python من السلاسل النصية إلى بيئة LaTeX itemize ويُدرجها في صفحة PDF. استخدام مقاطع LaTeX مثالي عندما ترغب في عرض صيغ رياضية، رموز، أو قوائم منظمة بتنسيق دقيق.

1. إنشاء مستند PDF جديد وإضافة صفحة.
1. تعريف قائمة Python من السلاسل النصية التي ستصبح نقاطًا نقطية في بيئة LaTeX itemize.
1. تحويل القائمة إلى بيئة LaTeX itemize:
- غلف العناصر بـ \begin{itemize} و \end{itemize}.
- يسبق كل عنصر بـ \item باستخدام تعبير تفصيلي (list comprehension).
1. تحويل سلسلة LaTeX إلى كائن TeXFragment يمكن عرضه في PDF.
1. إضافة مقطع LaTeX إلى الصفحة.
1. حفظ مستند PDF.

```python

import aspose.pdf as ap
from aspose.pdf import Color
from aspose.pdf.drawing import Graph, Line
import os

# Global configuration
DATA_DIR = "your path here"

def create_bullet_list_latex_version(outfile):
    """
    Create a bulleted list using LaTeX formatting in a PDF document.

    Generates a PDF with an unordered list created using LaTeX markup.
    Demonstrates how to use TeXFragment to embed LaTeX itemize environments
    directly into PDF documents with proper mathematical and scientific formatting.

    Args:
        outfile (str): The file path where the generated PDF document will be saved.

    Returns:
        None: The function saves the document to the specified output file.

    Note:
        - Uses LaTeX \\begin{itemize} and \\item commands
        - TeXFragment handles LaTeX compilation and rendering
        - Supports mathematical expressions and scientific notation
        - Lists maintain proper bullet formatting and indentation
        - More powerful than HTML for mathematical content
        - Can include LaTeX math modes and special symbols

    Example:
        >>> create_bullet_list_latex_version("bullet_list_latex.pdf")
        # Creates a PDF with LaTeX-formatted bulleted list
    """

    document = ap.Document()
    page = document.pages.add()
    items = [
        "First item",
        "Second item with more text to demonstrate wrapping behavior.",
        "Third item",
        "Fourth item",
    ]
    tex_list = (
        "Lists are easy to create: \\begin{itemize}"
        + "".join([f"\\item {i}" for i in items])
        + "\\end{itemize}"
    )
    tex_fragment = ap.TeXFragment(tex_list)
    page.paragraphs.add(tex_fragment)
    document.save(outfile)
```

![قائمة نقطية معروضة في PDF تُظهر تنسيقًا تم إنشاؤه باستخدام LaTeX مع النص القائم على القوائم: القوائم سهلة الإنشاء: يتبعها أربعة عناصر نقطية: العنصر الأول، العنصر الثاني بنص إضافي لتوضيح سلوك الالتفاف، العنصر الثالث، والعنصر الرابع. توضح القائمة طباعة LaTeX احترافية مع تنسيق نقط مناسب، مسافات متسقة، وقدرات لف النص داخل تنسيق PDF نظيف](bullet_list_latex.png)

### إنشاء قائمة مرقمة بإصدار LaTeX

إنشاء قائمة مرقمة (مرتبة) في ملف PDF باستخدام مقاطع LaTeX (TeXFragment). يحول قائمة Python من السلاسل النصية إلى بيئة LaTeX enumerate ويُدرجها في صفحة PDF. استخدام مقاطع LaTeX مثالي عندما تريد تنسيقًا دقيقًا، قوائم منظمة، أو تدوين رياضي في ملفات PDF.

1. إنشاء مستند PDF جديد وإضافة صفحة.
1. تعريف قائمة Python من السلاسل النصية التي ستصبح عناصر مُرقمة في بيئة LaTeX enumerate.
1. تحويل القائمة إلى بيئة LaTeX enumerate.
1. تحويل سلسلة LaTeX إلى كائن TeXFragment يمكن عرضه في PDF.
1. إضافة مقطع LaTeX إلى الصفحة.
1. حفظ مستند PDF.

```python

import aspose.pdf as ap
from aspose.pdf import Color
from aspose.pdf.drawing import Graph, Line
import os

# Global configuration
DATA_DIR = "your path here"

def create_numbered_list_latex_version(outfile):
    """Create a numbered list using LaTeX."""

    document = ap.Document()
    page = document.pages.add()
    items = [
        "First item",
        "Second item with more text to demonstrate wrapping behavior.",
        "Third item",
        "Fourth item",
    ]
    tex_list = (
        "Lists are easy to create: \\begin{enumerate}"
        + "".join([f"\\item {i}" for i in items])
        + "\\end{enumerate}"
    )
    tex_fragment = ap.TeXFragment(tex_list)
    page.paragraphs.add(tex_fragment)
    document.save(outfile)
```

![قائمة مرقمة معروضة في PDF تُظهر تنسيقًا تم إنشاؤه باستخدام LaTeX مع العناصر 1. العنصر الأول، 2. العنصر الثاني بنص إضافي لتوضيح سلوك الالتفاف، 3. العنصر الثالث، و4. العنصر الرابع، مسبوقة بالنص القائم على القوائم سهلة الإنشاء](numbered_list_latex.png)

## الهوامش والحواشي

### إضافة هوامش

تُستخدم الهوامش للإشارة إلى ملاحظات داخل نص الوثيقة عن طريق وضع أرقام مرتفعة متتابعة بجوار النص المتعلق. تتطابق هذه الأرقام مع ملاحظات مفصلة تكون عادةً مُهَذَّبة وموجودة في أسفل نفس الصفحة، وتُوفر سياقًا إضافيًا أو استشهادات أو تعليقات.

أضف هامشًا إلى مقطع نصي في مستند PDF باستخدام Aspose.PDF للبايثون عبر .NET. تُعد الهوامش مفيدة لتوفير معلومات إضافية أو استشهادات أو توضيحات دون إبهام المحتوى الرئيسي. تضمن هذه الطريقة دمج الهوامش بصريًا وهيكليًا في تخطيط PDF.

1. إنشاء مستند جديد.
1. إنشاء TextFragment بالمحتوى الرئيسي.
1. إضافة نص داخل السطر. إنشاء TextFragment آخر يستمر في نفس الفقرة.
1. حفظ المستند.

```python

import aspose.pdf as ap
from aspose.pdf import Color
from aspose.pdf.drawing import Graph, Line
import os

# Global configuration
DATA_DIR = "your path here"

def add_footnote(outfile):
    """Add footnote to a PDF document."""

    document = ap.Document()
    page = document.pages.add()

    text_fragment = ap.text.TextFragment("This is a sample text with a footnote.")
    text_fragment.text_state.font = ap.text.FontRepository.find_font("Arial")
    text_fragment.text_state.font_size = 14
    text_fragment.foot_note = ap.Note("This is the footnote content.")
    page.paragraphs.add(text_fragment)

    inline_text = ap.text.TextFragment(
        " This is another text after footnote in the same paragraph."
    )
    inline_text.is_in_line_paragraph = True
    inline_text.text_state.font = ap.text.FontRepository.find_font("Arial")
    inline_text.text_state.font_size = 14
    page.paragraphs.add(inline_text)

    document.save(outfile)
```

### إضافة هامش مع تنسيق مخصص في PDF

1. تهيئة مستند PDF جديد وإضافة صفحة فارغة.
1. إنشاء مقطع النص الرئيسي.
1. إنشاء وتنسيق الهامش (الخط، الحجم، اللون، النمط).
1. إدراج مقطع النص المنسق مع الهامش في الصفحة.
1. إضافة مقطع نص آخر بدون هامش.
1. احفظ المستند.

```python

import aspose.pdf as ap
from aspose.pdf import Color
from aspose.pdf.drawing import Graph, Line
import os

# Global configuration
DATA_DIR = "your path here"

def add_footnote_custom_text_style(outfile):
    """Add footnote with custom text style."""

    document = ap.Document()
    page = document.pages.add()

    text_fragment = ap.text.TextFragment("This is a sample text with a footnote.")
    text_fragment.text_state.font = ap.text.FontRepository.find_font("Arial")
    text_fragment.text_state.font_size = 14

    note = ap.Note("This is the footnote content with custom text style.")
    note.text_state = ap.text.TextState()
    note.text_state.font = ap.text.FontRepository.find_font("Times New Roman")
    note.text_state.font_size = 10
    note.text_state.foreground_color = ap.Color.red
    note.text_state.font_style = ap.text.FontStyles.ITALIC
    text_fragment.foot_note = note

    page.paragraphs.add(text_fragment)

    another_text = ap.text.TextFragment(" This is another text without footnote.")
    another_text.text_state.font = ap.text.FontRepository.find_font("Arial")
    another_text.text_state.font_size = 14
    page.paragraphs.add(another_text)

    document.save(outfile)
```

### إضافة الحواشي مع رموز مخصصة في PDF

أضف حواشي إلى مقاطع النص في مستند PDF باستخدام Aspose.PDF للغة بايثون عبر .NET، مع إمكانية تخصيص رمز علامة الحاشية.

1. أنشئ مستند PDF وصفحة.
1. أضف مقطع النص الأول مع رمز حاشية مخصص.
1. أضف مقطع نص آخر يكمل الفقرة بدون حاشية.
1. أضف مقطع النص الثاني مع حاشية افتراضية.
1. احفظ المستند.

```python

import aspose.pdf as ap
from aspose.pdf import Color
from aspose.pdf.drawing import Graph, Line
import os

# Global configuration
DATA_DIR = "your path here"

def add_footnote_custom_text(outfile):
    """
    Add footnote with custom text marker to a PDF document.
    Creates a PDF document with text fragments that include footnotes with custom
    styling. The function demonstrates how to add footnotes with custom text markers
    and standard footnotes to different text fragments within the same document.
    Args:
        outfile (str): The output file path where the PDF document will be saved.
    Returns:
        None: The function saves the document to the specified output file.
    Example:
        add_footnote_custom_text("output_with_footnotes.pdf")
    Note:
        The document will contain:
        - Text with a custom footnote marker ("*")
        - Text without footnotes
        - Text with a standard footnote
    """

    document = ap.Document()
    page = document.pages.add()

    text_fragment = ap.text.TextFragment("This is a sample text with a footnote.")
    text_fragment.text_state.font = ap.text.FontRepository.find_font("Arial")
    text_fragment.text_state.font_size = 14

    note = ap.Note("This is the footnote content with custom text style.")
    note.text = "*"
    text_fragment.foot_note = note
    page.paragraphs.add(text_fragment)

    another_text = ap.text.TextFragment(" This is another text without footnote.")
    another_text.text_state.font = ap.text.FontRepository.find_font("Arial")
    another_text.text_state.font_size = 14
    page.paragraphs.add(another_text)

    text_fragment = ap.text.TextFragment("This is a sample text with a footnote.")
    text_fragment.text_state.font = ap.text.FontRepository.find_font("Arial")
    text_fragment.text_state.font_size = 14
    text_fragment.foot_note = ap.Note("This is the footnote content.")
    page.paragraphs.add(text_fragment)

    document.save(outfile)
```

### إضافة الحواشي مع نمط خط مخصص في PDF

خصص المظهر البصري لخطوط الحواشي في مستند PDF باستخدام مكتبة بايثون. تحسين خطوط الحواشي يعزز الوضوح البصري ويسمح بالاتساق الأسلوبي في المستندات مثل التقارير والأوراق الأكاديمية والمنشورات المشروحة.

1. أنشئ مستند PDF جديدًا وأضف صفحة.
1. عرّف نمط خط مخصص للوصلات الحاشية (اللون، العرض، ونمط الشرط).
1. أضف عدة مقاطع نصية مع حواشي.
1. احفظ المستند النهائي.

```python

import aspose.pdf as ap
from aspose.pdf import Color
from aspose.pdf.drawing import Graph, Line
import os

# Global configuration
DATA_DIR = "your path here"

def add_footnote_with_custom_line_style(outfile):
    """
    Add footnotes with custom line style to a PDF document.
    Creates a PDF document with text fragments that have footnotes and applies
    a custom line style for the footnote separator line. The custom style includes
    red color, increased line width, and dashed pattern.
    Args:
        outfile (str): Path where the generated PDF document will be saved.
    Returns:
        None: The function saves the document to the specified output file.
    Example:
        >>> add_footnote_with_custom_line_style("output.pdf")
        # Creates a PDF with footnoted text and custom separator line styling
    """

    document = ap.Document()
    page = document.pages.add()

    # Define custom line style
    graph_info = ap.GraphInfo()
    graph_info.line_width = 2
    graph_info.color = ap.Color.red
    graph_info.dash_array = [3]
    graph_info.dash_phase = 1
    page.note_line_style = graph_info

    # First text fragment with footnote
    text1 = ap.text.TextFragment("This is a sample text with a footnote.")
    text1.foot_note = ap.Note("foot note for text 1")
    page.paragraphs.add(text1)

    # Second text fragment with footnote
    text2 = ap.text.TextFragment("This is yet another sample text with a footnote.")
    text2.foot_note = ap.Note("foot note for text 2")
    page.paragraphs.add(text2)

    document.save(outfile)
```

### إضافة الحواشي مع صورة وجدول في PDF

كيف تُثرِي الحواشي في مستند PDF من خلال تضمين الصور والنص المنسق والجداول باستخدام Aspose.PDF للغة بايثون عبر .NET؟

1. أنشئ مستند PDF جديدًا وأضف صفحة.
1. أضف مقطع نص مع حاشية مرفقة.
1. قم بتضمين صورة، نص منسق، وجدول داخل الحاشية.
1. احفظ المستند.

```python

import aspose.pdf as ap
from aspose.pdf import Color
from aspose.pdf.drawing import Graph, Line
import os

# Global configuration
DATA_DIR = "your path here"

def add_footnote_with_image_and_table(outfile):
    """
    Add a footnote containing an image and table to a PDF document.
    Creates a new PDF document with sample text that includes a footnote. The footnote
    contains three elements: an image (logo.jpg), descriptive text, and a simple table
    with two cells. The image is resized to 20x20 pixels and the footnote text uses
    a 20pt font size.
    Args:
        outfile (str): The file path where the generated PDF document will be saved.
    Returns:
        None: The function saves the document to the specified output file.
    Note:
        - Requires the logo.jpg file to be present in the DATA_DIR directory
        - Uses the Aspose.PDF library (imported as 'ap')
        - The footnote is attached to the main text fragment on the page
    """

    document = ap.Document()
    page = document.pages.add()

    text = ap.text.TextFragment("This is a sample text with a footnote.")
    page.paragraphs.add(text)

    note = ap.Note()

    # Add image
    image_note = ap.Image()
    image_note.file = os.path.join(DATA_DIR, "logo.jpg")
    image_note.fix_height = 20
    image_note.fix_width = 20
    note.paragraphs.add(image_note)

    # Add text
    text_note = ap.text.TextFragment("This is the footnote content.")
    text_note.text_state.font_size = 20
    text_note.is_in_line_paragraph = True
    note.paragraphs.add(text_note)

    # Add table
    table = ap.Table()
    table.rows.add().cells.add("Cell 1,1")
    table.rows.add().cells.add("Cell 1,2")
    note.paragraphs.add(table)

    text.foot_note = note

    document.save(outfile)
```

### إضافة الهوامش الختامية إلى مستندات PDF

الهوامش الختامية هي نوع من الاقتباس يوجه القراء إلى قسم مخصص في نهاية المستند، حيث يمكنهم العثور على المرجع الكامل للاقتباس أو الفكرة المعاد صياغتها أو المحتوى الملخص. عند استخدام الهوامش الختامية، يُوضع رقم فوقي مباشرةً بعد المادة المشار إليها، مما يوجه القارئ إلى الملاحظة المقابلة في نهاية الورقة.

يوضح هذا المقتطف البرمجي كيفية إضافة هامش ختامي إلى مقطع نص في مستند PDF. على عكس الحواشي التي تظهر بالقرب من النص المشار إليه، تُوضع الهوامش الختامية عادةً في نهاية المستند أو القسم. تُحاكي هذه الطريقة أيضًا مستندًا أطول لتوضيح سلوك الهوامش الختامية في المحتوى الممتد.

1. أنشئ مستند PDF وصفحة.
1. أضف مقطع نص مع هامش ختامي.
1. حمّل محتوى نص خارجي.
1. احاكي مستندًا طويلًا. أضف النص المحمّل عدة مرات لمحاكاة مستند أطول.
1. احفظ المستند.

```python

import aspose.pdf as ap
from aspose.pdf import Color
from aspose.pdf.drawing import Graph, Line
import os

# Global configuration
DATA_DIR = "your path here"

def add_endnote(outfile):
    """Add endnote to a PDF document.
    Creates a new PDF document with a text fragment containing an endnote,
    followed by additional lorem ipsum content to simulate a longer document.
    The endnote is attached to the first text fragment and will be displayed
    according to the PDF viewer's endnote handling.
    Args:
        outfile (str): The file path where the generated PDF document will be saved.
    Returns:
        None: The function saves the document to the specified output file path.
    Note:
        This function requires the aspose-pdf library and assumes the existence
        of a DATA_DIR variable pointing to a directory containing 'lorem.txt'.
        If the lorem.txt file is not found, fallback text will be used.
    """

    document = ap.Document()
    page = document.pages.add()

    text_fragment = ap.text.TextFragment("This is a sample text with an endnote.")
    text_fragment.text_state.font = ap.text.FontRepository.find_font("Arial")
    text_fragment.text_state.font_size = 14
    text_fragment.end_note = ap.Note("This is the EndNote content.")
    page.paragraphs.add(text_fragment)

    lorem_path = os.path.join(DATA_DIR, "lorem.txt")
    text_content = (
        open(lorem_path, encoding="utf-8").read()
        if os.path.exists(lorem_path)
        else "Lorem ipsum sample text not found."
    )

    # Simulate long text
    for _ in range(5):
        tf = ap.text.TextFragment(text_content)
        tf.text_state.font = ap.text.FontRepository.find_font("Arial")
        tf.text_state.font_size = 14
        page.paragraphs.add(tf)

    document.save(outfile)
```

### إضافة الهوامش الختامية مع نص علامة مخصص في PDF

أضف هامشًا ختاميًا إلى مقطع نص في مستند PDF، مع رمز علامة مخصص (مثال: "***"). تُوضع الهوامش الختامية عادةً في نهاية المستند أو القسم وتُفيد في توفير سياق إضافي أو اقتباسات أو تعليقات.

1. أنشئ مستند PDF وصفحة.
1. أضف مقطع نص منسق مع هامش ختامي.
1. خصص نص علامة الهامش الختامي.
1. حمّل محتوى خارجي من ملف .txt.
1. احاكي محتوى طويل الشكل لتوضيح موضع الهامش الختامي.
1. احفظ مستند PDF.

```python

import aspose.pdf as ap
from aspose.pdf import Color
from aspose.pdf.drawing import Graph, Line
import os

# Global configuration
DATA_DIR = "your path here"

def add_endnote_custom_text(outfile):
    """
    Add endnote with custom text marker to a PDF document.
    Creates a PDF document with a text fragment that contains an endnote with
    a custom marker ("***"). The document is populated with sample text content
    from a lorem.txt file, repeated multiple times to simulate a longer document.
    Args:
        outfile (str): Path where the generated PDF document will be saved.
    Returns:
        None: The function saves the document to the specified output file path.
    Note:
        - Requires lorem.txt file in DATA_DIR for sample content
        - Falls back to default text if lorem.txt is not found
        - Uses Arial font with 14pt size for all text elements
        - The endnote marker is set to "***" instead of default numbering
    """

    document = ap.Document()
    page = document.pages.add()

    text_fragment = ap.text.TextFragment("This is a sample text with an endnote.")
    text_fragment.text_state.font = ap.text.FontRepository.find_font("Arial")
    text_fragment.text_state.font_size = 14
    text_fragment.end_note = ap.Note("This is the EndNote content.")
    text_fragment.end_note.text = "***"
    page.paragraphs.add(text_fragment)

    lorem_path = os.path.join(DATA_DIR, "lorem.txt")
    text_content = (
        open(lorem_path, encoding="utf-8").read()
        if os.path.exists(lorem_path)
        else "Lorem ipsum sample text not found."
    )

    # Simulate long text
    for _ in range(5):
        tf = ap.text.TextFragment(text_content)
        tf.text_state.font = ap.text.FontRepository.find_font("Arial")
        tf.text_state.font_size = 14
        page.paragraphs.add(tf)

    document.save(outfile)
```

## التخطيط والتحكم في الصفحات

### إجبار جدول على البدء في صفحة جديدة في PDF

أضف محتوى محدد للبدء في صفحة جديدة في مستند PDF باستخدام Aspose.PDF للغة بايثون عبر .NET.
من خلال ضبط الخاصية 'is_in_new_page'، يمكنك التحكم بدقة في تخطيط الصفحات والبنية، مما يضمن أن الأقسام المحددة (مثل الجداول أو التقارير أو الملخصات) تبدأ دائمًا في صفحة جديدة — وهو مثالي لتنسيق المستندات، التقارير الجاهزة للطباعة، أو توليد مخرجات منظمة.

1. أنشئ وجدول وضبط إعداده.
1. أضف بيانات إلى الجدول.
1. إجبار صفحة جديدة للجدول. يضمن ذلك أن يبدأ الجدول في أعلى صفحة جديدة، حتى إذا كان هناك محتوى موجود في الحالية.
1. أضف الجدول إلى الصفحة. استخدم 'page.paragraphs.add()' لتضمين الجدول في تخطيط PDF.
1. احفظ المستند.

```python

import aspose.pdf as ap
from aspose.pdf import Color
from aspose.pdf.drawing import Graph, Line
import os

# Global configuration
DATA_DIR = "your path here"

def force_new_page(output_file_name):
    """
    Create a PDF document demonstrating forced page breaks with tables.

    Creates a PDF document with a table that is forced to start on a new page
    using the is_in_new_page property. This is useful for controlling page layout
    and ensuring specific content starts on fresh pages.

    Args:
        output_file_name (str): The file path where the generated PDF document will be saved.

    Returns:
        None: The function saves the document to the specified output file.

    Note:
        - Creates a 3-column table with 5 rows of sample data
        - Table uses uniform column widths of 150 units each
        - All cells have borders for clear visual separation
        - is_in_new_page=True forces the table to start on a new page
        - Useful for reports, documents with sections, or content organization

    Example:
        >>> force_new_page("new_page_table.pdf")
        # Creates a PDF with a table that starts on a new page
    """
    # Create new PDF document
    document = ap.Document()
    page = document.pages.add()

    # Create a table
    table = ap.Table()
    table.column_widths = "150 150 150"
    table.default_cell_border = ap.BorderInfo(ap.BorderSide.ALL)

    # Add rows with sample data
    for i in range(5):
        row = table.rows.add()
        row.cells.add(f"Row {i + 1} - Col 1")
        row.cells.add(f"Row {i + 1} - Col 2")
        row.cells.add(f"Row {i + 1} - Col 3")

    # --- Key part: force table to start on a new PDF page ---
    table.is_in_new_page = True

    # Add table to page
    page.paragraphs.add(table)

    # Save the PDF
    document.save(output_file_name)
```

### استخدام خاصية الفقرة المتضمنة في PDF

تتيح مكتبتنا لك استخدام خاصية 'is_in_line_paragraph' للتحكم في التدفق المتضمن بين النص والصور داخل PDF.
عادةً، عندما تضيف عناصر جديدة (مثل مقاطع النص أو الصور)، يبدأ كل منها في سطر جديد أو فقرة جديدة.
عن طريق ضبط 'is_in_line_paragraph = True'، يمكنك جعل العناصر تظهر في نفس السطر أو داخل نفس الفقرة، مما يخلق تخطيطات متضمنة سلسة—مثالية لدمج النص والصور ضمنًا، مثل إضافة الشعارات أو الأيقونات أو الرموز داخل الجمل.

يظهر مقطع النص الأول، الصورة، ومقطع النص الثاني في نفس السطر، مُكوّنين فقرة متضمنة مستمرة.
يبدأ الجزء النصي الثالث فقرةً جديدةً، موضحًا سلوك الانكسار الافتراضي للسطر.

1. أنشئ مستند PDF جديد.
1. أضف الجزء النصي الأول.
1. أدخل صورة مدمجة.
1. أضف المزيد من النص المدمج.
1. أضف فقرة جديدة.
1. احفظ ملف PDF.

```python

import aspose.pdf as ap
from aspose.pdf import Color
from aspose.pdf.drawing import Graph, Line
import os

# Global configuration
DATA_DIR = "your path here"

def using_inline_paragraph_property(output_file_name):
    """
    Demonstrate inline paragraph behavior in PDF document layout.

    Creates a PDF document showing how the is_in_line_paragraph property affects
    the flow of text and images. Elements with this property continue the flow
    of the previous paragraph instead of starting a new one.

    Args:
        output_file_name (str): The file path where the generated PDF document will be saved.

    Returns:
        None: The function saves the document to the specified output file.

    Note:
        - First text fragment starts a new paragraph
        - Image with is_in_line_paragraph=True continues the same line
        - Second text fragment also continues the same paragraph line
        - Third text fragment starts a new paragraph (default behavior)
        - Demonstrates inline flow control for mixed content (text + images)
        - Image is resized to 30x30 pixels and flows inline with text

    Example:
        >>> using_inline_paragraph_property("inline_paragraph.pdf")
        # Creates a PDF demonstrating inline paragraph flow
    """
    # Create a PDF document
    document = ap.Document()
    page = document.pages.add()

    # --- First text fragment (normal paragraph) ---
    fragment1 = ap.text.TextFragment("This is the first part of the paragraph. ")
    fragment1.text_state.font = ap.text.FontRepository.find_font("Arial")
    fragment1.text_state.font_size = 14
    page.paragraphs.add(fragment1)

    # --- Inline image (continues same paragraph flow) ---
    image = ap.Image()
    image.is_in_line_paragraph = True  # Makes image inline with previous paragraph
    image.file = os.path.join(DATA_DIR, "logo.jpg")
    image.fix_height = 30
    image.fix_width = 30
    page.paragraphs.add(image)

    # --- Second inline text fragment (keeps same paragraph flow) ---
    fragment2 = ap.text.TextFragment("This is the second part of the same paragraph.")
    fragment2.is_in_line_paragraph = True
    fragment2.text_state.font = ap.text.FontRepository.find_font("Arial")
    fragment2.text_state.font_size = 14
    page.paragraphs.add(fragment2)

    # --- Third fragment (starts new paragraph automatically) ---
    fragment3 = ap.text.TextFragment("This is a new paragraph.")
    fragment3.text_state.font = ap.text.FontRepository.find_font("Arial")
    fragment3.text_state.font_size = 14
    page.paragraphs.add(fragment3)

    # Save PDF
    document.save(output_file_name)
```

### إنشاء ملف PDF متعدد الأعمدة

أنشئ تخطيطًا على نمط الصحيفة متعدد الأعمدة في ملف PDF باستخدام Aspose.PDF للـ Python عبر .NET.
يعرض كيفية دمج النص وتنسيق HTML والرسومات داخل FloatingBox، مما يتيح التحكم المتقدم في التخطيط مماثل لتصميمات المجلات أو النشرات المتعددة الأعمدة.

1. ابدأ مستند PDF.
1. أضف خط فاصل أفقي في الأعلى.
1. أضف عنوان HTML منسق.
1. أنشئ FloatingBox للتحكم في التخطيط.
1. اضبط تخطيط متعدد الأعمدة.
1. أضف معلومات المؤلف.
1. ارسم خطًا أفقيًا داخليًا آخر.
1. أضف نص المقال.
1. احفظ ملف PDF النهائي.

```python

import aspose.pdf as ap
from aspose.pdf import Color
from aspose.pdf.drawing import Graph, Line
import os

# Global configuration
DATA_DIR = "your path here"

def create_multi_column_pdf(output_file_name):
    """
    Create a PDF document with multi-column layout using FloatingBox.

    Creates a professional-looking PDF with a multi-column newspaper-style layout.
    Demonstrates advanced layout techniques including floating boxes, column
    configuration, and mixed content with graphics and text.

    Args:
        output_file_name (str): The file path where the generated PDF document will be saved.

    Returns:
        None: The function saves the document to the specified output file.

    Note:
        - Document margins: 40 points left and right
        - Top horizontal line for visual separation
        - HTML-formatted heading with custom styling
        - FloatingBox with 2-column layout (105 units wide each)
        - Column spacing: 5 units between columns
        - Includes author attribution with italic styling
        - Internal horizontal line within the floating box
        - Long text content automatically flows between columns
        - Demonstrates professional document layout techniques

    Example:
        >>> create_multi_column_pdf("multi_column_layout.pdf")
        # Creates a PDF with newspaper-style multi-column layout
    """
    # Create PDF document
    document = ap.Document()

    # Set margins
    document.page_info.margin.left = 40
    document.page_info.margin.right = 40

    page = document.pages.add()

    #
    # Draw horizontal line at the top
    #
    graph1 = ap.drawing.Graph(500.0, 2.0)
    page.paragraphs.add(graph1)

    pos_arr = [1.0, 2.0, 500.0, 2.0]
    line1 = ap.drawing.Line(pos_arr)
    graph1.shapes.add(line1)

    #
    # Add HTML heading text
    #
    html = "<span style=\"font-family: 'Times New Roman'; font-size: 18px;\"><strong>How to Steer Clear of money scams</strong></span>"
    heading_text = ap.HtmlFragment(html)
    page.paragraphs.add(heading_text)

    #
    # Floating box: enables multi-column layout
    #
    box = ap.FloatingBox()

    box.column_info.column_count = 2  # Two columns
    box.column_info.column_spacing = "5"  # Space between columns
    box.column_info.column_widths = "105 105"  # Width of each column

    #
    # Add title text to the FloatingBox
    #
    text1 = ap.text.TextFragment("By A Googler (The Official Google Blog)")
    text1.text_state.font_size = 8
    text1.text_state.line_spacing = 2
    box.paragraphs.add(text1)

    text1.text_state.font_size = 10
    text1.text_state.font_style = ap.text.FontStyles.ITALIC

    #
    # Add another horizontal line inside the box
    #
    graph2 = ap.drawing.Graph(50.0, 10.0)

    pos_arr2 = [1.0, 10.0, 100.0, 10.0]
    line2 = ap.drawing.Line(pos_arr2)
    graph2.shapes.add(line2)

    box.paragraphs.add(graph2)

    #
    # Add long text content
    #
    lorem_path = os.path.join(DATA_DIR, "lorem.txt")
    lorem_text = (
        open(lorem_path, "r", encoding="utf-8").read()
        if os.path.exists(lorem_path)
        else "Lorem ipsum text not found."
    )
    text2 = ap.text.TextFragment(lorem_text * 5)
    box.paragraphs.add(text2)

    page.paragraphs.add(box)

    # Save PDF
    document.save(output_file_name)
```

### إيقافات تبويب مخصصة لمحاذاة النص في PDF

أنشئ تخطيطًا نصيًا يشبه الجدول في ملف PDF باستخدام إيقافات تبويب مخصصة — دون الاعتماد على هياكل الجداول.
من خلال تعريف مواضع إيقافات التبويب، والمحاذاة، وأنماط القادة، يمكنك محاذاة النص بدقة عبر الأعمدة. وهذا مفيد للفواتير، والتقارير، أو البيانات النصية المهيكلة.

1. أنشئ مستند PDF جديد.
1. حدّد إيقافات تبويب مخصصة.
1. استخدم عناصر نائبة #$TAB في النص.
1. أضف نصًا إلى ملف PDF.
1. احفظ ملف PDF.

```python

import aspose.pdf as ap
from aspose.pdf import Color
from aspose.pdf.drawing import Graph, Line
import os

# Global configuration
DATA_DIR = "your path here"

def custom_tab_stops(output_file_name):
    """
    Create a PDF document demonstrating custom tab stops for table-like formatting.

    Creates a PDF document that uses custom tab stops to format text in a table-like
    structure without using actual table elements. This demonstrates advanced text
    formatting with precise positioning and leader styles.

    Args:
        output_file_name (str): The file path where the generated PDF document will be saved.

    Returns:
        None: The function saves the document to the specified output file.

    Note:
        - Tab stop 1: Position 100, right-aligned, solid leader line
        - Tab stop 2: Position 200, center-aligned, dashed leader line
        - Tab stop 3: Position 300, left-aligned, dotted leader line
        - Uses #$TAB placeholder for tab positions in text
        - Creates table-like structure with headers and data rows
        - Demonstrates mixing TextFragment and TextSegment approaches
        - Leader lines provide visual guides between columns
        - Alternative to HTML tables for precise text positioning

    Example:
        >>> custom_tab_stops("custom_tabs.pdf")
        # Creates a PDF with custom tab stop formatting
    """
    # Create PDF document
    document = ap.Document()
    page = document.pages.add()

    # Define tab stops
    tab_stops = ap.text.TabStops()

    tab_stop1 = tab_stops.add(100)
    tab_stop1.alignment_type = ap.text.TabAlignmentType.RIGHT
    tab_stop1.leader_type = ap.text.TabLeaderType.SOLID

    tab_stop2 = tab_stops.add(200)
    tab_stop2.alignment_type = ap.text.TabAlignmentType.CENTER
    tab_stop2.leader_type = ap.text.TabLeaderType.DASH

    tab_stop3 = tab_stops.add(300)
    tab_stop3.alignment_type = ap.text.TabAlignmentType.LEFT
    tab_stop3.leader_type = ap.text.TabLeaderType.DOT

    # Create TextFragments with tab placeholders
    header = ap.text.TextFragment(
        "This is an example of forming table with TAB stops", tab_stops
    )
    text0 = ap.text.TextFragment("#$TABHead1 #$TABHead2 #$TABHead3", tab_stops)
    text1 = ap.text.TextFragment("#$TABdata11 #$TABdata12 #$TABdata13", tab_stops)

    text2 = ap.text.TextFragment("#$TABdata21 ", tab_stops)
    text2.segments.append(ap.text.TextSegment("#$TAB"))
    text2.segments.append(ap.text.TextSegment("data22 "))
    text2.segments.append(ap.text.TextSegment("#$TAB"))
    text2.segments.append(ap.text.TextSegment("data23"))

    # Add text fragments to page
    page.paragraphs.add(header)
    page.paragraphs.add(text0)
    page.paragraphs.add(text1)
    page.paragraphs.add(text2)

    # Save PDF document
    document.save(output_file_name)
```
