---
title: دمج ملفات PDF في بايثون
linktitle: دمج ملفات PDF
type: docs
weight: 50
url: /ar/python-net/merge-pdf-documents/
description: تعرف على كيفية دمج ملفات PDF متعددة في مستند واحد في Python.
lastmod: "2026-06-11"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: ادمج صفحات PDF باستخدام Python
Abstract: تتناول هذه المقالة الحاجة الشائعة لدمج ملفات PDF متعددة في مستند واحد، وهي عملية ذات قيمة لتنظيم وتحسين تخزين ومشاركة محتوى PDF. يستكشف استخدام Aspose.PDF لـ Python عبر .NET لدمج ملفات PDF بكفاءة، مع الاعتراف بأن دمج ملفات PDF في Python يمكن أن يكون تحديًا بدون مكتبات الطرف الثالث. توفر المقالة دليلًا تفصيليًا لتسلسل ملفات PDF - إنشاء مستند جديد ودمج الملفات وحفظ المستند المدمج. يوضح مقتطف الشفرة التنفيذ باستخدام Aspose.PDF، ويسلط الضوء على قدرة المكتبة على تبسيط عملية الدمج. بالإضافة إلى ذلك، فإنه يقدم Aspose.PDF Merger، وهي أداة عبر الإنترنت لدمج ملفات PDF، مما يتيح للمستخدمين استكشاف الوظائف في بيئة قائمة على الويب.
---

## دمج أو دمج ملفات PDF متعددة في ملف PDF واحد في Python

يعد دمج ملفات PDF استعلامًا شائعًا جدًا بين المستخدمين. يمكن أن يكون هذا مفيدًا عندما يكون لديك العديد من ملفات PDF التي تريد مشاركتها أو تخزينها معًا كمستند واحد.

يمكن أن يساعدك دمج ملفات PDF في تنظيم مستنداتك وإفساح المجال للتخزين على جهاز الكمبيوتر الخاص بك ومشاركة العديد من ملفات PDF مع الآخرين من خلال دمجها في مستند واحد.

إن دمج PDF في Python عبر .NET ليس بالمهمة السهلة دون استخدام مكتبة طرف ثالث.
توضح هذه المقالة كيفية دمج ملفات PDF متعددة في مستند PDF واحد باستخدام Aspose.PDF لـ Python عبر .NET. 

## دمج ملفات PDF باستخدام بايثون وDOM

لربط ملفين من ملفات PDF:

1. قم بإنشاء مستند جديد.
1. دمج ملفات PDF
1. احفظ المستند المدمج

دمج مستندات PDF متعددة في ملف واحد:

```python
import sys
import aspose.pdf as ap
from os import path


def merge_two_documents(infile1, infile2, outfile):
    document1 = ap.Document(infile1)
    document2 = ap.Document(infile2)
    document1.pages.add(document2.pages)
    document1.save(outfile)
```

## إلحاق نطاق صفحات من ملف PDF إلى آخر

انسخ وألحق نطاقًا محددًا من الصفحات من مستند PDF المصدر إلى مستند PDF الوجهة باستخدام Aspose.PDF لـ Python.

1. افتح ملفات PDF باستخدام فئة المستند.
1. تحقق مما إذا كان المستند المصدر يحتوي على صفحات.
1. تحقق من نطاق الصفحات.
1. تخطي العملية إذا كانت صفحة البداية أكبر من صفحة النهاية.
1. قم بالتكرار من خلال نطاق الصفحات.
1. قم بإلحاق صفحات بالمستند الوجهة.

```python
import sys
import aspose.pdf as ap
from os import path


def _append_page_range(source_document, destination_document, start_page, end_page):
    total_pages = len(source_document.pages)
    if total_pages == 0:
        return

    start = max(1, start_page)
    end = min(end_page, total_pages)
    if start > end:
        return

    for page_number in range(start, end + 1):
        destination_document.pages.add(source_document.pages[page_number])
```

## دمج مستندات PDF متعددة في مستند واحد

يشرح مقتطف الشفرة هذا كيفية دمج ملفات PDF متعددة في مستند واحد:

1. قم بإنشاء مستند إخراج فارغ.
1. قم بالتكرار من خلال ملفات الإدخال.
1. قم بتحميل كل مستند مصدر.
1. حدد نطاق الصفحات.
1. قم بإلحاق صفحات بمستند الإخراج.
1. كرر ذلك لجميع المستندات.
1. احفظ ملف PDF المدمج.

```python
import sys
import aspose.pdf as ap
from os import path


def merge_multiple_documents(input_files, outfile):
    output_document = ap.Document()

    for input_file in input_files:
        source_document = ap.Document(input_file)
        _append_page_range(
            source_document, output_document, 1, len(source_document.pages)
        )

    output_document.save(outfile)
```

## دمج نطاقات الصفحات المحددة من ملفات PDF متعددة

1. قم بتحميل مستندات PDF المصدر.
1. قم بإنشاء مستند إخراج.
1. حدد نطاقات الصفحات لكل مستند.
1. قم بإلحاق صفحات من المستند الأول.
1. قم بإلحاق صفحات من المستند الثاني.
1. ادمج الصفحات بالترتيب المطلوب.
1. احفظ ملف PDF المدمج.

```python
import sys
import aspose.pdf as ap
from os import path


def merge_selected_page_ranges(infile1, infile2, outfile):
    document1 = ap.Document(infile1)
    document2 = ap.Document(infile2)
    output_document = ap.Document()

    _append_page_range(document1, output_document, 1, 2)
    _append_page_range(document2, output_document, 2, 3)

    output_document.save(outfile)
```

