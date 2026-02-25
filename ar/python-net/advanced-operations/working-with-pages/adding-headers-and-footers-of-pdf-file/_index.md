---
title: إضافة رأس وتذييل إلى ملف PDF باستخدام بايثون
linktitle: إضافة رأس وتذييل إلى PDF
type: docs
weight: 50
url: /ar/python-net/add-headers-and-footers-of-pdf-file/
description: Aspose.PDF للبايثون عبر .NET يتيح لك إضافة رؤوس وتذييلات إلى ملف PDF الخاص بك باستخدام فئة TextStamp.
lastmod: "2025-11-16"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: كيفية إضافة رأس وتذييل إلى PDF باستخدام بايثون
Abstract: المقالة توفر دليلًا شاملاً حول استخدام **Aspose.PDF للبايثون عبر .NET** لإضافة رؤوس وتذييلات إلى ملفات PDF، مع القدرة على دمج النص أو الصور. يبدأ بتفصيل استخدام فئة `TextStamp` لإدراج النص في رأس مستند PDF. الخصائص الرئيسية مثل حجم الخط، والنمط، واللون قابلة للتعديل، ويتم توضيح طريقة إضافة النص إلى الرأس باستخدام مقتطف كود بايثون. يشرح المقال بنفس الطريقة كيفية إضافة النص إلى التذييل، متبعًا نفس الخطوات الإجرائية. لإضافة الصور، تُستخدم فئة `ImageStamp`، ويتم وصف العملية لكل من الرؤوس والتذييلات، مدعومة بأمثلة كود بايثون. بالإضافة إلى ذلك، يناقش المقال إضافة عدة رؤوس في ملف PDF واحد. يشمل ذلك إنشاء عدة كائنات `TextStamp`، كل منها بتنسيق مميز، وتطبيقها على صفحات مختلفة. يُكمل الشرح مقتطف كود مفصل يوضح هذه الوظيفة.
---

