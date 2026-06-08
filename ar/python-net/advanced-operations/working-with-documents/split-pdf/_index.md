---
title: تقسيم ملفات PDF في Python
linktitle: تقسيم ملفات PDF
type: docs
weight: 60
url: /ar/python-net/split-pdf-document/
description: تعلم كيفية تقسيم ملفات PDF في بايثون إلى صفحات فردية، أجزاء متساوية، مجموعات بحجم ثابت، نطاقات صفحات مخصصة، والصفحات الفردية أو الزوجية.
lastmod: "2026-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: قسّم ملف PDF إلى صفحات ونطاقات صفحات باستخدام بايثون
Abstract: هذه المقالة توضح كيفية تقسيم ملفات PDF باستخدام Aspose.PDF for Python via .NET. تتناول تقسيم ملف PDF إلى صفحات فردية، جزأين متساويين، مجموعات صفحات ذات حجم ثابت، نطاقات صفحات مخصصة، مجموعات صفحات مسماة، أسماء ملفات ثابتة، وملفات الصفحات الفردية أو الزوجية.
---

تُظهر هذه الصفحة كيفية **تقسيم ملفات PDF في Python** باستخدام Aspose.PDF for Python via .NET.

استخدم هذه الأمثلة عندما تحتاج إلى تقسيم ملف PDF كبير إلى ملفات صفحة واحدة، أو أجزاء متساوية، أو مجموعات بحجم ثابت، أو نطاقات صفحات مخصصة، أو مجموعات الصفحات الفردية والزوجية للتوزيع أو المراجعة أو المعالجة اللاحقة.

## مثال تقسيم PDF عبر الإنترنت

