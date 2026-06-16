---
title: معالجة مستندات PDF في بايثون
linktitle: معالجة مستند PDF
type: docs
weight: 20
url: /ar/python-net/manipulate-pdf-document/
description: تعرف على كيفية التحقق من مستندات PDF وتنظيمها وتعديلها في Python، بما في ذلك إدارة TOC وفحوصات PDF/A.
lastmod: "2026-06-11"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: دليل حول معالجة مستندات PDF باستخدام Python
Abstract: توفر هذه المقالة دليلًا شاملاً حول معالجة مستندات PDF باستخدام Python، وتحديدًا مع مكتبة Aspose.PDF. ويغطي العديد من الوظائف، بما في ذلك التحقق من صحة مستندات PDF لتوافق PDF/A-1a و PDF/A-1b باستخدام طريقة «التحقق من الصحة» لفئة «المستند». كما يوضح بالتفصيل كيفية إضافة جدول المحتويات (TOC) وتخصيصه وإدارته في ملفات PDF، مثل إعداد TabLeaderTypes المختلفة وإخفاء أرقام الصفحات وتخصيص ترقيم الصفحات باستخدام بادئة. بالإضافة إلى ذلك، توضح المقالة كيفية تعيين تاريخ انتهاء صلاحية لمستند PDF من خلال تضمين JavaScript لتقييد الوصول وكيفية تسوية النماذج القابلة للتعبئة في PDF لجعلها غير قابلة للتحرير. يرافق كل قسم مقتطفات التعليمات البرمجية التي توضح تنفيذ هذه الميزات باستخدام Aspose.PDF في Python.
---

هذه الصفحة مفيدة عندما تحتاج إلى التحقق من توافق PDF، أو إنشاء جدول محتويات أو تخصيصه، أو تعيين سلوك انتهاء صلاحية المستند، أو تسوية ملفات PDF القابلة للتعبئة في عمليات سير عمل Python.

## معالجة وثيقة PDF في بايثون

## التحقق من صحة وثيقة PDF لمعيار PDF A (A 1A و A 1B)

للتحقق من صحة وثيقة PDF لتوافق PDF/A-1a أو PDF/A-1b، استخدم [مستند](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) صنف [التحقق من صحة](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) طريقة. تسمح لك هذه الطريقة بتحديد اسم الملف الذي سيتم حفظ النتيجة فيه ونوع التحقق المطلوب (تعداد PDF_Format: PDF_A_1A أو PDF_A_1B).

يوضح لك مقتطف الشفرة التالي كيفية التحقق من صحة مستند PDF لـ PDF/A-1A.

```python
import sys
from os import path
import aspose.pdf as ap


def validate_pdfa_standard_a1a(input_pdf, output_pdf):
    document = ap.Document(input_pdf)
    document.validate(output_pdf, ap.PdfFormat.PDF_A_1A)
```

يوضح لك مقتطف الشفرة التالي كيفية التحقق من صحة مستند PDF لـ PDF/a-1b.

```python
import sys
from os import path
import aspose.pdf as ap


def validate_pdfa_standard_a1b(input_pdf, output_pdf):
    document = ap.Document(input_pdf)
    document.validate(output_pdf, ap.PdfFormat.PDF_A_1B)
```

## العمل مع TOC

### إضافة جدول المحتويات إلى ملف PDF الحالي

يرمز TOC في PDF إلى «جدول المحتويات». إنها ميزة تتيح للمستخدمين التنقل بسرعة عبر المستند من خلال تقديم نظرة عامة على أقسامه وعناوينه. 

