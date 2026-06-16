---
title: استبدال الصورة في ملف PDF الحالي باستخدام Python
linktitle: استبدال الصورة
type: docs
weight: 70
url: /ar/python-net/replace-image-in-existing-pdf-file/
description: تعرف على كيفية استبدال الصور المضمنة في ملفات PDF الموجودة في Python.
lastmod: "2026-06-11"
TechArticle: true
AlternativeHeadline: استبدل الصور في ملفات PDF الموجودة باستخدام Python
Abstract: توضح هذه المقالة كيفية استبدال الصور في مستندات PDF بـ Aspose.PDF لـ Python عبر .NET. وهي تغطي استبدال صورة بفهرس الموارد واستبدال صورة معينة تم العثور عليها باستخدام ImagePlacementAbsorber.
---

## استبدال صورة في PDF

استخدم هذه الصفحة عندما تحتاج إلى تحديث الشعارات أو الرسوم التخطيطية أو غيرها من الرسومات المضمنة في PDF دون إعادة إنشاء تخطيط المستند.

1. قم بتحميل ملف PDF المصدر باستخدام `ap.Document(infile)`.
1. افتح الصورة البديلة كتدفق ثنائي.
1. استبدل مورد الصورة بالفهرس على الصفحة.
1. احفظ ملف PDF المحدث.

```python
import aspose.pdf as ap
from io import FileIO


def replace_image(infile, image_file, outfile):
    document = ap.Document(infile)

    with FileIO(image_file, "rb") as image_stream:
        document.pages[1].resources.images.replace(1, image_stream)

    document.save(outfile)
```

## استبدال صورة محددة

يستبدل هذا المثال موضع صورة معين تم العثور عليه بواسطة `ImagePlacementAbsorber`.

1. قم بتحميل ملف PDF المصدر.
1. ابتكر `ImagePlacementAbsorber` وقم بتجميع مواضع الصور على الصفحة.
1. تحقق من وجود أي مواضع للصور على الصفحة.
1. استبدل الموضع المحدد بدفق صور جديد.
1. احفظ ملف PDF المحدث.

```python
import aspose.pdf as ap
from io import FileIO


def replace_image_with_absorber(infile, image_file, outfile):
    document = ap.Document(infile)
    absorber = ap.ImagePlacementAbsorber()
    document.pages[1].accept(absorber)

    if len(absorber.image_placements) > 0:
        image_placement = absorber.image_placements[1]
        with FileIO(image_file, "rb") as image_stream:
            image_placement.replace(image_stream)

    document.save(outfile)
```

## موضوعات الصور ذات الصلة

- [العمل مع الصور في PDF باستخدام Python](/pdf/ar/python-net/working-with-images/)
- [حذف الصور من ملفات PDF](/pdf/ar/python-net/delete-images-from-pdf-file/)
- [استخراج الصور من ملفات PDF](/pdf/ar/python-net/extract-images-from-pdf-file/)
- [إضافة صور إلى ملفات PDF الموجودة](/pdf/ar/python-net/add-image-to-existing-pdf-file/)
