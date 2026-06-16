---
title: شكل التعليقات التوضيحية عبر بايثون
linktitle: التعليقات التوضيحية للشكل
type: docs
weight: 20
url: /ar/python-net/shape-annotations/
description: تعرف على كيفية إضافة التعليقات التوضيحية الخطية والمربعة والدائرة والمضلع والمتعددة الأسطر وفحصها وحذفها في مستندات PDF باستخدام Aspose.PDF لـ Python عبر .NET.
lastmod: "2026-06-11"
sitemap:
    changefreq: "monthly"
    priority: 0.5
TechArticle: true
AlternativeHeadline: اعمل مع التعليقات التوضيحية الهندسية لـ PDF في Python.
Abstract: تشرح هذه المقالة كيفية إنشاء التعليقات التوضيحية وقراءتها وإزالتها في مستندات PDF باستخدام Aspose.PDF لـ Python عبر .NET. ويغطي التعليقات التوضيحية للسطر والمربع والدائرة والمضلع والمتعدد الخطوط، مع تقسيم كل سير عمل إلى خطوات صغيرة وأمثلة التعليمات البرمجية الكاملة.
---

توضح هذه المقالة كيفية التعامل مع التعليقات التوضيحية للشكل في مستندات PDF باستخدام Aspose.PDF لـ Python عبر .NET.

يوضح البرنامج النصي النموذجي العديد من عمليات سير عمل التعليقات التوضيحية القائمة على الهندسة:

- التعليقات التوضيحية للسطر
- التعليقات التوضيحية المربعة
- التعليقات التوضيحية للدائرة
- التعليقات التوضيحية المضلعة
- التعليقات التوضيحية متعددة الأسطر

## تعليق توضيحي على السطر 

### إضافة تعليق توضيحي للسطر 

يضيف هذا المثال تعليقًا سطريًا إلى الصفحة الأولى ويقوم بتكوين أنماط الأسهم وعرض الخط والنافذة المنبثقة.

#### افتح ملف PDF المصدر

```python
document = ap.Document(infile)
```

#### إنشاء التعليق التوضيحي للسطر وتكوينه

```python
line_annotation = ap.annotations.LineAnnotation(
    document.pages[1],
    ap.Rectangle(550, 93, 562, 439, True),
    ap.Point(556, 99),
    ap.Point(556, 443),
)

line_annotation.title = "John Smith"
line_annotation.color = ap.Color.red
line_annotation.width = 3
line_annotation.starting_style = ap.annotations.LineEnding.OPEN_ARROW
line_annotation.ending_style = ap.annotations.LineEnding.OPEN_ARROW
```

#### أرفق النافذة المنبثقة واحفظ ملف PDF

```python
popup = ap.annotations.PopupAnnotation(
    document.pages[1],
    ap.Rectangle(842, 124, 1021, 266, True),
)
line_annotation.popup = popup

document.pages[1].annotations.append(line_annotation)
document.save(outfile)
```

#### مثال كامل

```python
def line_annotation_add(infile, outfile):
    document = ap.Document(infile)

    line_annotation = ap.annotations.LineAnnotation(
        document.pages[1],
        ap.Rectangle(550, 93, 562, 439, True),
        ap.Point(556, 99),
        ap.Point(556, 443),
    )

    line_annotation.title = "John Smith"
    line_annotation.color = ap.Color.red
    line_annotation.width = 3
    line_annotation.starting_style = ap.annotations.LineEnding.OPEN_ARROW
    line_annotation.ending_style = ap.annotations.LineEnding.OPEN_ARROW

    popup = ap.annotations.PopupAnnotation(
        document.pages[1],
        ap.Rectangle(842, 124, 1021, 266, True),
    )
    line_annotation.popup = popup

    document.pages[1].annotations.append(line_annotation)
    document.save(outfile)
```

### احصل على تعليق توضيحي للخط 

لفحص التعليقات التوضيحية للسطر، قم بتصفية مجموعة التعليقات التوضيحية في الصفحة الأولى وقم بإرسال كل نتيجة إلى `LineAnnotation` حتى تتمكن من قراءة نقاط البداية والنهاية.

#### قم بتحميل ملف PDF وجمع التعليقات التوضيحية للسطر

```python
document = ap.Document(infile)

line_annotation = [
    cast(ap.annotations.LineAnnotation, annotation)
    for annotation in document.pages[1].annotations
    if annotation.annotation_type == ap.annotations.AnnotationType.LINE
]
```

