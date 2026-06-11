---
title: التعليقات التوضيحية المستندة إلى النص باستخدام Python
linktitle: التعليقات التوضيحية النصية
type: docs
weight: 10
url: /ar/python-net/text-based-annotations/
description: تعرف على كيفية إضافة نص حر وفحصه وحذفه، وتمييز التعليقات التوضيحية وتسطيرها وتعرجها وشطبها في مستندات PDF باستخدام Aspose.PDF لـ Python عبر .NET.
lastmod: "2026-06-11"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: اعمل مع التعليقات التوضيحية لملف PDF لترميز النص والنص في Python.
Abstract: تشرح هذه المقالة كيفية إنشاء التعليقات التوضيحية النصية وقراءتها وإزالتها في مستندات PDF باستخدام Aspose.PDF لـ Python عبر .NET. ويغطي التعليقات التوضيحية للنص الحر والتعليقات التوضيحية لترميز النص مثل التمييز والتسطير والتعرج والشطب، بما في ذلك عمليات سير عمل التسطير المتقدمة مثل التسطيح والنقاط الرباعية واستخراج النص المحدد.
---

توضح هذه المقالة كيفية التعامل مع التعليقات التوضيحية النصية في مستندات PDF باستخدام Aspose.PDF لـ Python عبر .NET.

يوضح البرنامج النصي النموذجي العديد من عمليات سير عمل التعليقات التوضيحية النصية:

- التعليقات التوضيحية النصية المجانية
- تسليط الضوء على التعليقات التوضيحية
- تسطير التعليقات التوضيحية
- التعليقات التوضيحية المتعرجة
- التعليقات التوضيحية المشطوبة

## التعليقات التوضيحية للنص الحر

### إضافة تعليقات توضيحية من FreeText 

تتيح لك التعليقات التوضيحية النصية المجانية وضع تعليقات نصية مرئية مباشرة على صفحة PDF. يضيف هذا المثال تعليقًا توضيحيًا بسيطًا للنص المجاني إلى الصفحة الأولى.

#### افتح ملف PDF المصدر

```python
document = ap.Document(infile)
```

#### إنشاء وتكوين التعليق التوضيحي للنص المجاني

```python
free_text_annotation = ap.annotations.FreeTextAnnotation(
    document.pages[1],
    ap.Rectangle(299, 713, 308, 720, True),
    ap.annotations.DefaultAppearance(),
)
free_text_annotation.title = "Aspose User"
free_text_annotation.color = ap.Color.light_green
```

#### أضف التعليق التوضيحي واحفظ ملف PDF

```python
document.pages[1].annotations.append(free_text_annotation)
document.save(outfile)
```

#### مثال كامل

```python
def free_text_annotation_add(infile, outfile):
    document = ap.Document(infile)

    free_text_annotation = ap.annotations.FreeTextAnnotation(
        document.pages[1],
        ap.Rectangle(299, 713, 308, 720, True),
        ap.annotations.DefaultAppearance(),
    )
    free_text_annotation.title = "Aspose User"
    free_text_annotation.color = ap.Color.light_green

    document.pages[1].annotations.append(free_text_annotation)
    document.save(outfile)
```

### احصل على تعليقات FreeText 

لفحص التعليقات التوضيحية للنص الحر، قم بتصفية التعليقات التوضيحية للصفحة الأولى حسب `FREE_TEXT` اكتب واطبع كل مستطيل للتعليق التوضيحي.

#### قم بتحميل المستند وجمع التعليقات التوضيحية النصية المجانية

```python
document = ap.Document(infile)
free_text_annotations = [
    annotation
    for annotation in document.pages[1].annotations
    if annotation.annotation_type == ap.annotations.AnnotationType.FREE_TEXT
]
```

#### اطبع مستطيلات التعليقات التوضيحية

```python
for annotation in free_text_annotations:
    print(annotation.rect)
```

#### مثال كامل

```python
def free_text_annotation_get(infile, outfile):
    document = ap.Document(infile)
    free_text_annotations = [
        annotation
        for annotation in document.pages[1].annotations
        if annotation.annotation_type == ap.annotations.AnnotationType.FREE_TEXT
    ]

    for annotation in free_text_annotations:
        print(annotation.rect)
```

