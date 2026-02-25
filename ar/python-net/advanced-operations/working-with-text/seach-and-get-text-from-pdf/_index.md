---
title: البحث والحصول على النص من صفحات PDF
linktitle: البحث والحصول على النص
type: docs
weight: 60
url: /ar/python-net/search-and-get-text-from-pdf/
description: تعرف على كيفية البحث واستخراج النص من مستندات PDF في بايثون باستخدام Aspose.PDF لتحليل المستندات.
lastmod: "2025-11-13"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: كيفية البحث والحصول على النص من صفحات PDF
Abstract: توفر المقالة استكشافًا متعمقًا لإمكانيات استخراج النص ومعالجته ضمن مستندات PDF باستخدام مكتبة Aspose.PDF للبايثون عبر .NET. تقدم فئة TextFragmentAbsorber التي تسمح للمطورين بالبحث في المستند بأكمله أو في صفحات محددة عن عبارات معينة أو أنماط تعبيرات نمطية. تشرح الصفحة سيناريوهات عملية متنوعة—مثل استرجاع محتوى النص، تحديد موقعه (بما في ذلك الإحداثيات وقيم الإزاحة)، واستخراج خصائص الخط مثل الاسم والحجم وحالة التضمين واللون—من مقاطع النص المطابقة. تُظهر أمثلة الشيفرة المفصلة العملية خطوة بخطوة، مما يسهل على المطورين دمج قدرات البحث عن النص في تطبيقاتهم.
---

## البحث عن النص في PDF

ابحث واستخرج النص من مساحة مستطيلة محددة في مستند PDF باستخدام فئة TextAbsorber. تستخدم وضع تنسيق النص النقي للحصول على إخراج نص نظيف وغير منسق، مما يجعله مثاليًا لاستخراج المحتوى من مناطق منظمة مثل الترويسات، التذييلات، أو مناطق الجداول. من خلال دمج TextExtractionOptions و TextSearchOptions مع قيود مستطيلة، يقدم هذا المثال تحكمًا دقيقًا في مكان وكيفية استخراج النص من المستند.

1. تحميل ملف PDF باستخدام 'ap.Document'.
1. تكوين خيارات استخراج النص.
1. تحديد مساحة البحث باستخدام قيود مستطيلة.
1. إنشاء وتكوين TextAbsorber.
1. معالجة جميع الصفحات في المستند.
1. استرجاع وعرض النص المستخرج.

```python

import io
import os
import re
import shutil
import aspose.pdf as ap
import aspose.pydrawing as drawing

# Global configuration
DATA_DIR = "your path here"

def text_absorber_search(input_file_path):
    """
    Search and extract text from PDF using TextAbsorber with area constraints.

    Demonstrates basic text extraction from a PDF document using TextAbsorber
    with pure text formatting mode and rectangular boundary constraints.
    Extracts text from all pages within the specified rectangular area.

    Args:
        input_file_path (str): Path to the input PDF file to search.

    Returns:
        None: Prints extracted text to console.

    Note:
        - Uses PURE text formatting mode for clean text extraction
        - Constrains search to rectangle (0, 0, 842, 250)
        - Processes all pages in the document
        - TextAbsorber provides high-level text extraction capabilities
        - Good for extracting text content without detailed positioning

    Example:
        >>> text_absorber_search("document.pdf")
        # Prints all text found in the specified rectangular area across all pages
    """
    # Open PDF document
    document = ap.Document(input_file_path)

    text_extraction_options = ap.text.TextExtractionOptions(
        ap.text.TextExtractionOptions.TextFormattingMode.PURE
    )
    text_search_options = ap.text.TextSearchOptions(ap.Rectangle(0, 0, 842, 250, True))

    absorber = ap.text.TextAbsorber(text_extraction_options, text_search_options)

    # Process all pages
    document.pages.accept(absorber)

    print(f"Text fragments found: {absorber.text}")
```

## البحث عن النص من صفحة PDF محددة

