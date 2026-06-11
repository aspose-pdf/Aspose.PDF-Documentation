---
title: احصل على الصور وابحث عنها في PDF
linktitle: احصل على الصور وابحث عنها
type: docs
weight: 40
url: /ar/python-net/search-and-get-images-from-pdf-document/
description: تعرف على كيفية البحث عن الصور وفحصها في مستندات PDF في Python.
lastmod: "2026-06-11"
TechArticle: true
AlternativeHeadline: ابحث وافحص الصور في ملفات PDF باستخدام Python
Abstract: توضح هذه المقالة كيفية البحث عن الصور وفحصها في مستندات PDF باستخدام Aspose.PDF لـ Python عبر .NET. ويغطي استخدام ImagePlacementAbsorber لتحليل موضع الصورة وحجمها ودقتها والنص البديل.
---

## افحص خصائص موضع الصورة في صفحة PDF

يوضح هذا المثال كيفية تحليل وعرض خصائص جميع الصور على صفحة PDF محددة باستخدام Aspose.PDF لـ Python عبر .NET.

استخدم هذه الصفحة عندما تحتاج إلى تدقيق موضع الصورة أو فحص دقة الصورة أو تحديد كائنات الصور المضمنة عبر صفحات PDF.

1. قم بإنشاء «ImagePlacementAbsorber» لجمع كل الصور على الصفحة.
1. اتصل بـ 'document.pages [1] .accept (absorder) 'لتحليل مواضع الصور في الصفحة الأولى.
1. قم بالتكرار من خلال «absorber.image_places» واعرض الخصائص الرئيسية لكل صورة:
    - العرض والارتفاع (نقاط).
    - إحداثيات X السفلية اليسرى (LLX) وأسفل اليسار Y (LLY).
    - الدقة الأفقية (X) والعمودية (Y) (DPI).

```python
import math
import aspose.pdf as ap
from aspose.pycore import cast, is_assignable
import aspose.pydrawing as drawing

def extract_image_params(infile):
    document = ap.Document(infile)
    absorber = ap.ImagePlacementAbsorber()
    document.pages[1].accept(absorber)

    for image_placement in absorber.image_placements:
        print("image width: " + str(image_placement.rectangle.width))
        print("image height: " + str(image_placement.rectangle.height))
        print("image LLX: " + str(image_placement.rectangle.llx))
        print("image LLY: " + str(image_placement.rectangle.lly))
        print("image horizontal resolution: " + str(image_placement.resolution.x))
        print("image vertical resolution: " + str(image_placement.resolution.y))
```

## استخراج وحساب أنواع الصور في PDF

تقوم هذه الوظيفة بتحليل جميع الصور الموجودة على الصفحة الأولى من ملف PDF وتحسب عدد الصور ذات التدرج الرمادي وصور RGB.

1. قم بإنشاء «ImagePlacementAbsorber» لجمع كل الصور على الصفحة.
1. قم بتهيئة العدادات لصور درجات الرمادي وصور RGB.
1. اتصل بـ «document.pages [1] .accept (absorder)» لتحليل مواضع الصور.
1. اطبع العدد الإجمالي للصور التي تم العثور عليها.
1. قم بالتكرار من خلال كل صورة في «absorber.image_places»:
    - احصل على نوع لون الصورة باستخدام 'image_placement.image.get_color_type () '.
    - قم بزيادة العداد المقابل (الرمادي أو rgb).
    - اطبع رسالة لكل صورة تشير إلى ما إذا كانت ذات تدرج رمادي أو RGB.

```python
import math
import aspose.pdf as ap
from aspose.pycore import cast, is_assignable
import aspose.pydrawing as drawing

def extract_image_types_from_pdf(infile):
    """
    Extract and count image types (grayscale/RGB) with resolution analysis.

    Args:
        infile (str): Input PDF filename

    Returns:
        None

    Example:
        extract_image_types_from_pdf("sample_extr.pdf")

    Note:
        Prints total images count, color type for each image, and resolution info.
    """

    document = ap.Document(infile)
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

    print("--------------------------------")
    print("Grayscale Images = " + str(grayscaled))
    print("RGB Images = " + str(rgb))
```

## استخراج معلومات الصورة التفصيلية من PDF

تقوم هذه الوظيفة بتحليل جميع الصور في الصفحة الأولى من PDF وحساب أبعادها المقاسة والدقة الفعالة بناءً على تحويلات رسومات الصفحة.

