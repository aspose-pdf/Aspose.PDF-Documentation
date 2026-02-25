---
title: إضافة صفحات في PDF باستخدام بايثون
linktitle: إضافة صفحات
type: docs
weight: 10
url: /ar/python-net/add-pages/
description: اكتشف كيفية إضافة صفحات إلى مستند PDF باستخدام بايثون واستخدام Aspose.PDF لإنشاء وتحرير المستندات بمرونة.
lastmod: "2025-11-16"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: كيفية إضافة صفحات في PDF باستخدام بايثون
Abstract: توفر المقالة دليلًا حول استخدام Aspose.PDF للغة بايثون عبر .NET API للتلاعب بالصفحات في مستند PDF. وتؤكد على المرونة التي توفرها API، لا سيما من خلال الفئة `PageCollection` التي تدير جميع الصفحات داخل ملف PDF. تفصل الوثيقة إجراءات إضافة أو إدراج صفحات في مواقع محددة داخل ملف PDF. وتحدد عمليتين أساسيتين - إدراج صفحة فارغة في موقع محدد داخل المستند وإضافة صفحة فارغة في نهاية المستند. لكلا العمليتين، يتضمن العملية إنشاء كائن `Document`، واستخدام طريقتي `insert` أو `add` من `PageCollection`، ثم حفظ المستند المعدل. تتضمن المقالة مقتطفات شفرة توضح هذه المهام، وتظهر مدى سهولة التلاعب بمستندات PDF باستخدام بايثون مع هذه API.
---

توفر Aspose.PDF للغة بايثون عبر .NET API مرونة كاملة للعمل مع صفحات مستند PDF باستخدام بايثون. تحتفظ بجميع صفحات مستند PDF في [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/) التي يمكن استخدامها للتعامل مع صفحات PDF.
تتيح لك Aspose.PDF للغة بايثون عبر .NET إدراج صفحة إلى [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) في أي موقع داخل الملف وكذلك إضافة صفحات إلى نهاية ملف PDF. يوضح هذا القسم كيفية إضافة صفحات إلى PDF باستخدام بايثون.

## إضافة أو إدراج صفحة في ملف PDF

تتيح لك Aspose.PDF للغة بايثون عبر .NET إدراج صفحة إلى [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) في أي موقع داخل الملف وكذلك إضافة صفحات إلى نهاية ملف PDF.

### إدراج صفحة فارغة في ملف PDF

لإدراج صفحة فارغة في ملف PDF:

1. افتح مستندًا موجودًا [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) باستخدام الأساليب المناسبة.
1. أدخل صفحة فارغة جديدة في فهرس محدد باستخدام طريقة `insert()` من [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/).
1. احفظ الـ[`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) المُعدل إلى مسار الإخراج المطلوب.

إدراج صفحة فارغة في ملف PDF موجود في موضع محدد:

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def insert_empty_page(input_file_name, output_file_name):
    document = ap.Document(input_file_name)
    document.pages.insert(2)
    document.save(output_file_name)
```

### إضافة صفحة فارغة في نهاية ملف PDF

أحيانًا، قد ترغب في التأكد من أن المستند ينتهي بصفحة فارغة. يشرح هذا الموضوع كيفية إدراج صفحة فارغة في نهاية مستند PDF.

لإدراج صفحة فارغة في نهاية ملف PDF:

1. افتح مستندًا موجودًا [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) باستخدام الأساليب المناسبة.
1. أضف صفحة فارغة جديدة إلى نهاية المستند باستخدام طريقة `add()` من [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/).
1. احفظ الـ[`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) المحدث.

يظهر مقطع الشفرة التالي لك كيفية إدراج صفحة فارغة في نهاية ملف PDF.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def add_empty_page_to_end(input_file_name, output_file_name):
    # Open document
    document = ap.Document(input_file_name)

    # Insert an empty page at the end of a PDF file
    document.pages.add()

    # Save output file
    document.save(output_file_name)
```

### إضافة صفحة من مستند PDF آخر

باستخدام مكتبة Aspose.PDF للغة بايثون، يمكنك إنشاء [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) جديد، وإضافة صفحة أولية، ثم استيراد صفحة من PDF آخر إليه.

1. أنشئ [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) جديدًا.
1. أضف [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) فارغًا جديدًا واكتب بعض النصوص عليه باستخدام [`TextFragment`](https://reference.aspose.com/pdf/python-net/aspose.pdf/textfragment/).
1. افتح مستندًا آخر موجودًا [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. انسخ [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) من ذلك المستند.
1. الصق الصفحة المنقولة إلى المستند الرئيسي الخاص بك باستخدام [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/).
1. احفظ الملف المدمج.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def add_page_from_another_document(input_file_name, output_file_name):
    # Open document
    document = ap.Document()
    page = document.pages.add()
    text_fragment = ap.text.TextFragment("This is first page!")
    page.paragraphs.add(text_fragment)

    another_document = ap.Document(input_file_name)
    document.pages.add(another_document.pages[1])

    # Save output file
    document.save(output_file_name)
```