### حذف التعليقات التوضيحية لـ FreeText 

يزيل سير العمل هذا جميع التعليقات التوضيحية النصية المجانية من الصفحة الأولى ويحفظ ملف PDF المحدث.

#### البحث عن التعليقات التوضيحية النصية المجانية وحذفها

```python
document = ap.Document(infile)
free_text_annotations = [
    annotation
    for annotation in document.pages[1].annotations
    if annotation.annotation_type == ap.annotations.AnnotationType.FREE_TEXT
]

for annotation in free_text_annotations:
    document.pages[1].annotations.delete(annotation)

document.save(outfile)
```

#### مثال كامل

```python
def free_text_annotation_delete(infile, outfile):
    document = ap.Document(infile)
    free_text_annotations = [
        annotation
        for annotation in document.pages[1].annotations
        if annotation.annotation_type == ap.annotations.AnnotationType.FREE_TEXT
    ]

    for annotation in free_text_annotations:
        document.pages[1].annotations.delete(annotation)

    document.save(outfile)
```


## التعليقات التوضيحية لترميز النص

### قم بتمييز التعليقات التوضيحية

#### إضافة تمييز النص

قم بتمييز التعليقات التوضيحية للتأكيد على أجزاء من المستند دون تغيير المحتوى الأساسي. يضيف هذا المثال تعليقًا توضيحيًا مميزًا إلى الصفحة الأولى.

```python
document = ap.Document(infile)

highlight_annotation = ap.annotations.HighlightAnnotation(
    document.pages[1],
    ap.Rectangle(300, 750, 320, 770, True),
)

document.pages[1].annotations.append(highlight_annotation)
document.save(outfile)
```

```python
def text_highlight_annotation_add(infile, outfile):
    document = ap.Document(infile)

    highlight_annotation = ap.annotations.HighlightAnnotation(
        document.pages[1],
        ap.Rectangle(300, 750, 320, 770, True),
    )

    document.pages[1].annotations.append(highlight_annotation)
    document.save(outfile)
```

#### احصل على تمييز النص

لفحص التعليقات التوضيحية المميزة، قم بتصفية التعليقات التوضيحية للصفحة حسب `HIGHLIGHT` اكتب واطبع المستطيلات الخاصة بهم.

```python
document = ap.Document(infile)
highlight_annotations = [
    annotation
    for annotation in document.pages[1].annotations
    if annotation.annotation_type == ap.annotations.AnnotationType.HIGHLIGHT
]

for annotation in highlight_annotations:
    print(annotation.rect)
```

```python
def text_highlight_annotation_get(infile, outfile):
    document = ap.Document(infile)
    highlight_annotations = [
        annotation
        for annotation in document.pages[1].annotations
        if annotation.annotation_type == ap.annotations.AnnotationType.HIGHLIGHT
    ]

    for annotation in highlight_annotations:
        print(annotation.rect)
```

#### حذف تمييز النص

يزيل سير العمل هذا جميع التعليقات التوضيحية المميزة من الصفحة الأولى ويحفظ ملف PDF الناتج.

```python
document = ap.Document(infile)
highlight_annotations = [
    annotation
    for annotation in document.pages[1].annotations
    if annotation.annotation_type == ap.annotations.AnnotationType.HIGHLIGHT
]

for annotation in highlight_annotations:
    document.pages[1].annotations.delete(annotation)

document.save(outfile)
```

```python
def text_highlight_annotation_delete(infile, outfile):
    document = ap.Document(infile)
    highlight_annotations = [
        annotation
        for annotation in document.pages[1].annotations
        if annotation.annotation_type == ap.annotations.AnnotationType.HIGHLIGHT
    ]

    for annotation in highlight_annotations:
        document.pages[1].annotations.delete(annotation)

    document.save(outfile)
```


### تسطير التعليقات التوضيحية

#### إضافة تعليقات توضيحية لتسطير النص

قم بتسطير التعليقات التوضيحية لوضع علامة على النص بتسطير مرئي. يضيف هذا المثال تعليقًا توضيحيًا أساسيًا ويقوم بتعيين البيانات الوصفية واللون.

