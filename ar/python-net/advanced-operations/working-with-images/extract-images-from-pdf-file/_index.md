---
title: استخراج الصور من ملف PDF باستخدام Python
linktitle: استخراج الصور
type: docs
weight: 30
url: /ar/python-net/extract-images-from-pdf-file/
description: تعرف على كيفية استخراج الصور المضمنة من ملفات PDF في Python.
lastmod: "2026-06-11"
TechArticle: true
AlternativeHeadline: استخراج الصور من ملفات PDF باستخدام Python
Abstract: توضح هذه المقالة كيفية استخراج الصور من مستندات PDF باستخدام Aspose.PDF لـ Python عبر .NET. وهي تغطي استخراج صورة مضمنة واحدة وتصدير الصور الموجودة داخل منطقة مستطيلة معينة على الصفحة.
---

استخدم هذه الصفحة عندما تحتاج إلى إعادة استخدام الرسومات المضمنة أو أرشفة أصول الصور أو معالجة محتوى الصورة خارج PDF.

1. قم بتحميل ملف PDF المصدر باستخدام `ap.Document(infile)`.
1. حدد الصفحة المستهدفة وفهرس موارد الصور.
1. احفظ كائن الصورة إلى دفق الإخراج.

```python
import aspose.pdf as ap
from io import FileIO


def extract_image(infile, outfile):
    document = ap.Document(infile)
    x_image = document.pages[1].resources.images[1]
    with FileIO(outfile, "wb") as output_image:
        x_image.save(output_image)
```

## استخراج الصور من منطقة معينة في PDF

يستخرج هذا المثال الصور الموجودة داخل منطقة مستطيلة محددة على صفحة PDF ويحفظها كملفات منفصلة.

1. قم بتحميل ملف PDF المصدر.
1. ابتكر `ImagePlacementAbsorber` واقبلها على الصفحة المستهدفة.
1. حدد المستطيل المستهدف.
1. قم بالتكرار من خلال مواضع الصور وتحقق مما إذا كانت حدود كل صورة تتناسب مع المنطقة.
1. احفظ الصور المتطابقة لإخراج الملفات.

```python
import aspose.pdf as ap
from io import FileIO


def extract_image_from_specific_region(infile, outfile):
    document = ap.Document(infile)
    rectangle = ap.Rectangle(0, 0, 590, 590, True)
    absorber = ap.ImagePlacementAbsorber()
    document.pages[1].accept(absorber)

    index = 1
    for image_placement in absorber.image_placements:
        point1 = ap.Point(image_placement.rectangle.llx, image_placement.rectangle.lly)
        point2 = ap.Point(image_placement.rectangle.urx, image_placement.rectangle.ury)

        if rectangle.contains(point1, True) and rectangle.contains(point2, True):
            with FileIO(outfile.replace("index", str(index)), "wb") as output_image:
                image_placement.image.save(output_image)
            index += 1
```

## موضوعات الصور ذات الصلة

- [العمل مع الصور في PDF باستخدام Python](/pdf/ar/python-net/working-with-images/)
- [استبدل الصور في ملفات PDF الموجودة](/pdf/ar/python-net/replace-image-in-existing-pdf-file/)
- [حذف الصور من ملفات PDF](/pdf/ar/python-net/delete-images-from-pdf-file/)
- [إضافة صور إلى ملفات PDF الموجودة](/pdf/ar/python-net/add-image-to-existing-pdf-file/)
