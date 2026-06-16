---
title: وضع علامة على التعليقات التوضيحية باستخدام Python
linktitle: التعليقات التوضيحية للتوصيف
type: docs
weight: 30
url: /ar/python-net/markup-annotations/
description: تعرف على كيفية إضافة نص وقراءته وحذفه، ووضع علامة، واستبدال التعليقات التوضيحية في مستندات PDF باستخدام Aspose.PDF لـ Python عبر .NET.
lastmod: "2026-06-11"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: اعمل مع التعليقات التوضيحية للترميز في ملفات PDF باستخدام Python.
Abstract: تشرح هذه المقالة كيفية إنشاء التعليقات التوضيحية للترميز وفحصها وإزالتها في مستندات PDF باستخدام Aspose.PDF لـ Python عبر .NET. ويغطي التعليقات التوضيحية النصية والتعليقات التوضيحية واستبدال التعليقات التوضيحية، مع تقسيم كل سير عمل إلى خطوات صغيرة وأمثلة للتعليمات البرمجية.
---

توضح هذه المقالة كيفية التعامل مع التعليقات التوضيحية للترميز في مستندات PDF باستخدام Aspose.PDF لـ Python عبر .NET.

يوضح البرنامج النصي النموذجي ثلاث عمليات سير عمل شائعة للتعليقات التوضيحية:

- التعليقات التوضيحية النصية للتعليقات ذات نمط الملاحظة
- التعليقات التوضيحية لعلامات الإدراج
- استبدال التعليقات التوضيحية لترميز استبدال النص

## التعليقات التوضيحية النصية

### إضافة تعليقات توضيحية نصية

يقوم هذا المثال بإنشاء تعليق توضيحي نصي على الصفحة الأولى ويربطه بنافذة منبثقة. تُعد التعليقات التوضيحية النصية مفيدة للتعليقات ذات نمط الملاحظات اللاصقة في عمليات سير عمل المراجعة.

#### افتح ملف PDF المصدر

```python
document = ap.Document(infile)
```

#### إنشاء التعليق التوضيحي النصي وتكوينه

حدد مستطيل التعليق التوضيحي وقم بتعيين العنوان والموضوع والمحتويات وعلامات العرض واللون والرمز.

```python
text_annotation = ap.annotations.TextAnnotation(
    document.pages[1],
    ap.Rectangle(299.988, 613.664, 428.708, 680.769, True),
)
text_annotation.title = "Aspose User"
text_annotation.subject = "Sticky Note"
text_annotation.contents = (
    "This is a text annotation added by Aspose.PDF for Python via .NET"
)
text_annotation.flags = ap.annotations.AnnotationFlags.PRINT
text_annotation.color = ap.Color.blue
text_annotation.icon = ap.annotations.TextIcon.HELP
```

#### قم بإنشاء التعليق التوضيحي المنبثق

قم بإنشاء نافذة منبثقة وقم بتوصيلها بالتعليق التوضيحي النصي.

```python
popup = ap.annotations.PopupAnnotation(
    document.pages[1],
    ap.Rectangle(428.708, 613.664, 528.708, 713.664, True),
)
popup.open = True

text_annotation.popup = popup
```

#### أضف التعليق التوضيحي واحفظ ملف PDF

```python
document.pages[1].annotations.add(text_annotation, consider_rotation=False)
document.save(outfile)
```

#### مثال كامل

```python
def text_annotation_add(infile, outfile):
    document = ap.Document(infile)

    text_annotation = ap.annotations.TextAnnotation(
        document.pages[1],
        ap.Rectangle(299.988, 613.664, 428.708, 680.769, True),
    )
    text_annotation.title = "Aspose User"
    text_annotation.subject = "Sticky Note"
    text_annotation.contents = (
        "This is a text annotation added by Aspose.PDF for Python via .NET"
    )
    text_annotation.flags = ap.annotations.AnnotationFlags.PRINT
    text_annotation.color = ap.Color.blue
    text_annotation.icon = ap.annotations.TextIcon.HELP

    popup = ap.annotations.PopupAnnotation(
        document.pages[1],
        ap.Rectangle(428.708, 613.664, 528.708, 713.664, True),
    )
    popup.open = True

    text_annotation.popup = popup

    document.pages[1].annotations.add(text_annotation, consider_rotation=False)
    document.save(outfile)
```