#### اطبع إحداثيات الخط

```python
for annotation in line_annotation:
    print(
        f"[{annotation.starting.x},{annotation.starting.y}]"
        f"-[{annotation.ending.x},{annotation.ending.y}]"
    )
```

#### مثال كامل

```python
def line_annotations_get(infile, outfile):
    document = ap.Document(infile)

    line_annotation = [
        cast(ap.annotations.LineAnnotation, annotation)
        for annotation in document.pages[1].annotations
        if annotation.annotation_type == ap.annotations.AnnotationType.LINE
    ]

    for annotation in line_annotation:
        print(
            f"[{annotation.starting.x},{annotation.starting.y}]"
            f"-[{annotation.ending.x},{annotation.ending.y}]"
        )
```

### حذف التعليق التوضيحي للسطر 

يزيل سير العمل هذا جميع التعليقات التوضيحية للسطر من الصفحة الأولى ويحفظ ملف PDF المحدث.

#### ابحث عن التعليقات التوضيحية للسطر لإزالتها

```python
document = ap.Document(infile)
page = document.pages[1]

line_annotations = [
    annotation
    for annotation in page.annotations
    if annotation.annotation_type == ap.annotations.AnnotationType.LINE
]
```

#### احذف التعليقات التوضيحية واحفظ ملف PDF

```python
for annotation in line_annotations:
    page.annotations.delete(annotation)

document.save(outfile)
```

#### مثال كامل

```python
def line_annotations_delete(infile, outfile):
    document = ap.Document(infile)
    page = document.pages[1]

    line_annotations = [
        annotation
        for annotation in page.annotations
        if annotation.annotation_type == ap.annotations.AnnotationType.LINE
    ]

    for annotation in line_annotations:
        page.annotations.delete(annotation)

    document.save(outfile)
```


## التعليقات التوضيحية للمربع والدائرة

### إضافة تعليق توضيحي على شكل مربع 

التعليقات التوضيحية المربعة مفيدة لوضع علامات على المساحات المستطيلة في المستند. يقوم هذا المثال بإنشاء تعليق توضيحي مربع مع إعدادات الحدود والتعبئة والشفافية.

#### افتح ملف PDF وقم بإنشاء التعليق التوضيحي المربع

```python
document = ap.Document(infile)

square_annotation = ap.annotations.SquareAnnotation(
    document.pages[1],
    ap.Rectangle(60, 600, 250, 450, True),
)
square_annotation.title = "John Smith"
square_annotation.color = ap.Color.blue
square_annotation.interior_color = ap.Color.blue_violet
square_annotation.opacity = 0.25
```

#### أضف التعليق التوضيحي واحفظ ملف PDF

```python
document.pages[1].annotations.append(square_annotation)
document.save(outfile)
```

#### مثال كامل

```python
def square_annotation_add(infile, outfile):
    document = ap.Document(infile)

    square_annotation = ap.annotations.SquareAnnotation(
        document.pages[1],
        ap.Rectangle(60, 600, 250, 450, True),
    )
    square_annotation.title = "John Smith"
    square_annotation.color = ap.Color.blue
    square_annotation.interior_color = ap.Color.blue_violet
    square_annotation.opacity = 0.25

    document.pages[1].annotations.append(square_annotation)
    document.save(outfile)
```

### احصل على تعليق توضيحي مربع 

لفحص التعليقات التوضيحية المربعة، قم بتصفية التعليقات التوضيحية للصفحة الأولى بواسطة `SQUARE` اكتب واطبع كل مستطيل.

#### قم بتحميل المستند وجمع التعليقات التوضيحية المربعة

```python
document = ap.Document(infile)
square_annotations = [
    annotation
    for annotation in document.pages[1].annotations
    if annotation.annotation_type == ap.annotations.AnnotationType.SQUARE
]
```

#### اطبع مستطيلات التعليقات التوضيحية

```python
for annotation in square_annotations:
    print(annotation.rect)
```

#### مثال كامل

```python
def square_annotation_get(infile, outfile):
    document = ap.Document(infile)
    square_annotations = [
        annotation
        for annotation in document.pages[1].annotations
        if annotation.annotation_type == ap.annotations.AnnotationType.SQUARE
    ]

    for annotation in square_annotations:
        print(annotation.rect)
```

### حذف التعليق التوضيحي للمربع 

يزيل سير العمل هذا جميع التعليقات التوضيحية المربعة من الصفحة الأولى ويحفظ المستند.