ابحث واستخرج النص من صفحة ومنطقة محددة في PDF باستخدام TextAbsorber من Aspose.PDF. يستهدف الصفحة 2 من المستند ويستخرج فقط النص الموجود داخل مساحة مستطيلة معرفة.
من خلال دمج TextExtractionOptions (للتحكم في التنسيق) و TextSearchOptions (لتحديد المنطقة)، يمكنك إجراء استخراج نص دقيق ومحدد للصفحة بكفاءة.

1. تحميل مستند PDF.
1. إعداد خيارات استخراج النص.
1. تقييد استخراج النص إلى مساحة مستطيلة محددة على الصفحة.
1. إنشاء وتكوين TextAbsorber.
1. معالجة صفحة محددة.
1. استرجاع وعرض النص المستخرج.

```python

import io
import os
import re
import shutil
import aspose.pdf as ap
import aspose.pydrawing as drawing

# Global configuration
DATA_DIR = "your path here"

def text_absorber_search_page(input_file_path):
    """
    Search and extract text from a specific PDF page using TextAbsorber.

    Demonstrates targeted text extraction from a single page (page 2) using
    TextAbsorber with area constraints. Shows how to limit search scope to
    specific pages and rectangular regions.

    Args:
        input_file_path (str): Path to the input PDF file to search.

    Returns:
        None: Prints extracted text from page 2 to console.

    Note:
        - Targets only page 2 of the document (document.pages[2])
        - Uses PURE text formatting mode for clean extraction
        - Constrains search to rectangle (0, 0, 842, 250)
        - Useful for page-specific text extraction
        - More efficient than processing entire document when targeting specific pages

    Example:
        >>> text_absorber_search_page("document.pdf")
        # Prints text found in the specified area on page 2 only
    """
    document = ap.Document(input_file_path)

    text_extraction_options = ap.text.TextExtractionOptions(
        ap.text.TextExtractionOptions.TextFormattingMode.PURE
    )
    text_search_options = ap.text.TextSearchOptions(ap.Rectangle(0, 0, 842, 250, True))

    absorber = ap.text.TextAbsorber(text_extraction_options, text_search_options)

    # Only page 2
    document.pages[2].accept(absorber)

    print(f"Text fragments found: {absorber.text}")

```

## تحليل واستخراج خصائص مفصلة لمقاطع النص من PDF

على عكس TextAbsorber الذي يستخرج النص الخام، يقدم TextFragmentAbsorber معلومات مفصلة ومنخفضة المستوى حول كل مقطع نصي — مثل موقعه، وسمات الخط، واللون، وتفاصيل التضمين.

1. تحميل مستند PDF.
1. تهيئة TextFragmentAbsorber.
1. معالجة جميع الصفحات في المستند.
1. التجاوز عبر مقاطع النص المستخرجة.
1. طباعة معلومات النص الأساسية.
1. طباعة تفاصيل الخط والتنسيق.

```python

import io
import os
import re
import shutil
import aspose.pdf as ap
import aspose.pydrawing as drawing

# Global configuration
DATA_DIR = "your path here"

def text_fragment_absorber_search(input_file_path):
    """
    Search and analyze all text fragments in a PDF with detailed properties.

    Demonstrates comprehensive text fragment analysis using TextFragmentAbsorber
    to extract all text with detailed positioning, font, and formatting information.
    Provides low-level access to text properties for detailed analysis.

    Args:
        input_file_path (str): Path to the input PDF file to analyze.

    Returns:
        None: Prints detailed text fragment information to console.

    Note:
        - Extracts all text fragments from all pages
        - Provides detailed properties: position, font info, colors, sizes
        - Shows font accessibility, embedding, and subset information
        - Useful for detailed text analysis and formatting inspection
        - TextFragmentAbsorber offers more granular control than TextAbsorber

    Example:
        >>> text_fragment_absorber_search("document.pdf")
        # Prints comprehensive details about every text fragment in the document
    """
    document = ap.Document(input_file_path)

    absorber = ap.text.TextFragmentAbsorber()
    document.pages.accept(absorber)

    for fragment in absorber.text_fragments:
        print("Text:", fragment.text)
        print("Position:", fragment.position)
        print("XIndent:", fragment.position.x_indent)
        print("YIndent:", fragment.position.y_indent)
        print("Font - Name:", fragment.text_state.font.font_name)
        print("Font - IsAccessible:", fragment.text_state.font.is_accessible)
        print("Font - IsEmbedded:", fragment.text_state.font.is_embedded)
        print("Font - IsSubset:", fragment.text_state.font.is_subset)
        print("Font Size:", fragment.text_state.font_size)
        print("Foreground Color:", fragment.text_state.foreground_color)
```

