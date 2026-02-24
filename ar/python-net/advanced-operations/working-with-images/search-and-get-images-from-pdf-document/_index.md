---
title: الحصول على الصور والبحث عنها في PDF
linktitle: الحصول على الصور والبحث عنها
type: docs
weight: 40
url: /ar/python-net/search-and-get-images-from-pdf-document/
description: تعلم كيفية البحث والحصول على الصور من مستند PDF في Python باستخدام Aspose.PDF.
lastmod: "2025-09-17"
TechArticle: true
AlternativeHeadline: البحث واستخراج الصور من PDF
Abstract: توفر مكتبة Aspose.PDF للـ Python عبر .NET قدرات قوية للبحث واستخراج الصور من مستندات PDF. باستخدام الفئة 'ImagePlacementAbsorber'، يمكن للمطورين تحديد مواقع الصور المدمجة عبر جميع صفحات PDF والوصول إليها بكفاءة.
---

## فحص خصائص موضع الصورة في صفحة PDF

يوضح هذا المثال كيفية تحليل وعرض خصائص جميع الصور في صفحة PDF محددة باستخدام Aspose.PDF للـ Python عبر .NET.

1. إنشاء كائن 'ImagePlacementAbsorber' لجمع جميع الصور في الصفحة.
1. استدعاء 'document.pages[1].accept(absorber)' لتحليل مواضع الصور في الصفحة الأولى.
1. التكرار عبر 'absorber.image_placements' وعرض الخصائص الرئيسية لكل صورة:
- العرض والارتفاع (نقاط).
- إحداثيات X السفلية اليسرى (LLX) وY السفلية اليسرى (LLY).
- الدقة الأفقية (X) والرأسية (Y) (نقطة في البوصة).

```python

    import math
    import aspose.pdf as ap
    from aspose.pycore import cast, is_assignable
    from os import path

    path_infile = path.join(self.data_dir, infile)

    document = ap.Document(path_infile)
    absorber = ap.ImagePlacementAbsorber()
    document.pages[1].accept(absorber)

    for image_placement in absorber.image_placements:
        # Display image placement properties for all placements
        print("image width: " + str(image_placement.rectangle.width))
        print("image height: " + str(image_placement.rectangle.height))
        print("image LLX: " + str(image_placement.rectangle.llx))
        print("image LLY: " + str(image_placement.rectangle.lly))
        print("image horizontal resolution: " + str(image_placement.resolution.x))
        print("image vertical resolution: " + str(image_placement.resolution.y))
```

## استخراج وعدّ أنواع الصور في PDF

تحلل هذه الدالة جميع الصور في الصفحة الأولى من PDF وتعد عدد الصور الرمادية والصور RGB.

1. إنشاء كائن 'ImagePlacementAbsorber' لجمع جميع الصور في الصفحة.
1. تهيئة عدادات للصور الرمادية والصور RGB.
1. استدعاء 'document.pages[1].accept(absorber)' لتحليل مواضع الصور.
1. طباعة إجمالي عدد الصور التي تم العثور عليها.
1. التكرار عبر كل صورة في 'absorber.image_placements':
- الحصول على نوع لون الصورة باستخدام 'image_placement.image.get_color_type()'.
- زيادة العداد المقابل (رمادي أو rgb).
- طباعة رسالة لكل صورة تشير إلى ما إذا كانت رمادية أو RGB.

```python

    import math
    import aspose.pdf as ap
    from aspose.pycore import cast, is_assignable
    from os import path

    path_infile = path.join(self.data_dir, infile)

    document = ap.Document(path_infile)
    absorber = ap.ImagePlacementAbsorber()

    # Counters for grayscale and RGB images
    grayscaled = 0
    rgb = 0

    document.pages[1].accept(absorber)

    print("--------------------------------")
    print("Total Images = " + str(len(absorber.image_placements)))

    image_counter = 1

    for image_placement in absorber.image_placements:
        # Determine the color type of the image
        colorType = image_placement.image.get_color_type()
        if colorType == ap.ColorType.GRAYSCALE:
            grayscaled += 1
            print(f"Image {image_counter} is Grayscale...")
        elif colorType == ap.ColorType.RGB:
            rgb += 1
            print(f"Image {image_counter} is RGB...")
        image_counter += 1
```