#### البحث عن التعليقات التوضيحية المربعة وحذفها

```python
document = ap.Document(infile)
square_annotations = [
    annotation
    for annotation in document.pages[1].annotations
    if annotation.annotation_type == ap.annotations.AnnotationType.SQUARE
]

for annotation in square_annotations:
    document.pages[1].annotations.delete(annotation)

document.save(outfile)
```

#### مثال كامل

```python
def square_annotation_delete(infile, outfile):
    document = ap.Document(infile)
    square_annotations = [
        annotation
        for annotation in document.pages[1].annotations
        if annotation.annotation_type == ap.annotations.AnnotationType.SQUARE
    ]

    for annotation in square_annotations:
        document.pages[1].annotations.delete(annotation)

    document.save(outfile)
```

### إضافة تعليق توضيحي للدائرة 

تشير التعليقات التوضيحية للدائرة إلى المناطق المستديرة في PDF. يضيف هذا المثال تعليقًا توضيحيًا دائريًا مع لون التعبئة والتعتيم والتعليق التوضيحي المنبثق.

#### افتح ملف PDF وقم بإنشاء التعليق التوضيحي للدائرة

```python
document = ap.Document(infile)

circle_annotation = ap.annotations.CircleAnnotation(
    document.pages[1],
    ap.Rectangle(270, 160, 483, 383, True),
)
circle_annotation.title = "John Smith"
circle_annotation.color = ap.Color.red
circle_annotation.interior_color = ap.Color.misty_rose
circle_annotation.opacity = 0.5
```

#### أرفق النافذة المنبثقة واحفظ ملف PDF

```python
circle_annotation.popup = ap.annotations.PopupAnnotation(
    document.pages[1],
    ap.Rectangle(842, 316, 1021, 459, True),
)

document.pages[1].annotations.append(circle_annotation)
document.save(outfile)
```

#### مثال كامل

```python
def circle_annotation_add(infile, outfile):
    document = ap.Document(infile)

    circle_annotation = ap.annotations.CircleAnnotation(
        document.pages[1],
        ap.Rectangle(270, 160, 483, 383, True),
    )
    circle_annotation.title = "John Smith"
    circle_annotation.color = ap.Color.red
    circle_annotation.interior_color = ap.Color.misty_rose
    circle_annotation.opacity = 0.5
    circle_annotation.popup = ap.annotations.PopupAnnotation(
        document.pages[1],
        ap.Rectangle(842, 316, 1021, 459, True),
    )

    document.pages[1].annotations.append(circle_annotation)
    document.save(outfile)
```

### احصل على تعليق توضيحي للدائرة 

لفحص التعليقات التوضيحية للدائرة، قم بتصفية التعليقات التوضيحية للصفحة بواسطة `CIRCLE` اكتب واطبع المستطيلات الخاصة بهم.

#### قم بتحميل المستند وجمع التعليقات التوضيحية للدائرة

```python
document = ap.Document(infile)
circle_annotations = [
    annotation
    for annotation in document.pages[1].annotations
    if annotation.annotation_type == ap.annotations.AnnotationType.CIRCLE
]
```

#### اطبع مستطيلات التعليقات التوضيحية

```python
for annotation in circle_annotations:
    print(annotation.rect)
```

#### مثال كامل

```python
def circle_annotation_get(infile, outfile):
    document = ap.Document(infile)
    circle_annotations = [
        annotation
        for annotation in document.pages[1].annotations
        if annotation.annotation_type == ap.annotations.AnnotationType.CIRCLE
    ]

    for annotation in circle_annotations:
        print(annotation.rect)
```

### حذف التعليق التوضيحي للدائرة 

يزيل سير العمل هذا جميع التعليقات التوضيحية للدائرة من الصفحة الأولى ويحفظ ملف PDF الناتج.

#### البحث عن التعليقات التوضيحية للدائرة وحذفها

```python
document = ap.Document(infile)
circle_annotations = [
    annotation
    for annotation in document.pages[1].annotations
    if annotation.annotation_type == ap.annotations.AnnotationType.CIRCLE
]

for annotation in circle_annotations:
    document.pages[1].annotations.delete(annotation)

document.save(outfile)
```

#### مثال كامل

```python
def circle_annotation_delete(infile, outfile):
    document = ap.Document(infile)
    circle_annotations = [
        annotation
        for annotation in document.pages[1].annotations
        if annotation.annotation_type == ap.annotations.AnnotationType.CIRCLE
    ]

    for annotation in circle_annotations:
        document.pages[1].annotations.delete(annotation)

    document.save(outfile)
```