```python
document = ap.Document(infile)

underline_annotation = ap.annotations.UnderlineAnnotation(
    document.pages[1],
    ap.Rectangle(299.988, 713.664, 308.708, 720.769, True),
)
underline_annotation.title = "Aspose User"
underline_annotation.subject = "Inserted Underline 1"
underline_annotation.flags = ap.annotations.AnnotationFlags.PRINT
underline_annotation.color = ap.Color.blue

document.pages[1].annotations.append(underline_annotation)
document.save(outfile)
```

```python
def text_underline_annotation_add(infile, outfile):
    document = ap.Document(infile)

    underline_annotation = ap.annotations.UnderlineAnnotation(
        document.pages[1],
        ap.Rectangle(299.988, 713.664, 308.708, 720.769, True),
    )
    underline_annotation.title = "Aspose User"
    underline_annotation.subject = "Inserted Underline 1"
    underline_annotation.flags = ap.annotations.AnnotationFlags.PRINT
    underline_annotation.color = ap.Color.blue

    document.pages[1].annotations.append(underline_annotation)
    document.save(outfile)
```

#### إضافة نص، تسطير، التعليقات التوضيحية، تسطيح 

إذا كنت تريد أن يصبح التسطير جزءًا من محتوى الصفحة بدلاً من أن يظل تعليقًا توضيحيًا تفاعليًا، فيمكنك تسويته بعد إضافته.

```python
document = ap.Document(infile)

underline_annotation = ap.annotations.UnderlineAnnotation(
    document.pages[1],
    ap.Rectangle(299.988, 713.664, 308.708, 720.769, True),
)
underline_annotation.title = "Aspose User"
underline_annotation.subject = "Inserted Underline to Flatten"
underline_annotation.flags = ap.annotations.AnnotationFlags.PRINT
underline_annotation.color = ap.Color.blue

document.pages[1].annotations.append(underline_annotation)
underline_annotation.flatten()

document.save(outfile)
```

```python
def text_underline_flatten_add(infile, outfile):
    document = ap.Document(infile)

    underline_annotation = ap.annotations.UnderlineAnnotation(
        document.pages[1],
        ap.Rectangle(299.988, 713.664, 308.708, 720.769, True),
    )
    underline_annotation.title = "Aspose User"
    underline_annotation.subject = "Inserted Underline to Flatten"
    underline_annotation.flags = ap.annotations.AnnotationFlags.PRINT
    underline_annotation.color = ap.Color.blue

    document.pages[1].annotations.append(underline_annotation)
    underline_annotation.flatten()

    document.save(outfile)
```

#### إضافة تعليقات توضيحية لتسطير النص باستخدام نقاط رباعية

تتيح لك النقاط الرباعية تحديد المنطقة المحددة بدقة للتعليق التوضيحي الخاص بالتسطير. يكون هذا مفيدًا عندما تحتاج إلى مزيد من التحكم مقارنة بالمستطيل البسيط.

```python
document = ap.Document(infile)
rect = ap.Rectangle(299.988, 713.664, 308.708, 720.769, True)

underline_annotation = ap.annotations.UnderlineAnnotation(document.pages[1], rect)
underline_annotation.title = "Aspose User"
underline_annotation.subject = "Inserted Underline with Quad Points"
underline_annotation.flags = ap.annotations.AnnotationFlags.PRINT
underline_annotation.color = ap.Color.blue
underline_annotation.quad_points = [
    ap.Point(rect.llx, rect.lly),
    ap.Point(rect.urx, rect.lly),
    ap.Point(rect.urx, rect.ury),
    ap.Point(rect.llx, rect.ury),
]

document.pages[1].annotations.append(underline_annotation)
document.save(outfile)
```

```python
def text_underline_with_quad_points_add(infile, outfile):
    document = ap.Document(infile)
    rect = ap.Rectangle(299.988, 713.664, 308.708, 720.769, True)

    underline_annotation = ap.annotations.UnderlineAnnotation(document.pages[1], rect)
    underline_annotation.title = "Aspose User"
    underline_annotation.subject = "Inserted Underline with Quad Points"
    underline_annotation.flags = ap.annotations.AnnotationFlags.PRINT
    underline_annotation.color = ap.Color.blue
    underline_annotation.quad_points = [
        ap.Point(rect.llx, rect.lly),
        ap.Point(rect.urx, rect.lly),
        ap.Point(rect.urx, rect.ury),
        ap.Point(rect.llx, rect.ury),
    ]

    document.pages[1].annotations.append(underline_annotation)
    document.save(outfile)
```

