---
title: إضافة صفحات PDF في بايثون
linktitle: إضافة صفحات
type: docs
weight: 10
url: /ar/python-net/add-pages/
description: تعرف على كيفية إضافة أو إدراج صفحات في مستندات PDF في Python.
lastmod: "2026-06-11"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: إضافة أو إدراج صفحات PDF باستخدام Python
Abstract: توضح هذه المقالة كيفية إضافة صفحات إلى ملفات PDF باستخدام Aspose.PDF لـ Python عبر .NET. تعرف على كيفية إدراج صفحات فارغة في مواضع محددة، وإلحاق صفحات في نهاية المستند، واستيراد صفحة من PDF آخر باستخدام واجهات برمجة تطبيقات Document and PageCollection.
---

يوفر Aspose.PDF لـ Python عبر .NET عمليات مرنة على مستوى الصفحة لمستندات PDF. يمكنك إدارة الصفحات من خلال [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/) وأضف صفحات إلى [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) في مواقع محددة أو في نهاية الملف.

استخدم هذه الصفحة عندما تحتاج إلى إدراج صفحات فارغة جديدة في PDF موجود أو إلحاق صفحات بنهاية المستند أثناء عمليات سير عمل الإنشاء.

## إضافة أو إدراج صفحات في ملف PDF

يدعم Aspose.PDF لـ Python عبر .NET كلاً من إدراج الصفحة في فهرس معين وإلحاق الصفحات في نهاية ملف PDF.

### إدراج صفحة فارغة في ملف PDF

لإدراج صفحة فارغة في ملف PDF:

1. افتح ملف موجود [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) باستخدام الطرق المناسبة.
1. أدخل صفحة فارغة جديدة في فهرس محدد باستخدام [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/) `insert()` طريقة.
1. احفظ التعديل [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) إلى مسار الإخراج المطلوب.

أدخل صفحة فارغة في ملف PDF موجود في موضع محدد:

```python
import aspose.pdf as ap

def insert_empty_page(input_file_name: str, output_file_name: str) -> None:
    document = ap.Document(input_file_name)
    document.pages.insert(2)
    document.save(output_file_name)
```

### أضف صفحة فارغة في نهاية ملف PDF

في بعض الأحيان، تريد التأكد من أن المستند ينتهي بصفحة فارغة. يشرح هذا الموضوع كيفية إدراج صفحة فارغة في نهاية وثيقة PDF.

لإدراج صفحة فارغة في نهاية ملف PDF:

1. افتح ملف موجود [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) باستخدام الطرق المناسبة.
1. أضف صفحة فارغة جديدة إلى نهاية المستند باستخدام [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/) `add()` طريقة.
1. احفظ التحديث [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).

يوضح لك مقتطف الشفرة التالي كيفية إدراج صفحة فارغة في نهاية ملف PDF.

```python
import aspose.pdf as ap

def add_empty_page_to_end(input_file_name: str, output_file_name: str) -> None:
    document = ap.Document(input_file_name)
    document.pages.add()
    document.save(output_file_name)
```

### إضافة صفحة من وثيقة PDF أخرى

باستخدام Aspose.PDF لبيثون عبر.NET، يمكنك إنشاء ملف جديد [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/)، قم بإضافة صفحة أولية، ثم قم باستيراد صفحة من PDF آخر إليها.

1. قم بإنشاء ملف جديد [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. إضافة فراغ جديد [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) واكتب بعض النص عليها باستخدام [`TextFragment`](https://reference.aspose.com/pdf/python-net/aspose.pdf/textfragment/).
1. افتح آخر موجود [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. انسخ أ [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) من تلك الوثيقة.
1. قم بلصق الصفحة المنسوخة في المستند الرئيسي باستخدام [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/).
1. احفظ الملف المدمج.

```python
import aspose.pdf as ap

def add_page_from_another_document(input_file_name: str, output_file_name: str) -> None:
    document = ap.Document()
    page = document.pages.add()
    text_fragment = ap.text.TextFragment("This is first page!")
    page.paragraphs.add(text_fragment)

    another_document = ap.Document(input_file_name)
    document.pages.add(another_document.pages[1])

    document.save(output_file_name)
```

## موضوعات الصفحة ذات الصلة

- [العمل مع صفحات PDF في بايثون](/pdf/ar/python-net/working-with-pages/)
- [نقل صفحات PDF في بايثون](/pdf/ar/python-net/move-pages/)
- [حذف صفحات PDF في بايثون](/pdf/ar/python-net/delete-pages/)
- [استخراج صفحات PDF في بايثون](/pdf/ar/python-net/extract-pages/)