[Aspose.PDF مقسّم](https://products.aspose.app/pdf/splitter) هو تطبيق ويب عبر الإنترنت يتيح لك اختبار وظيفة تقسيم ملفات PDF.

[![Aspose تقسيم PDF](splitter.png)](https://products.aspose.app/pdf/splitter)

لتقسيم صفحات PDF إلى ملفات PDF ذات صفحة واحدة في بايثون، اتبع الخطوات التالية:

1. التكرار عبر صفحات مستند PDF من خلال [مستند](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) الكائن [مجموعة الصفحات](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/) مجموعة
1. في كل تكرار، أنشئ كائن Document جديد وأضف الفرد [صفحة](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) كائن إلى المستند الفارغ
1. احفظ ملف PDF الجديد باستخدام [احفظ()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) طريقة

## تقسيم ملف PDF إلى عدة ملفات في بايثون

يظهر لك المقتطف التالي لشفرة بايثون كيفية تقسيم صفحات PDF إلى ملفات PDF فردية.

```python
import sys
import aspose.pdf as ap
from os import path


def split_documents(infile, outdir):
    document = ap.Document(infile)
    for page_num in range(1, len(document.pages) + 1):
        with ap.Document() as new_document:
            new_document.pages.add(document.pages[page_num])
            new_document.save(path.join(outdir, f"Page_{page_num}.pdf"))
```

## تقسيم PDF إلى جزأين متساويين

1. حمّل مستند PDF.
1. تحديد العدد الإجمالي للصفحات.
1. احسب نقطة المنتصف.
1. إنشاء مستند الإخراج الأول.
1. إزالة الصفحات من النصف الثاني للمستند الأول.
1. احفظ الجزء الأول.
1. إنشاء المستند الثاني الناتج.
1. أزل صفحات النصف الأول من المستند الثاني.
1. احفظ الجزء الثاني.

```python
import sys
import aspose.pdf as ap
from os import path


def split_documents_into_two_parts(infile, outdir):
    document = ap.Document(infile)
    total_pages = len(document.pages)
    mid_point = total_pages // 2

    # First part
    with ap.Document(infile) as first_document:
        first_part_range = range(mid_point + 1, total_pages + 1)
        first_document.pages.delete(first_part_range)
        first_document.save(path.join(outdir, "Part_1.pdf"))

    # Second part
    with ap.Document(infile) as second_document:
        second_part_range = range(1, mid_point + 1)
        second_document.pages.delete(second_part_range)
        second_document.save(path.join(outdir, "Part_2.pdf"))
```

## قسّم ملف PDF إلى ملفات متعددة كل N صفحات

قسم مستند PDF إلى ملفات متعددة أصغر بناءً على عدد ثابت من الصفحات باستخدام Aspose.PDF for Python.

1. حمّل مستند PDF.
1. تحديد العدد الإجمالي للصفحات.
1. حدد الصفحات لكل جزء.
1. التكرار عبر المستند على دفعات.
1. احسب نطاق الصفحات لكل جزء.
1. أنشئ مستندًا جديدًا لكل جزء.
1. انسخ الصفحات إلى المستند الجديد.
1. احفظ المستند المقسم.
1. كرر حتى يتم معالجة جميع الصفحات.

```python
import sys
import aspose.pdf as ap
from os import path


def split_documents_every_n_pages(infile, outdir, pages_per_part=3):
    document = ap.Document(infile)
    total_pages = len(document.pages)

    part_index = 1
    for start_page in range(1, total_pages + 1, pages_per_part):
        end_page = min(start_page + pages_per_part - 1, total_pages)

        with ap.Document() as part_document:
            for page_num in range(start_page, end_page + 1):
                part_document.pages.add(document.pages[page_num])
            part_document.save(
                path.join(outdir, f"Every_{pages_per_part}_Part_{part_index}.pdf")
            )

        part_index += 1
```

## قسّم ملف PDF وفق نطاقات الصفحات المخصصة

قسّم مستند PDF إلى ملفات متعددة بناءً على نطاقات صفحات معرفة مخصصًا باستخدام Aspose.PDF for Python.

1. حمّل مستند PDF.
1. تحديد العدد الإجمالي للصفحات.
1. إنشاء قائمة من الثنائيات تمثل نطاقات (start_page, end_page).
1. التكرار عبر النطاقات المحددة.
1. تحقق من صفحة البداية.
1. ضبط الصفحة النهائية.
1. تحقق من النطاق الفعّال.
1. إنشاء مستند جديد لكل نطاق.
1. انسخ الصفحات إلى المستند الجديد.
1. احفظ كل مستند مقسَّم.

```python
import sys
import aspose.pdf as ap
from os import path


def split_documents_by_page_ranges(infile, outdir):
    document = ap.Document(infile)
    total_pages = len(document.pages)
    # Define ranges as (start_page, end_page). Use None to indicate last page.
    ranges = [(1, 3), (4, 6), (7, None)]

    for index, (start_page, end_page) in enumerate(ranges, start=1):
        if start_page > total_pages:
            continue

        effective_end = total_pages if end_page is None else min(end_page, total_pages)
        if start_page > effective_end:
            continue

        with ap.Document() as range_document:
            for page_num in range(start_page, effective_end + 1):
                range_document.pages.add(document.pages[page_num])
            range_document.save(
                path.join(outdir, f"Range_{index}_{start_page}_to_{effective_end}.pdf")
            )
```

## قسّم PDF إلى الصفحة الأولى والصفحات المتبقية

افصل الصفحة الأولى من مستند PDF عن باقي الصفحات باستخدام Aspose.PDF for Python.

1. حمّل مستند PDF.
1. تحديد العدد الإجمالي للصفحات.
1. تحقق مما إذا كان المستند فارغًا.
1. إنشاء مستند للصفحة الأولى.
1. أضف الصفحة الأولى.
1. احفظ مستند الصفحة الأولى.
1. تحقق مما إذا كانت هناك صفحات إضافية.
1. إنشاء مستند للصفحات المتبقية.
1. نسخ الصفحات المتبقية.
1. احفظ مستند الصفحات المتبقية.

```python
import sys
import aspose.pdf as ap
from os import path


def split_documents_first_page_and_rest(infile, outdir):
    document = ap.Document(infile)
    total_pages = len(document.pages)

    if total_pages == 0:
        return

    with ap.Document() as first_page_document:
        first_page_document.pages.add(document.pages[1])
        first_page_document.save(path.join(outdir, "First_Page.pdf"))

    if total_pages == 1:
        return

    with ap.Document() as remaining_pages_document:
        for page_num in range(2, total_pages + 1):
            remaining_pages_document.pages.add(document.pages[page_num])
        remaining_pages_document.save(path.join(outdir, "Remaining_Pages.pdf"))
```

## قسّم ملف PDF إلى الصفحة الأخيرة والصفحات السابقة

استخرج الصفحة الأخيرة من مستند PDF وافصلها عن الصفحات المتبقية باستخدام Aspose.PDF for Python.

1. حمّل مستند PDF.
1. تحديد العدد الإجمالي للصفحات.
1. تحقق مما إذا كان المستند فارغًا.
1. إنشاء مستند للصفحة الأخيرة.
1. أضف الصفحة الأخيرة.
1. احفظ مستند الصفحة الأخيرة.
1. تحقق من المستندات ذات الصفحة الواحدة.
1. قم بإزالة الصفحة الأخيرة من المستند الأصلي.
1. احفظ الصفحات المتبقية.

```python
import sys
import aspose.pdf as ap
from os import path


def split_documents_last_page_and_rest(infile, outdir):
    document = ap.Document(infile)
    total_pages = len(document.pages)

    if total_pages == 0:
        return

    with ap.Document() as last_page_document:
        last_page_document.pages.add(document.pages[total_pages])
        last_page_document.save(path.join(outdir, "Last_Page.pdf"))

    if total_pages == 1:
        return

    document.pages.delete(total_pages)  # Remove last page from original document
    document.save(path.join(outdir, "Previous_Pages.pdf"))
```

## قسّم ملف PDF إلى ثلاثة أجزاء

قسّم مستند PDF إلى ثلاثة أجزاء منفصلة باستخدام Aspose.PDF for Python.

1. حمّل مستند PDF.
1. تحديد العدد الإجمالي للصفحات.
1. تحقق مما إذا كان المستند فارغًا.
1. احسب حجم الجزء.
1. تكرار عبر ثلاثة أجزاء.
1. تحديد نطاق الصفحات لكل جزء.
1. تحقق من نطاق الصفحات.
1. أنشئ مستندًا جديدًا لكل جزء.
1. نسخ الصفحات إلى المستند الجزئي.
1. احفظ كل جزء.

```python
import sys
import aspose.pdf as ap
from os import path


def split_documents_into_three_parts(infile, outdir):
    document = ap.Document(infile)
    total_pages = len(document.pages)

    if total_pages == 0:
        return

    part_size = max(1, (total_pages + 2) // 3)

    for part_index in range(3):
        start_page = part_index * part_size + 1
        end_page = min((part_index + 1) * part_size, total_pages)

        if start_page > total_pages:
            break

        with ap.Document() as part_document:
            for page_num in range(start_page, end_page + 1):
                part_document.pages.add(document.pages[page_num])
            part_document.save(path.join(outdir, f"Three_Parts_{part_index + 1}.pdf"))
```

## مقسم صفحات PDF مخصص

قسّم مستند PDF إلى ملفات متعددة بناءً على مجموعات صفحات معرفّة مخصّصة باستخدام Aspose.PDF for Python.

```python
import sys
import aspose.pdf as ap
from os import path


def split_documents_custom_page_groups(infile, outdir):
    document = ap.Document(infile)
    total_pages = len(document.pages)
    groups = [
        [1, 2, 5],
        [3, 4, 6, 7],
    ]

    for group_index, group in enumerate(groups, start=1):
        valid_pages = [page_num for page_num in group if 1 <= page_num <= total_pages]
        if not valid_pages:
            continue

        with ap.Document() as group_document:
            for page_num in valid_pages:
                group_document.pages.add(document.pages[page_num])
            group_document.save(path.join(outdir, f"Custom_Group_{group_index}.pdf"))
```

## تقسيم PDF إلى صفحات فردية بأسماء ملفات ثابتة

قسّم مستند PDF إلى صفحات فردية واحفظها بأسماء ملفات ثابتة باستخدام Aspose.PDF for Python.

```python
import sys
import aspose.pdf as ap
from os import path


def split_documents_with_stable_filenames(infile, outdir):
    document = ap.Document(infile)
    total_pages = len(document.pages)

    for page_num in range(1, total_pages + 1):
        with ap.Document() as new_document:
            new_document.pages.add(document.pages[page_num])
            new_document.save(path.join(outdir, f"Page_{page_num:03d}.pdf"))
```

## تقسيم ملف PDF إلى صفحات فردية وزوجية

قُم بتقسيم مستند PDF إلى ملفين منفصلين يحتوي أحدهما على الصفحات الفردية والآخر على الصفحات الزوجية على التوالي باستخدام Aspose.PDF for Python.

```python
import sys
import aspose.pdf as ap
from os import path


def split_documents_odd_even_pages(infile, outdir):
    document = ap.Document(infile)
    total_pages = len(document.pages)

    # Odd pages document
    with ap.Document(infile) as document:
        with ap.Document() as odd_document:
            for page_num in range(1, total_pages + 1, 2):
                odd_document.pages.add(document.pages[page_num])
            odd_document.save(path.join(outdir, "Odd_Pages.pdf"))

        with ap.Document() as even_document:
            for page_num in range(2, total_pages + 1, 2):
                even_document.pages.add(document.pages[page_num])
            even_document.save(path.join(outdir, "Even_Pages.pdf"))
```

## مواضيع المستندات ذات الصلة

- [العمل مع مستندات PDF في Python](/pdf/ar/python-net/working-with-documents/)
- [دمج ملفات PDF في Python](/pdf/ar/python-net/merge-pdf-documents/)
- [تحسين ملفات PDF في بايثون](/pdf/ar/python-net/optimize-pdf/)
- [معالجة مستندات PDF في Python](/pdf/ar/python-net/manipulate-pdf-document/)