#### حذف التعليقات التوضيحية لتسطير النص

يزيل سير العمل هذا جميع التعليقات التوضيحية السفلية من الصفحة الأولى ويحفظ المستند المحدث.

```python
document = ap.Document(infile)
underline_annotations = [
    annotation
    for annotation in document.pages[1].annotations
    if annotation.annotation_type == ap.annotations.AnnotationType.UNDERLINE
]

for annotation in underline_annotations:
    document.pages[1].annotations.delete(annotation)

document.save(outfile)
```

```python
def text_underline_annotation_delete(infile, outfile):
    document = ap.Document(infile)
    underline_annotations = [
        annotation
        for annotation in document.pages[1].annotations
        if annotation.annotation_type == ap.annotations.AnnotationType.UNDERLINE
    ]

    for annotation in underline_annotations:
        document.pages[1].annotations.delete(annotation)

    document.save(outfile)
```

#### حذف النص: تسطير التعليقات التوضيحية حسب العنوان

يوضح سير العمل هذا كيفية حذف التعليقات التوضيحية التي تحتها تسطير بشكل انتقائي بعد التحقق من عنوانها.

```python
document = ap.Document(infile)

underline_annotations = [
    cast(ap.annotations.UnderlineAnnotation, annotation)
    for annotation in document.pages[1].annotations
    if annotation.annotation_type == ap.annotations.AnnotationType.UNDERLINE
]

for annotation in underline_annotations:
    if annotation.title.startswith("a"):
        document.pages[1].annotations.delete(annotation)

document.save(outfile)
```

```python
def text_underline_by_title_delete(infile, outfile):
    document = ap.Document(infile)

    underline_annotations = [
        cast(ap.annotations.UnderlineAnnotation, annotation)
        for annotation in document.pages[1].annotations
        if annotation.annotation_type == ap.annotations.AnnotationType.UNDERLINE
    ]

    for annotation in underline_annotations:
        if annotation.title.startswith("a"):
            document.pages[1].annotations.delete(annotation)

    document.save(outfile)
```

#### احصل على التعليقات التوضيحية لتسطير النص

لفحص التعليقات التوضيحية الخاصة بالتسطير، قم بتصفية التعليقات التوضيحية للصفحة الأولى حسب `UNDERLINE` اكتب واطبع كل مستطيل.

```python
document = ap.Document(infile)
underline_annotations = [
    annotation
    for annotation in document.pages[1].annotations
    if annotation.annotation_type == ap.annotations.AnnotationType.UNDERLINE
]

for annotation in underline_annotations:
    print(annotation.rect)
```

```python
def text_underline_annotation_get(infile, outfile):
    document = ap.Document(infile)
    underline_annotations = [
        annotation
        for annotation in document.pages[1].annotations
        if annotation.annotation_type == ap.annotations.AnnotationType.UNDERLINE
    ]

    for annotation in underline_annotations:
        print(annotation.rect)
```

#### احصل على نص، تسطير، تعليقات توضيحية، نص مميز

يقوم سير العمل هذا بتحويل كل تعليق توضيحي للتسطير إلى `UnderlineAnnotation` كائن ويستخرج النص المحدد.

```python
document = ap.Document(infile)

underline_annotations = [
    annotation
    for annotation in document.pages[1].annotations
    if annotation.annotation_type == ap.annotations.AnnotationType.UNDERLINE
]

for annotation in underline_annotations:
    ua = cast(ap.annotations.UnderlineAnnotation, annotation)
    print(f"Marked text: {ua.get_marked_text()}")
```

```python
def text_underline_marked_text_get(infile, outfile):
    document = ap.Document(infile)

    underline_annotations = [
        annotation
        for annotation in document.pages[1].annotations
        if annotation.annotation_type == ap.annotations.AnnotationType.UNDERLINE
    ]

    for annotation in underline_annotations:
        ua = cast(ap.annotations.UnderlineAnnotation, annotation)
        print(f"Marked text: {ua.get_marked_text()}")
```

