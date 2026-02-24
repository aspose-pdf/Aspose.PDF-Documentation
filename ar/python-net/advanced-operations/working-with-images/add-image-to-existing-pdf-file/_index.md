---
title: إضافة صورة إلى ملف PDF باستخدام بايثون
linktitle: إضافة صورة
type: docs
weight: 10
url: /ar/python-net/add-image-to-existing-pdf-file/
description: يوضح هذا القسم كيفية إضافة صورة إلى ملف PDF موجود باستخدام مكتبة بايثون.
lastmod: "2025-09-27"
TechArticle: true
AlternativeHeadline: كيفية إضافة صور إلى PDF باستخدام بايثون
Abstract: توفر هذه المقالة إرشادات حول إضافة صور إلى ملفات PDF موجودة باستخدام بايثون مع مكتبة Aspose.PDF. تم توضيح طريقتين لتحقيق ذلك. الطريقة الأولى تنطوي على استخدام الفئة `Document` من Aspose.PDF، حيث يقوم المستخدم بتحميل ملف PDF، وتحديد رقم الصفحة، واستخدام طريقة `add_image` من الفئة `Page` لتحديد موضع الصورة. ثم يتم حفظ المستند باستخدام طريقة `save()`. الطريقة الثانية تستخدم الفئة `PdfFileMend` من مساحة الأسماء Aspose.PDF.Facades، والتي توفر واجهة أبسط. هنا يتم استدعاء طريقة `add_image()` لإضافة الصورة إلى الصفحة والإحداثيات المحددة، يليه حفظ ملف PDF المحدث وإغلاق كائن `PdfFileMend`. تُ提供 مقتطفات الشيفرة لكلا الطريقتين لتوضيح العملية.
---

## إضافة صورة في ملف PDF موجود

يوضح هذا المثال كيفية إدراج صورة في موضع محدد على صفحة PDF باستخدام Aspose.PDF لبايثون عبر .NET.

1. تحميل مستند PDF باستخدام 'ap.Document'.
1. اختيار الصفحة المستهدفة '(document.pages[1]' - الصفحة الأولى).
1. استخدام 'page.add_image()' لوضع الصورة:
- مسار ملف الصورة.
- كائن 'Rectangle' يحدد إحداثيات الصورة (left=20, bottom=730, right=120, top=830).
1. حفظ ملف PDF المحدث.

```python

    import aspose.pdf as ap
    from io import FileIO
    from os import path

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    document = ap.Document(path_infile)
    page = document.pages[1]
    page.add_image(
        path.join(self.data_dir, image_file),
        ap.Rectangle(20, 730, 120, 830, True),
    )
    document.save(path_outfile)
```

## إضافة صورة باستخدام المشغلات

يظهر مقطع الشيفرة التالي نهجًا منخفض المستوى لإضافة صورة إلى صفحة PDF عن طريق العمل يدويًا مع مشغلات PDF بدلاً من طرق المساعدة عالية المستوى.

الخطوات:

1. إنشاء 'Document' فارغ جديد.
1. إضافة صفحة وتحديد حجمها (842 × 595 - أفقية A4).
1. الوصول إلى موارد الصور للصفحة (page.resources.images).
1. تحميل ملف الصورة إلى تدفق وإضافته إلى الموارد.
- تُعيد الطريقة 'image_id'.
- يتم استرداد كائن الصورة المضافة حديثًا من الموارد.
1. تعريف مستطيل يحافظ على نسبة العرض إلى الارتفاع للصورة:
1. بناء تسلسل المشغلات:
- 'GSave()' - حفظ حالة الرسومات الحالية.
- 'ConcatenateMatrix(matrix)' - تطبيق التحويل (التحجيم وتوسيط الصورة عموديًا على الصفحة).
- 'Do(image_id)' - عرض الصورة.
- 'GRestore()' - استعادة حالة الرسومات.
1. إضافة تسلسل المشغلات إلى 'page.contents'.
1. حفظ ملف PDF الناتج.

```python

    import aspose.pdf as ap
    from io import FileIO
    from os import path

    path_infile = path.join(self.data_dir, image_file)
    path_outfile = path.join(self.data_dir, "python", outfile)

    document = ap.Document()
    page = document.pages.add()
    page.set_page_size(842,595)

    # Get page resources
    resources_images = page.resources.images

    # Add image to resources
    image_stream = FileIO(path.join(self.data_dir, path_infile), "rb")
    image_id = resources_images.add(image_stream)

    x_image = list(resources_images)[-1]

    rectangle = ap.Rectangle(
        0,
        0,
        page.media_box.width,
        (page.media_box.width * x_image.height) / x_image.width,
        True,
    )

    # Create operator sequence for adding image
    operators = []

    # Save graphics state
    operators.append(ap.operators.GSave())

    # Set transformation matrix (position and size)
    matrix = ap.Matrix(
        rectangle.urx - rectangle.llx,
        0,
        0,
        rectangle.ury - rectangle.lly,
        rectangle.llx,
        rectangle.llx + (page.media_box.height - rectangle.height) / 2,
    )
    operators.append(ap.operators.ConcatenateMatrix(matrix))

    # Draw the image
    operators.append(ap.operators.Do(image_id))

    # Restore graphics state
    operators.append(ap.operators.GRestore())

    # Add operators to page contents
    page.contents.add(operators)

    document.save(path_outfile)
```

## إضافة صورة مع نص بديل

يوضح هذا المثال كيفية إضافة صورة إلى صفحة PDF وتعيين نص بديل (alt text) للامتثال لإمكانية الوصول (مثل PDF/UA).

1. إنشاء 'Document' جديد وإضافة صفحة (842 × 595، أفقية A4).
1. وضع الصورة على الصفحة باستخدام 'page.add_image()' مع مستطيل يغطي الصفحة بالكامل.
1. الوصول إلى موارد صور الصفحة ('page.resources.images').
1. تعريف سلسلة نص بديلة (مثال: 'Alternative text for image').
1. استرداد كائن الصورة الأول من الموارد ('x_image = resources_images[1]').
1. استخدام 'try_set_alternative_text(alt_text, page)' لتعيين النص البديل للصورة.
1. حفظ ملف PDF الناتج.

```python

    import aspose.pdf as ap
    from io import FileIO
    from os import path

    path_image_file = path.join(self.data_dir, image_file)
    path_outfile = path.join(self.data_dir, "python", outfile)

    document = ap.Document()
    page = document.pages.add()
    page.set_page_size(842,595)

    page.add_image(
        path_image_file,
        ap.Rectangle(0, 0, 842, 595, True),
    )

    resources_images = page.resources.images
    alt_text = "Alternative text for image"
    x_image = resources_images[1]
    result = x_image.try_set_alternative_text(alt_text, page)

    # If set is successful, then get the alternative text for the image
    if (result):
        print ("Text has been added successfuly")
    document.save(path_outfile)
```
