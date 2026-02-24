---
title: استخراج الصفحات برمجيًا باستخدام بايثون
linktitle: استخراج صفحات PDF
type: docs
weight: 80
url: /ar/python-net/extract-pages/
description: يمكنك استخراج الصفحات من ملف PDF الخاص بك باستخدام مكتبة Aspose.PDF للبايثون عبر .NET.
lastmod: "2025-11-16"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: كيفية استخراج صفحات PDF باستخدام بايثون
Abstract: توضح هذه المقالة كيفية استخراج الصفحات من مستند PDF باستخدام مكتبة Aspose.PDF للبايثون. تغطي التقنيات كلًا من استخراج صفحة واحدة واستخراج صفحات متعددة، مما يسمح للمطورين بإنشاء ملفات PDF جديدة تحتوي فقط على الصفحات المحددة. توضح الأمثلة كيفية الوصول إلى صفحات معينة باستخدام فهرس يبدأ من 1، نسخها إلى مستند PDF جديد، وحفظ النتائج مع الحفاظ على المستند الأصلي دون تغيير. هذه الأساليب مفيدة لتقسيم المستندات الكبيرة، مشاركة أقسام مختارة، أو إنشاء مجموعات PDF مخصصة للتوزيع أو التحليل.
---

## استخراج صفحة واحدة من PDF

استخراج صفحة محددة من مستند PDF وحفظها كملف جديد. باستخدام مكتبة Aspose.PDF، يقوم السكريبت بنسخ الصفحة المطلوبة إلى PDF جديد، مع ترك المستند الأصلي دون تغيير. هذا مفيد لتقسيم ملفات PDF أو عزل الصفحات المهمة للتوزيع.

1. تحميل ملف PDF المصدر باستخدام واجهة برمجة التطبيقات [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) (`ap.Document()`).
1. إنشاء [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) جديد لتخزين الصفحة المستخرجة.
1. إضافة [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) المطلوبة من المستند المصدر إلى PDF الجديد باستخدام [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/) للمستند الوجهة (`dst_document.pages.add(...)`).
- في هذا المثال، تم استخراج الصفحة 2 (فهرسة تبدأ من 1).
1. حفظ [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) الجديد مع الصفحة المستخرجة إلى ملف الإخراج المحدد.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def extract_page(input_file_name, output_file_name):
    """
    Extract a single page from a PDF document.

    Demonstrates how to extract a specific page from a PDF document using
    the Aspose.PDF library. This function extracts page 2 from the input
    document and saves it as a new file containing only that page.

    Args:
        input_file_name (str): Path to the input PDF file from which to extract a page.
        output_file_name (str): Path where the extracted page will be saved.

    Returns:
        None: The function creates a new PDF containing the extracted page and saves it to the output path.

    Note:
        - Extracts page 2 (1-based indexing) from the document
        - Page numbering is 1-based (page 2 is the second page)
        - The original document is not modified; a new file is created
        - If the document has fewer than 2 pages, this may raise an error

    Example:
        >>> extract_page("input.pdf", "output.pdf")
        # Extracts page 2 from input.pdf and saves result as output.pdf
    """
    # Open source PDF as Document
    src_document = ap.Document(input_file_name)
    # Create destination Document to hold extracted pages
    dst_document = ap.Document()
    # Add a Page from source to destination using PageCollection API
    dst_document.pages.add(src_document.pages[2])
    # Save destination Document
    dst_document.save(output_file_name)
```

## استخراج صفحات متعددة من PDF

استخراج عدة صفحات محددة من مستند PDF وحفظها في ملف جديد. باستخدام مكتبة Aspose.PDF، يتم نسخ الصفحات المختارة إلى PDF جديد مع ترك المستند الأصلي دون تعديل. هذا مفيد لإنشاء ملفات PDF أصغر تحتوي فقط على الأقسام ذات الصلة من مستند أكبر.

1. تحميل ملف PDF المصدر باستخدام واجهة برمجة التطبيقات [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) (`ap.Document()`).
1. إنشاء [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) جديد لتخزين الصفحات المستخرجة.
1. اختيار الصفحات التي سيتم استخراجها (في هذا المثال، الصفحتان 2 و3 باستخدام فهرسة تبدأ من 1).
1. إضافة كل [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) مختارة من المستند المصدر إلى PDF الجديد باستخدام [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/).
1. حفظ [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) الجديد مع الصفحات المستخرجة إلى ملف الإخراج المحدد.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def extract_bunch_pages(input_file_name, output_file_name):
    """
    Extract specific pages from a PDF document and save them to a new file.

    This function reads a PDF document, extracts pages 2 and 3 (1-indexed),
    and saves them to a new PDF file.

    Args:
        input_file_name (str): Path to the input PDF file to extract pages from.
        output_file_name (str): Path where the new PDF file with extracted pages will be saved.

    Returns:
        None

    Note:
        The function specifically extracts pages 2 and 3 from the source document.
        Page indexing appears to be 1-based in this implementation.
    """
    # Open source Document
    document = ap.Document(input_file_name)
    pages = [2,3]
    # Create destination Document
    another_document = ap.Document()
    # Copy selected Page objects via PageCollection API
    for page_index in pages:
        another_document.pages.add(document.pages[page_index])
    # Save destination Document
    another_document.save(output_file_name)
```
