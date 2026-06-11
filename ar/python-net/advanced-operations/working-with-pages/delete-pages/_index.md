---
title: حذف صفحات PDF في بايثون
linktitle: حذف صفحات PDF
type: docs
weight: 80
url: /ar/python-net/delete-pages/
description: تعرف على كيفية حذف الصفحات من ملفات PDF في Python.
lastmod: "2026-06-11"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: احذف صفحة PDF واحدة أو أكثر في Python
Abstract: توضح هذه المقالة كيفية إزالة الصفحات من ملفات PDF باستخدام Aspose.PDF لـ Python عبر .NET. تعرف على كيفية حذف صفحة واحدة أو عدة صفحات من مستند باستخدام PageCollection API ثم حفظ ملف PDF المحدث.
---

يمكنك حذف صفحات من ملف PDF باستخدام Aspose.PDF لبيثون عبر.NET. لحذف صفحة معينة، استخدم [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/) من أ [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).

استخدم سير العمل هذا عندما تحتاج إلى إزالة الصفحات غير المرغوب فيها من PDF قبل مشاركة المستندات أو أرشفتها أو دمجها.

## حذف صفحة من ملف PDF

Aspose.PDF لـ Python عبر .NET يحذف الصفحة 2 من ملف PDF المُدخل ويحفظ المستند المحدث إلى ملف جديد. هذه الميزة مفيدة لإزالة الصفحات غير المرغوب فيها أو الحساسة دون تغيير بقية المستند.

1. قم بتحميل ملف PDF المُدخل كملف [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. احذف الصفحة باستخدام [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/).
1. اتصل بـ [`Document.save()`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) طريقة لحفظ ملف PDF المحدث.

يوضح مقتطف الشفرة التالي كيفية حذف صفحة معينة من ملف PDF باستخدام Python.

```python
import aspose.pdf as ap

def delete_page(input_file_name: str, output_file_name: str) -> None:
    document = ap.Document(input_file_name)
    document.pages.delete(2)
    document.save(output_file_name)
```

## حذف صفحات متعددة من وثيقة PDF

يتيح لك حذف صفحات متعددة إزالة مجموعة من الصفحات المحددة في عملية واحدة، وهي أكثر كفاءة من حذف الصفحات واحدة تلو الأخرى. يتم حفظ ملف PDF الناتج في ملف جديد، مع الحفاظ على المستند الأصلي.

1. قم بتحميل ملف PDF المُدخل كملف [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. احذف الصفحات المدرجة في مصفوفة الصفحات باستخدام [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/).
1. احفظ التحديث [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) إلى ملف جديد.

```python
import aspose.pdf as ap

def delete_multiple_pages(input_file_name: str, output_file_name: str) -> None:
    document = ap.Document(input_file_name)
    # Example: delete pages 2, 3, and 4.
    pages = [2, 3, 4]
    document.pages.delete(pages)
    document.save(output_file_name)
```

## موضوعات الصفحة ذات الصلة

- [العمل مع صفحات PDF في بايثون](/pdf/ar/python-net/working-with-pages/)
- [إضافة صفحات PDF في بايثون](/pdf/ar/python-net/add-pages/)
- [نقل صفحات PDF في بايثون](/pdf/ar/python-net/move-pages/)
- [استخراج صفحات PDF في بايثون](/pdf/ar/python-net/extract-pages/)