## البحث عن عبارة نصية محددة في صفحة PDF واحدة

ابحث عن عبارة نصية محددة داخل صفحة من مستند PDF باستخدام TextFragmentAbsorber. على عكس البحث في المستند بأكمله، يقتصر هذا الأسلوب على صفحة واحدة فقط، مما يجعله أكثر كفاءة لتأكيد وجود النص وموقعه في مناطق مستهدفة مثل الترويسات، التذييلات، أو أقسام المحتوى المحددة.

1. تحميل مستند PDF.
1. تهيئة TextFragmentAbsorber مع عبارة البحث.
1. تطبيق Absorber على صفحة محددة.
1. التجاوز على المقاطع المكتشفة.

```python

import io
import os
import re
import shutil
import aspose.pdf as ap
import aspose.pydrawing as drawing

# Global configuration
DATA_DIR = "your path here"

def text_fragment_absorber_search_page(input_file_path):
    """
    Search for specific text phrase on a particular PDF page.

    Demonstrates targeted text search for a specific phrase ("whale") on
    a single page. Shows how to combine phrase searching with page-specific
    scope for efficient and focused text location.

    Args:
        input_file_path (str): Path to the input PDF file to search.

    Returns:
        None: Prints matching text fragments and their positions to console.

    Note:
        - Searches for the phrase "whale" on page 2 only
        - Returns text fragments with position information
        - More efficient than document-wide search when targeting specific pages
        - Useful for validating content presence in specific document sections
        - Provides exact positioning coordinates for found text

    Example:
        >>> text_fragment_absorber_search_page("document.pdf")
        # Prints all instances of "whale" found on page 2 with their positions
    """
    document = ap.Document(input_file_path)

    absorber = ap.text.TextFragmentAbsorber("whale")
    document.pages[2].accept(absorber)

    for fragment in absorber.text_fragments:
        print("Text:", fragment.text)
        print("Position:", fragment.position)
```

## بحث نصي متسلسل صفحة بصفحة مع نتائج تراكمية

ابحث عن النص بشكل تدريجي عبر صفحات متعددة من مستند PDF باستخدام TextFragmentAbsorber من Aspose.PDF.
على عكس البحث في صفحة واحدة أو في كامل المستند، يتيح لك هذا الأسلوب معالجة الصفحات بشكل متسلسل، جمع النتائج تدريجيًا، وتحليل مقاطع النص بسياق مخصص لكل صفحة. هذه الطريقة مثالية للمستندات الكبيرة أو سير عمل المعالجة المتقدمة.

1. تحميل مستند PDF.
1. تهيئة TextFragmentAbsorber وتعيين عبارة البحث.
1. معالجة الصفحة الأولى. البحث فقط في الصفحة 1. طباعة النص، رقم الصفحة، والموقع. توفير نتائج معزولة مخصصة للصفحة لتوضيح أفضل.
1. معالجة الصفحة التالية تسلسليًا. الانتقال إلى الصفحة 2 ومتابعة باقي المستند اختياريًا. يضمن 'absorber.visit()' تجميع النتائج من جميع الصفحات التي تمت زيارتها. يطبع نتائج البحث التراكمية، مع عرض النص والموقع.

