---
title: استبدال النص في PDF عبر بايثون
linktitle: استبدال النص في PDF
type: docs
weight: 40
url: /ar/python-net/replace-text-in-pdf/
description: تعرف على المزيد حول الطرق المختلفة لاستبدال وإزالة النص من مكتبة Aspose.PDF for Python عبر .NET.
lastmod: "2025-10-13"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
aliases: 
    - /python-net/replace-text-in-a-pdf-document/
TechArticle: true
AlternativeHeadline: كيفية استبدال النص في PDF باستخدام بايثون
Abstract: توفر المقالة دليلًا شاملاً حول تقنيات مختلفة للتلاعب بالنص داخل مستندات PDF باستخدام Aspose.PDF for Python عبر .NET. تغطي عدة استراتيجيات لاستبدال النص، بما في ذلك استبدال النص عبر جميع الصفحات، داخل مناطق محددة من الصفحة، واستخدام التعابير النمطية. كما تشرح المقالة كيفية استبدال الخطوط داخل ملفات PDF، مع التأكد من إزالة الخطوط غير المستخدمة، وكيفية إدارة استبدال النص لإعادة ترتيب محتوى الصفحة تلقائيًا. بالإضافة إلى ذلك، تتعمق في عملية عرض الرموز القابلة للاستبدال أثناء إنشاء PDF، بما في ذلك استخدامها في مناطق الرأس/التذييل، لتعزيز تخصيص المستند. أخيرًا، توضح طرق إزالة جميع النصوص من مستند PDF، مما يحسن العمليات في السيناريوهات التي يتطلب فيها حذف النص بالكامل. يتم تدعيم كل قسم مع مقتطفات شفرة بلغة بايثون وغيرها من اللغات المدعومة لتوضيح التطبيق العملي.
---

تُظهر هذه الأمثلة كيفية **تعديل أو إزالة النص في ملف PDF موجود**.

## استبدال النص الموجود

### استبدال النص في جميع صفحات مستند PDF

{{% alert color="primary" %}}