## استخراج معلومات مفصلة عن الصورة من PDF

تحلل هذه الدالة جميع الصور في الصفحة الأولى من PDF وتحسب أبعادها المقاسة والدقة الفعلية بناءً على تحويلات الرسومات في الصفحة.

1. تحميل PDF وتهيئة المتغيرات
1. جمع موارد الصور
1. معالجة عمليات محتوى الصفحة:
- 'GSave' - دفع التحويل الحالي (CTM) إلى المكدس.
- 'GRestore' - سحب آخر تحويل (CTM) من المكدس.
- 'ConcatenateMatrix' - تحديث التحويل الحالي (CTM) عن طريق الضرب بمصفوفة العملية.
1. طباعة اسم الصورة، أبعادها المقاسة، والدقة المحسوبة.

```python

    import math
    import aspose.pdf as ap
    from aspose.pycore import cast, is_assignable
    from os import path

    path_infile = path.join(self.data_dir, infile)

    document = ap.Document(path_infile)

    default_resolution = 72
    graphics_state = []

    image_names = list(document.pages[1].resources.images.names)

    graphics_state.append(drawing.drawing2d.Matrix(float(1), float(0), float(0), float(1), float(0), float(0)))

    for op in document.pages[1].contents:
        if is_assignable(op, ap.operators.GSave):
            graphics_state.append(cast(drawing.drawing2d.Matrix, graphics_state[-1]).clone())

        elif is_assignable(op, ap.operators.GRestore):
            graphics_state.pop()

        elif is_assignable(op, ap.operators.ConcatenateMatrix):
            opCM = cast(ap.operators.ConcatenateMatrix, op)
            cm = drawing.drawing2d.Matrix(
                float(opCM.matrix.a),
                float(opCM.matrix.b),
                float(opCM.matrix.c),
                float(opCM.matrix.d),
                float(opCM.matrix.e),
                float(opCM.matrix.f),
            )

            graphics_state[-1].multiply(cm)
            continue

        elif is_assignable(op, ap.operators.Do):
            opDo = cast(ap.operators.Do, op)
            if opDo.name in image_names:
                last_ctm = cast(drawing.drawing2d.Matrix, graphics_state[-1])
                index = image_names.index(opDo.name) + 1
                image = document.pages[1].resources.images[index]

                scaled_width = math.sqrt(last_ctm.elements[0] ** 2 + last_ctm.elements[1] ** 2)
                scaled_height = math.sqrt(last_ctm.elements[2] ** 2 + last_ctm.elements[3] ** 2)

                original_width = image.width
                original_height = image.height

                res_horizontal = original_width * default_resolution / scaled_width
                res_vertical = original_height * default_resolution / scaled_height

                print(
                    f"{self.data_dir}image {opDo.name} "
                    f"({scaled_width:.2f}:{scaled_height:.2f}): "
                    f"res {res_horizontal:.2f} x {res_vertical:.2f}"
                )
```

## استخراج النص البديل من الصور في PDF

تسترجع هذه الدالة النص البديل (alt text) من جميع الصور في الصفحة الأولى من PDF، وهو مفيد للتحقق من إمكانية الوصول والامتثال لـ PDF/UA.

1. تحميل مستند PDF باستخدام 'ap.Document()'.
1. إنشاء كائن 'ImagePlacementAbsorber' لجمع جميع الصور في الصفحة.
1. قبول الامتصاص في الصفحة الأولى (page.accept(absorber)).
1. التكرار عبر كل صورة في 'absorber.image_placements':
- طباعة اسم الصورة في مجموعة موارد الصفحة (get_name_in_collection()).
- استرجاع النص البديل باستخدام 'get_alternative_text(page)'.
- طباعة السطر الأول من النص البديل.

```python

    import math
    import aspose.pdf as ap
    from aspose.pycore import cast, is_assignable
    from os import path

    path_infile = path.join(self.data_dir, infile)

    document = ap.Document(path_infile)
    absorber = ap.ImagePlacementAbsorber()
    page = document.pages[1]
    page.accept(absorber)

    for image_placement in absorber.image_placements:
        print(
            "Name in collection: "
            + str(image_placement.image.get_name_in_collection())
        )
        lines = image_placement.image.get_alternative_text(page)
        print("Alt Text: " + lines[0])
```