```python

import io
import os
import re
import shutil
import aspose.pdf as ap
import aspose.pydrawing as drawing

# Global configuration
DATA_DIR = "your path here"

def text_fragment_absorber_sequential_search(input_file_path):
    """
    Demonstrate sequential page-by-page text search with cumulative results.

    Shows how to perform incremental text searches across multiple pages,
    accumulating results from each page. Demonstrates both individual page
    processing and document-wide search continuation.

    Args:
        input_file_path (str): Path to the input PDF file to search.

    Returns:
        None: Prints text fragments from sequential page searches to console.

    Note:
        - Searches for "whale" on page 1, then continues to page 2
        - Uses absorber.visit(document) to process remaining pages
        - Demonstrates incremental search accumulation
        - Shows page numbers for found fragments
        - Useful for progressive document processing and result accumulation

    Example:
        >>> text_fragment_absorber_sequential_search("document.pdf")
        # Prints "whale" instances from page 1, then from all remaining pages
    """
    document = ap.Document(input_file_path)

    absorber = ap.text.TextFragmentAbsorber()
    absorber.phrase = "whale"

    # First page
    document.pages[1].accept(absorber)
    for fragment in absorber.text_fragments:
        print("Text:", fragment.text)
        print("Page:", fragment.page.number)
        print("Position:", fragment.position)

    print("--")

    # Continue to next page
    document.pages[2].accept(absorber)
    absorber.visit(document)

    for fragment in absorber.text_fragments:
        print("Text:", fragment.text)
        print("Page:", fragment.page.number)
        print("Position:", fragment.position)
```

## البحث المستهدف عن عبارة داخل منطقة مستطيلة

ابحث عن عبارة محددة داخل ملف PDF مع قصر البحث على منطقة مستطيلة محددة في صفحة واحدة.
من خلال دمج البحث عن العبارة مع القيود المكانية، يمكنك تحديد المحتوى بدقة في المناطق المخصصة دون مسح الصفحة أو المستند بالكامل. وهذا مفيد بشكل خاص للنماذج، الرؤوس، التذييلات، أو التقارير المهيكلة حيث يظهر المحتوى في مواقع متوقعة.

1. تحميل مستند PDF.
1. تهيئة TextFragmentAbsorber بالعبارة والقيود المستطيلة
1. تطبيق Absorber على الصفحة 2. يحد من المعالجة إلى الصفحة 2، مما يقلل من الحساب غير الضروري. يضمن أن يكون البحث مخصصًا للصفحة.
1. التجول عبر القطع المكتشفة وطبعها

```python

import io
import os
import re
import shutil
import aspose.pdf as ap
import aspose.pydrawing as drawing

# Global configuration
DATA_DIR = "your path here"

def text_fragment_absorber_search_phrase(input_file_path):
    """
    Search for specific phrase within a rectangular area constraint.

    Demonstrates targeted phrase searching with both text matching and
    spatial constraints. Combines phrase search with rectangular boundary
    limitations for precise content location.

    Args:
        input_file_path (str): Path to the input PDF file to search.

    Returns:
        None: Prints matching text fragments and positions to console.

    Note:
        - Searches for "elephant" phrase on page 2
        - Constrains search to rectangle (0, 0, 842, 250)
        - Combines text matching with spatial filtering
        - Useful for finding content in specific document regions
        - More precise than page-wide or document-wide searches

    Example:
        >>> text_fragment_absorber_search_phrase("document.pdf")
        # Prints "elephant" instances found within the specified rectangular area on page 2
    """
    document = ap.Document(input_file_path)

    absorber = ap.text.TextFragmentAbsorber(
        "elephant", ap.text.TextSearchOptions(ap.Rectangle(0, 0, 842, 250, True))
    )

    document.pages[2].accept(absorber)

    for fragment in absorber.text_fragments:
        print("Text:", fragment.text)
        print("Position:", fragment.position)
```

## البحث عن أنماط النص في PDF باستخدام التعبيرات النمطية

ابحث عن أنماط النص في ملف PDF باستخدام التعبيرات النمطية. من خلال تمكين وضع regex في TextFragmentAbsorber، يمكنك تحديد أنماط معقدة مثل الأرقام، التواريخ، الأسعار، الإحداثيات، أو تنسيقات النص المخصصة. تقتصر الدالة على صفحة محددة، مما يجعلها فعّالة لاستخراج البيانات المهيكلة المستهدفة.

1. تحميل مستند PDF.
1. تهيئة TextFragmentAbsorber بنمط regex.
1. تطبيق Absorber على الصفحة 2. يحد من البحث إلى الصفحة 2 للكفاءة والدقة. يتم تحليل النص على هذه الصفحة فقط.
1. التجول عبر القطع المكتشفة. يطبع قطع النص المطابقة وإحداثياتها. يوفر معلومات موقع دقيقة للأنماط المستخرجة.