### احصل على تعليقات توضيحية نصية

لفحص التعليقات التوضيحية النصية الموجودة، قم بتصفية مجموعة التعليقات التوضيحية في الصفحة الأولى واحتفظ فقط بالعناصر التي يكون نوعها `TEXT`.

#### قم بتحميل المستند وجمع التعليقات التوضيحية النصية

```python
document = ap.Document(infile)
text_annotations = [
    annotation
    for annotation in document.pages[1].annotations
    if annotation.annotation_type == ap.annotations.AnnotationType.TEXT
]
```

#### اطبع مستطيلات التعليقات التوضيحية

```python
for annotation in text_annotations:
    print(annotation.rect)
```

#### مثال كامل

```python
def text_annotation_get(infile, outfile):
    document = ap.Document(infile)
    text_annotations = [
        annotation
        for annotation in document.pages[1].annotations
        if annotation.annotation_type == ap.annotations.AnnotationType.TEXT
    ]

    for annotation in text_annotations:
        print(annotation.rect)
```

### حذف التعليقات التوضيحية النصية

يزيل سير العمل هذا جميع التعليقات التوضيحية النصية من الصفحة الأولى ويحفظ ملف PDF المعدل.

#### ابحث عن التعليقات التوضيحية النصية لإزالتها

```python
document = ap.Document(infile)
text_annotations = [
    annotation
    for annotation in document.pages[1].annotations
    if annotation.annotation_type == ap.annotations.AnnotationType.TEXT
]
```

#### احذف التعليقات التوضيحية واحفظ الملف

```python
for annotation in text_annotations:
    document.pages[1].annotations.delete(annotation)

document.save(outfile)
```

#### مثال كامل

```python
def text_annotation_delete(infile, outfile):
    document = ap.Document(infile)
    text_annotations = [
        annotation
        for annotation in document.pages[1].annotations
        if annotation.annotation_type == ap.annotations.AnnotationType.TEXT
    ]

    for annotation in text_annotations:
        document.pages[1].annotations.delete(annotation)

    document.save(outfile)
```

## تعليقات كاريت

### إضافة التعليقات التوضيحية لـ Caret

تُستخدم التعليقات التوضيحية لعلامة Caret لوضع علامة على نقاط الإدراج في سيناريوهات المراجعة. يضيف هذا المثال تعليقًا توضيحيًا مع ملاحظة منبثقة مرفقة.

#### افتح المستند واحصل على الصفحة المستهدفة

```python
document = ap.Document(infile)
page = document.pages[1]
```

#### إنشاء التعليق التوضيحي للسجاد وتكوينه

```python
caret_annotation = ap.annotations.CaretAnnotation(
    page, ap.Rectangle(299.988, 713.664, 308.708, 720.769, True)
)
caret_annotation.title = "Aspose User"
caret_annotation.subject = "Inserted text 1"
caret_annotation.flags = ap.annotations.AnnotationFlags.PRINT
caret_annotation.color = ap.Color.blue
```

#### أرفق النافذة المنبثقة واحفظ المستند

```python
caret_annotation.popup = ap.annotations.PopupAnnotation(
    page, ap.Rectangle(310, 713, 410, 730, True)
)
page.annotations.append(caret_annotation)

document.save(outfile)
```

#### مثال كامل

```python
def caret_annotations_add(infile, outfile):
    document = ap.Document(infile)
    page = document.pages[1]

    caret_annotation = ap.annotations.CaretAnnotation(
        page, ap.Rectangle(299.988, 713.664, 308.708, 720.769, True)
    )
    caret_annotation.title = "Aspose User"
    caret_annotation.subject = "Inserted text 1"
    caret_annotation.flags = ap.annotations.AnnotationFlags.PRINT
    caret_annotation.color = ap.Color.blue
    caret_annotation.popup = ap.annotations.PopupAnnotation(
        page, ap.Rectangle(310, 713, 410, 730, True)
    )
    page.annotations.append(caret_annotation)

    document.save(outfile)
```

