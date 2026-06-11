---
title: إضافة صورة إلى ملف PDF الموجود في Python
linktitle: إضافة صورة إلى PDF
type: docs
weight: 10
url: /ar/python-net/add-image-to-existing-pdf-file/
description: تعرف على كيفية إضافة صورة إلى ملف PDF موجود في Python، ووضعها في إحداثيات ثابتة، وتعيين نص بديل، واستخدام ضغط الصور.
lastmod: "2026-06-11"
TechArticle: true
AlternativeHeadline: إضافة صور إلى ملفات PDF الموجودة باستخدام Python
Abstract: توضح هذه المقالة كيفية إضافة صور إلى مستندات PDF باستخدام Aspose.PDF لـ Python عبر .NET. وهي تغطي وضع صورة في إحداثيات ثابتة، ورسم الصور باستخدام مشغلات PDF منخفضة المستوى، وتخصيص نص بديل لإمكانية الوصول، وتضمين الصور باستخدام ضغط Flate.
---

## إضافة صورة إلى ملف PDF موجود في Python

يوضح هذا المثال كيفية وضع صورة في موضع ثابت على صفحة PDF موجودة باستخدام Aspose.PDF لـ Python عبر .NET.

استخدم هذه الأمثلة عندما تحتاج إلى إضافة شعار أو صورة أو ختم أو مخطط أو رسم آخر إلى تخطيط PDF موجود. يمكنك وضع الصورة مع إحداثيات الصفحة أو رسمها باستخدام عوامل التشغيل أو إضافة نص إمكانية الوصول أو التحكم في ضغط الصور.

1. قم بتحميل ملف PDF موجود باستخدام `ap.Document(infile)`.
1. حدد الصفحة المستهدفة (`document.pages[1]` للصفحة الأولى).
1. اتصل `page.add_image()` مع:
    - مسار ملف الصورة.
    - أ `Rectangle` تحديد إحداثيات التنسيب.
1. احفظ ملف PDF المحدث.

```python
import aspose.pdf as ap


def add_image(infile, image_file, outfile):
    document = ap.Document(infile)
    page = document.pages[1]
    page.add_image(image_file, ap.Rectangle(20, 730, 120, 830, True))
    document.save(outfile)
```

## إضافة صورة إلى PDF باستخدام عوامل التشغيل

يضيف هذا الأسلوب صورة باستخدام مشغلات PDF منخفضة المستوى بدلاً من المستوى العالي `add_image()` مساعد.

1. قم بإنشاء ملف جديد `Document` وأضف صفحة.
1. إضافة الصورة إلى موارد الصفحة (`page.resources.images`).
1. إنشاء عوامل تحويل (`GSave`, `ConcatenateMatrix`, `Do`, `GRestore`).
1. أضف عوامل تشغيل إلى محتويات الصفحة.
1. احفظ ملف PDF الناتج.

```python
import aspose.pdf as ap
from io import FileIO


def add_image_using_operators(image_file, outfile):
    document = ap.Document()
    page = document.pages.add()
    page.set_page_size(842, 595)
    resources_images = page.resources.images

    with FileIO(image_file, "rb") as image_stream:
        image_id = resources_images.add(image_stream)

    rectangle = ap.Rectangle(0, 0, page.media_box.width, page.media_box.height, True)

    operators = [
        ap.operators.GSave(),
        ap.operators.ConcatenateMatrix(
            ap.Matrix(
                rectangle.urx - rectangle.llx,
                0,
                0,
                rectangle.ury - rectangle.lly,
                rectangle.llx,
                rectangle.lly,
            )
        ),
        ap.operators.Do(image_id),
        ap.operators.GRestore(),
    ]

    page.contents.add(operators)
    document.save(outfile)
```

## إضافة صورة إلى PDF بنص بديل

يضيف هذا المثال صورة ويعين نصًا بديلًا لإمكانية الوصول.

1. قم بإنشاء ملف جديد `Document` وأضف صفحة.
1. أضف الصورة إلى الصفحة باستخدام `page.add_image()`.
1. احصل على موارد الصور من `page.resources.images`.
1. تعيين نص بديل باستخدام `try_set_alternative_text()`.
1. احفظ ملف PDF الناتج.

```python
import aspose.pdf as ap


def add_image_set_alternative_text(image_file, outfile):
    document = ap.Document()
    page = document.pages.add()
    page.set_page_size(842, 595)

    page.add_image(image_file, ap.Rectangle(0, 0, 842, 595, True))
    resources_images = page.resources.images
    x_image = resources_images[1]
    result = x_image.try_set_alternative_text("Alternative text for image", page)

    if result:
        print("Alternative text has been added successfully")

    document.save(outfile)
```

## أضف صورة إلى PDF باستخدام ضغط Flate

يقوم هذا المثال بتضمين صورة باستخدام `ImageFilterType.FLATE` ضغط.

1. قم بإنشاء ملف جديد `Document` وأضف صفحة.
1. أضف الصورة إلى موارد الصفحة باستخدام ضغط Flate.
1. استخدم عوامل تشغيل المصفوفة لوضع الصورة ورسمها.
1. احفظ المستند.

```python
import aspose.pdf as ap
from io import FileIO


def add_image_to_pdf_with_flate_compression(image_file, outfile):
    document = ap.Document()
    page = document.pages.add()
    resources_images = page.resources.images

    with FileIO(image_file, "rb") as image_stream:
        image_id = resources_images.add(image_stream, ap.ImageFilterType.FLATE)

    rectangle = ap.Rectangle(0, 0, 600, 600, True)
    matrix = ap.Matrix(
        rectangle.urx - rectangle.llx,
        0,
        0,
        rectangle.ury - rectangle.lly,
        rectangle.llx,
        rectangle.lly,
    )

    page.contents.add([ap.operators.GSave()])
    page.contents.add([ap.operators.ConcatenateMatrix(matrix)])
    page.contents.add([ap.operators.Do(image_id)])
    page.contents.add([ap.operators.GRestore()])

    document.save(outfile)
```

## موضوعات الصور ذات الصلة

- [العمل مع الصور في PDF باستخدام Python](/pdf/ar/python-net/working-with-images/)
- [استبدل الصور في ملفات PDF الموجودة](/pdf/ar/python-net/replace-image-in-existing-pdf-file/)
- [حذف الصور من ملفات PDF](/pdf/ar/python-net/delete-images-from-pdf-file/)
- [استخراج الصور من ملفات PDF](/pdf/ar/python-net/extract-images-from-pdf-file/)