```python

import io
import os
import re
import shutil
import aspose.pdf as ap
import aspose.pydrawing as drawing

# Global configuration
DATA_DIR = "your path here"

def text_fragment_absorber_search_regex(input_file_path):
    """
    Search for text patterns using regular expressions.

    Demonstrates advanced text searching using regular expression patterns
    to find complex text structures like numbers, dates, or custom formats.
    Shows how to enable regex mode in TextFragmentAbsorber.

    Args:
        input_file_path (str): Path to the input PDF file to search.

    Returns:
        None: Prints matching text fragments and positions to console.

    Note:
        - Uses regex pattern r"\\d+\\.\\d+" to find decimal numbers
        - Enables regex mode with is_regular_expression_used=True
        - Searches on page 2 only
        - Powerful for finding formatted data like prices, coordinates, dates
        - Regular expressions provide flexible pattern matching capabilities

    Example:
        >>> text_fragment_absorber_search_regex("document.pdf")
        # Prints all decimal numbers (e.g., "12.34", "0.99") found on page 2
    """
    document = ap.Document(input_file_path)

    absorber = ap.text.TextFragmentAbsorber(r"\d+\.\d+", ap.text.TextSearchOptions(is_regular_expression_used=True))

    document.pages[2].accept(absorber)

    for fragment in absorber.text_fragments:
        print("Text:", fragment.text)
        print("Position:", fragment.position)
```

## تحويل تطابقات النص إلى روابط تشعبية في PDF باستخدام TextFragmentAbsorber

ابحث عن عبارات نصية محددة في PDF وحولها إلى روابط تشعبية قابلة للنقر. باستخدام TextFragmentAbsorber مع أنماط regex، يتم تحديد الكلمات المستهدفة وتطبيق تنسيق مرئي (لون وتسطير) مع روابط تفاعلية.

1. تحميل مستند PDF.
1. تهيئة TextFragmentAbsorber بنمط regex.
1. تطبيق Absorber على الصفحة 1.
1. تنسيق وإضافة روابط تشعبية للمطابقات.
1. حفظ ملف PDF المعدل.

```python

import io
import os
import re
import shutil
import aspose.pdf as ap
import aspose.pydrawing as drawing

# Global configuration
DATA_DIR = "your path here"

def text_fragment_absorber_search_and_add_hyperlink(input_file_path):
    """
    Search for text and convert matches to hyperlinks with styling.

    Demonstrates advanced text processing by finding specific words and
    converting them into clickable hyperlinks with visual styling. Shows
    how to combine text search with document modification.

    Args:
        input_file_path (str): Path to the input PDF file to process.

    Returns:
        None: Saves modified PDF with hyperlinks to output file.

    Note:
        - Searches for "whale|elephant" using regex pattern on page 1
        - Converts found text to Wikipedia hyperlinks
        - Applies blue color and underline styling to hyperlinks
        - Creates new output file with "_out.pdf" suffix
        - Demonstrates practical text enhancement and interactivity
        - Combines search, styling, and hyperlinking in one operation

    Example:
        >>> text_fragment_absorber_search_and_add_hyperlink("document_in.pdf")
        # Creates "document_out.pdf" with "whale" and "elephant" as clickable Wikipedia links
    """
    document = ap.Document(input_file_path)

    absorber = ap.text.TextFragmentAbsorber("whale|elephant")
    absorber.text_search_options = ap.text.TextSearchOptions(True)

    absorber.visit(document.pages[1])

    for fragment in absorber.text_fragments:
        fragment.text_state.foreground_color = ap.Color.blue
        fragment.text_state.underline = True
        fragment.hyperlink = ap.WebHyperlink(
            f"https://en.wikipedia.org/wiki/{fragment.text}"
        )

    output = input_file_path.replace("in.pdf", "out.pdf")
    document.save(output)
```

## البحث وتحديد النص المنسق في PDF باستخدام TextFragmentAbsorber

