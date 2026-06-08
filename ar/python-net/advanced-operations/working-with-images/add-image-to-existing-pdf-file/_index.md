---
title: إضافة صورة إلى ملف PDF موجود في بايثون
linktitle: إضافة صورة إلى PDF
type: docs
weight: 10
url: /ar/python-net/add-image-to-existing-pdf-file/
description: تعرف على كيفية إضافة صورة إلى ملف PDF موجود في بايثون، وضعها عند إحداثيات ثابتة، تعيين نص بديل، واستخدام ضغط الصورة.
lastmod: "2026-06-05"
TechArticle: true
AlternativeHeadline: إضافة صور إلى ملفات PDF موجودة باستخدام بايثون
Abstract: تُظهر هذه المقالة كيفية إضافة صور إلى مستندات PDF باستخدام Aspose.PDF for Python via .NET. تغطي وضع صورة عند إحداثيات ثابتة، ورسم الصور باستخدام عمليات PDF منخفضة المستوى، وتعيين نص بديل لإمكانية الوصول، وتضمين الصور باستخدام ضغط Flate.
---

## إضافة صورة إلى ملف PDF موجود في بايثون

يوضح هذا المثال كيفية وضع صورة في موضع ثابت على صفحة PDF موجودة باستخدام Aspose.PDF for Python via .NET.

استخدم هذه الأمثلة عندما تحتاج إلى إضافة شعار أو صورة أو ختم أو رسم بياني أو أي رسم آخر إلى تخطيط PDF موجود. يمكنك وضع الصورة بإحداثيات الصفحة، رسمها باستخدام العمليات، إضافة نص قابلية وصول، أو التحكم في ضغط الصورة.

1. حمّل ملف PDF موجود باستخدام `ap.Document(infile)`.
1. حدد الصفحة المستهدفة (`document.pages[1]` للصفحة الأولى)
1. اتصال `page.add_image()` مع:
    - مسار ملف الصورة.
    - أ `Rectangle` تحديد إحداثيات الموضع.
1. احفظ ملف PDF المحدث.

```python
import aspose.pdf as ap


def add_image(infile, image_file, outfile):
    document = ap.Document(infile)
    page = document.pages[1]
    page.add_image(image_file, ap.Rectangle(20, 730, 120, 830, True))
    document.save(outfile)
```

## إضافة صورة إلى PDF باستخدام العوامل

تضيف هذه الطريقة صورة باستخدام مشغلات PDF منخفضة المستوى بدلاً من المشغلات عالية المستوى `add_image()` مساعد.

1. إنشاء جديد `Document` وأضف صفحةً.
1. أضف الصورة إلى موارد الصفحة (`page.resources.images`).
1. إنشاء عوامل التحويل (`GSave`, `ConcatenateMatrix`, `Do`, `GRestore`).
1. أضف عوامل إلى محتويات الصفحة.
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

## إضافة صورة إلى PDF مع نص بديل

يضيف هذا المثال صورة ويُعين نصًا بديلًا من أجل إمكانية الوصول.

1. إنشاء جديد `Document` وأضف صفحةً.
1. أضف الصورة إلى الصفحة باستخدام `page.add_image()`.
1. احصل على موارد الصور من `page.resources.images`.
1. تعيين النص البديل باستخدام `try_set_alternative_text()`.
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

## إضافة صورة إلى PDF باستخدام ضغط Flate

هذا المثال يدمج صورة باستخدام `ImageFilterType.FLATE` ضغط.

1. إنشاء جديد `Document` وأضف صفحةً.
1. أضف الصورة إلى موارد الصفحة باستخدام ضغط Flate.
1. استخدم عمليات المصفوفة لتحديد موضع ورسم الصورة.
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

## المواضيع ذات الصلة بالصور

- [العمل مع الصور في PDF باستخدام بايثون](/pdf/ar/python-net/working-with-images/)
- [استبدال الصور في ملفات PDF الموجودة](/pdf/ar/python-net/replace-image-in-existing-pdf-file/)
- [حذف الصور من ملفات PDF](/pdf/ar/python-net/delete-images-from-pdf-file/)
- [استخراج الصور من ملفات PDF](/pdf/ar/python-net/extract-images-from-pdf-file/)