## التعليقات التوضيحية المضلعة والمتعددة الخطوط

### إضافة تعليق توضيحي على شكل مضلع 

تحدد التعليقات التوضيحية المضلعة شكلًا مغلقًا متعدد النقاط. يقوم هذا المثال بإنشاء تعليق توضيحي على شكل مضلع من مستطيل وقائمة بالنقاط.

#### افتح ملف PDF وقم بإنشاء التعليق التوضيحي المضلع

```python
document = ap.Document(infile)

polygon_annotation = ap.annotations.PolygonAnnotation(
    document.pages[1],
    ap.Rectangle(200, 300, 400, 400, True),
    [
        ap.Point(200, 300),
        ap.Point(220, 300),
        ap.Point(250, 330),
        ap.Point(300, 304),
        ap.Point(300, 400),
    ],
)
polygon_annotation.title = "John Smith"
polygon_annotation.color = ap.Color.blue
polygon_annotation.interior_color = ap.Color.blue_violet
polygon_annotation.opacity = 0.25
```

#### أضف التعليق التوضيحي واحفظ ملف PDF

```python
document.pages[1].annotations.append(polygon_annotation)
document.save(outfile)
```

#### مثال كامل

```python
def polygon_annotation_add(infile, outfile):
    document = ap.Document(infile)

    polygon_annotation = ap.annotations.PolygonAnnotation(
        document.pages[1],
        ap.Rectangle(200, 300, 400, 400, True),
        [
            ap.Point(200, 300),
            ap.Point(220, 300),
            ap.Point(250, 330),
            ap.Point(300, 304),
            ap.Point(300, 400),
        ],
    )
    polygon_annotation.title = "John Smith"
    polygon_annotation.color = ap.Color.blue
    polygon_annotation.interior_color = ap.Color.blue_violet
    polygon_annotation.opacity = 0.25

    document.pages[1].annotations.append(polygon_annotation)
    document.save(outfile)
```

### احصل على التعليق التوضيحي للمضلع 

لفحص التعليقات التوضيحية المضلعة، قم بتصفية التعليقات التوضيحية للصفحة الأولى بواسطة `POLYGON` اكتب واطبع كل مستطيل للتعليق التوضيحي.

#### قم بتحميل المستند وجمع التعليقات التوضيحية المضلعة

```python
document = ap.Document(infile)
polygon_annotations = [
    annotation
    for annotation in document.pages[1].annotations
    if annotation.annotation_type == ap.annotations.AnnotationType.POLYGON
]
```

#### اطبع مستطيلات التعليقات التوضيحية

```python
for annotation in polygon_annotations:
    print(annotation.rect)
```

#### مثال كامل

```python
def polygon_annotation_get(infile, outfile):
    document = ap.Document(infile)
    polygon_annotations = [
        annotation
        for annotation in document.pages[1].annotations
        if annotation.annotation_type == ap.annotations.AnnotationType.POLYGON
    ]

    for annotation in polygon_annotations:
        print(annotation.rect)
```

### حذف التعليق التوضيحي المضلع 

يزيل سير العمل هذا جميع التعليقات التوضيحية المضلعة من الصفحة الأولى ويحفظ ملف PDF المحدث.

#### البحث عن التعليقات التوضيحية المضلعة وحذفها

```python
document = ap.Document(infile)
polygon_annotations = [
    annotation
    for annotation in document.pages[1].annotations
    if annotation.annotation_type == ap.annotations.AnnotationType.POLYGON
]

for annotation in polygon_annotations:
    document.pages[1].annotations.delete(annotation)

document.save(outfile)
```

#### مثال كامل

```python
def polygon_annotation_delete(infile, outfile):
    document = ap.Document(infile)
    polygon_annotations = [
        annotation
        for annotation in document.pages[1].annotations
        if annotation.annotation_type == ap.annotations.AnnotationType.POLYGON
    ]

    for annotation in polygon_annotations:
        document.pages[1].annotations.delete(annotation)

    document.save(outfile)
```

### إضافة تعليق توضيحي متعدد الأسطر 

تحدد التعليقات التوضيحية متعددة الخطوط مسارًا مفتوحًا عبر نقاط متعددة. يقوم هذا المثال بإنشاء تعليق توضيحي متعدد الأسطر مع ملاحظة منبثقة.