توفر هذه الصفحة نظرة موجزة على إضافة الرؤوس والتذييلات إلى مستندات PDF باستخدام Aspose.PDF للبايثون عبر .NET، مع تغطية نهج النص، HTML، LaTeX، الصور، والجداول بالإضافة إلى ترقيم الصفحات الديناميكي والعديد من الرؤوس لكل صفحة؛ تشرح كيفية إنشاء وتنسيق كائنات [`HeaderFooter`](https://reference.aspose.com/pdf/python-net/aspose.pdf/headerfooter/) (باستخدام [`TextFragment`](https://reference.aspose.com/pdf/python-net/aspose.pdf/textfragment/)، [`HtmlFragment`](https://reference.aspose.com/pdf/python-net/aspose.pdf/htmlfragment/)، [`TeXFragment`](https://reference.aspose.com/pdf/python-net/aspose.pdf/texfragment/)، [`Image`](https://reference.aspose.com/pdf/python-net/aspose.pdf/image/)، [`Table`](https://reference.aspose.com/pdf/python-net/aspose.pdf/table/)، إلخ)، ضبط [`MarginInfo`](https://reference.aspose.com/pdf/python-net/aspose.pdf/margininfo/) و [`TextState`](https://reference.aspose.com/pdf/python-net/aspose.pdf/textstate/) للحصول على وضعية دقيقة، وإرفاق النتائج بالصفحات باستخدام أمثلة عملية لكود بايثون.

**Aspose.PDF للبايثون عبر .NET** يتيح لك إضافة رأس وتذييل في الـ[`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/). يمكنك إضافة صور أو نص إلى مستند PDF. كما يمكنك تجربة إضافة رؤوس مختلفة في ملف PDF واحد باستخدام بايثون.

## إضافة رؤوس وتذييلات كقطع نصية

إضافة رؤوس وتذييلات نصية بسيطة إلى جميع صفحات PDF. تقوم بإنشاء كائنات [`HeaderFooter`](https://reference.aspose.com/pdf/python-net/aspose.pdf/headerfooter/)، وتُدرج عناصر [`TextFragment`](https://reference.aspose.com/pdf/python-net/aspose.pdf/textfragment/) فيها، وتضبط [`MarginInfo`](https://reference.aspose.com/pdf/python-net/aspose.pdf/margininfo/) لضمان التموضع الصحيح، وتُرفقها بكل صفحة في المستند. النتيجة هي PDF حيث تعرض كل صفحة نص رأس وتذييل موحد.

المقتطف البرمجي التالي يوضح كيفية إضافة الرؤوس والتذييلات كقطع نصية في ملف PDF باستخدام بايثون:

1. إنشاء قطع نصية للرأس والتذييل.
1. إنشاء كائنات HeaderFooter وإضافة قطع النص إليها.
1. تحديد إعدادات الهوامش للتحكم في موضع الرأس والتذييل.
1. تحميل مستند PDF من ملف الإدخال.
1. التجول عبر جميع الصفحات في المستند.
1. تعيين الرأس والتذييل لكل صفحة.
1. حفظ PDF المعدل إلى ملف الإخراج.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def add_header_and_footer_as_text(input_file, output_file):
    """
    Add simple text headers and footers to all pages of a PDF document.

    Creates basic text-based headers and footers that appear on every page
    of the PDF document. Headers show "header" text and footers show "footer" text.

    Args:
        input_file (str): Path to the input PDF file.
        output_file (str): Path where the modified PDF will be saved.

    Returns:
        None: The function modifies the PDF and saves it to the output path.

    Note:
        - Adds identical headers and footers to all pages
        - Sets margins of 50 units left and 20 units top
        - Uses simple TextFragment elements for content
        - Headers and footers are created separately for each page

    Example:
        >>> add_header_and_footer_as_text("input.pdf", "output.pdf")
        # Adds text headers and footers to all pages
    """
    # Create header text
    header_text = ap.text.TextFragment("Demo header")
    # Create header
    header = ap.HeaderFooter()
    header.paragraphs.add(header_text)

    # Create footer text
    footer_text = ap.text.TextFragment("Demo footer")

    # Create footer
    footer = ap.HeaderFooter()
    footer.paragraphs.add(footer_text)

    # Set header margin
    margin = ap.MarginInfo()
    margin.left = 50
    margin.top = 20
    header.margin = margin

    # Set footer margin
    footer.margin = margin

    # Open PDF document
    with ap.Document(input_file) as document:
        for i in range(1, len(document.pages) + 1):
            # Bind the header and footer to the page
            document.pages[i].header = header
            document.pages[i].footer = footer

        # Save PDF document
        document.save(output_file)
```

هذه الطريقة مفيدة لإضافة عناوين موحدة، مؤشرات صفحات، أو إخلاءات مسؤولية قانونية في أعلى وأسفل كل صفحة. يمكنك أيضًا توسيعها لتشمل الصور أو المحتوى الديناميكي مثل أرقام الصفحات.

## إضافة رؤوس وتذييلات لترقيم الصفحات

إضافة ترقيم صفحات تلقائي إلى رؤوس وتذييلات مستند PDF باستخدام Aspose.PDF للبايثون. باستخدام المتغيرات المدمجة $p (رقم الصفحة الحالي) و $P (إجمالي عدد الصفحات)، يقوم السكريبت بإدراج ترقيم الصفحات ديناميكيًا في كل صفحة. تعرض الرؤوس الصيغة 'Page X from Y'، بينما تُظهر التذييلات 'Page X / Y'. يضمن [`MarginInfo`](https://reference.aspose.com/pdf/python-net/aspose.pdf/margininfo/) التموضع الصحيح في كل صفحة.

1. إنشاء TextFragment للرأس باستخدام "Page $p from $P" لعرض الصفحة الحالية والإجمالية.
1. إنشاء كائن HeaderFooter وإضافة نص الرأس إليه.
1. إنشاء TextFragment للتذييل باستخدام "Page $p / $P" لنمط ترقيم بديل.
1. إنشاء كائن Footer وإضافة نص التذييل.
1. تحديد إعدادات الهوامش (اليسار = 50، الأعلى = 20) وتطبيقها على كل من الرأس والتذييل.
1. فتح مستند PDF من ملف الإدخال.
1. التكرار عبر جميع الصفحات وتعيين الرأس والتذييل لكل صفحة.
1. حفظ PDF المحدث إلى مسار الإخراج.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def using_header_and_footer_for_page_numbering(input_file, output_file):
    """
    Add page numbering headers and footers to all pages of a PDF document.

    Creates headers and footers with dynamic page numbering using special variables.
    The $p variable represents the current page number and $P represents the total
    number of pages in the document.

    Args:
        input_file (str): Path to the input PDF file.
        output_file (str): Path where the modified PDF will be saved.

    Returns:
        None: The function modifies the PDF and saves it to the output path.

    Note:
        - Uses $p for current page number and $P for total pages
        - Header shows "Page X from Y" format
        - Footer shows "Page X / Y" format
        - Variables are automatically replaced by Aspose.PDF
        - Sets margins of 50 units left and 20 units top
        - Page numbering updates dynamically for each page

    Example:
        >>> using_header_and_footer_for_page_numbering("input.pdf", "output.pdf")
        # Adds page numbering headers and footers to all pages
    """
    # Create header text
    header_text = ap.text.TextFragment("Page $p from $P")
    # Create header
    header = ap.HeaderFooter()
    header.paragraphs.add(header_text)

    # Create footer text
    footer_text = ap.text.TextFragment("Page $p / $P")

    # Create footer
    footer = ap.HeaderFooter()
    footer.paragraphs.add(footer_text)

    # Create margins
    margin = ap.MarginInfo()
    margin.left = 50
    margin.top = 20

    # Set header margin
    header.margin = margin
    # Set footer margin
    footer.margin = margin

    # Open PDF document
    with ap.Document(input_file) as document:
        for i in range(1, len(document.pages) + 1):
            # Bind the header and footer to the page
            document.pages[i].header = header
            document.pages[i].footer = footer

        # Save PDF document
        document.save(output_file)
```

## إضافة رؤوس وتذييلات كقطع HTML

تطبيق رؤوس وتذييلات مهيأة بـ HTML على كل صفحة من مستند PDF باستخدام Aspose.PDF للبايثون. باستخدام [`HtmlFragment`](https://reference.aspose.com/pdf/python-net/aspose.pdf/htmlfragment/)، يسمح السكريبت بتنسيق نص غني—مثل الغامق والمائل—للعرض في الرأس والتذييل. يتم تطبيق [`MarginInfo`](https://reference.aspose.com/pdf/python-net/aspose.pdf/margininfo/) للتموضع الصحيح، وتُرفق العناصر المُنسقة نفسها بكل صفحة في المستند.

المقتطف البرمجي التالي يوضح كيفية إضافة الرؤوس والتذييلات كقطع HTML إلى PDF باستخدام بايثون:

1. إنشاء مقطع رأس HTML باستخدام HtmlFragment—متضمنًا نصًا منسقًا مثل '<strong>' للغميق.
1. إنشاء كائن HeaderFooter وإضافة رأس HTML إليه.
1. إنشاء مقطع تذييل HTML باستخدام '<i>' لتنسيق مائل.
1. إنشاء كائن Footer وإضافة HTML التذييل إليه.
1. ضبط الهوامش (اليسار = 50، الأعلى = 20) وتعيينها لكل من الرأس والتذييل.
1. تحميل مستند PDF باستخدام 'ap.Document()'.
1. التكرار عبر جميع الصفحات وتعيين الرأس والتذييل لكل منها.
1. حفظ PDF المعدل إلى مسار الإخراج المحدد.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def add_header_and_footer_as_html(input_file, output_file):
    """
    Add HTML-formatted headers and footers to all pages of a PDF document.

    Creates rich HTML-based headers and footers with formatting like bold
    and italic text. Demonstrates how to use HtmlFragment for styled content.

    Args:
        input_file (str): Path to the input PDF file.
        output_file (str): Path where the modified PDF will be saved.

    Returns:
        None: The function modifies the PDF and saves it to the output path.

    Note:
        - Uses HtmlFragment for rich text formatting
        - Header includes HTML with <strong> tag for bold text
        - Footer includes HTML with <i> tag for italic text
        - Sets margins of 50 units left and 20 units top
        - HTML tags are rendered properly in the PDF

    Example:
        >>> add_header_and_footer_as_html("input.pdf", "output.pdf")
        # Adds HTML-formatted headers and footers to all pages
    """
    # Create header HTML
    header_html = ap.HtmlFragment("This is an HTML <strong>Header</strong>")
    # Create header
    header = ap.HeaderFooter()
    header.paragraphs.add(header_html)

    # Create footer HTML
    footer_html = ap.HtmlFragment("Powered by <i>Aspose.PDF</i>")

    # Create footer
    footer = ap.HeaderFooter()
    footer.paragraphs.add(footer_html)

    # Set header margin
    margin = ap.MarginInfo()
    margin.left = 50
    margin.top = 20
    header.margin = margin

    # Set footer margin
    footer.margin = margin

    # Open PDF document
    with ap.Document(input_file) as document:
        for i in range(1, len(document.pages) + 1):
            # Bind the header and footer to the page
            document.pages[i].header = header
            document.pages[i].footer = footer

        # Save PDF document
        document.save(output_file)
```

استخدام HtmlFragment يتيح تنسيقًا غنيًا مع الأنماط المضمنة أو العلامات HTML، مما يمنحك مرونة تصميم أكبر مقارنة بالنص العادي.

## إضافة رؤوس وتذييلات كصور

إضافة رؤوس وتذييلات تعتمد على الصور إلى كل صفحة من مستند PDF باستخدام Aspose.PDF للبايثون. يتم استخدام نفس ملف الصورة لكل من الرأس والتذييل في كل صفحة. يقوم [`MarginInfo`](https://reference.aspose.com/pdf/python-net/aspose.pdf/margininfo/) بتموضع الصور، وتضبط الصورة تلقائيًا لتناسب مساحة الرأس/التذييل.

يظهر مقتطف الشيفرة التالي كيفية إضافة رؤوس وتذييلات كصور إلى ملف PDF باستخدام بايثون:

1. قم بتحميل الصورة إلى كائن 'ap.Image' وتحضيرها للاستخدام كرأس.
1. إنشاء كائن HeaderFooter وإرفاق صورة الرأس به.
1. تحميل نفس الصورة مرة أخرى لاستخدامها كتذييل.
1. إنشاء كائن Footer وإضافة صورة التذييل إليه.
1. تحميل مستند PDF المدخل باستخدام 'ap.Document()'.
1. التكرار عبر جميع صفحات المستند.
1. تطبيق الهوامش (اليسار = 50) لتحديد موضع كل من الرأس والتذييل.
1. إسناد الرأس والتذييل إلى كل صفحة في ملف PDF.
1. حفظ ملف PDF المحدث إلى ملف الإخراج المحدد.

هذه التقنية مثالية لتوسيم المستندات بشعارات أو علامات مائية في منطقة الرأس/التذييل.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def add_header_and_footer_as_image(input_file, image_file, output_file):
    """
    Add image-based headers and footers to all pages of a PDF document.

    Creates headers and footers using image files. The same image is used
    for both header and footer positioning on each page.

    Args:
        input_file (str): Path to the input PDF file.
        image_file (str): Path to the image file to use for headers and footers.
        output_file (str): Path where the modified PDF will be saved.

    Returns:
        None: The function modifies the PDF and saves it to the output path.

    Note:
        - Uses the same image file for both header and footer
        - Creates separate Image objects for header and footer
        - Sets margin of 50 units left for positioning
        - Image files should be in supported formats (PNG, JPG, etc.)
        - Images are automatically sized to fit header/footer areas

    Example:
        >>> add_header_and_footer_as_image("input.pdf", "logo.png", "output.pdf")
        # Adds image headers and footers using logo.png
    """

    # Create header image
    header_image = ap.Image()
    header_image.file = image_file
    # Create header
    header = ap.HeaderFooter()
    header.paragraphs.add(header_image)

    # Create footer image
    footer_image = ap.Image()
    footer_image.file = image_file

    # Create footer
    footer = ap.HeaderFooter()
    footer.paragraphs.add(footer_image)

    # Open PDF document
    with ap.Document(input_file) as document:
        for i in range(1, len(document.pages) + 1):
            # Set header margin
            margin = ap.MarginInfo()
            margin.left = 50
            header.margin = margin

            # Set footer margin
            footer.margin = margin

            # Bind the header and footer to the page
            document.pages[i].header = header
            document.pages[i].footer = footer

        # Save PDF document
        document.save(output_file)
```

## إضافة رؤوس وتذييلات كجدول

أضف رؤوس وتذييلات منظمة على شكل جدول إلى جميع صفحات مستند PDF باستخدام Aspose.PDF للبايثون. كائنات [`Table`](https://reference.aspose.com/pdf/python-net/aspose.pdf/table/) توفر تحكمًا أفضل في التخطيط، والمحاذاة، وتنسيقًا ثابتًا للرؤوس والتذييلات المعقدة. نص الرأس مُوسَّط بينما نص التذييل مُحاذى إلى اليسار، وكلاهما يستخدم خط Arial بحجم 12 نقطة. تُحسب عرض الأعمدة بصورة ديناميكية بناءً على أبعاد الصفحة لضمان وضع صحيح.

يضيف هذا مقتطف الشيفرة رؤوس وتذييلات (باستخدام الجداول) إلى كل صفحة من مستند PDF باستخدام Aspose.PDF للبايثون عبر .NET.

1. تعريف أنماط النص باستخدام [`TextState`](https://reference.aspose.com/pdf/python-net/aspose.pdf/textstate/) للرأس والتذييل (الخط، الحجم، المحاذاة).
1. إنشاء كائنات [`HeaderFooter`](https://reference.aspose.com/pdf/python-net/aspose.pdf/headerfooter/) للرأس والتذييل.
1. بناء رأس الـ[`Table`](https://reference.aspose.com/pdf/python-net/aspose.pdf/table/) بصف واحد وخلية تحتوي على نص الرأس.
1. بناء تذييل الـ[`Table`](https://reference.aspose.com/pdf/python-net/aspose.pdf/table/) بصف واحد وخلية تحتوي على نص التذييل.
1. إضافة الجداول إلى كائنات [`HeaderFooter`](https://reference.aspose.com/pdf/python-net/aspose.pdf/headerfooter/) المقابلة.
1. تعيين [`MarginInfo`](https://reference.aspose.com/pdf/python-net/aspose.pdf/margininfo/) للتذييل لضبط التموضع الأفقي بشكل صحيح.
1. فتح الـ[`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) باستخدام الأساليب المناسبة.
1. التكرار عبر جميع الصفحات وإسناد الرأس والتذييل القائمين على الجدول إلى كل صفحة.
1. حفظ الـ[`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) المعدل إلى ملف الإخراج.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def add_header_and_footer_as_table(input_file, output_file):
    """
    Add table-based headers and footers to all pages of a PDF document.

    Creates headers and footers using table structures for better layout
    control and alignment. Demonstrates advanced formatting with text states.

    Args:
        input_file (str): Path to the input PDF file.
        output_file (str): Path where the modified PDF will be saved.

    Returns:
        None: The function modifies the PDF and saves it to the output path.

    Note:
        - Uses Table objects for structured layout
        - Header table has centered Arial 12pt text
        - Footer table has left-aligned Arial 12pt text
        - Column width calculated based on page width minus margins
        - Provides more precise control over text positioning

    Example:
        >>> add_header_and_footer_as_table("input.pdf", "output.pdf")
        # Adds table-structured headers and footers to all pages
    """
    text_state_header = ap.text.TextState()
    text_state_header.font = ap.text.FontRepository.find_font("Arial")
    text_state_header.font_size = 12
    text_state_header.horizontal_alignment = ap.HorizontalAlignment.CENTER
    text_state_footer = ap.text.TextState()
    text_state_footer.font = ap.text.FontRepository.find_font("Arial")
    text_state_footer.font_size = 12
    text_state_footer.horizontal_alignment = ap.HorizontalAlignment.LEFT
    # Create header
    header = ap.HeaderFooter()
    # Create footer
    footer = ap.HeaderFooter()
    # Create header Table
    table_header = ap.Table()
    table_header.column_widths = str(594 - header.margin.left - header.margin.right)
    header_row = table_header.rows.add()
    header_row.cells.add("This is a Table Header", text_state_header)
    # Create footer Table
    table = ap.Table()
    table.column_widths = str(594 - footer.margin.left - footer.margin.right)
    table.rows.add().cells.add("Powered by Aspose.PDF", text_state_footer)
    header.paragraphs.add(table_header)
    footer.paragraphs.add(table)
    # Set footer margin
    footer.margin.left = 150

    # Open PDF document
    with ap.Document(input_file) as document:
        for i in range(1, len(document.pages) + 1):
            # Bind the header and footer to the page
            document.pages[i].header = header
            document.pages[i].footer = footer

        # Save PDF document
        document.save(output_file)
```

## إضافة رؤوس وتذييلات بصيغة LaTeX

أضف رؤوس وتذييلات تحتوي على محتوى مُنسَّق بـ LaTeX إلى جميع صفحات مستند PDF باستخدام Aspose.PDF للبايثون. يتيح LaTeX عرض الرموز الرياضية، والتواريخ، وعلامات حقوق النشر، وغيرها من التنسيقات المتقدمة. يتضمن الرأس تاريخًا ديناميكيًا، بينما يعرض التذييل رمز حقوق النشر إلى جانب رقم الصفحة الحالي وإجمالي عدد الصفحات.

يعرض مقتطف الشيفرة التالي كيفية استخدام [`TeXFragment`](https://reference.aspose.com/pdf/python-net/aspose.pdf/texfragment/) في الرؤوس والتذييلات لملف PDF باستخدام Aspose.PDF للبايثون عبر .NET.

1. فتح الـ[`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) باستخدام الأساليب المناسبة.
1. تحديد إجمالي عدد الصفحات لاستخدامه في التذييلات الديناميكية.
1. التكرار عبر جميع صفحات المستند.
1. إنشاء كائن [`HeaderFooter`](https://reference.aspose.com/pdf/python-net/aspose.pdf/headerfooter/) للرأس.
1. إنشاء [`TeXFragment`](https://reference.aspose.com/pdf/python-net/aspose.pdf/texfragment/) لنص الرأس يحتوي على أوامر LaTeX (مثال: `\\today\\`).
1. إنشاء كائن [`HeaderFooter`](https://reference.aspose.com/pdf/python-net/aspose.pdf/headerfooter/) للتذييل.
1. إنشاء [`TeXFragment`](https://reference.aspose.com/pdf/python-net/aspose.pdf/texfragment/) لنص التذييل يتضمن رموز LaTeX وترقيم الصفحات.
1. إضافة [`TeXFragment`](https://reference.aspose.com/pdf/python-net/aspose.pdf/texfragment/) إلى كائن الرأس/التذييل المقابل.
1. ربط الرأس والتذييل بالصفحة الحالية.
1. حفظ الـ[`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) المعدل إلى ملف الإخراج.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def add_header_and_footer_as_latex(input_file, output_file):
    """
    Add LaTeX-formatted headers and footers to all pages of a PDF document.

    Creates headers and footers using LaTeX markup for mathematical expressions,
    symbols, and advanced formatting. Demonstrates TeXFragment usage.

    Args:
        input_file (str): Path to the input PDF file.
        output_file (str): Path where the modified PDF will be saved.

    Returns:
        None: The function modifies the PDF and saves it to the output path.

    Note:
        - Uses TeXFragment for LaTeX rendering
        - Header includes LaTeX date command (\\today\\)
        - Footer includes copyright symbol and page numbering
        - LaTeX commands are processed and rendered properly
        - Page count is dynamically calculated and inserted

    Example:
        >>> add_header_and_footer_as_latex("input.pdf", "output.pdf")
        # Adds LaTeX-formatted headers and footers with symbols and page numbers
    """
    # Open PDF document
    with ap.Document(input_file) as document:
        page_count = len(document.pages)
        for i in range(1, page_count + 1):
            # Create header
            header = ap.HeaderFooter()
            h_latex_text = "This is a LaTex Header. \\today\\"
            h_l_text = ap.TeXFragment(h_latex_text, True)
            # Create footer
            footer = ap.HeaderFooter()
            f_latex_text = f"\\copyright\\ 2025 My Company -- Page \\thepage\\ is {page_count}"
            f_l_text = ap.TeXFragment(f_latex_text, True)

            header.paragraphs.add(h_l_text)
            footer.paragraphs.add(f_l_text)
            # Bind the header and footer to the page
            document.pages[i].header = header
            document.pages[i].footer = footer

        # Save PDF document
        document.save(output_file)
```