### احصل على تعليقات Caret التوضيحية

لفحص التعليقات التوضيحية للحرف، قم بتكرار التعليقات التوضيحية للصفحة والتصفية حسب `CARET` نوع التعليق التوضيحي.

#### قم بتحميل المستند والصفحة

```python
document = ap.Document(infile)
page = document.pages[1]
```

#### طباعة مستطيلات التعليق التوضيحي للبطاقة

```python
for annot in page.annotations:
    if annot.annotation_type == ap.annotations.AnnotationType.CARET:
        print(annot.rect)
```

#### مثال كامل

```python
def caret_annotations_get(infile, outfile):
    document = ap.Document(infile)
    page = document.pages[1]

    for annot in page.annotations:
        if annot.annotation_type == ap.annotations.AnnotationType.CARET:
            print(annot.rect)
```

### حذف التعليقات التوضيحية لـ Caret

يقوم سير العمل هذا بجمع التعليقات التوضيحية أولاً، وحذفها واحدة تلو الأخرى، ثم حفظ الملف المحدث.

#### قم بتحميل المستند وجمع التعليقات التوضيحية

```python
document = ap.Document(infile)
page = document.pages[1]

caret_annotations = [
    annot
    for annot in page.annotations
    if annot.annotation_type == ap.annotations.AnnotationType.CARET
]
```

#### احذف التعليقات التوضيحية واحفظ المستند

```python
for annot in caret_annotations:
    page.annotations.delete(annot)

document.save(outfile)
```

#### مثال كامل

```python
def caret_annotations_delete(infile, outfile):
    document = ap.Document(infile)
    page = document.pages[1]

    caret_annotations = [
        annot
        for annot in page.annotations
        if annot.annotation_type == ap.annotations.AnnotationType.CARET
    ]

    for annot in caret_annotations:
        page.annotations.delete(annot)

    document.save(outfile)
```

## استبدال التعليقات التوضيحية

### إضافة تعليقات توضيحية بديلة

استبدل التعليقات التوضيحية بالجمع بين التعليق التوضيحي المتدرج والتعليق التوضيحي المجمّع. يحدد هذا النمط النص الذي يجب استبداله ويربط ملاحظة الاستبدال بالمحتوى المشطوب.

#### افتح المستند واحصل على الصفحة

```python
document = ap.Document(infile)
page = document.pages[1]
```

#### قم بإنشاء التعليق التوضيحي للنص البديل

```python
caret_annotation = ap.annotations.CaretAnnotation(
    page, ap.Rectangle(361.246, 727.908, 370.081, 735.107, True)
)
caret_annotation.flags = ap.annotations.AnnotationFlags.PRINT
caret_annotation.subject = "Inserted text 2"
caret_annotation.title = "Aspose User"
caret_annotation.color = ap.Color.blue
caret_annotation.popup = ap.annotations.PopupAnnotation(
    page, ap.Rectangle(310, 713, 410, 730, True)
)
```

#### قم بإنشاء التعليق التوضيحي المجمّع للشطب

حدد منطقة الشطب، وقم بتعيين نقاط رباعية، واربطها بالتعليق التوضيحي من خلال `in_reply_to` و `reply_type`.

```python
strikeout_annotation = ap.annotations.StrikeOutAnnotation(
    page, ap.Rectangle(318.407, 727.826, 368.916, 740.098, True)
)
strikeout_annotation.color = ap.Color.blue
strikeout_annotation.quad_points = [
    ap.Point(321.66, 739.416),
    ap.Point(365.664, 739.416),
    ap.Point(321.66, 728.508),
    ap.Point(365.664, 728.508),
]
strikeout_annotation.subject = "Cross-out"
strikeout_annotation.in_reply_to = caret_annotation
strikeout_annotation.reply_type = ap.annotations.ReplyType.GROUP
``` 

#### أضف كلا الشروح واحفظ ملف PDF

```python
page.annotations.append(caret_annotation)
page.annotations.append(strikeout_annotation)

document.save(outfile)
```