#### احصل على أجزاء مميزة لتسطير النص

إذا كنت بحاجة إلى كل جزء محدد بشكل منفصل، فيمكنك التكرار من خلال المجموعة التي تم إرجاعها بواسطة `get_marked_text_fragments()`.

```python
document = ap.Document(infile)

underline_annotations = [
    annotation
    for annotation in document.pages[1].annotations
    if annotation.annotation_type == ap.annotations.AnnotationType.UNDERLINE
]

for annotation in underline_annotations:
    ua = cast(ap.annotations.UnderlineAnnotation, annotation)
    for fragment in ua.get_marked_text_fragments():
        print(f"Fragment text: {fragment.text}")
```

```python
def text_underline_marked_fragments_get(infile, outfile):
    document = ap.Document(infile)

    underline_annotations = [
        annotation
        for annotation in document.pages[1].annotations
        if annotation.annotation_type == ap.annotations.AnnotationType.UNDERLINE
    ]

    for annotation in underline_annotations:
        ua = cast(ap.annotations.UnderlineAnnotation, annotation)
        for fragment in ua.get_marked_text_fragments():
            print(f"Fragment text: {fragment.text}")
```


### التعليقات التوضيحية المتعرجة

#### إضافة التعليقات التوضيحية المتعرجة

غالبًا ما تُستخدم التعليقات التوضيحية المتقشرة لوضع علامة على مناطق التدقيق الإملائي أو النحوي أو الانتباه في النص. يضيف هذا المثال تعليقًا توضيحيًا متعرجًا إلى الصفحة الأولى.

```python
document = ap.Document(infile)
page = document.pages[1]

squiggly_annotation = ap.annotations.SquigglyAnnotation(
    page,
    ap.Rectangle(67, 317, 261, 459, True),
)
squiggly_annotation.title = "John Smith"
squiggly_annotation.color = ap.Color.blue

page.annotations.append(squiggly_annotation)
document.save(outfile)
```

```python
def text_squiggly_annotation_add(infile, outfile):
    document = ap.Document(infile)
    page = document.pages[1]

    squiggly_annotation = ap.annotations.SquigglyAnnotation(
        page,
        ap.Rectangle(67, 317, 261, 459, True),
    )
    squiggly_annotation.title = "John Smith"
    squiggly_annotation.color = ap.Color.blue

    page.annotations.append(squiggly_annotation)
    document.save(outfile)
```

#### احصل على التعليقات التوضيحية المتعرجة

لفحص التعليقات التوضيحية المتعرجة، قم بتصفية التعليقات التوضيحية للصفحة بواسطة `SQUIGGLY` اكتب واطبع المستطيلات الخاصة بهم.

```python
document = ap.Document(infile)
squiggly_annotations = [
    annotation
    for annotation in document.pages[1].annotations
    if annotation.annotation_type == ap.annotations.AnnotationType.SQUIGGLY
]

for annotation in squiggly_annotations:
    print(annotation.rect)
```

```python
def text_squiggly_annotation_get(infile, outfile):
    document = ap.Document(infile)
    squiggly_annotations = [
        annotation
        for annotation in document.pages[1].annotations
        if annotation.annotation_type == ap.annotations.AnnotationType.SQUIGGLY
    ]

    for annotation in squiggly_annotations:
        print(annotation.rect)
```

#### حذف التعليقات التوضيحية لـ Squiggly

يزيل سير العمل هذا جميع التعليقات التوضيحية المتعرجة من الصفحة الأولى ويحفظ النتيجة.

```python
document = ap.Document(infile)
squiggly_annotations = [
    annotation
    for annotation in document.pages[1].annotations
    if annotation.annotation_type == ap.annotations.AnnotationType.SQUIGGLY
]

for annotation in squiggly_annotations:
    document.pages[1].annotations.delete(annotation)

document.save(outfile)
```

```python
def text_squiggly_annotation_delete(infile, outfile):
    document = ap.Document(infile)
    squiggly_annotations = [
        annotation
        for annotation in document.pages[1].annotations
        if annotation.annotation_type == ap.annotations.AnnotationType.SQUIGGLY
    ]

    for annotation in squiggly_annotations:
        document.pages[1].annotations.delete(annotation)

    document.save(outfile)
```


