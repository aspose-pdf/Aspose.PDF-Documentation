---
title: حذف الصور من ملف PDF باستخدام Python
linktitle: حذف الصور
type: docs
weight: 20
url: /ar/python-net/delete-images-from-pdf-file/
description: تعرف على كيفية حذف صور محددة أو كلها من ملفات PDF في Python.
lastmod: "2026-06-11"
TechArticle: true
AlternativeHeadline: احذف الصور من ملفات PDF باستخدام Python
Abstract: توضح هذه المقالة كيفية حذف الصور من مستندات PDF باستخدام Aspose.PDF لـ Python عبر .NET. يغطي إزالة مورد صورة معين وحذف جميع الصور من صفحة محددة.
---

استخدم هذه الصفحة عندما تحتاج إلى إزالة الرسومات غير الضرورية أو تقليل حجم PDF أو تنظيف المحتوى المرئي الحساس من المستند.

## حذف الصور من ملف PDF

استخدم الخطوات التالية لحذف صورة واحدة من الصفحة:

1. قم بتحميل ملف PDF المصدر باستخدام `ap.Document(infile)`.
1. حدد فهرس موارد الصفحة والصورة.
1. احذف الصورة باستخدام `resources.images.delete(index)`.
1. احفظ ملف PDF المحدث.

```python
import aspose.pdf as ap


def delete_image(infile, outfile):
    document = ap.Document(infile)
    document.pages[1].resources.images.delete(1)
    document.save(outfile)
```

## احذف جميع الصور من الصفحة

استخدم هذا المثال لإزالة كل صورة من صفحة معينة.

```python
import aspose.pdf as ap


def delete_all_images_from_page(infile, outfile, page_number):
    document = ap.Document(infile)
    page = document.pages[page_number]

    while len(page.resources.images) != 0:
        page.resources.images.delete(1)

    document.save(outfile)
```

## موضوعات الصور ذات الصلة

- [العمل مع الصور في PDF باستخدام Python](/pdf/ar/python-net/working-with-images/)
- [استبدل الصور في ملفات PDF الموجودة](/pdf/ar/python-net/replace-image-in-existing-pdf-file/)
- [استخراج الصور من ملفات PDF](/pdf/ar/python-net/extract-images-from-pdf-file/)
- [إضافة صور إلى ملفات PDF الموجودة](/pdf/ar/python-net/add-image-to-existing-pdf-file/)