لإضافة جدول المحتويات إلى ملف PDF موجود، استخدم فئة العنوان في [aspose.pdf](https://reference.aspose.com/pdf/python-net/aspose.pdf/) مساحة الاسم. ال [aspose.pdf](https://reference.aspose.com/pdf/python-net/aspose.pdf/) يمكن لمساحة الاسم إنشاء ملفات PDF جديدة ومعالجتها. لإضافة جدول المحتويات إلى PDF موجود، استخدم مساحة الاسم Aspose.Pdf. يوضح مقتطف الشفرة التالي كيفية إنشاء جدول محتويات داخل ملف PDF موجود باستخدام Python عبر .NET.

```python
import sys
from os import path
import aspose.pdf as ap


def add_table_of_contents(input_pdf, output_pdf):
    document = ap.Document(input_pdf)
    toc_page = document.pages.insert(1)
    toc_info = ap.TocInfo()
    title = ap.text.TextFragment("Table Of Contents")
    title.text_state.font_size = 20
    title.text_state.font_style = ap.text.FontStyles.BOLD
    toc_info.title = title
    toc_page.toc_info = toc_info

    titles = ["First page", "Second page"]
    for index, title_text in enumerate(titles[:2]):
        heading = ap.Heading(1)
        segment = ap.text.TextSegment(title_text)
        heading.toc_page = toc_page
        heading.segments.append(segment)
        destination_page = document.pages[index + 2]
        heading.destination_page = destination_page
        heading.top = destination_page.rect.height
        toc_page.paragraphs.add(heading)

    document.save(output_pdf)
```

### قم بتعيين TabLeaderType مختلفة لمستويات جدول المحتويات المختلفة

يسمح Aspose.PDF لبيثون أيضًا بتعيين TabLeaderType مختلفة لمستويات جدول المحتويات المختلفة. تحتاج إلى ضبط [لين_داش](https://reference.aspose.com/pdf/python-net/aspose.pdf/tocinfo/#properties) ملكية لـ [معلومات مركز التنسيق](https://reference.aspose.com/pdf/python-net/aspose.pdf/tocinfo/).

```python
import sys
from os import path
import aspose.pdf as ap


def set_toc_levels(input_pdf, output_pdf):
    document = ap.Document(input_pdf)
    toc_page = document.pages.add()
    toc_info = ap.TocInfo()
    toc_info.line_dash = ap.text.TabLeaderType.SOLID
    title = ap.text.TextFragment("Table Of Contents")
    title.text_state.font_size = 30
    toc_info.title = title
    toc_page.toc_info = toc_info

    toc_info.format_array_length = 4
    toc_info.format_array[0].margin.left = 0
    toc_info.format_array[0].margin.right = 30
    toc_info.format_array[0].line_dash = ap.text.TabLeaderType.DOT
    toc_info.format_array[0].text_state.font_style = (
        ap.text.FontStyles.BOLD | ap.text.FontStyles.ITALIC
    )
    toc_info.format_array[1].margin.left = 10
    toc_info.format_array[1].margin.right = 30
    toc_info.format_array[1].line_dash = 3
    toc_info.format_array[1].text_state.font_size = 10
    toc_info.format_array[2].margin.left = 20
    toc_info.format_array[2].margin.right = 30
    toc_info.format_array[2].text_state.font_style = ap.text.FontStyles.BOLD
    toc_info.format_array[3].line_dash = ap.text.TabLeaderType.SOLID
    toc_info.format_array[3].margin.left = 30
    toc_info.format_array[3].margin.right = 30
    toc_info.format_array[3].text_state.font_style = ap.text.FontStyles.BOLD

    page = document.pages.add()
    for level in range(1, 5):
        heading = ap.Heading(level)
        heading.is_auto_sequence = True
        heading.toc_page = toc_page
        heading.text_state.font = ap.text.FontRepository.find_font("Arial")
        segment = ap.text.TextSegment(f"Sample Heading{level}")
        heading.segments.append(segment)
        heading.is_in_list = True
        page.paragraphs.add(heading)

    document.save(output_pdf)
```

### إخفاء أرقام الصفحات في TOC

في حالة عدم رغبتك في عرض أرقام الصفحات، إلى جانب العناوين في جدول المحتويات، يمكنك استخدام [هو _عرض_أرقام_الصفحات_](https://reference.aspose.com/pdf/python-net/aspose.pdf/tocinfo/#properties) ملكية لـ [معلومات مركز التنسيق](https://reference.aspose.com/pdf/python-net/aspose.pdf/tocinfo/) صنف على أنه خطأ. يرجى التحقق من مقتطف الشفرة التالي لإخفاء أرقام الصفحات في جدول المحتويات:

```python
import sys
from os import path
import aspose.pdf as ap


def hide_page_numbers_in_toc(input_pdf, output_pdf):
    document = ap.Document(input_pdf)
    toc_page = document.pages.add()
    toc_info = ap.TocInfo()
    title = ap.text.TextFragment("Table Of Contents")
    title.text_state.font_size = 20
    title.text_state.font_style = ap.text.FontStyles.BOLD
    toc_info.title = title
    toc_info.is_show_page_numbers = False
    toc_page.toc_info = toc_info

    toc_info.format_array_length = 4
    toc_info.format_array[0].margin.right = 0
    toc_info.format_array[0].text_state.font_style = (
        ap.text.FontStyles.BOLD | ap.text.FontStyles.ITALIC
    )
    toc_info.format_array[1].margin.left = 30
    toc_info.format_array[1].text_state.underline = True
    toc_info.format_array[1].text_state.font_size = 10
    toc_info.format_array[2].text_state.font_style = ap.text.FontStyles.BOLD
    toc_info.format_array[3].text_state.font_style = ap.text.FontStyles.BOLD

    page = document.pages.add()
    for level in range(1, 2):
        heading = ap.Heading(level)
        heading.toc_page = toc_page
        heading.is_auto_sequence = True
        heading.is_in_list = True
        segment = ap.text.TextSegment(f"this is heading of level {level}")
        heading.segments.append(segment)
        page.paragraphs.add(heading)

    document.save(output_pdf)
```

### تخصيص أرقام الصفحات أثناء إضافة TOC

من الشائع تخصيص ترقيم الصفحات في جدول المحتويات أثناء إضافة جدول المحتويات في مستند PDF. على سبيل المثال، قد نحتاج إلى إضافة بعض البادئات قبل رقم الصفحة مثل P1 و P2 و P3 وما إلى ذلك. في مثل هذه الحالة، يوفر Aspose.PDF لبيثون [بادئة أرقام الصفحات](https://reference.aspose.com/pdf/python-net/aspose.pdf/tocinfo/#properties) ملكية لـ [معلومات مركز التنسيق](https://reference.aspose.com/pdf/python-net/aspose.pdf/tocinfo/) فئة يمكن استخدامها لتخصيص أرقام الصفحات كما هو موضح في نموذج التعليمات البرمجية التالي.

```python
import sys
from os import path
import aspose.pdf as ap


def customize_page_numbers_in_toc(input_pdf, output_pdf):
    document = ap.Document(input_pdf)
    toc_page = document.pages.insert(1)
    toc_info = ap.TocInfo()
    title = ap.text.TextFragment("Table Of Contents")
    title.text_state.font_size = 20
    title.text_state.font_style = ap.text.FontStyles.BOLD
    toc_info.title = title
    toc_info.page_numbers_prefix = "P"
    toc_page.toc_info = toc_info

    for index, page in enumerate(document.pages, start=1):
        heading = ap.Heading(1)
        heading.toc_page = toc_page
        heading.destination_page = page
        heading.top = page.rect.height
        segment = ap.text.TextSegment(f"Page {index}")
        heading.segments.append(segment)
        toc_page.paragraphs.add(heading)

    document.save(output_pdf)
```

## كيفية تعيين تاريخ انتهاء صلاحية PDF

نحن نطبق امتيازات الوصول على ملفات PDF حتى تتمكن مجموعة معينة من المستخدمين من الوصول إلى ميزات/كائنات معينة من مستندات PDF. من أجل تقييد الوصول إلى ملف PDF، نقوم عادةً بتطبيق التشفير وقد يكون لدينا شرط لتعيين انتهاء صلاحية ملف PDF، بحيث يحصل المستخدم الذي يصل إلى/يعرض المستند على مطالبة صالحة بشأن انتهاء صلاحية ملف PDF.

```python
import sys
from os import path
import aspose.pdf as ap


def set_pdf_expiry_date(input_pdf, output_pdf):
    document = ap.Document(input_pdf)
    document.pages.add()
    document.pages[1].paragraphs.add(ap.text.TextFragment("Hello World..."))
    script = ap.annotations.JavascriptAction(
        "var year=2017;"
        "var month=5;"
        "today = new Date(); today = new Date(today.getFullYear(), today.getMonth());"
        "expiry = new Date(year, month);"
        "if (today.getTime() > expiry.getTime())"
        "app.alert('The file is expired. You need a new one.');"
    )
    document.open_action = script
    document.save(output_pdf)
```

## تسطيح ملف PDF قابل للتعبئة في بايثون

غالبًا ما تتضمن مستندات PDF نماذج ذات عناصر واجهة مستخدم تفاعلية قابلة للتعبئة مثل أزرار الاختيار ومربعات الاختيار ومربعات النص والقوائم وما إلى ذلك لجعلها غير قابلة للتحرير لأغراض التطبيق المختلفة، نحتاج إلى تسوية ملف PDF.
يوفر Aspose.PDF وظيفة تسوية ملف PDF الخاص بك في Python باستخدام بضعة أسطر من التعليمات البرمجية:

```python
import sys
from os import path
import aspose.pdf as ap


def flatten_fillable_pdf(input_pdf, output_pdf):
    document = ap.Document(input_pdf)
    if document.form and document.form.fields:
        for field in document.form.fields:
            field.flatten()
    document.save(output_pdf)
```

## موضوعات المستندات ذات الصلة

- [العمل مع مستندات PDF في بايثون](/pdf/ar/python-net/working-with-documents/)
- [تنسيق مستندات PDF في بايثون](/pdf/ar/python-net/formatting-pdf-document/)
- [إنشاء ملفات PDF في بايثون](/pdf/ar/python-net/create-pdf-document/)
- [تحسين ملفات PDF في بايثون](/pdf/ar/python-net/optimize-pdf/)