ابحث عن قطع النص في PDF بناءً على خصائص تنسيقها بدلاً من محتواها. باستخدام TextFragmentAbsorber، يتم تحديد النص ذو الأنماط المحددة، مثل النص الغامق.

1. تحميل مستند PDF.
1. تهيئة TextFragmentAbsorber.
1. تطبيق Absorber على الصفحة 1.
1. فحص قطع النص بناءً على التنسيق. يتحقق من نمط الخط لتحديد التنسيق الغامق.

```python

import io
import os
import re
import shutil
import aspose.pdf as ap
import aspose.pydrawing as drawing

# Global configuration
DATA_DIR = "your path here"

def text_fragment_absorber_search_styled_text(input_file_path):
    """
    Search and identify text based on formatting properties.

    Demonstrates how to find text fragments based on their formatting
    characteristics rather than content. Shows detection of bold text
    and invisible text within the document.

    Args:
        input_file_path (str): Path to the input PDF file to analyze.

    Returns:
        None: Prints formatted text findings to console.

    Note:
        - Searches all text fragments on page 1
        - Identifies text with FontStyles.BOLD formatting
        - Detects invisible/hidden text using text_state.invisible
        - Useful for formatting analysis and hidden content detection
        - Demonstrates text property-based filtering capabilities

    Example:
        >>> text_fragment_absorber_search_styled_text("document.pdf")
        # Prints all bold text and any hidden/invisible text found on page 1
    """
    document = ap.Document(input_file_path)

    absorber = ap.text.TextFragmentAbsorber()
    absorber.text_search_options = ap.text.TextSearchOptions(True)

    absorber.visit(document.pages[1])

    for fragment in absorber.text_fragments:
        if fragment.text_state.font_style == ap.text.FontStyles.BOLD:
            print(f"Bold: {fragment.text}")
```

يكشف النص المخفي أو غير المرئي في مستند PDF عن طريق تحليل خصائص تنسيق النص:

1. تحميل مستند PDF.
1. تهيئة TextFragmentAbsorber.
1. تطبيق Absorber على الصفحة 1.
1. فحص قطع النص بناءً على التنسيق. تحقق من 'fragment.text_state.invisible' للكشف عن النص المخفي.

```python

import io
import os
import re
import shutil
import aspose.pdf as ap
import aspose.pydrawing as drawing

# Global configuration
DATA_DIR = "your path here"

def text_fragment_absorber_search_styled_text(input_file_path):
    """
    Search and identify text based on formatting properties.

    Demonstrates how to find text fragments based on their formatting
    characteristics rather than content. Shows detection of bold text
    and invisible text within the document.

    Args:
        input_file_path (str): Path to the input PDF file to analyze.

    Returns:
        None: Prints formatted text findings to console.

    Note:
        - Searches all text fragments on page 1
        - Identifies text with FontStyles.BOLD formatting
        - Detects invisible/hidden text using text_state.invisible
        - Useful for formatting analysis and hidden content detection
        - Demonstrates text property-based filtering capabilities

    Example:
        >>> text_fragment_absorber_search_styled_text("document.pdf")
        # Prints all bold text and any hidden/invisible text found on page 1
    """
    document = ap.Document(input_file_path)

    absorber = ap.text.TextFragmentAbsorber()
    absorber.text_search_options = ap.text.TextSearchOptions(True)

    absorber.visit(document.pages[1])

    for fragment in absorber.text_fragments:
        if fragment.text_state.invisible:
            print(f"Invisible: {fragment.text}")
```

## تظليل النص بصريًا في صفحات PDF

تجمع هذه الدالة بين التعرف على النص والتصوير في سير عمل واحد. لا تقتصر على استخراج النص فقط، بل تُظهره أيضًا بتظليل القطع، المقاطع، والحروف في مستطيلات ملونة على صور PNG لكل صفحة.

مثالنا ينفّذ تصورًا متقدمًا للنص على PDF عن طريق:

- البحث عن جميع قطع النص المرئية باستخدام التعبيرات النمطية
- تحويل كل صفحة PDF إلى صورة PNG عالية الدقة
- رسم مستطيلات ملونة حول قطع النص، المقاطع النصية، والحروف الفردية