#### افتح ملف PDF وقم بإنشاء التعليق التوضيحي متعدد الأسطر

```python
document = ap.Document(infile)

polyline_annotation = ap.annotations.PolylineAnnotation(
    document.pages[1],
    ap.Rectangle(270, 193, 571, 383, True),
    [
        ap.Point(545, 150),
        ap.Point(545, 190),
        ap.Point(667, 190),
        ap.Point(667, 110),
        ap.Point(626, 111),
    ],
)
polyline_annotation.title = "John Smith"
polyline_annotation.color = ap.Color.red
```

#### أرفق النافذة المنبثقة واحفظ ملف PDF

```python
polyline_annotation.popup = ap.annotations.PopupAnnotation(
    document.pages[1],
    ap.Rectangle(842, 196, 1021, 338, True),
)

document.pages[1].annotations.append(polyline_annotation)
document.save(outfile)
```

#### مثال كامل

```python
def polyline_annotation_add(infile, outfile):
    document = ap.Document(infile)

    polyline_annotation = ap.annotations.PolylineAnnotation(
        document.pages[1],
        ap.Rectangle(270, 193, 571, 383, True),
        [
            ap.Point(545, 150),
            ap.Point(545, 190),
            ap.Point(667, 190),
            ap.Point(667, 110),
            ap.Point(626, 111),
        ],
    )
    polyline_annotation.title = "John Smith"
    polyline_annotation.color = ap.Color.red
    polyline_annotation.popup = ap.annotations.PopupAnnotation(
        document.pages[1],
        ap.Rectangle(842, 196, 1021, 338, True),
    )

    document.pages[1].annotations.append(polyline_annotation)
    document.save(outfile)
```

### احصل على تعليق توضيحي متعدد الخطوط 

لفحص التعليقات التوضيحية متعددة الأسطر، قم بتصفية التعليقات التوضيحية للصفحة بواسطة `POLY_LINE` اكتب واطبع المستطيلات الخاصة بهم.

#### قم بتحميل المستند وجمع التعليقات التوضيحية متعددة الأسطر

```python
document = ap.Document(infile)
polyline_annotations = [
    annotation
    for annotation in document.pages[1].annotations
    if annotation.annotation_type == ap.annotations.AnnotationType.POLY_LINE
]
```

#### اطبع مستطيلات التعليقات التوضيحية

```python
for annotation in polyline_annotations:
    print(annotation.rect)
```

#### مثال كامل

```python
def polyline_annotation_get(infile, outfile):
    document = ap.Document(infile)
    polyline_annotations = [
        annotation
        for annotation in document.pages[1].annotations
        if annotation.annotation_type == ap.annotations.AnnotationType.POLY_LINE
    ]

    for annotation in polyline_annotations:
        print(annotation.rect)
```

### حذف التعليق التوضيحي متعدد الأسطر 

يزيل سير العمل هذا جميع التعليقات التوضيحية متعددة الأسطر من الصفحة الأولى ويحفظ ملف PDF الناتج.

#### البحث عن التعليقات التوضيحية متعددة الأسطر وحذفها

```python
document = ap.Document(infile)
polyline_annotations = [
    annotation
    for annotation in document.pages[1].annotations
    if annotation.annotation_type == ap.annotations.AnnotationType.POLY_LINE
]

for annotation in polyline_annotations:
    document.pages[1].annotations.delete(annotation)

document.save(outfile)
```

#### مثال كامل

```python
def polyline_annotation_delete(infile, outfile):
    document = ap.Document(infile)
    polyline_annotations = [
        annotation
        for annotation in document.pages[1].annotations
        if annotation.annotation_type == ap.annotations.AnnotationType.POLY_LINE
    ]

    for annotation in polyline_annotations:
        document.pages[1].annotations.delete(annotation)

    document.save(outfile)
```

## موضوعات ذات صلة

- [استيراد التعليقات التوضيحية وتصديرها](/python-net/import-export-annotations/)
- [التعليقات التوضيحية التفاعلية](/python-net/interactive-annotations/)
- [التعليقات التوضيحية للتوصيف](/python-net/markup-annotations/)
- [التعليقات التوضيحية لوسائل الإعلام](/python-net/media-annotations/)
- [التعليقات التوضيحية للأمان](/python-net/security-annotations/)
- [التعليقات التوضيحية المستندة إلى النص](/python-net/text-based-annotations/)
- [التعليقات التوضيحية للعلامة المائية](/python-net/watermark-annotations/)