### التعليقات التوضيحية لـ StrikeOut

#### إضافة تعليقات توضيحية لشطب النص

تشير التعليقات التوضيحية لـ Strikeout إلى النص الذي يجب التعامل معه على أنه تمت إزالته أو شطبه. يضيف هذا المثال تعليقًا توضيحيًا ويحدد البيانات الوصفية واللون.

```python
document = ap.Document(infile)

strikeout_annotation = ap.annotations.StrikeOutAnnotation(
    document.pages[1],
    ap.Rectangle(299.988, 713.664, 308.708, 720.769, True),
)
strikeout_annotation.title = "Aspose User"
strikeout_annotation.subject = "Inserted text 1"
strikeout_annotation.flags = ap.annotations.AnnotationFlags.PRINT
strikeout_annotation.color = ap.Color.blue

document.pages[1].annotations.append(strikeout_annotation)
document.save(outfile)
```

```python
def text_strikeout_annotation_add(infile, outfile):
    document = ap.Document(infile)

    strikeout_annotation = ap.annotations.StrikeOutAnnotation(
        document.pages[1],
        ap.Rectangle(299.988, 713.664, 308.708, 720.769, True),
    )
    strikeout_annotation.title = "Aspose User"
    strikeout_annotation.subject = "Inserted text 1"
    strikeout_annotation.flags = ap.annotations.AnnotationFlags.PRINT
    strikeout_annotation.color = ap.Color.blue

    document.pages[1].annotations.append(strikeout_annotation)
    document.save(outfile)
```

#### احصل على التعليقات التوضيحية لشطب النص

لفحص التعليقات التوضيحية للشطب، قم بتصفية التعليقات التوضيحية للصفحة حسب `STRIKE_OUT` اكتب واطبع المستطيلات الخاصة بهم.

```python
document = ap.Document(infile)
strikeout_annotations = [
    annotation
    for annotation in document.pages[1].annotations
    if annotation.annotation_type == ap.annotations.AnnotationType.STRIKE_OUT
]

for annotation in strikeout_annotations:
    print(annotation.rect)
```

```python
def text_strikeout_annotation_get(infile, outfile):
    document = ap.Document(infile)
    strikeout_annotations = [
        annotation
        for annotation in document.pages[1].annotations
        if annotation.annotation_type == ap.annotations.AnnotationType.STRIKE_OUT
    ]

    for annotation in strikeout_annotations:
        print(annotation.rect)
```

#### حذف التعليقات التوضيحية لشطب النص

يزيل سير العمل هذا جميع التعليقات التوضيحية من الصفحة الأولى ويحفظ المستند المحدث.

```python
document = ap.Document(infile)
strikeout_annotations = [
    annotation
    for annotation in document.pages[1].annotations
    if annotation.annotation_type == ap.annotations.AnnotationType.STRIKE_OUT
]

for annotation in strikeout_annotations:
    document.pages[1].annotations.delete(annotation)

document.save(outfile)
```

```python
def text_strikeout_annotation_delete(infile, outfile):
    document = ap.Document(infile)
    strikeout_annotations = [
        annotation
        for annotation in document.pages[1].annotations
        if annotation.annotation_type == ap.annotations.AnnotationType.STRIKE_OUT
    ]

    for annotation in strikeout_annotations:
        document.pages[1].annotations.delete(annotation)

    document.save(outfile)
```

## موضوعات ذات صلة

- [استيراد التعليقات التوضيحية وتصديرها](/python-net/import-export-annotations/)
- [التعليقات التوضيحية التفاعلية](/python-net/interactive-annotations/)
- [التعليقات التوضيحية للتوصيف](/python-net/markup-annotations/)
- [التعليقات التوضيحية لوسائل الإعلام](/python-net/media-annotations/)
- [التعليقات التوضيحية للأمان](/python-net/security-annotations/)
- [التعليقات التوضيحية للشكل](/python-net/shape-annotations/)
- [التعليقات التوضيحية للعلامة المائية](/python-net/watermark-annotations/)