## إدراج ملف PDF واحد في آخر في موضع محدد

1. قم بتحميل القاعدة وإدراج المستندات.
1. قم بإنشاء مستند إخراج.
1. حدد إجمالي الصفحات في المستند الأساسي.
1. تحقق من صحة فهرس الإدراج.
1. قم بإلحاق الصفحات قبل نقطة الإدراج.
1. قم بإلحاق جميع الصفحات من مستند الإدراج.
1. قم بإلحاق الصفحات المتبقية من المستند الأساسي.
1. احفظ ملف PDF الناتج.

```python
import sys
import aspose.pdf as ap
from os import path


def merge_insert_document_at_position(infile1, infile2, insert_after_page, outfile):
    base_document = ap.Document(infile1)
    insert_document = ap.Document(infile2)
    output_document = ap.Document()

    base_total_pages = len(base_document.pages)
    insert_index = max(0, min(insert_after_page, base_total_pages))

    _append_page_range(base_document, output_document, 1, insert_index)
    _append_page_range(insert_document, output_document, 1, len(insert_document.pages))
    _append_page_range(
        base_document, output_document, insert_index + 1, base_total_pages
    )

    output_document.save(outfile)
```

## دمج ملفات PDF عن طريق الصفحات البديلة

يوضح هذا المثال كيفية دمج مستندين PDF عن طريق تبديل صفحاتهما باستخدام Aspose.PDF لـ Python.

1. قم بتحميل مستندات PDF المدخلة.
1. قم بإنشاء مستند إخراج.
1. احصل على عدد الصفحات في كل مستند.
1. احسب الحد الأقصى لعدد الصفحات.
1. قم بالتكرار من خلال أرقام الصفحات.
1. قم بإلحاق الصفحات بالتناوب.
1. تعامل مع عدد الصفحات غير المتكافئ.
1. احفظ ملف PDF المدمج.

```python
import sys
import aspose.pdf as ap
from os import path


def merge_alternating_pages(infile1, infile2, outfile):
    document1 = ap.Document(infile1)
    document2 = ap.Document(infile2)
    output_document = ap.Document()

    document1_pages = len(document1.pages)
    document2_pages = len(document2.pages)
    max_pages = max(document1_pages, document2_pages)

    for page_number in range(1, max_pages + 1):
        if page_number <= document1_pages:
            output_document.pages.add(document1.pages[page_number])
        if page_number <= document2_pages:
            output_document.pages.add(document2.pages[page_number])

    output_document.save(outfile)
```

## دمج ملفات PDF مع فواصل الأقسام والإشارات المرجعية

قم بدمج مستندات PDF متعددة في ملف واحد مع أقسام منظمة وإشارات مرجعية للتنقل باستخدام Aspose.PDF لـ Python.

1. قم بإنشاء مستند إخراج.
1. قم بالتكرار من خلال ملفات الإدخال.
1. قم بتحميل المستند المصدر.
1. أضف صفحة فاصلة.
1. قم بإنشاء إشارة مرجعية للقسم.
1. قم بإلحاق صفحات المستند المصدر.
1. تتبع صفحة المحتوى الأولى.
1. إضافة إشارة مرجعية للمحتوى المتداخل (اختياري).
1. كرر ذلك لجميع المستندات.
1. احفظ ملف PDF المدمج.

```python
import sys
import aspose.pdf as ap
from os import path


def merge_with_section_separators_and_bookmarks(input_files, outfile):
    output_document = ap.Document()

    for section_index, input_file in enumerate(input_files, start=1):
        source_document = ap.Document(input_file)
        source_page_count = len(source_document.pages)

        separator_page = output_document.pages.add()
        separator_page.paragraphs.add(
            ap.text.TextFragment(
                f"Section {section_index}: {path.basename(input_file)}"
            )
        )

        section_bookmark = ap.OutlineItemCollection(output_document.outlines)
        section_bookmark.title = f"Section {section_index}"
        section_bookmark.action = ap.annotations.GoToAction(separator_page)
        output_document.outlines.append(section_bookmark)

        first_content_page_number = len(output_document.pages) + 1
        _append_page_range(source_document, output_document, 1, source_page_count)

        if source_page_count > 0 and first_content_page_number <= len(
            output_document.pages
        ):
            content_bookmark = ap.OutlineItemCollection(output_document.outlines)
            content_bookmark.title = f"Section {section_index} Content"
            content_bookmark.action = ap.annotations.GoToAction(
                output_document.pages[first_content_page_number]
            )
            section_bookmark.append(content_bookmark)

    output_document.save(outfile)
```

## مثال مباشر

[عملية دمج Aspose.PDF](https://products.aspose.app/pdf/merger) هو تطبيق ويب مجاني عبر الإنترنت يسمح لك بالتحقيق في كيفية عمل وظيفة دمج العروض التقديمية.

[![عملية دمج Aspose.PDF](merger.png)](https://products.aspose.app/pdf/merger)

## موضوعات المستندات ذات الصلة

- [العمل مع مستندات PDF في بايثون](/pdf/ar/python-net/working-with-documents/)
- [تقسيم ملفات PDF في بايثون](/pdf/ar/python-net/split-document/)
- [تحسين ملفات PDF في بايثون](/pdf/ar/python-net/optimize-pdf/)
- [معالجة مستندات PDF في Python](/pdf/ar/python-net/manipulate-pdf-document/)