1. تعيين دقة صورة الإخراج. تُحوَّل كل صفحة PDF إلى صورة PNG بدقة 150 DPI.
1. فتح ملف PDF وتهيئة Text Absorber.
1. معالجة كل صفحة. تطبيق الـ absorber على كل صفحة. جمع جميع قطع النص المكتشفة ومواقعها الهندسية.
1. تحويل الصفحة إلى تدفق PNG.
1. إعداد كائن الرسوميات للرسم.
1. تطبيق تحويل الإحداثيات. تحويل إحداثيات PDF إلى بكسل الصورة.
1. رسم مستطيلات لعناصر النص.
1. حفظ النتيجة.

```python

import io
import os
import re
import shutil
import aspose.pdf as ap
import aspose.pydrawing as drawing

# Global configuration
DATA_DIR = "your path here"

def text_fragment_absorber_search_and_highlight(infile):
    """
    Search text and create visual highlighting with PNG output.

    Advanced function that combines text search with visual highlighting.
    Converts PDF pages to PNG images and draws colored rectangles around
    found text fragments, segments, and individual characters.

    Args:
        infile (str): Path to the input PDF file to process.

    Returns:
        None: Saves highlighted PNG images for each page.

    Note:
        - Uses regex pattern r"[\\S]+" to find all non-whitespace sequences
        - Converts each page to 150 DPI PNG image using PngDevice
        - Draws yellow rectangles around text fragments
        - Draws green rectangles around text segments
        - Draws black rectangles around individual characters
        - Creates detailed visual analysis of text structure
        - Output files named with page numbers: "filename1_out.png", etc.
        - Complex coordinate transformation for proper overlay positioning

    Example:
        >>> text_fragment_absorber_search_and_highlight("document_in.pdf")
        # Creates PNG files with visual highlighting of all text elements
    """
    resolution = 150
    png_device = ap.devices.PngDevice(ap.devices.Resolution(resolution, resolution))

    # Open PDF document
    document = ap.Document(infile)
    absorber = ap.text.TextFragmentAbsorber(r"[\S]+")
    absorber.text_search_options.is_regular_expression_used = True

    for page in document.pages:
        page.accept(absorber)
        stream = io.BytesIO()
        png_device.process(page, stream)
        with drawing.Bitmap.from_stream(stream) as bmp:
            with drawing.Graphics.from_image(bmp) as gr:
                scale = resolution / 72
                gr.transform = drawing.drawing2d.Matrix(
                    float(scale),
                    float(0),
                    float(0),
                    float(-scale),
                    float(0),
                    float(bmp.height),
                )
                text_fragment_collection = absorber.text_fragments
                # Loop through the fragments
                for text_fragment in text_fragment_collection:
                    gr.draw_rectangle(
                        drawing.Pens.yellow,
                        float(text_fragment.position.x_indent),
                        float(text_fragment.position.y_indent),
                        float(text_fragment.rectangle.width),
                        float(text_fragment.rectangle.height),
                    )
                    for seg_num in range(1, len(text_fragment.segments) + 1):
                        segment = text_fragment.segments[seg_num]
                        for char_num in range(1, len(segment.characters) + 1):
                            character_info = segment.characters[char_num]
                            rect = page.get_page_rect(True)
                            print(
                                f"TextFragment = {text_fragment.text}"
                                + f" Page URY = {rect.ury}"
                                + f" TextFragment URY = {text_fragment.rectangle.ury}"
                            )
                            gr.draw_rectangle(
                                drawing.Pens.black,
                                float(character_info.rectangle.llx),
                                float(character_info.rectangle.lly),
                                float(character_info.rectangle.width),
                                float(character_info.rectangle.height),
                            )
                        gr.draw_rectangle(
                            drawing.Pens.green,
                            float(segment.rectangle.llx),
                            float(segment.rectangle.lly),
                            float(segment.rectangle.width),
                            float(segment.rectangle.height),
                        )

                # Save result
                bmp.save(
                    infile.replace("_in.pdf", str(page.number) + "_out.png"),
                    drawing.imaging.ImageFormat.png,
                )
```
