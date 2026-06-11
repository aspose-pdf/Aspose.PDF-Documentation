---
title: نقل صفحات PDF في بايثون
linktitle: نقل صفحات PDF
type: docs
weight: 100
url: /ar/python-net/move-pages/
description: تعرف على كيفية نقل صفحات PDF داخل مستند أو بين المستندات في Python.
lastmod: "2026-06-11"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: نقل صفحات PDF بين المستندات في Python
Abstract: توضح هذه المقالة كيفية نقل الصفحات في ملفات PDF باستخدام Aspose.PDF لـ Python عبر .NET. تعرف على كيفية نقل صفحة واحدة أو عدة صفحات إلى مستند آخر، وكيفية إعادة وضع صفحة داخل نفس PDF باستخدام واجهات برمجة تطبيقات Document و PageCollection.
---

## نقل صفحة من وثيقة PDF إلى أخرى

يتيح لك Aspose.PDF for Python نقل صفحة (وليس نسخها فقط) من ملف PDF إلى آخر. يقوم بإزالة الصفحة المحددة من المستند الأصلي ثم إضافتها إلى ملف PDF جديد.

فكر في الأمر على أنه قطع صفحة من كتاب ولصقها في كتاب آخر - لم تعد الصفحة موجودة في الملف الأصلي بعد النقل.

1. افتح مستند PDF المصدر باستخدام [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) فئة.
1. حدد صفحة معينة لنقلها (في هذه الحالة، الصفحة 2) - يشير هذا إلى [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/).
1. قم بإنشاء مستند PDF جديد (قم بإنشاء مثيل آخر) [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/)).
1. أضف الصفحة المحددة إلى مستند PDF الجديد باستخدام مستند الوجهة [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/) (على سبيل المثال, `another_document.pages.add(page)`).
1. احذف الصفحة من المستند الأصلي عبر [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/) (على سبيل المثال, `document.pages.delete(index)`).
1. احفظ كلا المستندين.

يوضح لك مقتطف الشفرة التالي كيفية نقل صفحة واحدة.

```python
import aspose.pdf as ap

def move_page_from_one_document_to_another(
    input_file_name: str, output_file_name: str
) -> None:

    document = ap.Document(input_file_name)
    page = document.pages[2]
    another_document = ap.Document()
    another_document.pages.add(page)
    document.pages.delete(2)
    document.save(input_file_name.replace(".pdf", "_new.pdf"))
    another_document.save(output_file_name)
```

## نقل صفحات متعددة من وثيقة PDF إلى أخرى

على عكس النسخ، تقوم هذه العملية بنقل الصفحات المحددة - إزالتها من الملف المصدر وحفظها في PDF جديد.

1. إنشاء مستند وجهة جديد فارغ (`Document`).
1. حدد صفحات متعددة (في هذه الحالة، الصفحتان 1 و 3) من المستند المصدر [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/).
1. قم بالتمرير عبر الصفحات المحددة وأضف كل منها إلى مستند الوجهة [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/).
1. احفظ مستند الوجهة الذي يحتوي على الصفحات المنقولة.
1. احذف الصفحات المنقولة من المستند المصدر باستخدام [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/).
1. احفظ المستند المصدر المعدل باسم ملف جديد للحفاظ على كلا الإصدارين.

يعرض مقتطف الشفرة التالي كيفية نقل صفحات متعددة.

```python
import aspose.pdf as ap

def move_multiple_pages_from_one_document_to_another(
    input_file_name: str, output_file_name: str
) -> None:
    src_document = ap.Document(input_file_name)
    dst_document = ap.Document()
    pages = [1, 2]
    for page_index in pages:
        page = src_document.pages[page_index]
        dst_document.pages.add(page)
    # Save output files
    dst_document.save(output_file_name)
    src_document.pages.delete(pages)
    src_document.save(input_file_name.replace(".pdf", "_new.pdf"))
```

## نقل صفحة إلى موقع جديد في نفس وثيقة PDF

يوضح كيفية نقل صفحة معينة إلى موضع مختلف داخل نفس المستند - وهي حاجة شائعة عند إعادة تنظيم تخطيطات PDF أو تحريرها.

1. قم بتحميل مستند PDF المُدخل باستخدام [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) فئة.
1. حدد الصفحة التي تريد نقلها (الصفحة 2) - هذه هي [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/).
1. قم بإضافته إلى نهاية المستند باستخدام المستند [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/).
1. احذف الصفحة الأصلية من موقعها السابق عبر [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/).
1. احفظ المستند المعدل كملف جديد.

```python
import aspose.pdf as ap

def move_page_in_new_location_in_same_document(
    input_file_name: str, output_file_name: str
) -> None:
    src_document = ap.Document(input_file_name)

    page = src_document.pages[2]
    src_document.pages.add(page)
    src_document.pages.delete(2)

    # Save output file
    src_document.save(output_file_name)
```

## موضوعات الصفحة ذات الصلة

- [العمل مع صفحات PDF في بايثون](/pdf/ar/python-net/working-with-pages/)
- [إضافة صفحات PDF في بايثون](/pdf/ar/python-net/add-pages/)
- [حذف صفحات PDF في بايثون](/pdf/ar/python-net/delete-pages/)
- [استخراج صفحات PDF في بايثون](/pdf/ar/python-net/extract-pages/)
