---
title: استخراج صفحات PDF في بايثون
linktitle: استخراج صفحات PDF
type: docs
weight: 80
url: /ar/python-net/extract-pages/
description: تعرف على كيفية استخراج صفحات PDF مفردة أو متعددة إلى ملفات جديدة في Python.
lastmod: "2026-06-11"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: كيفية استخراج صفحات PDF باستخدام Python
Abstract: توضح هذه المقالة كيفية استخراج الصفحات من ملفات PDF باستخدام Aspose.PDF لـ Python عبر .NET. تعرف على كيفية نسخ صفحة واحدة أو عدة صفحات إلى مستند جديد باستخدام فهرسة الصفحة المستندة إلى 1 وواجهة برمجة تطبيقات PageCollection.
---

## استخراج صفحة واحدة من PDF

قم باستخراج صفحة معينة من وثيقة PDF وحفظها كملف جديد. باستخدام مكتبة Aspose.PDF، يقوم البرنامج النصي بنسخ الصفحة المطلوبة إلى PDF جديد، مع ترك المستند الأصلي بدون تغيير. هذا مفيد لتقسيم ملفات PDF أو عزل الصفحات المهمة للتوزيع.

1. قم بتحميل ملف PDF المصدر باستخدام [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) API (`ap.Document()`).
1. قم بإنشاء ملف جديد [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) للاحتفاظ بالصفحة المستخرجة.
1. أضف المطلوب [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) من المستند المصدر إلى PDF الجديد باستخدام مستند الوجهة [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/) (`dst_document.pages.add(...)`).
    - في هذا المثال، يتم استخراج الصفحة 2 (الفهرسة المستندة إلى 1).
1. احفظ الجديد [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) مع الصفحة المستخرجة إلى ملف الإخراج المحدد.

```python
import aspose.pdf as ap

def extract_page(input_file_name: str, output_file_name: str) -> None:
    src_document = ap.Document(input_file_name)
    dst_document = ap.Document()
    dst_document.pages.add(src_document.pages[2])
    dst_document.save(output_file_name)
```

## استخراج صفحات متعددة من PDF

استخرج عدة صفحات محددة من وثيقة PDF واحفظها في ملف جديد. باستخدام مكتبة Aspose.PDF، يتم نسخ الصفحات المحددة إلى PDF جديد مع ترك المستند الأصلي كما هو. هذا مفيد لإنشاء ملفات PDF أصغر تحتوي فقط على الأقسام ذات الصلة من مستند أكبر.

1. قم بتحميل ملف PDF المصدر باستخدام [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) API (`ap.Document()`).
1. قم بإنشاء ملف جديد [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) للاحتفاظ بالصفحات المستخرجة.
1. حدد الصفحات لاستخراجها (في هذا المثال، الصفحتان 2 و 3 باستخدام الفهرسة المستندة إلى 1).
1. إضافة كل اختيار [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) من المستند المصدر إلى ملف PDF الجديد باستخدام [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/).
1. احفظ الجديد [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) مع الصفحات المستخرجة إلى ملف الإخراج المحدد.

```python
import aspose.pdf as ap

def extract_multiple_pages(input_file_name: str, output_file_name: str) -> None:
    document = ap.Document(input_file_name)
    pages = [2, 3]
    another_document = ap.Document()
    for page_index in pages:
        another_document.pages.add(document.pages[page_index])
    another_document.save(output_file_name)
```

## موضوعات الصفحة ذات الصلة

- [العمل مع صفحات PDF في بايثون](/pdf/ar/python-net/working-with-pages/)
- [حذف صفحات PDF في بايثون](/pdf/ar/python-net/delete-pages/)
- [نقل صفحات PDF في بايثون](/pdf/ar/python-net/move-pages/)
- [تقسيم ملفات PDF في بايثون](/pdf/ar/python-net/split-document/)
