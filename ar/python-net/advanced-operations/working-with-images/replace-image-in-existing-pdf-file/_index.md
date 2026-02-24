---
title: استبدال صورة في ملف PDF موجود باستخدام بايثون
linktitle: استبدال صورة
type: docs
weight: 70
url: /ar/python-net/replace-image-in-existing-pdf-file/
description: يوضح هذا القسم كيفية استبدال صورة في ملف PDF موجود باستخدام مكتبة بايثون.
lastmod: "2025-09-17"
TechArticle: true
AlternativeHeadline: استبدال صورة في ملف PDF
Abstract: توفر وثائق Aspose.PDF للبايثون عبر .NET دليلًا شاملاً حول استبدال الصور داخل ملفات PDF الموجودة. هذه الوظيفة أساسية للمهام مثل تحديث الشعارات والرسومات أو العناصر البصرية الأخرى في وثيقة PDF دون تغيير محتواها النصي.
---

## استبدال صورة في ملف PDF

كيف يمكنك استبدال صورة موجودة في صفحة PDF بصورة جديدة؟ نفّذ ذلك باستخدام Aspose.PDF للبايثون عبر .NET.

1. استورد الوحدات اللازمة (aspose.pdf, os.path, FileIO).
1. حدد المسارات لـ:
- ملف PDF الإدخال (infile)
- ملف الصورة الجديد (image_file)
- ملف PDF الإخراج (outfile)
1. حمّل مستند PDF باستخدام 'apdf.Document(path_infile)'.
1. افتح ملف الصورة الجديد في وضع القراءة الثنائي.
1. استبدل الصورة الأولى في الصفحة الأولى:
- 'document.pages[1].resources.images.replace(1, image_stream)'
1. احفظ ملف PDF المحدث إلى 'path_outfile'.

```python

    import aspose.pdf as apdf
    from io import FileIO
    from os import path

    path_infile = path.join(self.data_dir, infile)
    path_image_file = path.join(self.data_dir, image_file)
    path_outfile = path.join(self.data_dir, outfile)

    document = apdf.Document(path_infile)

    with FileIO(path_image_file, "rb") as image_stream:
        document.pages[1].resources.images.replace(1, image_stream)

    document.save(path_outfile)
```

## استبدال صورة محددة

يوضح هذا المثال كيفية استبدال صورة محددة في صفحة PDF عن طريق تحديد موقعها باستخدام اكتشاف موضع الصورة.

1. حمّل ملف PDF باستخدام 'apdf.Document()'.
1. أنشئ كائن 'ImagePlacementAbsorber' لجمع جميع مواضع الصور في الصفحة.
1. قَبِل الماصِل في الصفحة الأولى ('document.pages[1].accept(absorber)').
1. تحقق مما إذا كانت هناك أي مواضع للصور في الصفحة.
1. اختر أول موضع صورة (absorber.image_placements[1]) واستبدله.
1. احفظ ملف PDF المعدل إلى 'path_outfile'.

```python

    import aspose.pdf as apdf
    from io import FileIO
    from os import path

    path_infile = path.join(self.data_dir, infile)
    path_image_file = path.join(self.data_dir, image_file)
    path_outfile = path.join(self.data_dir, outfile)

    document = apdf.Document(path_infile)

    # Create ImagePlacementAbsorber to find image placements
    absorber = apdf.ImagePlacementAbsorber()

    # Accept the absorber for the first page
    document.pages[1].accept(absorber)

    # Replace the first image placement found
    if len(absorber.image_placements) > 0:
        image_placement = absorber.image_placements[1]
        with FileIO(path_image_file, "rb") as image_stream:
            image_placement.replace(image_stream)

    document.save(path_outfile)
```