1. قم بتحميل PDF وتهيئة المتغيرات
1. جمع موارد الصور
1. مشغلو محتوى صفحة المعالجة:
    - «GSave» - ادفع CTM الحالي إلى المكدس.
    - 'GreStore' - أخرج آخر CTM من المكدس.
    - «ConcatenateMatrix» - قم بتحديث CTM الحالي عن طريق الضرب بمصفوفة المشغل.
1. قم بطباعة اسم الصورة والأبعاد المقاسة والدقة المحسوبة.

```python
import math
import aspose.pdf as ap
from aspose.pycore import cast, is_assignable
import aspose.pydrawing as drawing

def extract_image_information_from_pdf(infile):
    with ap.Document(infile) as document:
        default_resolution = 72
        graphics_state = []

        image_names = list(document.pages[1].resources.images.names)

        graphics_state.append(
            drawing.drawing2d.Matrix(
                float(1), float(0), float(0), float(1), float(0), float(0)
            )
        )

        for op in document.pages[1].contents:
            if is_assignable(op, ap.operators.GSave):
                graphics_state.append(
                    cast(drawing.drawing2d.Matrix, graphics_state[-1]).clone()
                )

            elif is_assignable(op, ap.operators.GRestore):
                graphics_state.pop()

            elif is_assignable(op, ap.operators.ConcatenateMatrix):
                op_cm = cast(ap.operators.ConcatenateMatrix, op)
                cm = drawing.drawing2d.Matrix(
                    float(op_cm.matrix.a),
                    float(op_cm.matrix.b),
                    float(op_cm.matrix.c),
                    float(op_cm.matrix.d),
                    float(op_cm.matrix.e),
                    float(op_cm.matrix.f),
                )

                graphics_state[-1].multiply(cm)
                continue

            elif is_assignable(op, ap.operators.Do):
                op_do = cast(ap.operators.Do, op)
                if op_do.name in image_names:
                    last_ctm = cast(drawing.drawing2d.Matrix, graphics_state[-1])
                    index = image_names.index(op_do.name) + 1
                    image = document.pages[1].resources.images[index]

                    scaled_width = math.sqrt(
                        last_ctm.elements[0] ** 2 + last_ctm.elements[1] ** 2
                    )
                    scaled_height = math.sqrt(
                        last_ctm.elements[2] ** 2 + last_ctm.elements[3] ** 2
                    )

                    original_width = image.width
                    original_height = image.height

                    res_horizontal = (
                        original_width * default_resolution / scaled_width
                    )
                    res_vertical = (
                        original_height * default_resolution / scaled_height
                    )

                    info = (
                        f"{infile} image {op_do.name} "
                        f"({scaled_width:.2f}:{scaled_height:.2f}): "
                        f"res {res_horizontal:.2f} x {res_vertical:.2f}\n"
                    )
                    print(info.rstrip())
```

## استخراج نص بديل من الصور في PDF

تقوم هذه الوظيفة باسترداد النص البديل (النص البديل) من جميع الصور على الصفحة الأولى من PDF، وهي مفيدة لإمكانية الوصول وفحوصات التوافق مع PDF/UA.

1. قم بتحميل مستند PDF باستخدام «AP.document ()».
1. قم بإنشاء «ImagePlacementAbsorber» لجمع كل الصور على الصفحة.
1. اقبل جهاز الامتصاص في الصفحة الأولى (page.accept (absorber)).
1. قم بالتكرار من خلال كل صورة في «absorber.image_places»:
    - اطبع اسم الصورة في مجموعة موارد الصفحة (get_name_in_collection ()).
    - استرجع النص البديل باستخدام «get_alternative_text (صفحة)».
    - اطبع السطر الأول من النص البديل.

```python
import math
import aspose.pdf as ap
from aspose.pycore import cast, is_assignable
import aspose.pydrawing as drawing

def extract_image_alt_text(infile):
    document = ap.Document(infile)
    absorber = ap.ImagePlacementAbsorber()
    page = document.pages[1]
    page.accept(absorber)

    for image_placement in absorber.image_placements:
        print(
            "Name in collection: " + str(image_placement.image.get_name_in_collection())
        )
        lines = image_placement.image.get_alternative_text(page)
        print("Alt Text: " + lines[0])
```

## موضوعات الصور ذات الصلة

- [العمل مع الصور في PDF باستخدام Python](/pdf/ar/python-net/working-with-images/)
- [استخراج الصور من ملفات PDF](/pdf/ar/python-net/extract-images-from-pdf-file/)
- [استبدل الصور في ملفات PDF الموجودة](/pdf/ar/python-net/replace-image-in-existing-pdf-file/)
- [إضافة صور إلى ملفات PDF الموجودة](/pdf/ar/python-net/add-image-to-existing-pdf-file/)