يمكنك تجربة البحث عن النص واستبداله في المستند باستخدام Aspose.PDF والحصول على النتائج عبر الإنترنت على هذا [الرابط](https://products.aspose.app/pdf/redaction)

{{% /alert %}}

استبدال النص هو مطلب شائع عند تحديث أو تصحيح المحتوى في مستندات PDF القائمة — على سبيل المثال، تغيير أسماء المنتجات، تصحيح الأخطاء المطبعية، أو تحديث المصطلحات عبر صفحات متعددة.

تقدم Aspose.PDF for Python عبر .NET طريقة قوية وفعّالة للبحث واستبدال النص برمجيًا من خلال الفئة [TextFragmentAbsorber](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragmentabsorber/).

يوضح هذا المثال كيفية العثور على جميع تكرارات عبارة محددة (في هذه الحالة، "Black cat") واستبدالها بعبارة جديدة ("White dog") في مستند PDF بأكمله.

1. حدد عبارات البحث والاستبدال. اضبط النص الذي تريد العثور عليه والنص الذي تريد استبداله به.
1. تحميل مستند PDF.
1. إنشاء أداة امتصاص النص. يتم تهيئة TextFragmentAbsorber بعبارة البحث. يقوم بمسح المستند للعثور على جميع تكرارات العبارة المحددة.
1. تطبيق أداة الامتصاص على جميع الصفحات. تقوم هذه العملية بالتكرار عبر جميع الصفحات وتجمع شظايا النص المتطابقة مع العبارة.
1. استبدال كل شظية تم العثور عليها. يجب تغيير كل تكرار لـ "Black cat" إلى "White dog".
1. حفظ PDF المحدث.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def replace_text_on_all_pages(infile, outfile):
    """
    Replace text on all pages of a PDF document.

    Searches for a specific text phrase throughout all pages of a PDF document
    and replaces all occurrences with a new phrase. This function demonstrates
    global text replacement using TextFragmentAbsorber.

    Args:
        infile (str): Path to the input PDF file to process.
        outfile (str): Path where the modified PDF will be saved.

    Returns:
        None: The function modifies the PDF and saves it to the output path.

    Note:
        - Replaces "Black cat" with "White dog" as demonstration
        - Searches across all pages in the document
        - Preserves original formatting and layout
        - Uses TextFragmentAbsorber for efficient text search

    Example:
        >>> replace_text_on_all_pages("input.pdf", "output.pdf")
        # Replaces all instances of "Black cat" with "White dog"
    """
    search_phrase = "Black cat"
    replace_phrase = "White dog"

    with ap.Document(infile) as document:
        absorber = ap.text.TextFragmentAbsorber(search_phrase)
        document.pages.accept(absorber)

        for fragment in absorber.text_fragments:
            fragment.text = replace_phrase

        document.save(outfile)
```

### استبدال النص في منطقة صفحة معينة

أحيانًا قد تحتاج إلى استبدال النص فقط ضمن منطقة محددة من صفحة PDF بدلاً من البحث في المستند بأكمله — على سبيل المثال، تحديث عنوان أو تذييل أو خلية جدول في موضع معروف.

تمكن مكتبة Aspose.PDF for Python عبر .NET هذه الوظيفة من خلال استخدام [TextFragmentAbsorber](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragmentabsorber/) بالتعاون مع البحث النصي القائم على المنطقة.

يوضح هذا المثال كيفية العثور على جميع تكرارات عبارة مستهدفة واستبدالها داخل منطقة مستطيلة محددة في صفحة معينة.

1. حدد عبارات البحث والاستبدال.
1. تحميل مستند PDF.
1. إنشاء أداة امتصاص النص للبحث. تهيئة TextFragmentAbsorber للعثور على النص المطلوب.
1. تقييد منطقة البحث. يحدد المستطيل حدود إحداثيات x و y على الصفحة.
1. تطبيق أداة الامتصاص على صفحة محددة. تقوم هذه العملية بإجراء البحث وجمع شظايا النص المتطابقة ضمن المنطقة المحددة.
1. استبدال النص المكتشف. كل تكرار لـ 'doc' في المنطقة المحددة يصبح 'DOC'.
1. حفظ PDF المحدث.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def replace_text_in_particular_page_region(infile, outfile):
    """
    Replace text in a particular region of a page.

    Performs targeted text replacement within a specific rectangular region
    on the first page of a PDF document. This allows for precise control
    over which text gets replaced based on its location.

    Args:
        infile (str): Path to the input PDF file to process.
        outfile (str): Path where the modified PDF will be saved.

    Returns:
        None: The function modifies the PDF and saves it to the output path.

    Note:
        - Replaces "doc" with "DOC" within the specified region
        - Only affects text within coordinates (300, 442, 500, 742)
        - Uses limit_to_page_bounds for precise region control
        - Only processes the first page (pages[1])

    Example:
        >>> replace_text_in_particular_page_region("input.pdf", "output.pdf")
        # Replaces "doc" with "DOC" only in the specified rectangular area
    """
    search_phrase = "doc"
    replace_phrase = "DOC"

    with ap.Document(infile) as document:
        absorber = ap.text.TextFragmentAbsorber(search_phrase)
        absorber.text_search_options.limit_to_page_bounds = True
        absorber.text_search_options.rectangle = ap.Rectangle(300, 442, 500, 742, True)
        document.pages[1].accept(absorber)

        for fragment in absorber.text_fragments:
            fragment.text = replace_phrase

        document.save(outfile)
```

### تغيير حجم النص وتحريكه دون تغيير حجم الخط

عند استبدال النص في PDF، قد ترغب أحيانًا في ملاءمة أو إعادة وضع النص الجديد داخل منطقة محددة دون تعديل حجم الخط.
توفر Aspose.PDF for Python عبر .NET خيارات لضبط تخطيط النص والمسافات مع الحفاظ على حجم الخط الأصلي دون تغيير.

1. تحميل مستند PDF.
1. جمع جميع شظايا النص على الصفحة باستخدام 'TextFragmentAbsorber'.
1. تحديد الشظية المراد تعديلها.
1. تحريك وتغيير حجم مستطيل النص.
1. ضبط تباعد النص. تمكين تعديل التباعد لتناسب النص داخل المستطيل المعدل.
1. استبدال نص الشظية.
1. حفظ PDF المحدث.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def replace_text_and_resize_and_shift_without_changing_font_size(infile, outfile):
    """
    Resize and shift text without changing the font size.

    Demonstrates how to replace text content while adjusting its position
    and width within a modified rectangular area. The font size remains
    unchanged, but spacing is adjusted to fit the new content.

    Args:
        infile (str): Path to the input PDF file to process.
        outfile (str): Path where the modified PDF will be saved.

    Returns:
        None: The function modifies the PDF and saves it to the output path.

    Note:
        - Targets the second text fragment on the first page
        - Narrows the text rectangle by 50 units on each side
        - Duplicates the original text content
        - Uses ADJUST_SPACE_WIDTH for proper spacing
        - Maintains original font size and style

    Example:
        >>> replace_text_and_resize_and_shift_without_changing_font_size("input.pdf", "output.pdf")
        # Duplicates text in a narrower space with adjusted spacing
    """
    with ap.Document(infile) as document:
        absorber = ap.text.TextFragmentAbsorber()
        absorber.visit(document.pages[1])
        fragment = absorber.text_fragments[1]
        text = fragment.text
        rect = fragment.rectangle
        rect.llx += 50
        rect.urx -= 50
        fragment.replace_options.rectangle = rect
        fragment.replace_options.replace_adjustment_action = (
             ap.text.TextReplaceOptions.ReplaceAdjustment.ADJUST_SPACE_WIDTH
        )
        fragment.text = f"{text} {text}"
        document.save(outfile)
```

### تغيير حجم الفقرة وتحريكها في PDF

عند العمل مع ملفات PDF، قد تحتاج أحيانًا إلى استبدال فقرة أو توسيعها مع الحفاظ على محاذاتها البصرية مع تخطيط الصفحة. يتيح لك Aspose.PDF تغيير حجم المستطيل المحدد للفقرة وضبط التباعد لتناسب النص الجديد، كل ذلك دون تغيير حجم الخط.

1. تحميل مستند PDF.
1. استخدم 'TextFragmentAbsorber' لجمع جميع أجزاء النص في الصفحة.
1. اختر الجزء المراد تعديله.
1. غير حجم الفقرة وحركها. استخدم مربع وسائط الصفحة لتحديد الحدود وتعديل المستطيل.
1. ضبط التباعد. هذا يعدل التباعد بين الكلمات/الحروف بدلاً من تغيير حجم الخط.
1. استبدال نص الجزء.
1. حفظ ملف PDF المعدل.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def replace_text_and_resize_and_shift_paragraph(infile, outfile):
    """
    Resize and shift a paragraph in the document.

    Demonstrates paragraph-level text replacement with automatic resizing
    to fit within the page's media box boundaries. Adjusts the text area
    to provide margins while duplicating content.

    Args:
        infile (str): Path to the input PDF file to process.
        outfile (str): Path where the modified PDF will be saved.

    Returns:
        None: The function modifies the PDF and saves it to the output path.

    Note:
        - Uses page media box as base rectangle
        - Adds 20-unit margins on left, right, and top
        - Targets the second text fragment on the first page
        - Duplicates original text content
        - Automatically adjusts space width for proper fit

    Example:
        >>> replace_text_and_resize_and_shift_paragraph("input.pdf", "output.pdf")
        # Resizes paragraph to fit within page margins with duplicated text
    """
    with ap.Document(infile) as document:
        absorber = ap.text.TextFragmentAbsorber()
        absorber.visit(document.pages[1])
        fragment = absorber.text_fragments[1]
        text = fragment.text
        rect = document.pages[1].media_box
        rect.llx += 20
        rect.urx -= 20
        rect.ury -= 20
        fragment.replace_options.rectangle = rect
        fragment.replace_options.replace_adjustment_action = (
             ap.text.TextReplaceOptions.ReplaceAdjustment.ADJUST_SPACE_WIDTH
        )
        fragment.text = f"{text} {text}"
        document.save(outfile)
```

### استبدال النص وتوسيع الخط تلقائيًا لملء المنطقة المستهدفة

استبدال النص في ملف PDF مع تغيير حجم الخط وتوسيعها تلقائيًا لملء مساحة مستطيلة محددة. باستخدام مكتبة Aspose.PDF للـ Python عبر .NET، يقوم الكود بتعديل حجم الخط والتباعد ديناميكيًا بحيث يتناسب المحتوى النصي الجديد تمامًا داخل الصندوق المحدد — دون الحاجة إلى حسابات يدوية لحجم الخط.

1. تحميل ملف PDF.
1. التقاط أجزاء النص.
1. اختيار جزء معين.
1. تحديد المستطيل المستهدف.
1. تمكين خيارات تعديل النص.
1. استبدال النص.
1. حفظ المستند.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def replace_text_and_resize_and_expand_font(infile, outfile):
    """
    Resize and expand font to fill target area.

    Demonstrates automatic font scaling to fill a specified rectangular area.
    The font size is dynamically adjusted to make the text content fit
    perfectly within the defined target rectangle.

    Args:
        infile (str): Path to the input PDF file to process.
        outfile (str): Path where the modified PDF will be saved.

    Returns:
        None: The function modifies the PDF and saves it to the output path.

    Note:
        - Defines target rectangle at coordinates (100, 300, 512, 692)
        - Uses SCALE_TO_FILL for automatic font size adjustment
        - Duplicates original text content
        - Adjusts space width for optimal text distribution
        - Font size scales up or down to fill the entire rectangle

    Example:
        >>> replace_text_and_resize_and_expand_font("input.pdf", "output.pdf")
        # Scales font to completely fill the specified rectangular area
    """
    with ap.Document(infile) as document:
        absorber = ap.text.TextFragmentAbsorber()
        absorber.visit(document.pages[1])
        fragment = absorber.text_fragments[1]
        text = fragment.text
        fragment.replace_options.rectangle = ap.Rectangle(100, 300, 512, 692, True)
        fragment.replace_options.replace_adjustment_action = (
             ap.text.TextReplaceOptions.ReplaceAdjustment.ADJUST_SPACE_WIDTH
        )
        fragment.replace_options.font_size_adjustment_action = (
            ap.text.TextReplaceOptions.FontSizeAdjustment.SCALE_TO_FILL
        )
        fragment.text = f"{text} {text}"
        document.save(outfile)

```

### استبدال النص وتكييفه داخل مستطيل

استبدال النص في مستند PDF مع ضمان أن المحتوى الجديد يتناسب داخل مساحة النص الأصلية المستطيلة عن طريق تقليل حجم الخط تلقائيًا عند الحاجة.

باستخدام مكتبة Aspose.PDF للـ Python عبر .NET، تقوم هذه الدالة بتعديل كل من تخطيط النص وحجم الخط بشكل ديناميكي، مع الحفاظ على بنية الوثيقة ومنع الفائض.

1. إنشاء كائن TextFragmentAbsorber لاستخراج جميع أجزاء النص من الصفحة الأولى.
1. الوصول إلى جزء نص معين.
1. تحديد منطقة الاستبدال.
1. تكوين خيارات تعديل النص. اضبط خيارين رئيسيين للاستبدال:
- تعديل حجم الخط - 'SHRINK_TO_FIT' يقلل حجم الخط تلقائيًا إذا был النص الجديد طويلًا جدًا.
- تعديل التباعد - 'ADJUST_SPACE_WIDTH' يحافظ على التباعد بشكل متناسب.
1. استبدال النص.
1. حفظ ملف PDF المعدل.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def replace_text_and_fit_text_into_rectangle(infile, outfile):
    """
    Fit text into a rectangle by adjusting font size.

    Demonstrates how to ensure text content fits within its original
    rectangle by automatically shrinking the font size when the new
    content is longer than the original.

    Args:
        infile (str): Path to the input PDF file to process.
        outfile (str): Path where the modified PDF will be saved.

    Returns:
        None: The function modifies the PDF and saves it to the output path.

    Note:
        - Uses original text fragment rectangle as target area
        - Employs SHRINK_TO_FIT to reduce font size if needed
        - Duplicates original text content (making it longer)
        - Adjusts space width for proper text distribution
        - Prevents text overflow by automatic font scaling

    Example:
        >>> replace_text_and_fit_text_into_rectangle("input.pdf", "output.pdf")
        # Shrinks font size to fit doubled text content in original space
    """
    with ap.Document(infile) as document:
        absorber = ap.text.TextFragmentAbsorber()
        absorber.visit(document.pages[1])
        fragment = absorber.text_fragments[1]
        text = fragment.text
        fragment.replace_options.rectangle = fragment.rectangle
        fragment.replace_options.font_size_adjustment_action = (
            ap.text.TextReplaceOptions.FontSizeAdjustment.SHRINK_TO_FIT
        )
        fragment.replace_options.replace_adjustment_action = (
            ap.text.TextReplaceOptions.ReplaceAdjustment.ADJUST_SPACE_WIDTH

        )
        fragment.text = f"{text} {text}"
        document.save(outfile)
```

### استبدال نص العنصر النائب تلقائيًا وإعادة ترتيب تخطيط PDF

استبدال النص النائب داخل ملف PDF (مثل القوالب أو النماذج) ببيانات فعلية مثل الأسماء أو معلومات الشركة.
يقوم تلقائيًا بضبط تخطيط الصفحة لتناسب النص الجديد مع تطبيق تنسيق مخصص (الخط، اللون، الحجم).

1. استيراد وتحميل ملف PDF.
1. إنشاء Text Absorber للعنصر النائب.
1. تطبيق الـ Absorber على جميع الصفحات.
1. التكرار عبر أجزاء النص المكتشفة.
1. تطبيق تنسيق نص مخصص.
1. حفظ المستند المحدث.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def automatically_rearrange_page_contents(input_file, output_file):
    """
    Replace placeholder text in PDF with actual content.

    Demonstrates how to replace long placeholder text with actual content
    and automatically rearrange page layout. Shows dynamic content replacement
    with custom formatting applied to the new text.

    Args:
        input_file (str): Path to the input PDF file containing placeholders.
        output_file (str): Path where the modified PDF will be saved.

    Returns:
        None: The function modifies the PDF and saves it to the output path.

    Note:
        - Searches for "[Long_placeholder_Long_placeholder]" placeholders
        - Replaces with either "John Smith" or extended version with studio info
        - Applies Calibri font, size 12, navy blue color
        - Automatically adjusts page layout to accommodate content changes
        - Demonstrates real-world template filling scenarios

    Example:
        >>> automatically_rearrange_page_contents("template.pdf", "filled.pdf")
        # Replaces placeholders with formatted actual content
    """
    document = ap.Document(input_file)

    absorber = ap.text.TextFragmentAbsorber("[Long_placeholder_Long_placeholder]")
    document.pages.accept(absorber)

    for text_fragment in absorber.text_fragments:
        # text_fragment.text = "John Smith"
        text_fragment.text = "John Smith, South Development Studio"
        text_fragment.text_state.font = ap.text.FontRepository.find_font("Calibri")
        text_fragment.text_state.font_size = 12
        text_fragment.text_state.foreground_color = ap.Color.navy

    # Save PDF document
    document.save(output_file)
```

### استبدال النص بناءً على تعبير نمطي

عند العمل مع مستندات PDF، قد تحتاج إلى استبدال نص يتبع نمطًا معينًا بدلاً من عبارة محددة — مثل أرقام الهواتف، أو الرموز، أو صيغ تشبه التواريخ.

Aspose.PDF للـ Python عبر .NET يتيح لك إجراء هذه الاستبدالات باستخدام التعابير النمطية (regex) مع فئة TextFragmentAbsorber.

يوضح هذا المثال كيفية العثور على أنماط النص (في هذه الحالة، أي نص يطابق الصيغة ####-####، مثل 1234-5678) واستبداله بسلسلة منسقة 'ABC1-2XZY'. كما يوضح كيفية تخصيص الخط واللون والحجم للنص المستبدل.

المقتطف البرمجي التالي يوضح لك كيفية استبدال النص بناءً على تعبير نمطي.

1. تحميل مستند PDF.
1. إنشاء Text Absorber يعتمد على تعبير نمطي. قم بتهيئة TextFragmentAbsorber بنمط تعبير نمطي.
1. تفعيل وضع التعبير النمطي. المعامل 'True' يفعّل وضع البحث بالتعبير النمطي.
1. تطبيق الـ Absorber على صفحة. يقوم هذا بمسح الصفحة للعثور على جميع أجزاء النص التي تطابق نمط الـ regex المحدد.
1. استبدال كل تطابق بنص جديد وتطبيق تنسيق مخصص.
1. حفظ المستند المعدل.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def replace_text_based_on_regex(infile, outfile):
    """
    Replace text based on a regular expression pattern.

    Demonstrates pattern-based text replacement using regular expressions
    to find and replace text that matches specific formats. Also shows
    how to apply formatting changes to the replaced text.

    Args:
        infile (str): Path to the input PDF file to process.
        outfile (str): Path where the modified PDF will be saved.

    Returns:
        None: The function modifies the PDF and saves it to the output path.

    Note:
        - Uses regex pattern r"\\d{4}-\\d{4}" to find 4-digit-4-digit patterns
        - Replaces matched patterns with "ABC1-2XZY"
        - Applies custom formatting: Verdana font, size 12, blue text
        - Sets light green background color for replaced text
        - Enables regex mode with TextSearchOptions(True)

    Example:
        >>> replace_text_based_on_regex("input.pdf", "output.pdf")
        # Replaces patterns like "1234-5678" with formatted "ABC1-2XZY"
    """
    with ap.Document(infile) as document:
        absorber = ap.text.TextFragmentAbsorber(r"\d{4}-\d{4}")
        absorber.text_search_options = ap.text.TextSearchOptions(True)
        document.pages[1].accept(absorber)

        for fragment in absorber.text_fragments:
            fragment.text = "ABC1-2XZY"
            fragment.text_state.font = ap.text.FontRepository.find_font("Verdana")
            fragment.text_state.font_size = 12
            fragment.text_state.foreground_color = ap.Color.blue
            fragment.text_state.background_color = ap.Color.light_green

        document.save(outfile)
```

## استبدال الخطوط أو إزالة الخطوط غير المستخدمة

### استبدال الخطوط في ملف PDF موجود

في بعض الأحيان، تحتاج إلى توحيد أو تحديث الخطوط عبر ملف PDF — على سبيل المثال، استبدال خط قديم أو مملوك بآخر أكثر إمكانية للوصول. تسمح لك مكتبة Aspose.PDF for Python via .NET باكتشاف الخطوط واستبدالها برمجيًا، مما يضمن طباعية متسقة وتوافق المستند.

يوضح هذا المثال كيفية استبدال جميع الحالات لخط محدد (مثل 'Arial-BoldMT') بخط آخر (مثل 'Verdana') في جميع أنحاء مستند PDF.

يُظهر مقتطف الشيفرة التالي كيفية استبدال الخط داخل مستند PDF:

1. افتح مستند PDF.
1. قم بتهيئة كائن TextFragmentAbsorber.
1. استخدم الـ Absorber لاستخراج قطع النص من كل صفحة في المستند.
1. التعرف على الخطوط واستبدالها. يتحقق البرنامج النصي مما إذا كان الخط الحالي للجزء هو 'Arial-BoldMT'. إذا كان كذلك، يستبدله بخط 'Verdana' باستخدام طريقة FontRepository.find_font().
1. احفظ المستند المعدل.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def replace_fonts(infile, outfile):
    """
    Replace specific fonts in a PDF document.

    Demonstrates how to find and replace specific fonts throughout a PDF
    document. Searches for text using a particular font and changes it
    to a different font while preserving the text content.

    Args:
        infile (str): Path to the input PDF file to process.
        outfile (str): Path where the modified PDF will be saved.

    Returns:
        None: The function modifies the PDF and saves it to the output path.

    Note:
        - Searches for text using "Arial-BoldMT" font
        - Replaces font with "Verdana" while keeping text content
        - Processes all text fragments across all pages
        - Maintains original text size and formatting properties
        - Useful for font standardization across documents

    Example:
        >>> replace_fonts("input.pdf", "output.pdf")
        # Changes all Arial-BoldMT text to use Verdana font instead
    """
    with ap.Document(infile) as document:
        absorber = ap.text.TextFragmentAbsorber()
        document.pages.accept(absorber)

        for fragment in absorber.text_fragments:
            if fragment.text_state.font.font_name == "Arial-BoldMT":
                fragment.text_state.font = ap.text.FontRepository.find_font("Verdana")

        document.save(outfile)
```

### إزالة الخطوط غير المستخدمة

مع مرور الوقت، قد تتراكم الخطوط غير المستخدمة أو المدمجة في مستندات PDF مما يزيد من حجم الملف ويبطئ المعالجة. غالبًا ما تظل هذه الخطوط غير المستخدمة موجودة حتى بعد تعديل النص أو استبداله، خاصةً عند العمل مع ملفات PDF الكبيرة أو المعقدة.

توفر مكتبة Aspose.PDF for Python via .NET طريقة فعّالة لإزالة هذه الخطوط الزائدة باستخدام فئة TextEditOptions. هذا لا يحسّن مستندك فحسب، بل يضمن أيضًا أنه يستخدم فقط الخطوط المطبقة فعليًا على النص الظاهر.

طريقة 'remove_unused_fonts()' هي طريقة بسيطة لكنها قوية لتحسين ملفات PDF عن طريق إزالة بيانات الخطوط الزائدة.

يوضح هذا المثال كيفية:

- فحص ملف PDF للخطوط غير المستخدمة.
- إزالة هذه الخطوط بأمان.
- إعادة تعيين قطع النص النشطة إلى خط ثابت (مثل Times New Roman).

1. افتح مستند PDF.
1. تكوين خيارات تحرير النص. هذا يُعطي المحرك تعليمات لإزالة أي خطوط مدمجة غير مستخدمة حاليًا في النص الظاهر.
1. إنشاء Text Absorber مع الخيارات. يقوم TextFragmentAbsorber باستخراج قطع النص من المستند للتحرير.
1. إعادة تعيين خط قياسي. بمجرد أن يجمع الـ absorber جميع القطع، يتم المرور عليها وتطبيق خط ثابت.
1. احفظ ملف PDF المنظف.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def remove_unused_fonts(input_file, output_file):
    """
    Remove unused fonts from a PDF document.

    Optimizes PDF file size by removing fonts that are embedded but not
    actually used in the document. Also demonstrates how to standardize
    all text to use a specific font family.

    Args:
        input_file (str): Path to the input PDF file to optimize.
        output_file (str): Path where the optimized PDF will be saved.

    Returns:
        None: The function modifies the PDF and saves it to the output path.

    Note:
        - Uses REMOVE_UNUSED_FONTS option for optimization
        - Changes all text to use TimesNewRoman font
        - Processes all text fragments across the document
        - Reduces file size by eliminating unnecessary font data
        - Useful for PDF optimization and standardization

    Example:
        >>> remove_unused_fonts("input.pdf", "optimized.pdf")
        # Removes unused fonts and standardizes text to TimesNewRoman
    """

    # Open PDF document
    document = ap.Document(input_file)

    # Initialize text edit options to remove unused fonts
    options = ap.text.TextEditOptions(ap.text.TextEditOptions.FontReplace.REMOVE_UNUSED_FONTS)

    # Create a TextFragmentAbsorber with the specified options
    absorber = ap.text.TextFragmentAbsorber(options)
    document.pages.accept(absorber)

    # Iterate through all TextFragments
    for text_fragment in absorber.text_fragments:
        text_fragment.text_state.font = ap.text.FontRepository.find_font("TimesNewRoman")

    # Save the updated PDF document
    document.save(output_file)
```

## إزالة كل النص

### إزالة النص من PDF

إزالة جميع محتويات النص من ملف PDF مع الحفاظ على الصور والأشكال وهياكل التخطيط دون تغيير.
باستخدام TextFragmentAbsorber، تقوم الشيفرة بمسح المستند بأكمله بكفاءة وتزيل كل قطعة نصية موجودة في كل صفحة.

1. حمّل مستند PDF.
1. يتم إنشاء كائن TextFragmentAbsorber للكشف عن قطع النص ومعالجتها في PDF.
1. إزالة جميع محتويات النص. الطريقة 'absorber.remove_all_text()' تزيل كل عنصر نصي من المستند المحمّل، مع ترك المكونات غير النصية دون تغيير.
1. احفظ المستند المحدث.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def remove_all_text_using_absorber1(infile, outfile):
    """
    Remove all text from a PDF using TextFragmentAbsorber.

    Demonstrates complete text removal from an entire PDF document,
    leaving only non-text elements like images, shapes, and layout
    structures intact.

    Args:
        infile (str): Path to the input PDF file to process.
        outfile (str): Path where the text-free PDF will be saved.

    Returns:
        None: The function modifies the PDF and saves it to the output path.

    Note:
        - Removes all text content from the entire document
        - Preserves images, graphics, and page structure
        - Uses document-level text removal for complete cleanup
        - Useful for creating templates or removing sensitive text
        - Maintains page layout and non-text elements

    Example:
        >>> remove_all_text_using_absorber1("input.pdf", "no_text.pdf")
        # Creates a PDF with all text removed but graphics preserved
    """
    with ap.Document(infile) as document:
        absorber = ap.text.TextFragmentAbsorber()
        absorber.remove_all_text(document)
        document.save(outfile)
```

### إزالة كل النص من صفحة محددة

إزالة كل النص من صفحة واحدة في مستند PDF باستخدام فئة TextFragmentAbsorber في Aspose.PDF.
على عكس إزالة النص من المستند بالكامل، تقوم هذه الطريقة بتنظيف النص على مستوى الصفحة، حيث تحذف النص فقط من الصفحة المختارة مع ترك باقي الصفحات دون تعديل.

1. حمّل ملف PDF.
1. أنشئ مثيلًا من TextFragmentAbsorber.
1. إزالة كل النص من الصفحة الأولى.
1. احفظ ملف PDF المعدل.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def remove_all_text_using_absorber2(infile, outfile):
    """
    Remove all text from page using TextFragmentAbsorber.

    Demonstrates text removal from a specific page while leaving text
    on other pages intact. Useful for selective text cleanup or
    creating mixed-content documents.

    Args:
        infile (str): Path to the input PDF file to process.
        outfile (str): Path where the modified PDF will be saved.

    Returns:
        None: The function modifies the PDF and saves it to the output path.

    Note:
        - Removes text only from the first page (pages[1])
        - Preserves text content on all other pages
        - Maintains page structure and non-text elements
        - Useful for page-specific text removal operations
        - Images and graphics on the target page remain intact

    Example:
        >>> remove_all_text_using_absorber2("input.pdf", "first_page_clean.pdf")
        # Removes all text from first page only
    """
    with ap.Document(infile) as document:
        absorber = ap.text.TextFragmentAbsorber()
        absorber.remove_all_text(document.pages[1])
        document.save(outfile)
```

### إزالة كل النص من منطقة معينة على صفحة PDF

إزالة كل النص من منطقة مستقيمة محددة على صفحة باستخدام TextFragmentAbsorber في Aspose.PDF.
بدلاً من مسح صفحة كاملة، تقوم هذه الطريقة بإزالة النص المستهدف، مما يسمح بالتحكم الدقيق في الجزء المتأثر من الصفحة.

1. حمّل مستند PDF.
1. أنشئ TextFragmentAbsorber.
1. حدد المنطقة المستهدفة (مستطيل).
1. إزالة النص من المنطقة المحددة.
1. احفظ باقي المستند.
1. احفظ ملف PDF المعدل.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def remove_all_text_using_absorber3(infile, outfile):
    """
    Remove all text from particular area on PDF page using TextFragmentAbsorber.

    Demonstrates precise text removal from a specific rectangular region
    on a page. Allows for surgical text removal while preserving text
    outside the target area.

    Args:
        infile (str): Path to the input PDF file to process.
        outfile (str): Path where the modified PDF will be saved.

    Returns:
        None: The function modifies the PDF and saves it to the output path.

    Note:
        - Removes text only within rectangle (10, 200, 120, 600)
        - Targets the first page only (pages[1])
        - Preserves text outside the specified rectangle
        - Maintains all non-text elements in the region
        - Useful for removing watermarks, headers, or specific sections

    Example:
        >>> remove_all_text_using_absorber3("input.pdf", "region_clean.pdf")
        # Removes text only from the specified rectangular area
    """
    with ap.Document(infile) as document:
        absorber = ap.text.TextFragmentAbsorber()
        absorber.remove_all_text(document.pages[1], ap.Rectangle(10, 200, 120, 600))
        document.save(outfile)
```

### إزالة كل النص المخفي من مستند PDF

إزالة كل النص من منطقة مستقيمة محددة على صفحة باستخدام TextFragmentAbsorber في Aspose.PDF.
بدلاً من مسح صفحة كاملة، تقوم هذه الطريقة بإزالة النص المستهدف، مما يسمح بالتحكم الدقيق في الجزء المتأثر من الصفحة.

1. حمّل مستند PDF.
1. إنشاء TextFragmentAbsorber.
1. تعريف المنطقة المستهدفة (المستطيل).
1. إزالة النص من المنطقة المحددة.
1. الحفاظ على باقي المستند.
1. حفظ ملف PDF المعدل.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def remove_hidden_text(infile, outfile):
    """
    Remove all hidden (invisible) text from a PDF document.

    Identifies and removes text that has been marked as invisible while
    preserving all visible text content. Useful for cleaning documents
    that may contain hidden tracking text or metadata.

    Args:
        infile (str): Path to the input PDF file to process.
        outfile (str): Path where the cleaned PDF will be saved.

    Returns:
        None: The function modifies the PDF and saves it to the output path.

    Note:
        - Detects text fragments with invisible text state
        - Replaces hidden text with empty strings
        - Uses NONE replacement adjustment to prevent layout shifts
        - Preserves all visible text and document structure
        - Useful for privacy and security document cleanup

    Example:
        >>> remove_hidden_text("input.pdf", "no_hidden_text.pdf")
        # Removes all invisible text while keeping visible content intact
    """
    # Open PDF document
    with ap.Document(infile) as document:
        text_absorber = ap.text.TextFragmentAbsorber()
        # This option can be used to prevent other text fragments from moving after hidden text replacement
        text_absorber.text_replace_options = ap.text.TextReplaceOptions(ap.text.TextReplaceOptions.ReplaceAdjustment.NONE)
        document.pages.accept(text_absorber)
        # Remove hidden text
        for fragment in text_absorber.text_fragments:
            if fragment.text_state.invisible:
                fragment.text = ""
        # Save PDF document
        document.save(outfile)
```
