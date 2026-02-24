---
title: استخراج الصور من ملف PDF باستخدام بايثون
linktitle: استخراج الصور
type: docs
weight: 30
url: /ar/python-net/extract-images-from-pdf-file/
description: يوضح هذا القسم كيفية استخراج الصور من ملف PDF باستخدام مكتبة بايثون.
lastmod: "2025-09-27"
TechArticle: true
AlternativeHeadline: استخراج الصور من PDF باستخدام بايثون
Abstract: تناقش هذه المقالة عملية استخراج الصور من ملفات PDF باستخدام Aspose.PDF for Python. تُبرز فائدة فصل الصور لأغراض مثل الإدارة، الأرشفة، التحليل أو المشاركة. توضح المقالة أن الصور داخل PDF تُخزن في مجموعة موارد كل صفحة، تحديدًا في مجموعة XImage. لاستخراج صورة، يمكن للمستخدمين الوصول إلى صفحة معينة واسترجاع الصورة باستخدام مؤشرها من مجموعة Images. كائن XImage المرتجع من المؤشر يوفر طريقة `save()` لحفظ الصورة المستخرجة. تم توفير مقطع شفرة لتوضيح الخطوات اللازمة لفتح مستند PDF، واستخراج صورة محددة من الصفحة الثانية باستخدام مؤشرها، وحفظها إلى ملف.
---

هل تحتاج إلى فصل الصور عن ملفات PDF الخاصة بك؟ لإدارة مبسطة، أو أرشفة، أو تحليل، أو مشاركة صور مستنداتك، استخدم **Aspose.PDF for Python** واستخراج الصور من ملفات PDF.

1. قم بتحميل مستند PDF باستخدام 'ap.Document()'.
1. الوصول إلى الصفحة المطلوبة من المستند (document.pages[1]).
1. اختيار الصورة من موارد الصفحة (مثال، resources.images[1]).
1. إنشاء تدفق إخراج (FileIO) للملف المستهدف.
1. حفظ الصورة المستخرجة باستخدام 'xImage.save(output_image)'.

```python

    import aspose.pdf as ap
    from io import FileIO
    from os import path

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, outfile)

    document = ap.Document(path_infile)
    xImage = document.pages[1].resources.images[1]
    with FileIO(path_outfile, "w") as output_image:
        xImage.save(output_image)
```

## استخراج الصور من منطقة محددة في PDF

يوضح هذا المثال استخراج الصور الموجودة داخل منطقة مستطيلة محددة على صفحة PDF وحفظها كملفات منفصلة.

1. تحميل مستند PDF باستخدام 'ap.Document'.
1. إنشاء 'ImagePlacementAbsorber' لجمع جميع الصور على الصفحة الأولى.
1. استدعاء 'document.pages[1].accept(absorber)' لتحليل مواضع الصور.
1. التكرار عبر جميع الصور في 'absorber.image_placements':
- الحصول على صندوق حد الصورة (llx, lly, urx, ury).
- التحقق مما إذا كانت زوايا مستطيل الصورة تقع داخل المستطيل المستهدف (rectangle.contains()).
- إذا كان صحيحًا، حفظ الصورة إلى ملف باستخدام FileIO، مع استبدال 'index' في اسم الملف برقم تسلسلي.
1. زيادة الفهرس لكل صورة محفوظة.

```python

    import aspose.pdf as ap
    from io import FileIO
    from os import path

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, outfile)

    rectangle = ap.Rectangle(0, 0, 590, 590, True)

    document = ap.Document(path_infile)
    absorber = ap.ImagePlacementAbsorber()
    document.pages[1].accept(absorber)
    index = 1
    for image_placement in absorber.image_placements:
        point1 = ap.Point(
            image_placement.rectangle.llx, image_placement.rectangle.lly
        )
        point2 = ap.Point(
            image_placement.rectangle.urx, image_placement.rectangle.urx
        )
        if rectangle.contains(point1, True) and rectangle.contains(point2, True):
            with FileIO(path_outfile.replace("index", str(index)), "w") as output_image:
                image_placement.image.save(output_image)
            index = index + 1
```

## استخراج معلومات الصورة من PDF

يوضح المثال أدناه كيفية تحليل الصور المدمجة في صفحة PDF وحساب دقتها الفعلية.

1. فتح PDF باستخدام 'ap.Document'.
1. تتبع حالة الرسومات أثناء قراءة محتوى الصفحة.
1. معالجة المشغلين:
- 'GSave'/'GRestore' - دفع/سحب المصفوفة.
- 'ConcatenateMatrix' - تحديث التحويل.
- 'Do' - إذا كانت صورة، احصل على الحجم وطبق التحويل.
1. حساب DPI الفعلي.
1. طباعة اسم الصورة، الحجم المُقَّم، و DPI.

```python

    import aspose.pdf as ap
    from io import FileIO
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