#### مثال كامل

```python
def replace_annotations_add(infile, outfile):
    document = ap.Document(infile)
    page = document.pages[1]

    caret_annotation = ap.annotations.CaretAnnotation(
        page, ap.Rectangle(361.246, 727.908, 370.081, 735.107, True)
    )
    caret_annotation.flags = ap.annotations.AnnotationFlags.PRINT
    caret_annotation.subject = "Inserted text 2"
    caret_annotation.title = "Aspose User"
    caret_annotation.color = ap.Color.blue
    caret_annotation.popup = ap.annotations.PopupAnnotation(
        page, ap.Rectangle(310, 713, 410, 730, True)
    )

    strikeout_annotation = ap.annotations.StrikeOutAnnotation(
        page, ap.Rectangle(318.407, 727.826, 368.916, 740.098, True)
    )
    strikeout_annotation.color = ap.Color.blue
    strikeout_annotation.quad_points = [
        ap.Point(321.66, 739.416),
        ap.Point(365.664, 739.416),
        ap.Point(321.66, 728.508),
        ap.Point(365.664, 728.508),
    ]
    strikeout_annotation.subject = "Cross-out"
    strikeout_annotation.in_reply_to = caret_annotation
    strikeout_annotation.reply_type = ap.annotations.ReplyType.GROUP

    page.annotations.append(caret_annotation)
    page.annotations.append(strikeout_annotation)

    document.save(outfile)
```

### احصل على استبدال التعليقات التوضيحية

لتحديد التعليقات التوضيحية البديلة، ابحث عن التعليقات التوضيحية التي تم تجميعها كردود على تعليق توضيحي آخر. تقوم العينة بإلقاء كل تعليق توضيحي قبل التحقق من حقول العلاقة الخاصة بها.

#### قم بتحميل المستند وتكراره من خلال التعليقات التوضيحية

```python
document = ap.Document(infile)
page = document.pages[1]
```

#### تصفية التعليقات التوضيحية المجمعة للشطب

```python
for annot in page.annotations:
    if annot.annotation_type == ap.annotations.AnnotationType.STRIKE_OUT:
        sa = cast(ap.annotations.StrikeOutAnnotation, annot)
        if (
            sa.in_reply_to is not None
            and sa.reply_type == ap.annotations.ReplyType.GROUP
        ):
            print(f"Replace annotation rect: {sa.rect}")
```

#### مثال كامل

```python
def replace_annotations_get(infile, outfile):
    document = ap.Document(infile)
    page = document.pages[1]

    for annot in page.annotations:
        if annot.annotation_type == ap.annotations.AnnotationType.STRIKE_OUT:
            sa = cast(ap.annotations.StrikeOutAnnotation, annot)
            if (
                sa.in_reply_to is not None
                and sa.reply_type == ap.annotations.ReplyType.GROUP
            ):
                print(f"Replace annotation rect: {sa.rect}")
```

### حذف استبدال التعليقات التوضيحية

يقوم سير العمل هذا بتجميع التعليقات التوضيحية المُستخدمة لاستبدال الترميز، وإزالتها من الصفحة، وحفظ ملف PDF الناتج.

#### قم بتحميل المستند وجمع التعليقات التوضيحية البديلة

```python
document = ap.Document(infile)
page = document.pages[1]

replace_annotations = [
    cast(ap.annotations.StrikeOutAnnotation, annot)
    for annot in page.annotations
    if annot.annotation_type == ap.annotations.AnnotationType.STRIKE_OUT
]
```

#### احذف التعليقات التوضيحية واحفظ المستند

```python
for annot in replace_annotations:
    page.annotations.delete(annot)

document.save(outfile)
```

#### مثال كامل

```python
def replace_annotations_delete(infile, outfile):
    document = ap.Document(infile)
    page = document.pages[1]

    replace_annotations = [
        cast(ap.annotations.StrikeOutAnnotation, annot)
        for annot in page.annotations
        if annot.annotation_type == ap.annotations.AnnotationType.STRIKE_OUT
    ]

    for annot in replace_annotations:
        page.annotations.delete(annot)

    document.save(outfile)
```
