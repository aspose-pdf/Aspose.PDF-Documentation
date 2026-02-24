---
title: نقل صفحات PDF برمجيًا باستخدام Python
linktitle: نقل صفحات PDF
type: docs
weight: 100
url: /ar/python-net/move-pages/
description: حاول نقل الصفحات إلى الموقع المطلوب أو إلى نهاية ملف PDF باستخدام Aspose.PDF for Python عبر .NET.
lastmod: "2025-11-16"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: نقل الصفحات بين مستندات PDF باستخدام Python
Abstract: توفر المقالة دليلًا شاملًا حول نقل الصفحات بين مستندات PDF أو داخل مستند PDF واحد باستخدام Python، وبشكل خاص من خلال مكتبة Aspose.PDF. تستعرض خطوات مفصلة لثلاثة سيناريوهات - نقل صفحة واحدة من PDF إلى آخر، نقل عدة صفحات، وإعادة توطين صفحة داخل نفس المستند. كل سيناريو يتضمن إنشاء كائنات فئة `Document` للملفات المصدر والوجهة، التعامل مع الصفحات عبر فئة `PageCollection`، واستخدام طرق `add` و `delete` و `save` لتحقيق إعادة تنظيم الصفحات المطلوبة. يتم توفير مقاطع شفرة للتنفيذ العملي، موضحة كيفية نقل الصفحات بفعالية باستخدام سكريبتات Python.
---

## نقل صفحة من مستند PDF إلى آخر

يتيح لك Aspose.PDF for Python نقل صفحة (ليس مجرد نسخها) من ملف PDF إلى آخر. يزيل الصفحة المحددة من المستند الأصلي ثم يضيفها إلى ملف PDF جديد.

فكر في ذلك كقص صفحة من كتاب ولصقها في آخر — لا توجد الصفحة بعد الآن في الملف الأصلي بعد النقل.

1. افتح مستند PDF المصدر باستخدام فئة [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) .
1. اختر صفحة معينة للنقل (في هذه الحالة، الصفحة 2) — هذا يشير إلى [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) .
1. أنشئ مستند PDF جديد (قم بإنشاء كائن آخر من فئة [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) ).
1. أضف الصفحة المختارة إلى مستند PDF الجديد باستخدام `PageCollection` الخاص بالمستند الوجهة [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/) (على سبيل المثال، `another_document.pages.add(page)`).
1. احذف الصفحة من المستند الأصلي عبر `PageCollection` الخاص به [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/) (على سبيل المثال، `document.pages.delete(index)`).
1. احفظ كلا المستندين.

مقتطف الشفرة التالي يوضح لك كيفية نقل صفحة واحدة.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def moving_page_from_one_document_to_another(input_file_name, output_file_name):
    """
    Move a single page from one PDF document to another.

    Parameters:
    - input_file_name (str): Path to the source PDF file.
    - output_file_name (str): Path to the destination PDF file after moving the page.
    """
    document = ap.Document(input_file_name)
    page = document.pages[2]
    another_document = ap.Document()
    another_document.pages.add(page)
    document.pages.delete(2)
    document.save(input_file_name.replace(".pdf","_new.pdf"))
    another_document.save(output_file_name)
```

## نقل مجموعة من الصفحات من مستند PDF إلى آخر

على عكس النسخ، تقوم هذه العملية بنقل الصفحات المحددة — إزالتها من الملف المصدر وحفظها في PDF جديد.

1. أنشئ مستند وجهة جديد وفارغ (`Document`).
1. اختر عدة صفحات (في هذه الحالة، الصفحات 1 و 3) من `PageCollection` الخاص بالمستند المصدر [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/).
1. قم بالتكرار عبر الصفحات المختارة وأضف كل واحدة إلى `PageCollection` الخاص بالمستند الوجهة [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/).
1. احفظ مستند الوجهة الذي يحتوي على الصفحات المنقولة.
1. احذف الصفحات المنقولة من المستند المصدر باستخدام `PageCollection` الخاص به [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/).
1. احفظ المستند المصدر المعدل باسم ملف جديد للحفاظ على النسختين.

مقتطف الشفرة التالي يوضح لك كيفية إدراج صفحة فارغة في نهاية ملف PDF.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def moving_bunch_pages_from_one_document_to_another(input_file_name, output_file_name):
    """
    Move a set of pages from one PDF document to another.

    Parameters:
    - input_file_name (str): Path to the source PDF file.
    - output_file_name (str): Path to the destination PDF file where selected pages will be saved.
    """
    src_document = ap.Document(input_file_name)
    dst_document = ap.Document()
    pages = [1, 3]
    for page_index in pages:
        page = src_document.pages[page_index]
        dst_document.pages.add(page)
    # Save output files
    dst_document.save(output_file_name)
    src_document.pages.delete(pages)
    src_document.save(input_file_name.replace(".pdf","_new.pdf"))
```

## نقل صفحة إلى موقع جديد في مستند PDF الحالي

يظهر كيف يمكن نقل صفحة محددة إلى موضع مختلف داخل نفس المستند — حاجة شائعة عند إعادة تنظيم أو تحرير تخطيطات PDF.

1. حمّل مستند PDF الإدخال باستخدام فئة [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) .
1. اختر الصفحة التي تريد نقلها (الصفحة 2) — هذه هي [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) .
1. أضفها إلى نهاية المستند باستخدام `PageCollection` الخاص بالمستند [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/) .
1. احذف الصفحة الأصلية من موقعها السابق عبر `PageCollection` [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/) .
1. احفظ المستند المعدل كملف جديد.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def moving_page_in_new_location_in_same_document(input_file_name, output_file_name):
    """
    Move a page to a new location within the same PDF document.

    Parameters:
    - input_file_name (str): Path to the source PDF file.
    - output_file_name (str): Path to the destination PDF file after moving the page.
    """
    srcDocument = ap.Document(input_file_name)

    page = srcDocument.pages[2]
    srcDocument.pages.add(page)
    srcDocument.pages.delete(2)

    # Save output file
    srcDocument.save(output_file_name)
```


